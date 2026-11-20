---
title: Discrete Grouping of Pivot Field Items
description: Learn how to group pivot field items into custom named groups such as fruit and vegetables using DiscreteGroupItem and PivotFieldGroupOptions.discreteGroupItems in Aspose.Cells for JavaScript via C++.
linktitle: Discrete Grouping
keywords: Aspose.Cells, pivot table, discrete grouping, DiscreteGroupItem, PivotFieldGroupOptions, group pivot items, custom groups, PivotField.group, Aspose.Cells for JavaScript via C++, Excel pivot table
type: docs
weight: 90
url: /javascript-cpp/discrete-group-pivot-fields/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**
- Automatic grouping collects items by data type, such as dates into months and quarters or numbers into ranges. Discrete grouping solves the opposite problem, collecting specific, unrelated items into custom named groups, for example products into fruit and vegetables, stores into regions, or accounts into zones. Aspose.Cells provides discrete grouping through the `DiscreteGroupItem` class and the `PivotFieldGroupOptions.discreteGroupItems` property.
- A `DiscreteGroupItem` is a group name plus the items that belong to it. The items can be identified in two ways, by their names (`new DiscreteGroupItem("fruit", ["grape", "cherry"])`) or by their zero-based positions in the source data (`new DiscreteGroupItem("fruit", [0, 3])`). Both forms produce the same result.
- Discrete grouping is applied to a field in the row or column area of the pivot table by passing the options to `PivotField.group(PivotFieldGroupOptions)`.

## **Group Pivot Field Items by Item Names**
The following example builds a small sales list (product, date and amount), creates a pivot table from it with `product` in the row area, `date` in the column area and `amount` in the data area, then defines two custom groups by item names, fruit (grape, cherry) and vegetables (carrot, potato). The result shows a two-level row layout, the group name as the outer level and the original items nested underneath, so trends can be read per custom group and per item.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
            const { Workbook, DiscreteGroupItem, PivotFieldGroupOptions } = AsposeCells;
            document.getElementById('runExample').addEventListener('click', async () => {
                const workbook = new Workbook();
                const sheet = workbook.worksheets.get(0);
                const cells = sheet.cells;
                cells.get(0, 0).value = "product";
                cells.get(1, 0).value = "grape";
                cells.get(2, 0).value = "carrot";
                cells.get(3, 0).value = "potato";
                cells.get(4, 0).value = "cherry";
                const dateStyle = workbook.createStyle();
                dateStyle.custom = "m/d/yyyy";
                cells.get(0, 1).value = "date";
                cells.get(1, 1).value = new Date(2021, 1, 5);
                cells.get(2, 1).value = new Date(2022, 2, 8);
                cells.get(3, 1).value = new Date(2023, 3, 10);
                cells.get(4, 1).value = new Date(2024, 4, 16);
                for (let r = 1; r <= 4; r++) {
                    cells.get(r, 1).style = dateStyle;
                }
                cells.get(0, 2).value = "amount";
                cells.get(1, 2).value = 50;
                cells.get(2, 2).value = 60;
                cells.get(3, 2).value = 70;
                cells.get(4, 2).value = 80;
                // Add a pivot table with the destination cell A12 (row 11, column 0)
                const pivotTable = sheet.pivotTables.add("=Sheet1!A1:C5", 11, 0);
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "product");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "date");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "amount");
                pivotTable.pivotTableStyleType =
                    AsposeCells.PivotTableStyleType.PivotTableStyleMedium10;
                // Group specific items into custom groups by item names
                const fruit = new DiscreteGroupItem("fruit", ["grape", "cherry"]);
                const vegetable = new DiscreteGroupItem("vegetable", ["carrot", "potato"]);
                const groupOptions = new PivotFieldGroupOptions();
                groupOptions.discreteGroupItems = [fruit, vegetable];
                pivotTable.rowFields.get(0).group(groupOptions);
                pivotTable.calculateData();
                const outputData = workbook.save(AsposeCells.SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "outputDiscreteGroupPivotField.xlsx";
                downloadLink.style.display = "block";
                document.getElementById('result').innerHTML =
                    '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            });
        });
    </script>
</html>
```

After `calculateData()` the row area of the pivot table shows fruit (grape 50, cherry 80) and vegetable (carrot 60, potato 70) with the grand total 260, and the column labels keep the four dates (2/5/2021, 3/8/2022, 4/10/2023, 5/16/2024).

## **Group Pivot Field Items by Item Indices**
When the item names are long or localized, the second constructor of `DiscreteGroupItem` identifies the items by index. The indices are zero-based positions of the items in the order they appear in the source data, not alphabetical order. In the sample data above grape is item 0, carrot is item 1, potato is item 2 and cherry is item 3, so fruit is `{ 0, 3 }` and vegetable is `{ 1, 2 }`. The result is identical to the name-based example.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            const {
                Workbook,
                SaveFormat,
                DiscreteGroupItem,
                PivotFieldGroupOptions
            } = AsposeCells;
            console.log("Aspose.Cells initialized");
            document.getElementById('runExample').addEventListener('click', async () => {
                const workbook = new Workbook();
                const sheet = workbook.worksheets.get(0);
                const cells = sheet.cells;
                cells.get(0, 0).value = "product";
                cells.get(1, 0).value = "grape";
                cells.get(2, 0).value = "carrot";
                cells.get(3, 0).value = "potato";
                cells.get(4, 0).value = "cherry";
                const dateStyle = workbook.createStyle();
                dateStyle.custom = "m/d/yyyy";
                cells.get(0, 1).value = "date";
                cells.get(1, 1).value = new Date(2021, 1, 5);
                cells.get(2, 1).value = new Date(2022, 2, 8);
                cells.get(3, 1).value = new Date(2023, 3, 10);
                cells.get(4, 1).value = new Date(2024, 4, 16);
                for (let r = 1; r <= 4; r++) {
                    cells.get(r, 1).style = dateStyle;
                }
                cells.get(0, 2).value = "amount";
                cells.get(1, 2).value = 50;
                cells.get(2, 2).value = 60;
                cells.get(3, 2).value = 70;
                cells.get(4, 2).value = 80;
                // Add a pivot table with the destination cell A12 (row 11, column 0)
                const pivotTable = sheet.pivotTables.add("=Sheet1!A1:C5", 11, 0);
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "product");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "date");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "amount");
                pivotTable.pivotTableStyleType = AsposeCells.PivotTableStyleType.PivotTableStyleMedium10;
                // grape is item 0, carrot is item 1, potato is item 2, cherry is item 3
                // (zero-based positions in the order the items appear in the source data)
                const fruit = new DiscreteGroupItem("fruit", [0, 3]);
                const vegetable = new DiscreteGroupItem("vegetable", [1, 2]);
                const groupOptions = new PivotFieldGroupOptions();
                groupOptions.discreteGroupItems = [fruit, vegetable];
                pivotTable.rowFields.get(0).group(groupOptions);
                pivotTable.calculateData();
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "outputDiscreteGroupPivotFieldByIndex.xlsx";
                downloadLink.style.display = "block";
                document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            });
        });
    </script>
</html>
```

## **Note**

{{% alert color="primary" %}}
- Items that are not assigned to any custom group are not lost. They stay in the pivot table at the same level as the custom groups, each as its own single-item entry. In the example above, defining only the fruit group leaves carrot and potato in the row area as standalone entries next to the fruit group.
- The `PivotFieldGroupOptions.newPivotField` property controls the layout of discrete grouping. It defaults to true, which adds the grouped field as a new outer field beside the original one, producing the two-level layout shown above (`rowFields` grows to 2). Set it to false to replace the original field instead, the row area then shows a single level containing only the group names with their aggregated values, fruit 130 (50 + 80) and vegetable 130 (60 + 70).
- The name-based and index-based constructors of `DiscreteGroupItem` can be mixed within the same `discreteGroupItems` array.
{{% /alert %}}

## **Related Articles**
- [Group Pivot Fields in the Pivot Table](/cells/javascript-cpp/group-pivot-fields-in-the-pivot-table/)
- [Add Row and Column Fields in Pivot Table](/cells/javascript-cpp/pivot-table-add-row-and-column-fields/)
- [Filtering Pivot Tables by Label or Value](/cells/javascript-cpp/filter-by-label-or-value-of-pivot-table/)
- [Apply Style to Pivot Table](/cells/javascript-cpp/apply-style-to-pivot-table/)
- [Refresh Pivot Table](/cells/javascript-cpp/refresh-pivot-table/)

{{< app/cells/assistant language="javascript-cpp" >}}