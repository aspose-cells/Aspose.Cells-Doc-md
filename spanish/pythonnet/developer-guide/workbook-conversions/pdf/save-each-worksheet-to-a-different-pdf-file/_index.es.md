---
title: Guarde cada hoja de trabajo en un archivo PDF diferente
type: docs
weight: 130
url: /es/python-net/save-each-worksheet-to-a-different-pdf-file/
description: Aprenda a guardar cada hoja de trabajo en un archivo PDF diferente con Aspose.Cells for Python via .NET API.
keywords: Python Save Each Worksheet to a Different PDF File
---
{{% alert color="primary" %}} 

Aspose.Cells for Python via .NET admite la conversión de archivos XLS (que contienen imágenes, gráficos, etc.) a documentos PDF. Aspose.Cells for Python via .NET puede funcionar de forma independiente para convertir una hoja de cálculo a PDF y no es necesario utilizar Aspose.PDF for .NET para la conversión. La conversión no requiere que el software cree o utilice ningún archivo temporal ya que todo el proceso se puede realizar en la memoria.

{{% /alert %}} 
##  **Guarde cada hoja de trabajo en un archivo PDF diferente**
 Si necesita guardar cada hoja de trabajo en su archivo de plantilla de Excel para generar diferentes archivos PDF, puede hacerlo fácilmente. Puede intentar establecer el índice de una hoja en**[`PdfSaveOptions.sheet_set`](https://reference.aspose.com/cells/python-net/aspose.cells/paginatedsaveoptions/sheet_set/)** opción a la vez para rendir al PDF.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-SaveEachWorksheetToDifferentPDF-1.py" >}}

{{% alert color="primary" %}} 

 Si su hoja de cálculo contiene fórmulas, es mejor llamar[**Libro de trabajo.calculate_formula()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) justo antes de renderizar la hoja de cálculo al formato PDF. Al hacerlo, se garantizará que los valores dependientes de la fórmula se vuelvan a calcular y que los valores correctos se representen en PDF.

{{% /alert %}}
