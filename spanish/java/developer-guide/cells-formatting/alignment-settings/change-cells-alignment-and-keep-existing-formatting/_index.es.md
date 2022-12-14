---
title: Cambiar la alineación Cells y mantener el formato existente
type: docs
weight: 260
url: /es/java/change-cells-alignment-and-keep-existing-formatting/
---
## **Posibles escenarios de uso**

A veces, desea cambiar la alineación de varias celdas pero también desea mantener el formato existente. Aspose.Cells le permite hacerlo usando el[**StyleFlag.Alineaciones**](https://reference.aspose.com/cells/java/com.aspose.cells/styleflag#Alignments) propiedad. si lo vas a configurar**verdadero** , se producirán cambios en la alineación, de lo contrario no. Tenga en cuenta,[**Bandera de estilo**](https://reference.aspose.com/cells/java/com.aspose.cells/StyleFlag) El objeto se pasa como un parámetro a[**Rango.applyStyle()**](https://reference.aspose.com/cells/java/com.aspose.cells/range#applyStyle(com.aspose.cells.Style,%20com.aspose.cells.StyleFlag)) método que realmente aplica el formato al rango de celdas.

## **Cambiar la alineación Cells y mantener el formato existente**

El siguiente código de ejemplo carga el[ejemplo de archivo de Excel](67338592.xlsx), crea el rango y el centro lo alinea horizontal y verticalmente y mantiene intacto el formato existente. La siguiente captura de pantalla compara el archivo de ejemplo de Excel y[archivo de salida de Excel](67338591.xlsx)y muestra que todo el formato existente de las celdas es el mismo excepto que las celdas ahora están alineadas al centro horizontal y verticalmente.

![todo:imagen_alternativa_texto](change-cells-alignment-and-keep-existing-formatting_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Data-ChangeCellsAlignmentAndKeepExistingFormatting.java" >}}
