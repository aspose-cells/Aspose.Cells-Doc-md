---
title: Acercar o alejar la hoja de trabajo en GridDesktop
type: docs
weight: 160
url: /es/net/zooming-in-or-out-on-the-worksheet-in-griddesktop/
---
{{% alert color="primary" %}} 

A veces, cuando trabaja con sus datos, es posible que desee ampliar el contenido de la pantalla sin cambiar realmente el tamaño de la fuente. Por ejemplo, es posible que haya formateado su texto para que use una fuente pequeña. (A menudo, esto es necesario para obtener toda la información en una copia impresa). Sin embargo, cuando se trabaja en la hoja de trabajo, la fuente es difícil de leer porque es muy pequeña.

En Microsoft Excel, hay un control deslizante de zoom disponible para acercar y alejar los documentos de forma rápida y sencilla. El control deslizante de zoom generalmente se encuentra en la esquina inferior derecha de la ventana del software.

Aspose.Cells también permite a los desarrolladores establecer el factor de zoom de la hoja de trabajo, por lo que el contenido debe aparecer según el valor porcentual deseado.

{{% /alert %}} 
## **Acercar o alejar usando Aspose.Cells.GridDesktop**
Aspose.Cells proporciona la clase Aspose.Cells.GridDesktop.Worksheet que tiene una amplia gama de propiedades y métodos para administrar hojas de trabajo. Para establecer el factor de zoom de una hoja de trabajo, use la propiedad Zoom de la clase Worksheet. El factor de zoom se establece asignando un valor numérico (entero) a la propiedad Zoom.

Construimos un control deslizante de zoom similar a MS Excel usando el control TrackBar (.NET). En un proyecto de WinForm, colocamos el control Aspose.Cells.GridDesktop de Toolbox en el formulario y especificamos algunas propiedades para establecer su nombre, tamaño u otros aspectos en consecuencia. Ahora, colocamos el control TrackBar en la esquina inferior derecha debajo del control GridDesktop, también colocamos un control Label que mostraría el valor porcentual que especifica a través del identificador del control TrackBar. Agregamos líneas de código relativas en el evento de desplazamiento de TrackBar, de modo que cuando desplaza el control de Trackbar, GridDesktop debe acercar o alejar para mostrar los datos/contenidos en él.

A continuación se proporciona un ejemplo completo que demuestra cómo utilizar la propiedad Zoom para establecer el factor de zoom de la hoja de trabajo activa de GridDesktop. Primero importamos un archivo de plantilla de Excel a GridDesktop.

Escriba el código a continuación en el evento Cargar del formulario para configurar el archivo de plantilla de Excel en GridDesktop y el valor de la barra de seguimiento.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ZoomingInOut-LoadEvent.cs" >}}


Ahora copie el siguiente código dentro del evento de desplazamiento de la pista y ejecute la aplicación. Notará que mover la barra de seguimiento cambiará la propiedad de zoom de la hoja de trabajo.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ZoomingInOut-ZoomInOut.cs" >}}
