---
title: Limitar el número de páginas generadas  Conversión de Excel a PDF
type: docs
weight: 180
url: /es/python-net/limit-the-number-of-pages-generated-excel-to-pdf-conversion/
description: Aprenda cómo limitar el número de páginas generadas al representar Excel en PDF con Aspose.Cells para Python via .NET API.
keywords: Limitar el número de páginas generadas en la representación de Excel en PDF con Python, Limitar el número de páginas generadas al guardar Excel en PDF con Python, Establecer el número de páginas generadas al convertir Excel en PDF con Python, Controlar el número de páginas generadas para Excel a PDF en python
---

{{% alert color="primary" %}}

A veces, quieres imprimir un rango de páginas en un archivo PDF de salida. Aspose.Cells for Python via .NET tiene la capacidad de establecer un límite en cuántas páginas se generan al convertir una hoja de cálculo de Excel al formato de archivo PDF.

{{% /alert %}}

## **Limitar el número de páginas generadas**

El siguiente ejemplo muestra cómo renderizar un rango de páginas (3 y 4) en un archivo de Microsoft Excel a PDF.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-LimitNumberOfPagesGenerated-1.py" >}}

{{% alert color="primary" %}}

Si la hoja de cálculo contiene fórmulas, es mejor llamar al método [Workbook.calculate_formula](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) justo antes de renderizarlo a PDF. Hacerlo asegura que los valores dependientes de fórmulas se recalculen y que los valores correctos se representen en el archivo de salida.

{{% /alert %}}
{{< app/cells/assistant language="python-net" >}}
