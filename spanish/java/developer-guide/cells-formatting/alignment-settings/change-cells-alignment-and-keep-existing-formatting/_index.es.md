---
title: Cambiar la Alineación de las Celdas y Mantener el Formato Existente
type: docs
weight: 260
url: /es/java/change-cells-alignment-and-keep-existing-formatting/
---

## **Escenarios de uso posibles**

A veces, desea cambiar la alineación de múltiples celdas pero también desea mantener el formato existente. Aspose.Cells le permite hacerlo usando la propiedad [**StyleFlag.Alignments**](https://reference.aspose.com/cells/java/com.aspose.cells/styleflag#Alignments). Si lo establece como **true**, los cambios en la alineación se llevarán a cabo, de lo contrario no. Tenga en cuenta que se pasa el objeto [**StyleFlag**](https://reference.aspose.com/cells/java/com.aspose.cells/StyleFlag) como parámetro al método [**Range.applyStyle()**](https://reference.aspose.com/cells/java/com.aspose.cells/range#applyStyle(com.aspose.cells.Style,%20com.aspose.cells.StyleFlag)) que aplica efectivamente el formato al rango de celdas.

## **Cambiar la alineación de las celdas y mantener el formato existente**

El siguiente código de muestra carga el [archivo de Excel de muestra](67338592.xlsx), crea el rango y lo alinea vertical y horizontalmente en el centro manteniendo el formato existente. La siguiente captura de pantalla compara el archivo de Excel de muestra y el [archivo de Excel de salida](67338591.xlsx) y muestra que todo el formato existente de las celdas es el mismo excepto que ahora las celdas están alineadas en el centro tanto horizontal como verticalmente.

![todo:image_alt_text](change-cells-alignment-and-keep-existing-formatting_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Data-ChangeCellsAlignmentAndKeepExistingFormatting.java" >}}
