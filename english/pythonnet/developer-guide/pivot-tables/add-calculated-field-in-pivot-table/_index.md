---
title: Add Calculated Field in Pivot Table
type: docs
weight: 130
url: /python-net/add-calculated-field-in-pivot-table/
description: How to add a calculated field in a pivot table with Aspose.Cells for Python via .NET.
keywords: Aspose.Cells for Python Excel, Excel Python library, Adding a calculated field in pivot table using Python Excel Library.
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**
When you create a pivot table based on known data, you may find that the data in it is not what you want. The data you need is a combination of the original data. For example, you might need to add, subtract, multiply, or divide the original values before using them. At that point, you need to build a calculated field and set the corresponding formula for calculation, then perform some statistics and other operations on the calculated field. 

## **How to Add a Calculated Field in a Pivot Table in Excel**
Insert a calculated field in a PivotTable in Excel by following these steps:

1. Select the PivotTable to which you want to add a calculated field.  
2. Go to the **PivotTable Analyze** tab on the ribbon.  
3. Click on **Fields, Items, & Sets** and then select **Calculated Field** from the drop‑down menu.  
4. In the **Name** field, enter a name for the calculated field.  
5. In the **Formula** field, enter the formula for the calculation you want to perform using the appropriate PivotTable field names and mathematical operators.  
   <br>
   <img src="1.png" width=80% />
6. Click **OK** to create the calculated field.  
7. The new calculated field will appear in the PivotTable Field List under the **Values** section.  
8. Drag the calculated field to the **Values** section of the PivotTable to display the calculated values.  
   <br>
   <img src="2.png" width=80% />

## **How to Add a Calculated Field in a Pivot Table Using Aspose.Cells for Python via .NET**
Add a calculated field to an Excel file using Aspose.Cells for Python via .NET. Please see the following sample code. After executing the example code, a pivot table with a calculated field is added to the worksheet.

1. Set the original data and create a pivot table.  
2. Create the calculated field based on the existing PivotField in the pivot table.  
3. Add the calculated field to the data area.  
4. Finally, the workbook is saved in the [output XLSX](out.xlsx) format.  

## **Sample Code**
{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-Add-calculated-field-in-PivotTable.py" >}}
{{< app/cells/assistant language="python-net" >}}
