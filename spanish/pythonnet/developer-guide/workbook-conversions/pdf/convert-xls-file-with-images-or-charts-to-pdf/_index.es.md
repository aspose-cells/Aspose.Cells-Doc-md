---
title: Convierta el archivo XLS con imágenes o gráficos a PDF
type: docs
weight: 50
url: /es/python-net/convert-xls-file-with-images-or-charts-to-pdf/
description: Aprenda a convertir un archivo XLS con imágenes o gráficos a PDF con Aspose.Cells for Python via .NET API.
keywords: Python Convert XLS File with Images or Charts to PDF, Convert xls to pdf using Python, Python XLS file with images to pdf, xls file with charts to pdf in python, python xls to pdf
---
{{% alert color="primary" %}} 

Aspose.Cells for Python via .NET admite la conversión de archivos XLS que contienen imágenes y gráficos a documentos PDF. Aspose.Cells for Python via .NET API puede funcionar de forma independiente para convertir una hoja de cálculo a PDF: Aspose.PDF for .NET no es necesario para la conversión. El proceso se puede realizar en la memoria ya que no depende de archivos XML temporales o intermediarios. Esto significa que los archivos grandes de Excel, por ejemplo los que contienen imágenes, gráficos y otros objetos de dibujo, se pueden convertir de forma rápida y eficiente.

{{% /alert %}} 
##  **Código de muestra**


{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-ConvertXLSFileToPDF-1.py" >}}

{{% alert color="primary" %}} 

 Si la hoja de cálculo contiene fórmulas, es mejor llamar a la[Libro de trabajo.calcular_fórmula](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) método justo antes de renderizar en PDF. Al hacerlo, se garantiza que los valores dependientes de la fórmula se recalculen y que los valores correctos se representen en PDF.

{{% /alert %}}
