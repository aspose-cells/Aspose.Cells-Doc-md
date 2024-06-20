---
title: Guardar Cada Hoja de Cálculo en un Archivo PDF Diferente
type: docs
weight: 130
url: /es/net/save-each-worksheet-to-a-different-pdf-file/
---

{{% alert color="primary" %}} 

Aspose.Cells admite la conversión de archivos XLS (que contienen imágenes, gráficos, etc.) a documentos PDF. Aspose.Cells for .NET puede trabajar de forma independiente para convertir una hoja de cálculo a PDF y no es necesario utilizar Aspose.PDF para .NET para la conversión. La conversión no requiere que el software cree o utilice archivos temporales, ya que todo el proceso se puede realizar en la memoria.

{{% /alert %}} 
## **Guardar cada hoja de cálculo en un archivo PDF diferente**
Si necesita guardar cada hoja de cálculo en su archivo de plantilla de Excel para generar archivos PDF diferentes, puede lograrlo fácilmente. Puede intentar configurar un índice de hoja a la vez con la opción [**PdfSaveOptions.SheetSet**](https://reference.aspose.com/cells/net/aspose.cells/paginatedsaveoptions/sheetset/) para renderizar a PDF.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-SaveEachWorksheetToDifferentPDF-1.cs" >}}

{{% alert color="primary" %}} 

Si su hoja de cálculo contiene fórmulas, es mejor llamar a [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula) justo antes de renderizar la hoja de cálculo en formato PDF. Al hacerlo, se asegurará de que los valores dependientes de las fórmulas se recalculen y los valores correctos se muestren en el PDF.

{{% /alert %}}
