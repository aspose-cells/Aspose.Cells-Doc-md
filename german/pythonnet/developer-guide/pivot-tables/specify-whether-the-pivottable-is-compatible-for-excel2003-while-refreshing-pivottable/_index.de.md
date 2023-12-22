---
title: Geben Sie beim Aktualisieren von PivotTable an, ob die PivotTable mit Excel2003 kompatibel ist
type: docs
weight: 80
url: /de/python-net/specify-whether-the-pivottable-is-compatible-for-excel2003-while-refreshing-pivottable/
description: In diesem Artikel wird gezeigt, wie Sie angeben, ob die PivotTable mit Excel2003 kompatibel ist, während Sie PivotTable mit Aspose.Cells for Python via .NET aktualisieren.
keywords: Specify whether the PivotTable is compatible for Excel2003 while refreshing PivotTable
---
{{% alert color="primary" %}}

 Aspose.Cells for Python via .NET bietet die[**PivotTable.is_excel_2003_kompatibel**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/is_excel_2003_compatible/) -Eigenschaft, mit der Sie beim Aktualisieren von PivotTable angeben können, ob die PivotTable mit Excel2003 kompatibel ist. Bei „true“ muss eine Zeichenfolge kleiner oder gleich 255 Zeichen sein. Wenn die Zeichenfolge also mehr als 255 Zeichen umfasst, wird sie abgeschnitten. Bei *false** gilt für eine Zeichenfolge nicht die oben genannte Einschränkung. Der Standardwert ist *true**.

{{% /alert %}}

##  **Geben Sie beim Aktualisieren von PivotTable an, ob die PivotTable mit Excel2003 kompatibel ist**

 Der folgende Beispielcode erläutert die Verwendung von[**PivotTable.is_excel_2003_kompatibel**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/is_excel_2003_compatible/) Eigentum. Die ursprüngliche Zeichenfolge ist 383 Zeichen lang. Aber wenn[**PivotTable.is_excel_2003_kompatibel**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/is_excel_2003_compatible/) Eigenschaft ist festgelegt**WAHR** und die Pivot-Tabelle aktualisiert wird, werden die Daten der Zelle B5 der Pivot-Tabelle abgeschnitten und sie wird 255 Zeichen lang. Wann jedoch[**PivotTable.is_excel_2003_kompatibel**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/is_excel_2003_compatible/) Eigenschaft ist festgelegt**FALSCH**Wenn die Pivot-Tabelle erneut aktualisiert wird, werden die Daten der Zelle B5 der Pivot-Tabelle nicht abgeschnitten und bleiben weiterhin 383 Zeichen lang. Bitte lesen Sie die Kommentare im Code, um diese Eigenschaft besser zu verstehen.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-SpecifyCompatibility-1.py" >}}
