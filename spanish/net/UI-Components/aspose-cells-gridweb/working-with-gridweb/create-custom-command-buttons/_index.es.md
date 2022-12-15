---
title: Crear botones de comando personalizados
type: docs
weight: 100
url: /es/net/create-custom-command-buttons/
---
{{% alert color="primary" %}} 

 Aspose.Cells.GridWeb contiene botones especiales como**Enviar**, **Ahorrar** y**Deshacer**. Todos estos botones realizan tareas específicas para Aspose.Cells.GridWeb.
También es posible agregar botones personalizados que realizan tareas personalizadas. Este tema explica cómo utilizar esta función.

{{% /alert %}} 
## **Creación de botones de comando personalizados**
Para crear un botón de comando personalizado en Aspose.Cells.GridWeb:

1. Agregue el control Aspose.Cells.GridWeb al formulario web.
1. Accede a una hoja de trabajo.
1. Cree una instancia de la clase CustomCommandButton.
1. Establezca el comando del botón en algún valor. Este valor se usa en el controlador de eventos del botón.
1. Establece el texto del botón.
1. Establece la URL de la imagen del botón.
1. Finalmente, agregue el objeto CustomCommandButton a la colección CustomCommandButtons del control GridWeb.

{{% alert color="primary" %}} 

Los botones de comando personalizados también se pueden agregar en modo WYSIWYG mediante el cuadro de diálogo Propiedades de Visual Studio.

{{% /alert %}} 

La salida del fragmento de código se muestra a continuación:

**Un botón de comando personalizado agregado al control GridWeb** 

![todo:imagen_alternativa_texto](create-custom-command-buttons_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-InitCustomCommandButton.aspx-InitCustomCommandButton.cs" >}}
### **Gestión de eventos del botón de comando personalizado**
El aspecto más importante de los botones de comando personalizados es la acción que realizan cuando se les hace clic. Para establecer la acción, cree un controlador de eventos para el evento CustomCommand del control GridWeb.

El evento CustomCommand siempre se desencadena cuando se hace clic en un botón de comando personalizado. Por lo tanto, el controlador de eventos debe identificar el botón de comando personalizado específico al que se aplica mediante el conjunto de comandos al agregar el botón al control GridWeb. Finalmente, agregue código personalizado que se ejecuta cuando se hace clic en el botón.

En el ejemplo de código a continuación, se agrega un mensaje de texto a la celda A1 cuando se hace clic en el botón.

**Texto agregado a la celda A1 cuando se hace clic en el botón de comando personalizado** 

![todo:imagen_alternativa_texto](create-custom-command-buttons_2.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-HandleCustomCommandEvent.aspx-HandleCustomCommandEvent.cs" >}}
