---
title: Guarde cada hoja de trabajo en un archivo PDF diferente
type: docs
weight: 130
url: /es/net/save-each-worksheet-to-a-different-pdf-file/
---
{{% alert color="primary" %}} 

Aspose.Cells admite la conversión de archivos XLS (que contienen imágenes, gráficos, etc.) a documentos PDF. Aspose.Cells for .NET puede funcionar de forma independiente para convertir una hoja de cálculo a PDF y no necesita usar Aspose.PDF for .NET para la conversión. La conversión no requiere que el software cree o use ningún archivo temporal, ya que todo el proceso se puede realizar en la memoria.

{{% /alert %}} 
##  **Guarde cada hoja de trabajo en un archivo PDF diferente**
 Si necesita guardar cada hoja de trabajo en su archivo de plantilla de Excel para generar diferentes archivos PDF, puede lograrlo fácilmente. Puede intentar establecer el índice de una hoja en**[`PdfSaveOptions.SheetSet`](https://reference.aspose.com/cells/net/aspose.cells/paginatedsaveoptions/sheetset/)** Opción a la hora de rendir al PDF.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-SaveEachWorksheetToDifferentPDF-1.cs" >}}

{{% alert color="primary" %}} 

 Si su hoja de cálculo contiene fórmulas, es mejor llamar[Libro de trabajo. Calcular fórmula ()](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula) justo antes de renderizar la hoja de cálculo al formato PDF. Si lo hace, se asegurará de que los valores dependientes de la fórmula se vuelvan a calcular y los valores correctos se representen en el PDF.

{{% /alert %}}
