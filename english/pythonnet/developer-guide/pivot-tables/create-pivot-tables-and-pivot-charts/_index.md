---
title: Create Pivot Tables and Pivot Charts
type: docs
weight: 20
url: /python-net/create-pivot-tables-and-pivot-charts/
description: How to add Pivot Tables and Pivot Charts with Aspose.Cells for Python via .NET.
keywords: Aspose.Cells for Python Excel, Excel Python library, Add Pivot Tables and Pivot Charts Using Aspose.Cells for Python Excel Library.
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

A pivot table is an interactive summary of records. For example, you may have hundreds of invoice entries in a list in a worksheet. A pivot table can total the invoices by customer, product or date. With Microsoft Excel it is possible to quickly re-arrange the information in the pivot table by dragging buttons to a new position.

A pivot chart is an interactive graphical representation of the data in a pivot table. Pivot charts were introduced in Excel 2000. Using a pivot chart makes it even easier to understand the data since the pivot table creates subtotals and totals automatically.

Aspose.Cells for Python via .NET supports [pivot tables](/cells/python-net/create-pivot-tables-and-pivot-charts/) and [pivot charts](/cells/python-net/create-pivot-tables-and-pivot-charts/).

{{% /alert %}}

## **Add Pivot Tables and Charts Using Aspose.Cells for Python Excel Library**

Aspose.Cells for Python via .NET provides a special set of classes used to create pivot tables. These classes are used to create and set PivotTable objects, which act as a PivotTable object's basic building blocks:

- PivotField, a field in a pivot table report.
- PivotFields, a collection of all the PivotField objects in a pivot table.
- PivotTable, a PivotTable report on a worksheet.
- PivotTables, a collection of all the PivotTable objects on the worksheet.

### **Prepare to use Aspose.Cells for Python via .NET**
1. Install Aspose.Cells for Python via .NET from [pypi](https://pypi.org/project/aspose-cells-python/), use command as: $ pip install aspose-cells-python.
1. You can also follow the step-by-step instructions on how to install “Aspose.Cells for Python via .NET” to your developer environment.


### **How to Add a Pivot Table Using Aspose.Cells for Python Excel Library**

To create a pivot table using Aspose.Cells for Python via .NET:

1. Add some data to a worksheet cells using a Cell object's put_value method. You also use a template file already filled with data. The data will be used as the pivot table's data source.
1. Add a pivot table to the worksheet by calling the PivotTables collection's add method (encapsulated in the Worksheet object).
1. Access the new PivotTable object from the PivotTables collection by passing its index. # Use any of the pivot table objects encapsulated in the PivotTable object to manage the table.

Code examples are given below.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-CreatePivotTablesPivotCharts-CreatePivotTable-1.py" >}}

### **How to Add a Pivot Chart Using Aspsoe.Cells for Python Excel Library**

To create a PivotChart using Aspose.Cells for Python via .NET:

1. Add a chart.
1. Set the PivotSource of the chart to refer to an existing pivot table in the spreadsheet.
1. Set other attributes.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-CreatePivotTablesPivotCharts-CreatePivotChart-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
