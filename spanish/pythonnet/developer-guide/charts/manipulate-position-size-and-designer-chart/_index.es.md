---
title: Manipular la Posición, Tamaño y Diseño del Gráfico
description: Aprende cómo usar Aspose.Cells para Python via .NET para manipular efectivamente la posición, tamaño y diseño del gráfico en Microsoft Excel. Nuestra guía demostrará cómo ajustar estas propiedades para mejorar la distribución y visualización.
keywords: Aspose.Cells para Python via .NET, Posición, Tamaño, Gráfico de diseño, Microsoft Excel, Distribución, Visualización.
type: docs
weight: 45
url: /es/python-net/manipulate-position-size-and-designer-chart/
---

## **Posición y Tamaño del Gráfico**
A veces, quieres cambiar la posición o tamaño del gráfico nuevo o existente dentro de la hoja de cálculo. Aspose.Cells para Python via .NET proporciona la propiedad [Chart.chart_object](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/chart_object) para lograr esto. Puedes usar sus subpropiedades para redimensionar el gráfico con una nueva altura y anchura o reubicarlo con nuevas coordenadas X y Y.
### **Controlar la Posición y Tamaño del Gráfico**
Para cambiar la posición (coordenadas X, Y) o el tamaño (altura, ancho) del gráfico, use estas propiedades:

1. [Chart.chart_object.x](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/x)
1. [Chart.chart_object.y](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/y)
1. [Chart.chart_object.height](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/height)
1. [Chart.chart_object.width](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/width)

El siguiente ejemplo explica cómo usar las APIs anteriores, carga el libro existente que contiene un gráfico en su primera hoja y luego lo redimensiona y reubica usando Aspose.Cells para Python via .NET.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ChangeChartPosition-1.py" >}}
## **Manipulación de gráficos de diseñador**
Hay momentos en que necesitas manipular o modificar gráficos en archivos de plantilla de diseño. Aspose.Cells para Python via .NET soporta completamente la manipulación de contenidos y elementos de gráficos de diseño. Los datos, contenidos del gráfico, imagen de fondo y formatos pueden ser preservados con precisión.
### **Manipulación de gráficos de diseñador en archivos de plantillas**
Para manipular gráficos de diseñador en archivos de plantillas, utiliza la API relacionada con los gráficos. Por ejemplo, puedes usar la propiedad Worksheet.Charts para obtener la colección de gráficos existentes en el archivo de plantilla.
#### **Creación de un gráfico**
El siguiente ejemplo muestra cómo crear un gráfico de pirámide. Más adelante manipularemos este gráfico.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-HowToCreateChart-1.py" >}}
#### **Manipulación del gráfico**
El siguiente ejemplo muestra cómo manipular el gráfico existente. En este ejemplo, modificamos el gráfico creado anteriormente. En la salida generada, se observa que la etiqueta de fecha de un punto de datos se ha establecido en 'Reino Unido, 30K'.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ManipulateChart-ModifyPieChart-1.py" >}}
#### **Manipulación de un gráfico de líneas en la plantilla de diseñador**
En este ejemplo, manipularemos un gráfico de líneas. Agregaremos algunas series de datos al gráfico existente y cambiaremos sus colores de línea.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ManipulateChart-ModifyLineChart-1.py" >}}

