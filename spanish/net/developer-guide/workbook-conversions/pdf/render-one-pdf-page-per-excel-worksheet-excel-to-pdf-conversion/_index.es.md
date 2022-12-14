---
title: Renderizar una página PDF por hoja de cálculo de Excel - Conversión de Excel a PDF
type: docs
weight: 100
url: /es/net/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/
---
{{% alert color="primary" %}} 

Cuando trabaje con archivos grandes de Excel Microsoft (por ejemplo, un libro de trabajo que tiene muchas hojas, cada una con 50 columnas y 300 o más filas de datos), es posible que desee que la salida PDF muestre una página por hoja de trabajo, independientemente del tamaño de la hoja de trabajo . Esto significaría que es probable que cada página tenga un tamaño de página radicalmente diferente. Esto se puede lograr usando Aspose.Cells for .NET.

{{% /alert %}} 

Consulte el siguiente código de muestra que convierte un archivo de Excel con varias hojas de cálculo a PDF.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderOnePdfPagePerExcelWorksheet-1.cs" >}}

{{% alert color="primary" %}} 

 Si el[Una página por hoja](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/onepagepersheet) la opción está configurada para**verdadero**, todo el contenido de la hoja se representará en una página PDF.

{{% /alert %}} {{% alert color="primary" %}} 

 Si su hoja de cálculo contiene fórmulas, es mejor llamar[Libro de trabajo. Calcular fórmula ()](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula)justo antes de convertir la hoja de cálculo en PDF. Esto garantiza que los valores dependientes de la fórmula se vuelvan a calcular y que los valores correctos se representen en el PDF.

{{% /alert %}}
