---
title: Geben Sie an, ob das PivotTable für Excel2003 kompatibel ist, während das PivotTable aktualisiert wird
type: docs
weight: 80
url: /de/python-net/specify-whether-the-pivottable-is-compatible-for-excel2003-while-refreshing-pivottable/
description: In diesem Artikel wird gezeigt, wie Sie angeben, ob die Pivot Tabelle beim Aktualisieren der Pivot Tabelle mit Aspose.Cells für Python via .NET mit Excel2003 kompatibel ist.
keywords: Aspose.Cells für Python Excel, Excel Python Bibliothek, Angeben, ob die Pivot Tabelle beim Aktualisieren der Pivot Tabelle mit Excel2003 kompatibel ist
---

{{% alert color="primary" %}}

Aspose.Cells für Python via .NET bietet die Eigenschaft [**PivotTable.is_excel_2003_compatible**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/is_excel_2003_compatible/), mit der Sie angeben können, ob die Pivot-Tabelle beim Aktualisieren der Pivot-Tabelle mit Excel2003 kompatibel ist. Wenn der Wert **true** ist, muss die Zeichenfolge kleiner oder gleich 255 Zeichen sein. Ist die Zeichenfolge jedoch größer als 255 Zeichen, wird sie gekürzt. Ist **false** wird die Zeichenfolge nicht eingeschränkt. Der Standardwert ist **true**.

{{% /alert %}}

## **Wie man angibt, ob die Pivot-Tabelle beim Aktualisieren der Pivot-Tabelle mit Excel2003 kompatibel ist**

Der folgende Beispielcode erläutert die Verwendung der [**PivotTable.is_excel_2003_compatible**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/is_excel_2003_compatible/) Eigenschaft. Die ursprüngliche Zeichenfolge ist 383 Zeichen lang. Wenn die [**PivotTable.is_excel_2003_compatible**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/is_excel_2003_compatible/) Eigenschaft auf **true** gesetzt und das Pivot-Table aktualisiert wird, wird die Datenzelle B5 des Pivot-Table abgeschnitten und ist dann 255 Zeichen lang. Wenn jedoch die [**PivotTable.is_excel_2003_compatible**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/is_excel_2003_compatible/) Eigenschaft auf **false** gesetzt wird und das Pivot-Table erneut aktualisiert wird, wird die Datenzelle B5 des Pivot-Table nicht abgeschnitten und bleibt 383 Zeichen lang. Bitte lesen Sie die Kommentare im Code für ein besseres Verständnis dieser Eigenschaft.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-SpecifyCompatibility-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
