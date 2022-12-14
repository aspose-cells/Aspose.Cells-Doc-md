---
title: Ajustar todas las columnas de la hoja de trabajo en una sola página PDF
type: docs
weight: 160
url: /es/net/fit-all-worksheet-columns-on-single-pdf-page/
---
{{% alert color="primary" %}}

 veces desea generar un archivo PDF que se ajuste a todas las columnas de una hoja de trabajo en una sola página. los[**PdfSaveOptions.AllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/allcolumnsinonepagepersheet) property proporciona esta característica de una manera muy fácil de usar. Los cálculos complejos, como el alto y el ancho del PDF de salida, se manejan internamente y se basan en los datos de la hoja de cálculo.

{{% /alert %}}

## **Ajustar columnas de hoja de trabajo en una sola página PDF**

[**PdfSaveOptions.AllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/allcolumnsinonepagepersheet)garantiza que todas las columnas de una hoja de trabajo se representen en una sola página de PDF, aunque las filas pueden expandirse a varias páginas según los datos de la hoja de trabajo.

El siguiente código de ejemplo muestra cómo usar[**PdfSaveOptions.AllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/allcolumnsinonepagepersheet)propiedad para representar una gran hoja de trabajo de 100 columnas.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FitAllWorksheetColumns-1.cs" >}}

{{% alert color="primary" %}}

Cuando una hoja de cálculo determinada tiene muchas columnas, el archivo PDF representado puede mostrar el contenido en un tamaño muy pequeño. Todavía es legible cuando se amplía en una aplicación de visualización como Acrobat Reader.

{{% /alert %}} {{% alert color="primary" %}}

 Si su hoja de cálculo contiene fórmulas, es mejor llamar[**Libro de trabajo. Calcular fórmula ()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula) justo antes de convertir la hoja de cálculo en formato PDF. Si lo hace, se asegurará de que los valores dependientes de la fórmula se vuelvan a calcular y los valores correctos se representen en el PDF.

{{% /alert %}}
