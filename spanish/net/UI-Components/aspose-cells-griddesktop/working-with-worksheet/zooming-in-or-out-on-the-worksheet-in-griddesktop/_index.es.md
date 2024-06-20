---
title: Hacer zoom dentro o fuera de la Hoja de cálculo en GridDesktop
type: docs
weight: 160
url: /es/net/aspose-cells-griddesktop/zoom-in-or-out-on-the-worksheet-in-griddesktop/
keywords: GridDesktop, zoom, acercar, alejar
description: Este artículo presenta cómo hacer zoom dentro o fuera en GridDesktop.
---

{{% alert color="primary" %}} 

A veces, al trabajar con tus datos, es posible que desees ampliar el contenido en la pantalla sin necesariamente cambiar el tamaño de fuente. Por ejemplo, es posible que hayas formateado tu texto para que use una fuente pequeña. (A menudo es necesario para que toda la información que desees se pueda imprimir). Cuando trabajas en la hoja de cálculo, sin embargo, la fuente es difícil de leer porque es tan pequeña.

En Microsoft Excel, hay un control deslizante de zoom disponible para hacer zoom dentro y fuera de los documentos de manera rápida y sencilla. El control deslizante de zoom suele estar en la esquina inferior derecha de la ventana del software.

Aspose.Cells también permite a los desarrolladores establecer el factor de zoom de la hoja de cálculo, para que el contenido aparezca según el valor de porcentaje deseado.

{{% /alert %}} 
## **Hacer zoom dentro o fuera usando Aspose.Cells.GridDesktop**
Aspose.Cells proporciona la clase Aspose.Cells.GridDesktop.Worksheet que tiene una amplia gama de propiedades y métodos para gestionar hojas de cálculo. Para establecer el factor de zoom de una hoja de cálculo, utiliza la propiedad Zoom de la clase Worksheet. El factor de zoom se establece asignando un valor numérico (entero) a la propiedad Zoom.

Creamos un control deslizante de zoom similar al de MS Excel mediante el control TrackBar (.NET). En un proyecto WinForm, colocamos el control Aspose.Cells.GridDesktop desde la caja de herramientas en el formulario y especificamos algunas propiedades para establecer su nombre, tamaño u otros aspectos según corresponda. Ahora, colocamos el control TrackBar en la esquina inferior derecha debajo del control GridDesktop, también colocamos un control de etiqueta que mostrará el valor de porcentaje que especifiques a través del control TrackBar. Agregamos líneas de código relacionadas en el evento de desplazamiento del TrackBar, por lo que al desplazar el control TrackBar, GridDesktop debería hacer zoom para mostrar los datos o contenido en él.

A continuación se muestra un ejemplo completo que demuestra cómo usar la propiedad de zoom para establecer el factor de zoom de la hoja de cálculo activa de GridDesktop. Primero importamos un archivo de Excel de plantilla a GridDesktop.

Escribe el código a continuación en el evento Load del formulario para establecer el archivo de Excel de plantilla en GridDesktop y el valor de la barra de desplazamiento.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ZoomingInOut-LoadEvent.cs" >}}


Ahora copia el código a continuación dentro del evento de desplazamiento de la barra y ejecuta la aplicación. Notarás que al mover la barra de desplazamiento, el valor de zoom de la hoja de cálculo cambiará.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ZoomingInOut-ZoomInOut.cs" >}}
