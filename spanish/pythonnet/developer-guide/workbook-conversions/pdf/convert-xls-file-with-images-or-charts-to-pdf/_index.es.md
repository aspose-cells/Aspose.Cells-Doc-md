---
title: Convertir archivo XLS con imágenes o gráficos a PDF
type: docs
weight: 50
url: /es/python-net/convert-xls-file-with-images-or-charts-to-pdf/
description: Aprende cómo Convertir Archivo XLS con Imágenes o Gráficos a PDF con el API de Aspose.Cells para Python via .NET.
keywords: Python Convertir Archivo XLS con Imágenes o Gráficos a PDF, Convertir xls a pdf usando Python, Archivo xls con imágenes a pdf en python, archivo xls con gráficos a pdf en python, python xls a pdf
---

{{% alert color="primary" %}} 

Aspose.Cells para Python via .NET admite la conversión de archivos XLS que contienen imágenes y gráficos a documentos PDF. La API de Aspose.Cells para Python via .NET puede funcionar de forma independiente para convertir una hoja de cálculo a PDF: No se requiere Aspose.PDF para .NET para la conversión. El proceso puede realizarse en memoria ya que no depende de archivos XML temporales o intermedios. Esto significa que los archivos de Excel grandes, por ejemplo, aquellos que contienen imágenes, gráficos y otros objetos de dibujo, pueden convertirse de manera rápida y eficiente.

{{% /alert %}} 
## **Código de muestra**


{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-ConvertXLSFileToPDF-1.py" >}}

{{% alert color="primary" %}} 

Si la hoja de cálculo contiene fórmulas, es mejor llamar al método [Workbook.calculate_formula](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) justo antes de renderizar a PDF. De esta manera se asegura que los valores dependientes de la fórmula se recalculen y los valores correctos se representen en el PDF.

{{% /alert %}}
{{< app/cells/assistant language="python-net" >}}
