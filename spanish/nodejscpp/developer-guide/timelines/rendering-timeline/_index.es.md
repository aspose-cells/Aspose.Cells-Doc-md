---
title: Renderizar Línea de Tiempo
type: docs
weight: 40
url: /es/nodejs-cpp/rendering-timeline/
description: Gestionar líneas de tiempo de archivos de Excel con Aspose.Cells for Node.js via C++.
keywords: Renderización de línea de tiempo sin Office 2013, Office 2016, Office 2019 y Office 365
---

## **Escenarios de uso posibles**
Aspose.Cells for Node.js via C++ soporta el renderizado de formas de línea de tiempo sin utilizar Office 2013, Office 2016, Office 2019 y Office 365. Si conviertes tu hoja de cálculo en una imagen o guardas tu libro de trabajo en formato PDF o HTML, verás que las líneas de tiempo se renderizan correctamente.

## **Renderización de Línea de tiempo**
El siguiente código de muestra carga el [archivo de Excel de muestra](input.xlsx) que contiene una línea de tiempo existente. Obtenga el objeto de forma según el nombre de la línea de tiempo y luego renderícelo en una imagen a través del método Shape.ToImage(). La imagen resultante es la [imagen de salida](out.png) que muestra la línea de tiempo renderizada. Como puede ver, la línea de tiempo se ha renderizado correctamente y se ve igual que en el archivo de Excel de muestra.

![todo:image_alt_text](out.png)
### **Código de muestra**
{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Timelines-RenderingTimeline.js" >}}
