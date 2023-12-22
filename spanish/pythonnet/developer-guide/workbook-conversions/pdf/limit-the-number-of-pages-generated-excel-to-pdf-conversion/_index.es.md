---
title: "Limite el número de páginas generadas: conversión de Excel a PDF"
type: docs
weight: 180
url: /es/python-net/limit-the-number-of-pages-generated-excel-to-pdf-conversion/
description: Aprenda a limitar la cantidad de páginas generadas al renderizar Excel a PDF con Aspose.Cells for Python via .NET API.
keywords: Python Limit the Number of Pages Generated while Rendering Excel to PDF, Limit the Number of Pages Generated while saving Excel to PDF using Python, Python Set the Number of Pages Generated while converting Excel to PDF, Control the Number of Pages Generated for Excel to PDF in python
---
{{% alert color="primary" %}}

veces, desea imprimir un rango de páginas en un archivo de salida PDF. Aspose.Cells for Python via .NET tiene la capacidad de establecer un límite en la cantidad de páginas que se generan al convertir una hoja de cálculo de Excel al formato de archivo PDF.

{{% /alert %}}

##  **Limitar el número de páginas generadas**

El siguiente ejemplo muestra cómo representar un rango de páginas (3 y 4) en un archivo de Excel Microsoft a PDF.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-LimitNumberOfPagesGenerated-1.py" >}}

{{% alert color="primary" %}}

 Si la hoja de cálculo contiene fórmulas, es mejor llamar[Libro de trabajo.calcular_fórmula](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) método justo antes de representarlo en PDF. Hacerlo garantiza que los valores dependientes de la fórmula se recalculen y que los valores correctos se representen en el archivo de salida.

{{% /alert %}}
