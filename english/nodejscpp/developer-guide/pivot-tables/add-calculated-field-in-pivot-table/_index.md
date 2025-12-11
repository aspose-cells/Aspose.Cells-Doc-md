---
title: Add calculated field in Pivot Table
type: docs
weight: 130
url: /nodejs-cpp/add-calculated-field-in-pivot-table/
description: How to add a calculated field in a pivot table with Aspose.Cells for Node.js via C++.
keywords: Aspose.Cells for Node.js via C++ Excel, Excel Node.js library, Adding a calculated field in pivot table using Node.js Excel Library.
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**
When you create a pivot table based on known data, you may find that the data is not what you need. The data you require is often a combination of the original data. For example, you might need to add, subtract, multiply, or divide the original values before obtaining the desired results. In such cases, you need to build a calculated field and set the corresponding formula for the calculation, then perform statistical and other operations on that calculated field.

## **How to Add a Calculated Field in Pivot Table in Excel**
To insert a calculated field in a PivotTable in Excel, follow these steps:

1. Select the PivotTable to which you want to add a calculated field.  
2. Go to the **PivotTable Analyze** tab on the ribbon.  
3. Click **Fields, Items, & Sets** and then select **Calculated Field** from the drop‑down menu.  
4. In the **Name** field, enter a name for the calculated field.  
5. In the **Formula** field, enter the formula for the calculation you want to perform using the appropriate PivotTable field names and mathematical operators.  
   <br>
   <img src="1.png" width=80% />
6. Click **OK** to create the calculated field.  
7. The new calculated field will appear in the PivotTable Field List under the **Values** section.  
8. Drag the calculated field to the **Values** section of the PivotTable to display the calculated values.  
   <br>
   <img src="2.png" width=80% />

## **How to Add a Calculated Field in Pivot Table Using Aspose.Cells for Node.js via C++ Library**
Add a calculated field to an Excel file using Aspose.Cells for Node.js via C++. Please see the following sample code. After executing the example code, a pivot table with a calculated field is added to the worksheet.

1. Set the original data and create a pivot table.  
2. Create the calculated field according to the existing **PivotField** in the pivot table.  
3. Add the calculated field to the data area.  
4. Finally, the workbook is saved in [output XLSX](out.xlsx) format.  

## **Sample Code**
{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-Add-calculated-field-in-PivotTable.js" >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
