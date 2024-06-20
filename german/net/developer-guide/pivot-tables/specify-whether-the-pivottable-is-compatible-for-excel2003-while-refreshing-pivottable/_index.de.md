---
title: Geben Sie an, ob das PivotTable für Excel2003 kompatibel ist, während das PivotTable aktualisiert wird
type: docs
weight: 80
url: /de/net/specify-whether-the-pivottable-is-compatible-for-excel2003-while-refreshing-pivottable/
---

{{% alert color="primary" %}}

Aspose.Cells bietet die Eigenschaft [**PivotTable.IsExcel2003Compatible**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/properties/isexcel2003compatible), die Sie verwenden können, um anzugeben, ob das PivotTable für Excel2003 kompatibel ist, während das PivotTable aktualisiert wird. Wenn **true**, muss eine Zeichenfolge kleiner oder gleich 255 Zeichen sein, daher wird die Zeichenfolge bei einer Länge über 255 Zeichen abgeschnitten. Wenn **false**, hat eine Zeichenfolge keine Einschränkung. Der Standardwert ist **true**.

{{% /alert %}}

## **Geben Sie an, ob das PivotTable für Excel2003 kompatibel ist, während das PivotTable aktualisiert wird**

Der folgende Beispielcode erläutert die Verwendung der [**PivotTable.IsExcel2003Compatible**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/properties/isexcel2003compatible) Eigenschaft. Die ursprüngliche Zeichenfolge ist 383 Zeichen lang. Wenn die [**PivotTable.IsExcel2003Compatible**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/properties/isexcel2003compatible) Eigenschaft auf **true** gesetzt und das Pivot-Table aktualisiert wird, wird die Datenzelle B5 des Pivot-Table abgeschnitten und ist dann 255 Zeichen lang. Wenn jedoch die [**PivotTable.IsExcel2003Compatible**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/properties/isexcel2003compatible) Eigenschaft auf **false** gesetzt wird und das Pivot-Table erneut aktualisiert wird, wird die Datenzelle B5 des Pivot-Table nicht abgeschnitten und bleibt 383 Zeichen lang. Bitte lesen Sie die Kommentare im Code für ein besseres Verständnis dieser Eigenschaft.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTableExamples-SpecifyCompatibility-1.cs" >}}
