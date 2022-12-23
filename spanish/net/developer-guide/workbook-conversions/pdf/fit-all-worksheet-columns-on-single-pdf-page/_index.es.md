---
title: Ajustar todas las columnas de la hoja de trabajo en una sola página PDF
type: docs
weight: 160
url: /es/net/fit-all-worksheet-columns-on-single-pdf-page/
---
{{% alert color="primary" %}}

 A veces desea generar un archivo PDF que ajuste todas las columnas de una hoja de trabajo en una sola página. Él[**PdfSaveOptions.AllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/allcolumnsinonepagepersheet) property proporciona esta característica de una manera muy fácil de usar. Los cálculos complejos, como la altura y el ancho de la salida PDF, se manejan internamente y se basan en los datos de la hoja de trabajo.

{{% /alert %}}

## **Ajustar columnas de la hoja de trabajo en una sola página PDF**

[**PdfSaveOptions.AllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/allcolumnsinonepagepersheet)asegura que todas las columnas en una hoja de trabajo se representen en una sola página PDF, aunque las filas pueden expandirse a varias páginas dependiendo de los datos en la hoja de trabajo.

El siguiente código de ejemplo muestra cómo usar[**PdfSaveOptions.AllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/allcolumnsinonepagepersheet)propiedad para representar una gran hoja de trabajo de 100 columnas.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FitAllWorksheetColumns-1.cs" >}}

{{% alert color="primary" %}}

Cuando una hoja de cálculo determinada tiene muchas columnas, el archivo PDF representado puede mostrar el contenido en un tamaño muy pequeño. Todavía es legible cuando se amplía en una aplicación de visualización como Acrobat Reader.

{{% /alert %}} {{% alert color="primary" %}}

Si su hoja de cálculo contiene fórmulas, es mejor llamar[**Libro de trabajo. Calcular fórmula ()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula)justo antes de renderizar la hoja de cálculo al formato PDF. Si lo hace, se asegurará de que los valores dependientes de la fórmula se vuelvan a calcular y los valores correctos se representen en el PDF.

{{% /alert %}}
