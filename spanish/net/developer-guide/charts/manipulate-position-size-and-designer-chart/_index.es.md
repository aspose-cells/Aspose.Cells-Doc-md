---
title: Manipular el tamaño de la posición y el gráfico del diseñador
description: Aprenda a utilizar Aspose.Cells for .NET para manipular eficazmente la posición, el tamaño y el gráfico del diseñador en Microsoft Excel. Nuestra guía demostrará cómo ajustar estas propiedades para mejorar el diseño y la visualización.
keywords: Aspose.Cells for .NET, Position, Size, Designer Chart, Microsoft Excel, Layout, Visualization.
type: docs
weight: 45
url: /es/net/manipulate-position-size-and-designer-chart/
---
##  **Posición y tamaño del gráfico**
 A veces, desea cambiar la posición o el tamaño del gráfico nuevo o existente dentro de la hoja de trabajo. Aspose.Cells proporciona la[Gráfico.ChartObject](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/properties/chartobject) propiedad para lograrlo. Puede utilizar sus subpropiedades para cambiar el tamaño del gráfico con nuevos**altura** y**ancho** o reposicionarlo con uno nuevo**X y Y** coordenadas.
###  **Controlar la posición y el tamaño del gráfico**
Para cambiar la posición del gráfico (coordenadas X, Y) o el tamaño (alto, ancho), utilice estas propiedades:

1. [Gráfico.ChartObject.X](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/x)
1. [Gráfico.ChartObject.Y](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/y)
1. [Gráfico.ChartObject.Altura](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/height)
1. [Gráfico.ChartObject.Ancho](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/width)

El siguiente ejemplo explica el uso de las API anteriores; carga el libro de trabajo existente que contiene un gráfico en su primera hoja de trabajo. Luego cambia el tamaño y la posición del gráfico usando Aspose.Cells.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ChangeChartPosition-1.cs" >}}
##  **Manipulación de gráficos de diseñador**
Hay ocasiones en las que es necesario manipular o modificar gráficos en archivos de plantilla de diseñador. Aspose.Cells admite totalmente la manipulación de contenidos y elementos del gráfico del diseñador. Los datos, el contenido del gráfico, la imagen de fondo y el formato se pueden conservar con precisión.
###  **Manipulación de gráficos de Designer en archivos de plantilla**
Para manipular gráficos de diseñador en archivos de plantilla, use el gráfico relacionado API. Por ejemplo, puede usar la propiedad Worksheet.Charts para obtener la colección de gráficos existente en el archivo de plantilla.
####  **Crear un gráfico**
El siguiente ejemplo muestra cómo crear un gráfico piramidal. Manipularemos este gráfico más adelante.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-HowToCreateChart-1.cs" >}}
####  **Manipular el gráfico**
El siguiente ejemplo muestra cómo manipular el gráfico existente. En este ejemplo, modificamos el gráfico creado anteriormente. En el resultado generado, tenga en cuenta que la etiqueta de fecha de un punto de datos se ha establecido en "Reino Unido, 30K".



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-ModifyPieChart-1.cs" >}}
####  **Manipular un gráfico de líneas en la plantilla de diseñador**
En este ejemplo, manipularemos un gráfico de líneas. Agregaremos algunas series de datos al gráfico existente y cambiaremos los colores de sus líneas.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-ModifyLineChart-1.cs" >}}

