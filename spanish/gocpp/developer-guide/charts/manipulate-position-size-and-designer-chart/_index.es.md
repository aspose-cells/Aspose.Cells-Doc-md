---
title: Manipular tamaño, posición y diseñador del gráfico con Golang vía C++
linktitle: Manipular la Posición, Tamaño y Diseño del Gráfico
description: Aprende cómo usar Aspose.Cells for C++ para manipular eficazmente la posición, tamaño y diseñador de gráficos en Microsoft Excel. Nuestra guía demostrará cómo ajustar estas propiedades para mejorar el diseño y la visualización.
keywords: Aspose.Cells for C++, Posición, Tamaño, Diseñador de gráficos, Microsoft Excel, Diseño, Visualización.
type: docs
weight: 45
url: /es/go-cpp/manipulate-position-size-and-designer-chart/
---

## **Posición y Tamaño del Gráfico**
A veces, deseas cambiar la posición o tamaño del gráfico nuevo o existente dentro de la hoja de cálculo. Aspose.Cells proporciona la propiedad [Chart.GetChartObject()](https://reference.aspose.com/cells/go-cpp/chart/getchartobject/) para lograr esto. Puedes usar sus subpropiedades para cambiar el tamaño del gráfico con una nueva **altura** y **anchura** o reposicionarlo con nuevas coordenadas **X** y **Y**.

### **Controlar la Posición y Tamaño del Gráfico**
Para cambiar la posición (coordenadas X, Y) o el tamaño (altura, ancho) del gráfico, use estas propiedades:

1. [Chart.GetX()](https://reference.aspose.com/cells/go-cpp/shape/getx/)
1. [Chart.GetY()](https://reference.aspose.com/cells/go-cpp/shape/gety/)
1. [Chart.GetHeight()](https://reference.aspose.com/cells/go-cpp/shape/getheight/)
1. [Chart.GetWidth()](https://reference.aspose.com/cells/go-cpp/shape/getwidth/)

El siguiente ejemplo explica el uso de las API anteriores. Carga el libro existente que contiene un gráfico en su primera hoja de trabajo. Luego redimensiona y reposiciona el gráfico utilizando Aspose.Cells.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ManipulatePositionSizeAndDesignerChart.go" >}}
## **Manipulación de gráficos de diseñador**
Hay momentos en los que necesitas manipular o modificar gráficos en archivos de plantillas de diseñador. Aspose.Cells es compatible con la manipulación de contenidos y elementos de gráficos de diseñador. Los datos, los contenidos del gráfico, la imagen de fondo y los formatos se pueden preservar con precisión.

### **Manipulación de gráficos de diseñador en archivos de plantillas**
Para manipular gráficos de diseñador en archivos de plantillas, utiliza la API relacionada con los gráficos. Por ejemplo, puedes usar la propiedad Worksheet.Charts para obtener la colección de gráficos existentes en el archivo de plantilla.

#### **Creación de un gráfico**
El siguiente ejemplo muestra cómo crear un gráfico de pirámide. Más adelante manipularemos este gráfico.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ManipulatePositionSizeAndDesignerChart-1.go" >}}
#### **Manipulación del gráfico**
El siguiente ejemplo muestra cómo manipular el gráfico existente. En este ejemplo, modificamos el gráfico creado anteriormente. En la salida generada, se observa que la etiqueta de fecha de un punto de datos se ha establecido en 'Reino Unido, 30K'.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ManipulatePositionSizeAndDesignerChart-2.go" >}}
#### **Manipulación de un gráfico de líneas en la plantilla de diseñador**
En este ejemplo, manipularemos un gráfico de líneas. Agregaremos algunas series de datos al gráfico existente y cambiaremos sus colores de línea.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ManipulatePositionSizeAndDesignerChart-3.go" >}}
