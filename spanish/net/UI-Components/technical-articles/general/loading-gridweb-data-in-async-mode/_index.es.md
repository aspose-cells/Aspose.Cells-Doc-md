---
title: Carga de datos de GridWeb en modo asíncrono
type: docs
weight: 40
url: /es/net/loading-gridweb-data-in-async-mode/
---
{{% alert color="primary" %}} 

Al crear un libro de trabajo con grandes conjuntos de datos, o leer un gran archivo de Excel Microsoft, seguramente llevará más tiempo y recursos hacerlo. La memoria total que tomará el proceso es siempre una preocupación. Hay medidas que se pueden adoptar para hacer frente al desafío. Aspose.Cells.GridWeb proporciona algunas opciones y API relevantes para disminuir, reducir y optimizar el uso de la memoria. Además, puede ayudar a que el proceso funcione de manera más eficiente y se ejecute más rápido. Para una hoja de cálculo que contiene datos de celdas grandes, puede cargar el conjunto de datos de forma asíncrona, lo que puede mejorar el rendimiento general de la experiencia del usuario.

{{% /alert %}} 

Utilice la opción GridWeb.EnableAsync para optimizar la memoria y el rendimiento de los datos de las celdas. Al construir un gran conjunto de datos para celdas. Cuando configura la opción en verdadero, la carga de datos se basará solo en el área visible actual Windows. En resumen, cuando se desplaza por los datos de las celdas de la hoja de trabajo en GridWeb, se cargarán nuevos datos Windows basados únicamente en la posición de desplazamiento actual.

El siguiente ejemplo muestra cómo habilitar el modo asíncrono de GridWeb.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Articles-EnableAsyncMode.aspx-EnableAsync.cs" >}}
