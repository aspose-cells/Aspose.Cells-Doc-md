---
title: Convertir archivo XLS con imágenes o gráficos a PDF
type: docs
weight: 50
url: /es/net/convert-xls-file-with-images-or-charts-to-pdf/
---

{{% alert color="primary" %}} 

Aspose.Cells admite la conversión de archivos XLS que contienen imágenes y gráficos a documentos PDF. Aspose.Cells for .NET puede trabajar de forma independiente para convertir una hoja de cálculo a PDF: no se requiere Aspose.PDF para .NET para la conversión. El proceso puede realizarse en memoria ya que no depende de archivos XML temporales o intermedios. Esto significa que los archivos de Excel grandes, por ejemplo, aquellos que contienen imágenes, gráficos y otros objetos de dibujo, pueden convertirse rápidamente y de manera eficiente.

{{% /alert %}} 
## **Código de muestra**


{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ConvertXLSFileToPDF-1.cs" >}}

{{% alert color="primary" %}} 

Si la hoja de cálculo contiene fórmulas, es mejor llamar al método [Workbook.CalculateFormula](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula) justo antes de renderizar a PDF. Al hacerlo, se asegura que se vuelvan a calcular los valores dependientes de las fórmulas, y que los valores correctos se rendericen en el PDF.

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
