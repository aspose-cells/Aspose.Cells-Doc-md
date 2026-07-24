using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

// Create a new workbook and access the first worksheet
Workbook workbook = new Workbook();
Worksheet sheet = workbook.Worksheets[0];

// --- Build the source data: Fruit / Year / Amount (header + 9 rows) ---
sheet.Cells["A1"].PutValue("Fruit");
sheet.Cells["B1"].PutValue("Year");
sheet.Cells["C1"].PutValue("Amount");

sheet.Cells["A2"].PutValue("Grape");      sheet.Cells["B2"].PutValue(2020); sheet.Cells["C2"].PutValue(1000);
sheet.Cells["A3"].PutValue("Blueberry");  sheet.Cells["B3"].PutValue(2020); sheet.Cells["C3"].PutValue(2000);
sheet.Cells["A4"].PutValue("Kiwi");       sheet.Cells["B4"].PutValue(2020); sheet.Cells["C4"].PutValue(1500);
sheet.Cells["A5"].PutValue("Cherry");     sheet.Cells["B5"].PutValue(2020); sheet.Cells["C5"].PutValue(2500);
sheet.Cells["A6"].PutValue("Grape");      sheet.Cells["B6"].PutValue(2021); sheet.Cells["C6"].PutValue(3000);
sheet.Cells["A7"].PutValue("Blueberry");  sheet.Cells["B7"].PutValue(2021); sheet.Cells["C7"].PutValue(1800);
sheet.Cells["A8"].PutValue("Kiwi");       sheet.Cells["B8"].PutValue(2021); sheet.Cells["C8"].PutValue(2200);
sheet.Cells["A9"].PutValue("Cherry");     sheet.Cells["B9"].PutValue(2021); sheet.Cells["C9"].PutValue(2700);

// --- Add the first pivot table (Pivot1) at destination cell E3 ---
int idx1 = sheet.PivotTables.Add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable1 = sheet.PivotTables[idx1];
pivotTable1.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable1.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable1.AddFieldToArea(PivotFieldType.Data, "Amount");

// --- Add the SECOND pivot table (Pivot2) on the SAME source range ---
// Both Pivot1 and Pivot2 share ONE underlying PivotCache.
// This is exactly the scenario where the legacy per-table RefreshData()
// approach becomes inefficient: refreshing one table re-fetches the whole
// shared cache, so refreshing N tables does the same expensive fetch N times.
int idx2 = sheet.PivotTables.Add("A1:C9", "E15", "Pivot2");
PivotTable pivotTable2 = sheet.PivotTables[idx2];
pivotTable2.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable2.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable2.AddFieldToArea(PivotFieldType.Data, "Amount");

// --- Modify several Amount values in the source data ---
sheet.Cells["C2"].PutValue(5000);   // Grape  2020
sheet.Cells["C5"].PutValue(7500);   // Cherry 2020
sheet.Cells["C9"].PutValue(9500);   // Cherry 2021

// --- OBSOLETE pattern (pre-26.7) — PivotTable.RefreshData() ---
// pivotTable1.RefreshData();  // re-fetches from source, refreshes whole cache
// pivotTable2.RefreshData();  // re-fetches AGAIN — the cache is already fresh!
// Each call rebuilds the shared cache, so N tables = N redundant fetches.

// --- NEW v26.7+ pattern: refresh the cache ONCE, then re-render as needed ---
// One call to PivotCache.Refresh() pulls the modified values into the shared
// cache AND recalculates the display of EVERY pivot table that references it.
// Because Pivot1 and Pivot2 share one PivotCache, this single call updates
// both tables — no second source round-trip is required.
pivotTable1.PivotCache.Refresh();

// CalculateData() only re-renders a pivot table's display (data + style)
// from the data already held in the cache — it does NOT touch the source.
// We call it on Pivot2 here purely to demonstrate the API: after the cache
// has been refreshed once, any dependent table can be re-rendered without
// going back to the source. Use CalculateData() on its own when only the
// pivot table's view/layout settings have changed and the cache is current.
pivotTable2.CalculateData();

workbook.Save("output.xlsx");