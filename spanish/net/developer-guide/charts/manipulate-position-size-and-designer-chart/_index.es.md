---
title: Manipular la Posición, Tamaño y Diseño del Gráfico
description: Aprenda a utilizar Aspose.Cells for .NET para manipular de manera efectiva la posición, tamaño y diseño del gráfico en Microsoft Excel. Nuestra guía demostrará cómo ajustar estas propiedades para mejorar el diseño y la visualización.
keywords: Aspose.Cells for .NET, Posición, Tamaño, Diseño del Gráfico, Microsoft Excel, Diseño, Visualización.
type: docs
weight: 45
url: /es/net/manipulate-position-size-and-designer-chart/
---

## **Posición y Tamaño del Gráfico**
A veces, desea cambiar la posición o tamaño del gráfico nuevo o existente dentro de la hoja de cálculo. Aspose.Cells proporciona la propiedad [Chart.ChartObject](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/properties/chartobject) para lograr esto. Puede utilizar sus subpropiedades para cambiar el tamaño del gráfico con una nueva **altura** y **ancho** o reposicionarlo con nuevas coordenadas **X** y **Y**.
### **Controlar la Posición y Tamaño del Gráfico**
Para cambiar la posición (coordenadas X, Y) o el tamaño (altura, ancho) del gráfico, use estas propiedades:

1. [Chart.ChartObject.X](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/x)
1. [Chart.ChartObject.Y](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/y)
1. [Chart.ChartObject.Height](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/height)
1. [Chart.ChartObject.Width](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/width)

El siguiente ejemplo explica el uso de las API anteriores. Carga el libro existente que contiene un gráfico en su primera hoja de trabajo. Luego redimensiona y reposiciona el gráfico utilizando Aspose.Cells.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ChangeChartPosition-1.cs" >}}
## **Manipulación de gráficos de diseñador**
Hay momentos en los que necesitas manipular o modificar gráficos en archivos de plantillas de diseñador. Aspose.Cells es compatible con la manipulación de contenidos y elementos de gráficos de diseñador. Los datos, los contenidos del gráfico, la imagen de fondo y los formatos se pueden preservar con precisión.
### **Manipulación de gráficos de diseñador en archivos de plantillas**
Para manipular gráficos de diseñador en archivos de plantillas, utiliza la API relacionada con los gráficos. Por ejemplo, puedes usar la propiedad Worksheet.Charts para obtener la colección de gráficos existentes en el archivo de plantilla.
#### **Creación de un gráfico**
El siguiente ejemplo muestra cómo crear un gráfico de pirámide. Más adelante manipularemos este gráfico.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-HowToCreateChart-1.cs" >}}
#### **Manipulación del gráfico**
El siguiente ejemplo muestra cómo manipular el gráfico existente. En este ejemplo, modificamos el gráfico creado anteriormente. En la salida generada, se observa que la etiqueta de fecha de un punto de datos se ha establecido en 'Reino Unido, 30K'.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-ModifyPieChart-1.cs" >}}
#### **Manipulación de un gráfico de líneas en la plantilla de diseñador**
En este ejemplo, manipularemos un gráfico de líneas. Agregaremos algunas series de datos al gráfico existente y cambiaremos sus colores de línea.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-ModifyLineChart-1.cs" >}}

