let workbook = new AsposeCells.Workbook();
let sheet = workbook.getWorksheets().get(0);

// --- Build the source data: Fruit / Year / Amount (header + 9 rows) ---
sheet.getCells().get("A1").putValue("Fruit");
sheet.getCells().get("B1").putValue("Year");
sheet.getCells().get("C1").putValue("Amount");

sheet.getCells().get("A2").putValue("Grape");      sheet.getCells().get("B2").putValue(2020); sheet.getCells().get("C2").putValue(1000);
sheet.getCells().get("A3").putValue("Blueberry");  sheet.getCells().get("B3").putValue(2020); sheet.getCells().get("C3").putValue(2000);
sheet.getCells().get("A4").putValue("Kiwi");       sheet.getCells().get("B4").putValue(2020); sheet.getCells().get("C4").putValue(1500);
sheet.getCells().get("A5").putValue("Cherry");     sheet.getCells().get("B5").putValue(2020); sheet.getCells().get("C5").putValue(2500);
sheet.getCells().get("A6").putValue("Grape");      sheet.getCells().get("B6").putValue(2021); sheet.getCells().get("C6").putValue(3000);
sheet.getCells().get("A7").putValue("Blueberry");  sheet.getCells().get("B7").putValue(2021); sheet.getCells().get("C7").putValue(1800);
sheet.getCells().get("A8").putValue("Kiwi");       sheet.getCells().get("B8").putValue(2021); sheet.getCells().get("C8").putValue(2200);
sheet.getCells().get("A9").putValue("Cherry");     sheet.getCells().get("B9").putValue(2021); sheet.getCells().get("C9").putValue(2700);

// --- Add the first pivot table (Pivot1) at destination cell E3 ---
let idx1 = sheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
let pivotTable1 = sheet.getPivotTables().get(idx1);
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// --- Add the SECOND pivot table (Pivot2) on the SAME source range ---
// Both Pivot1 and Pivot2 share ONE underlying PivotCache.
// This is exactly the scenario where the legacy per-table RefreshData()
// approach becomes inefficient: refreshing one table re-fetches the whole
// shared cache, so refreshing N tables does the same expensive fetch N times.
let idx2 = sheet.getPivotTables().add("A1:C9", "E15", "Pivot2");
let pivotTable2 = sheet.getPivotTables().get(idx2);
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// --- Modify several Amount values in the source data ---
sheet.getCells().get("C2").putValue(5000);   // Grape  2020
sheet.getCells().get("C5").putValue(7500);   // Cherry 2020
sheet.getCells().get("C9").putValue(9500);   // Cherry 2021

// --- OBSOLETE pattern (pre-26.7) — PivotTable.RefreshData() ---
// pivotTable1.RefreshData();  // re-fetches from source, refreshes whole cache
// pivotTable2.RefreshData();  // re-fetches AGAIN — the cache is already fresh!
// Each call rebuilds the shared cache, so N tables = N redundant fetches.

// --- NEW v26.7+ pattern: refresh the cache ONCE, then re-render as needed ---
// One call to PivotCache.Refresh() pulls the modified values into the shared
// cache AND recalculates the display of EVERY pivot table that references it.
// Because Pivot1 and Pivot2 share one PivotCache, this single call updates
// both tables — no second source round-trip is required.
pivotTable1.getPivotCache().refresh();

// CalculateData() only re-renders a pivot table's display (data + style)
// from the data already held in the cache — it does NOT touch the source.
// We call it on Pivot2 here purely to demonstrate the API: after the cache
// has been refreshed once, any dependent table can be re-rendered without
// going back to the source. Use CalculateData() on its own when only the
// pivot table's view/layout settings have changed and the cache is current.
pivotTable2.calculateData();

workbook.save("output.xlsx");