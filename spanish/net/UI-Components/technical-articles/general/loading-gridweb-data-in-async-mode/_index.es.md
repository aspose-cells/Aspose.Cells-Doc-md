---
title: Cargando datos de GridWeb en modo asíncrono
type: docs
weight: 40
url: /es/net/aspose-cells-gridweb/loading-data-in-async-mode/
description: Este artículo describe cómo usar el modo asíncrono para obtener un mejor rendimiento en GridWeb.
keywords: GridWeb, rendimiento, asíncrono, modo asíncrono
---

{{% alert color="primary" %}} 

Al crear un libro con grandes conjuntos de datos, o al leer un gran archivo de Microsoft Excel, seguramente llevará más tiempo y recursos hacerlo. La memoria total que tomará el proceso siempre es una preocupación. Hay medidas que se pueden adoptar para enfrentar el desafío. Aspose.Cells.GridWeb proporciona algunas opciones y APIs relevantes para reducir y optimizar el uso de memoria. Además, puede ayudar a que el proceso trabaje de manera más eficiente y se ejecute más rápido. Para una hoja de cálculo que contiene grandes datos de celdas, puede cargar el conjunto de datos de forma asíncrona, lo que puede mejorar el rendimiento general para la experiencia del usuario.

{{% /alert %}} 

Utilice la opción GridWeb.EnableAsync para optimizar la memoria y el rendimiento de los datos de las celdas. Al construir un gran conjunto de datos para las celdas. Cuando establece la opción en true, la carga de datos se basará solo en el área visible actual de Windows. En resumen, al desplazarse por los datos de las celdas de la hoja de cálculo en GridWeb, cargará nuevos datos de Windows basándose solo en la posición de desplazamiento actual.

El siguiente ejemplo muestra cómo habilitar el modo asíncrono de GridWeb.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Articles-EnableAsyncMode.aspx-EnableAsync.cs" >}}
