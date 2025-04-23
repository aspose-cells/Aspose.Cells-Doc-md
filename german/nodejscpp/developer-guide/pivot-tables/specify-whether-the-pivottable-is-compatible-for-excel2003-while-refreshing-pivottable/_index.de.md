---
title: Geben Sie an, ob das PivotTable für Excel2003 kompatibel ist, während das PivotTable aktualisiert wird
type: docs
weight: 80
url: /de/nodejs-cpp/specify-whether-the-pivottable-is-compatible-for-excel2003-while-refreshing-pivottable/
---

{{% alert color="primary" %}}

Aspose.Cells for Node.js via C++ stellt die Eigenschaft [**PivotTable.setIsExcel2003Compatible**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#setIsExcel2003Compatible-boolean-) bereit, die verwendet werden kann, um anzugeben, ob die PivotTable kompatibel mit Excel2003 ist, während die PivotTable aktualisiert wird. Wenn true, muss ein String kleiner oder gleich 255 Zeichen sein, sodass bei längeren Strings diese abgeschnitten werden. Wenn **false**, unterliegt der String keine der genannten Beschränkungen. Der Standardwert ist **true**.

{{% /alert %}}

## **Geben Sie an, ob das PivotTable für Excel2003 kompatibel ist, während das PivotTable aktualisiert wird**

Der folgende Beispielcode erläutert die Verwendung der [**PivotTable.setIsExcel2003Compatible**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#setIsExcel2003Compatible-boolean-) Eigenschaft. Die ursprüngliche Zeichenfolge ist 383 Zeichen lang. Wenn die [**PivotTable.setIsExcel2003Compatible**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#setIsExcel2003Compatible-boolean-) Eigenschaft auf **true** gesetzt und das Pivot-Table aktualisiert wird, wird die Datenzelle B5 des Pivot-Table abgeschnitten und ist dann 255 Zeichen lang. Wenn jedoch die [**PivotTable.setIsExcel2003Compatible**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#setIsExcel2003Compatible-boolean-) Eigenschaft auf **false** gesetzt wird und das Pivot-Table erneut aktualisiert wird, wird die Datenzelle B5 des Pivot-Table nicht abgeschnitten und bleibt 383 Zeichen lang. Bitte lesen Sie die Kommentare im Code für ein besseres Verständnis dieser Eigenschaft.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-SpecifyCompatibility-1.js" >}}

