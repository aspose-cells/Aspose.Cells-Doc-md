---
title: Ajustar todas las columnas de la hoja de trabajo en una sola página de PDF
type: docs
weight: 160
url: /es/net/fit-all-worksheet-columns-on-single-pdf-page/
---

{{% alert color="primary" %}}

A veces deseas generar un archivo PDF que ajuste todas las columnas de una hoja de trabajo en una sola página. La propiedad [**PdfSaveOptions.AllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/allcolumnsinonepagepersheet) proporciona esta función de una manera muy fácil de usar. Los cálculos complejos como la altura y el ancho del PDF de salida se manejan internamente y se basan en los datos de la hoja de trabajo.

{{% /alert %}}

## **Ajustar las columnas de la hoja de trabajo en una sola página de PDF**

[**PdfSaveOptions.AllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/allcolumnsinonepagepersheet) asegura que todas las columnas de una hoja de trabajo se representen en una sola página de PDF, aunque las filas pueden expandirse en varias páginas dependiendo de los datos en la hoja de trabajo.

El código de muestra a continuación muestra cómo utilizar la propiedad [**PdfSaveOptions.AllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/allcolumnsinonepagepersheet) para representar una hoja de cálculo grande de 100 columnas.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FitAllWorksheetColumns-1.cs" >}}

{{% alert color="primary" %}}

Cuando una hoja de trabajo determinada tiene muchas columnas, el archivo PDF generado puede mostrar el contenido en un tamaño muy pequeño. Aún será legible cuando se amplíe en una aplicación de visualización como Acrobat Reader.

{{% /alert %}} {{% alert color="primary" %}}

Si su hoja de cálculo contiene fórmulas, es mejor llamar a [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula) justo antes de renderizar la hoja de cálculo en formato PDF. Al hacerlo, se asegurará de que los valores dependientes de las fórmulas se recalculen y los valores correctos se muestren en el PDF.

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
