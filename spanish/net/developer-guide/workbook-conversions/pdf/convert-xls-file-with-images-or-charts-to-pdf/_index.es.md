---
title: Convierta archivos XLS con imágenes o gráficos a PDF
type: docs
weight: 50
url: /es/net/convert-xls-file-with-images-or-charts-to-pdf/
---
{{% alert color="primary" %}} 

Aspose.Cells admite la conversión de archivos XLS que contienen imágenes y gráficos a documentos PDF. Aspose.Cells for .NET puede funcionar de forma independiente para convertir una hoja de cálculo a PDF: Aspose.PDF for .NET no es necesario para la conversión. El proceso se puede realizar en memoria ya que el proceso no depende de archivos XML temporales o intermediarios. Esto significa que los archivos grandes de Excel, por ejemplo, los que contienen imágenes, gráficos y otros objetos de dibujo, se pueden convertir de forma rápida y eficiente.

{{% /alert %}} 
## **Código de muestra**


{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ConvertXLSFileToPDF-1.cs" >}}

{{% alert color="primary" %}} 

 Si la hoja de cálculo contiene fórmulas, es mejor llamar al[Workbook.CalculateFormula](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula) justo antes de renderizar a PDF. Si lo hace, se asegurará de que los valores dependientes de la fórmula se vuelvan a calcular y los valores correctos se representen en el PDF.

{{% /alert %}}
