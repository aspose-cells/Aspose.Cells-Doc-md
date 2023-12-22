---
title: Cambiar la alineación Cells y mantener el formato existente
description: Utilice la biblioteca Aspose.Cells para cambiar la alineación de las celdas y conservar el formato existente
keywords: Aspose.Cells, C#, Cell alignment, preserve existing formatting
type: docs
weight: 340
url: /es/net/change-cells-alignment-and-keep-existing-formatting/
---
##  **Posibles escenarios de uso**

A veces, desea cambiar la alineación de varias celdas pero también desea mantener el formato existente. Aspose.Cells te permite hacerlo usando el[**StyleFlag.Alineaciones**](https://reference.aspose.com/cells/net/aspose.cells/styleflag/properties/alignments) propiedad. Si lo establece como *verdadero**, se realizarán cambios en la alineación; de lo contrario, no. Tenga en cuenta,[**Bandera de estilo**](https://reference.aspose.com/cells/net/aspose.cells/styleflag) El objeto se pasa como parámetro a[**Rango.ApplyStyle()**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/applystyle)método que realmente aplica el formato a un rango de celdas.

##  **Cambiar la alineación Cells y mantener el formato existente**

 El siguiente código de muestra carga el[archivo de Excel de muestra](67338585.xlsx) , crea el rango y el centro lo alinea horizontal y verticalmente y mantiene intacto el formato existente. La siguiente captura de pantalla compara el archivo de Excel de muestra y[archivo de salida de Excel](67338586.xlsx) y muestra que todo el formato existente de las celdas es el mismo excepto que las celdas ahora están alineadas en el centro horizontal y verticalmente.

![todo:image_alt_text](change-cells-alignment-and-keep-existing-formatting_1.png)

##  **Código de muestra**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Data-ChangeCellsAlignmentAndKeepExistingFormatting.cs" >}}
