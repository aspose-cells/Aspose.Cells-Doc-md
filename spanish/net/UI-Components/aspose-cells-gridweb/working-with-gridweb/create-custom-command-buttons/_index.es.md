---
title: Crear botones de comando personalizados
type: docs
weight: 100
url: /es/net/aspose-cells-gridweb/create-custom-command-buttons/
keywords: GridWeb, comando, botones de comando, personalizados
description: Este artículo presenta cómo personalizar botones de comando en GridWeb.
---

{{% alert color="primary" %}} 

Aspose.Cells.GridWeb contiene botones especiales como **Enviar**, **Guardar** y **Deshacer**. Todos estos botones realizan tareas específicas para Aspose.Cells.GridWeb.
También es posible agregar botones personalizados que realizan tareas personalizadas. Este tema explica cómo utilizar esta característica.

{{% /alert %}} 
## **Creación de botones de comando personalizados**
Para crear un botón de comando personalizado en Aspose.Cells.GridWeb:

1. Agregar el control Aspose.Cells.GridWeb al formulario web.
1. Acceder a una hoja de cálculo.
1. Crear una instancia de la clase CustomCommandButton.
1. Establecer el comando del botón en algún valor. Este valor se utiliza en el controlador de eventos del botón.
1. Establecer el texto del botón.
1. Establecer la URL de la imagen del botón.
1. Finalmente, agregar el objeto CustomCommandButton a la colección CustomCommandButtons del control GridWeb.

{{% alert color="primary" %}} 

También es posible agregar botones de comando personalizados en modo WYSIWYG utilizando el cuadro de diálogo de Propiedades de Visual Studio.

{{% /alert %}} 

La salida del fragmento de código se muestra a continuación:

**Un botón de comando personalizado agregado al control GridWeb** 

![todo:image_alt_text](create-custom-command-buttons_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-InitCustomCommandButton.aspx-InitCustomCommandButton.cs" >}}
### **Manejo de eventos del botón de comando personalizado**
El aspecto más importante de los botones de comando personalizados es la acción que realizan al hacer clic. Para configurar la acción, cree un controlador de eventos para el evento CustomCommand del control GridWeb.

El evento CustomCommand siempre se desencadena cuando se hace clic en un botón de comando personalizado. Por lo tanto, el controlador de eventos debe identificar el botón de comando personalizado específico al que se aplica mediante el comando establecido al agregar el botón al control GridWeb. Finalmente, agregue código personalizado que se ejecuta al hacer clic en el botón.

En el ejemplo de código a continuación, se agrega un mensaje de texto a la celda A1 cuando se hace clic en el botón.

**Texto agregado a la celda A1 cuando se hace clic en el botón de comando personalizado** 

![todo:image_alt_text](create-custom-command-buttons_2.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-HandleCustomCommandEvent.aspx-HandleCustomCommandEvent.cs" >}}
