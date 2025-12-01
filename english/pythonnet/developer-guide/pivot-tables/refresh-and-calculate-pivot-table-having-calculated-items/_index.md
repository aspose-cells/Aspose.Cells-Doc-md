---
title: Refresh and Calculate Pivot Table having Calculated Items
type: docs
weight: 40
url: /python-net/refresh-and-calculate-pivot-table-having-calculated-items/
description: This article shows how to Refresh and Calculate Pivot Table having Calculated Items with Aspose.Cells for Python via .NET.
keywords: Aspose.Cells for Python Excel, Excel Python library, Refresh and Calculate Pivot Table with Calculated Items
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET now supports refreshing and calculating pivot table having calculated items. Please use the [**PivotTable.refresh_data**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/refresh_data/#) and [**PivotTable.calculate_data**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/calculate_data/#) as usual to perform this function.

{{% /alert %}}

## **Refresh and Calculate Pivot Table having Calculated Items**

The following sample code loads the [source excel file](5115238.xlsx) which contains a pivot table having three calculated items such as "add", "div", "div2". We first change the value of cell D2 to 20 and then refresh and calculate pivot table using Aspose.Cells for Python via .NET APIs and save the workbook in PDF format. The results in the [output PDF](5115229.pdf) shows that Aspose.Cells for Python via .NET refreshed and calculated the pivot table having calculated items successfully. You can verify it using Microsoft Excel by manually putting the value 20 in cell D2 and then refreshing the pivot table via Alt+F5 shortcut key or clicking the pivot table Refresh button.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTable-RefreshAndCalculateItems-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
