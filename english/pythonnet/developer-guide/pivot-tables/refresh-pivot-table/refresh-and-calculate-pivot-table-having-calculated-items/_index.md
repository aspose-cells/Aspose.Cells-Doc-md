---
title: Refresh and Calculate Pivot Table having Calculated Items
type: docs
weight: 40
url: /python-net/refresh-and-calculate-pivot-table-having-calculated-items/
description: This article shows how to refresh and calculate a pivot table having calculated items with Aspose.Cells for Python via .NET.
keywords: Aspose.Cells for Python Excel, Excel Python library, Refresh and Calculate Pivot Table with Calculated Items
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET now supports refreshing and calculating pivot tables having calculated items. Please use the [**PivotTable.refresh_data**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/refresh_data/#) and [**PivotTable.calculate_data**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/calculate_data/#) as usual to perform this function.

{{% /alert %}}

## **Refresh and Calculate Pivot Table having Calculated Items**

The following sample code loads the [source Excel file](5115238.xlsx) which contains a pivot table with three calculated items such as "add", "div", and "div2". We first change the value of cell D2 to 20 and then refresh and calculate the pivot table using Aspose.Cells for Python via .NET APIs, and save the workbook in PDF format. The results in the [output PDF](5115229.pdf) show that Aspose.Cells for Python via .NET refreshed and calculated the pivot table with calculated items successfully. You can verify this using Microsoft Excel by manually placing the value 20 in cell D2 and then refreshing the pivot table via the Alt+F5 shortcut key or by clicking the Refresh button.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTable-RefreshAndCalculateItems-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
