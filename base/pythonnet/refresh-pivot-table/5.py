import aspose.cells as ac

# Create a new workbook and access the first worksheet
workbook = ac.Workbook()
sheet = workbook.worksheets[0]

# --- Build the source data: Fruit / Year / Amount (header + 9 rows) ---
sheet.cells["A1"].put_value("Fruit")
sheet.cells["B1"].put_value("Year")
sheet.cells["C1"].put_value("Amount")

sheet.cells["A2"].put_value("Grape")      ; sheet.cells["B2"].put_value(2020); sheet.cells["C2"].put_value(1000)
sheet.cells["A3"].put_value("Blueberry")  ; sheet.cells["B3"].put_value(2020); sheet.cells["C3"].put_value(2000)
sheet.cells["A4"].put_value("Kiwi")       ; sheet.cells["B4"].put_value(2020); sheet.cells["C4"].put_value(1500)
sheet.cells["A5"].put_value("Cherry")     ; sheet.cells["B5"].put_value(2020); sheet.cells["C5"].put_value(2500)
sheet.cells["A6"].put_value("Grape")      ; sheet.cells["B6"].put_value(2021); sheet.cells["C6"].put_value(3000)
sheet.cells["A7"].put_value("Blueberry")  ; sheet.cells["B7"].put_value(2021); sheet.cells["C7"].put_value(1800)
sheet.cells["A8"].put_value("Kiwi")       ; sheet.cells["B8"].put_value(2021); sheet.cells["C8"].put_value(2200)
sheet.cells["A9"].put_value("Cherry")     ; sheet.cells["B9"].put_value(2021); sheet.cells["C9"].put_value(2700)

# --- Add the first pivot table (Pivot1) at destination cell E3 ---
idx1 = sheet.pivot_tables.add("A1:C9", "E3", "Pivot1")
pivot_table1 = sheet.pivot_tables[idx1]
pivot_table1.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table1.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivot_table1.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

# --- Add the SECOND pivot table (Pivot2) on the SAME source range ---
# Both Pivot1 and Pivot2 share ONE underlying PivotCache.
# This is exactly the scenario where the legacy per-table RefreshData()
# approach becomes inefficient: refreshing one table re-fetches the whole
# shared cache, so refreshing N tables does the same expensive fetch N times.
idx2 = sheet.pivot_tables.add("A1:C9", "E15", "Pivot2")
pivot_table2 = sheet.pivot_tables[idx2]
pivot_table2.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table2.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivot_table2.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

# --- Modify several Amount values in the source data ---
sheet.cells["C2"].put_value(5000)   # Grape  2020
sheet.cells["C5"].put_value(7500)   # Cherry 2020
sheet.cells["C9"].put_value(9500)   # Cherry 2021

# --- OBSOLETE pattern (pre-26.7) — PivotTable.RefreshData() ---
# pivot_table1.refresh_data();  # re-fetches from source, refreshes whole cache
# pivot_table2.refresh_data();  # re-fetches AGAIN — the cache is already fresh!
# Each call rebuilds the shared cache, so N tables = N redundant fetches.

# --- NEW v26.7+ pattern: refresh the cache ONCE, then re-render as needed ---
# One call to PivotCache.Refresh() pulls the modified values into the shared
# cache AND recalculates the display of EVERY pivot table that references it.
# Because Pivot1 and Pivot2 share one PivotCache, this single call updates
# both tables — no second source round-trip is required.
pivot_table1.pivot_cache.refresh()

# CalculateData() only re-renders a pivot table's display (data + style)
# from the data already held in the cache — it does NOT touch the source.
# We call it on Pivot2 here purely to demonstrate the API: after the cache
# has been refreshed once, any dependent table can be re-rendered without
# going back to the source. Use CalculateData() on its own when only the
# pivot table's view/layout settings have changed and the cache is current.
pivot_table2.calculate_data()

workbook.save("output.xlsx")