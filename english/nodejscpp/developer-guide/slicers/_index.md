---
title: Insert Slicer
linktitle: Slicers
type: docs
weight: 170
url: /nodejs-cpp/create-slicer/
description: Manage slicers of Excel files with Aspose.Cells for Node.js via C++.
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**

A slicer is used to filter data quickly. It can be used to filter data both in a table **and** a pivot table. Microsoft Excel allows you to create **a** slicer by selecting a table or pivot table and then clicking *Insert > Slicer*. Aspose.Cells for Node.js via C++ also allows you to create **a** slicer using the [**Worksheet.getSlicers().add()**](https://reference.aspose.com/cells/nodejs-cpp/slicercollection/#add-pivottable-string-string-) method.

## **Create Slicer to a Pivot Table**

Please see the following sample code. It loads the [sample Excel file](67338470.xlsx) that contains the pivot table. It then creates the slicer based on the first base pivot field. Finally, it saves the workbook in [output XLSX](67338471.xlsx) and [output XLSB](67338472.xlsb) **formats**. The following screenshot shows the slicer created by Aspose.Cells for Node.js via C++ in the output Excel file.

![todo:image_alt_text](create-slicer-to-a-pivot-table_1.png)

### **Sample Code**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Slicers-CreateSlicerToPivotTable.js" >}}

## **Create Slicer to Excel Table**

Please see the following sample code. It loads the [sample Excel file](sampleCreateSlicerToExcelTable.xlsx) that contains a table. It then creates the slicer based on the first column. Finally, it saves the workbook in [output XLSX](outputCreateSlicerToExcelTable.xlsx) format.

### **Sample Code**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Slicers-CreateSlicerToExcelTable-1.js" >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
