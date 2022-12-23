---
title: Geben Sie beim Aktualisieren der PivotTable an, ob die PivotTable mit Excel2003 kompatibel ist
type: docs
weight: 80
url: /de/net/specify-whether-the-pivottable-is-compatible-for-excel2003-while-refreshing-pivottable/
---
{{% alert color="primary" %}}

 Aspose.Cells bietet die[**PivotTable.IstExcel2003kompatibel**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/properties/isexcel2003compatible)-Eigenschaft, mit der Sie angeben können, ob die PivotTable beim Aktualisieren der PivotTable mit Excel2003 kompatibel ist. Wenn „true“, muss eine Zeichenfolge kleiner oder gleich 255 Zeichen sein. Wenn die Zeichenfolge also länger als 255 Zeichen ist, wird sie abgeschnitten. Wenn**FALSCH** , hat eine Zeichenfolge die oben genannte Einschränkung nicht. Der Standardwert ist**wahr**.

{{% /alert %}}

## **Geben Sie beim Aktualisieren der PivotTable an, ob die PivotTable mit Excel2003 kompatibel ist**

 Der folgende Beispielcode erläutert die Verwendung von[**PivotTable.IstExcel2003kompatibel**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/properties/isexcel2003compatible) Eigentum. Die ursprüngliche Zeichenfolge ist 383 Zeichen lang. Aber wenn[**PivotTable.IstExcel2003kompatibel**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/properties/isexcel2003compatible) Eigenschaft eingestellt ist**wahr** und Pivot-Tabelle aktualisiert wird, werden die Daten der Zelle B5 der Pivot-Tabelle abgeschnitten und werden 255 Zeichen lang. Allerdings wann[**PivotTable.IstExcel2003kompatibel**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/properties/isexcel2003compatible) Eigenschaft eingestellt ist**FALSCH** und die Pivot-Tabelle erneut aktualisiert wird, werden die Daten der Zelle B5 der Pivot-Tabelle nicht abgeschnitten und bleiben 383 Zeichen lang. Bitte lesen Sie die Kommentare im Code, um diese Eigenschaft besser zu verstehen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTableExamples-SpecifyCompatibility-1.cs" >}}
