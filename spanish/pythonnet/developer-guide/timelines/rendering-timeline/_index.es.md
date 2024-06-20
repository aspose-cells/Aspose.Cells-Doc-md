---
title: Renderizar Línea de Tiempo
type: docs
weight: 40
url: /es/python-net/rendering-timeline/
description: Administrar líneas de tiempo de archivos de Excel con Aspose.Cells for Python via .NET.
keywords: Aspose.Cells para Python Excel, Biblioteca de Python de Excel, Renderizar línea de tiempo sin Excel, Renderizar línea de tiempo a imagen usando la biblioteca Aspose.Cells para Python.
---

## **Escenarios de uso posibles**
Aspose.Cells para Python via .NET admite el renderizado de formas de línea de tiempo sin necesidad de usar Office 2013, Office 2016, Office 2019 y Office 365. Si conviertes tu hoja de cálculo en una imagen o guardas tu libro de trabajo en formatos PDF o HTML, verás que las líneas de tiempo se renderizan correctamente.

## **Cómo Renderizar Línea de Tiempo Usando la Biblioteca de Excel Aspose.Cells para Python.**
El siguiente código de muestra carga el [archivo Excel de muestra](input.xlsx) que contiene una línea de tiempo existente. Obtiene el objeto de forma según el nombre de la línea de tiempo, y luego lo renderiza en una imagen a través del método Shape.to_image(). La imagen resultante es la [imagen de salida](out.png) que muestra la línea de tiempo renderizada. Como se puede ver, la línea de tiempo se ha renderizado correctamente y se ve igual que en el archivo Excel de muestra.

![todo:image_alt_text](out.png)
### **Código de muestra**
{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Timelines-RenderingTimeline.py" >}}

