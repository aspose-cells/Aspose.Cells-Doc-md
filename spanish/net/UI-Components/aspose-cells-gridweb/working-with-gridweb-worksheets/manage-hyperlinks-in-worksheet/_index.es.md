---
title: Administrar hipervínculos en la hoja de trabajo
type: docs
weight: 100
url: /es/net/manage-hyperlinks-in-worksheet/
---
{{% alert color="primary" %}} 

Este tema analiza qué tipos de hipervínculos se admiten en Aspose.Cells.GridWeb y cómo administrarlos mediante programación. Los hipervínculos se pueden usar para crear enlaces a direcciones URL web o para realizar una devolución de datos a un servidor.

{{% /alert %}} 
## **Trabajar con hipervínculos**
### **Tipos de hipervínculos**
En general, los siguientes hipervínculos son compatibles con Aspose.Cells.GridWeb:

- [Hipervínculos de URL](/cells/es/net/manage-hyperlinks-in-worksheet/), hipervínculos que se pueden vincular a URL web.
- [Hipervínculos de texto](/cells/es/net/manage-hyperlinks-in-worksheet/), Hipervínculos de URL aplicados al texto.
- [hipervínculos de imagen](/cells/es/net/manage-hyperlinks-in-worksheet/), hipervínculos URL aplicados a las imágenes.
- [Cell hipervínculos de comando](/cells/es/net/manage-hyperlinks-in-worksheet/), hipervínculos que publican datos en un servidor. Dichos hipervínculos actúan más como un botón que activa un evento del lado del servidor cuando se hace clic.

Las siguientes secciones describen el uso de todos los tipos de hipervínculos en detalle. También explica cómo acceder a los enlaces o eliminarlos.
### **Adición de hipervínculos**

#### **Hipervínculos de URL**
Los hipervínculos de URL se parecen más a los hipervínculos simples que normalmente ve en los sitios web. Un hipervínculo de URL funciona como un ancla en una celda. Cada vez que se hace clic, navega a una página web o abre una nueva ventana del navegador.

Hay diferentes tipos de hipervínculos de URL:

- Hipervínculos de texto.
- Hipervínculos de imágenes.

Los desarrolladores pueden especificar una imagen para el hipervínculo. Si no se especifica una imagen, se crea un hipervínculo de texto; de lo contrario, se crea un hipervínculo de imagen.


##### **Hipervínculos de texto**
Para agregar un hipervínculo de texto a una hoja de cálculo:

1. Agregue el control Aspose.Cells.GridWeb a su formulario web.
1. Accede a una hoja de trabajo.
1. Agregue un hipervínculo a una celda en la hoja de cálculo.
1. Establezca el texto que se mostrará en la celda.
1. Establezca la URL del hipervínculo.
1. Establezca el destino del hipervínculo, si lo desea.
1. Establezca una información sobre herramientas, si lo desea.

{{% alert color="primary" %}} 

 NOTA: El objetivo del hipervínculo se puede establecer en_ ser,_top o _parent para abrir URL web en una ventana nueva, actual o superior, respectivamente.

{{% /alert %}} 

El siguiente ejemplo agrega dos hipervínculos a una hoja de trabajo. Uno no tiene destino mientras que el otro está configurado como _parent.

**Salida: hipervínculos de texto agregados a la hoja de trabajo** 

![todo:imagen_alternativa_texto](manage-hyperlinks-in-worksheet_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AddHyperlinks.aspx-AddTextHyperlinks.cs" >}}


##### **Hipervínculos de imagen**
Para agregar un hipervínculo de imagen:

1. Agregue el control Aspose.Cells.GridWeb a su formulario web.
1. Accede a una hoja de trabajo.
1. Agregue un hipervínculo a una celda.
1. Establezca la URL de la imagen que se mostrará como hipervínculo.
1. Establezca la URL del hipervínculo.
1. Establezca una información sobre herramientas, si lo desea.
1. Configure el texto del hipervínculo, si lo desea.

**Salida: hipervínculos de imagen agregados a la hoja de trabajo** 

![todo:imagen_alternativa_texto](manage-hyperlinks-in-worksheet_2.png)

{{% alert color="primary" %}} 

 Establecer el AltText del hipervínculo de la imagen cumple una función similar a establecer un<ALT> etiqueta en HTML. El texto se muestra solo si la imagen con hipervínculo no se muestra. (Por ejemplo, si la imagen no está en la ubicación especificada). Si no se encuentra la imagen del segundo hipervínculo, la salida del fragmento de código a continuación se vería de la siguiente manera.

**No se pudo encontrar la imagen para la URL de la imagen** 

![todo:imagen_alternativa_texto](manage-hyperlinks-in-worksheet_3.png)

{{% /alert %}} 

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AddHyperlinks.aspx-AddImageHyperlinks.cs" >}}


#### **Cell hipervínculos de comando**
Un hipervínculo de comando de celda es un tipo especial de hipervínculo que activa un evento del lado del servidor en lugar de abrir una página web. Los desarrolladores pueden agregar código al evento del lado del servidor y realizar cualquier tarea cuando se hace clic en el hipervínculo. Esta función permite a los desarrolladores crear aplicaciones más interactivas.

Para agregar un hipervínculo de comando de celda:

1. Agregue el control Aspose.Cells.GridWeb a su formulario web.
1. Accede a una hoja de trabajo.
1. Agregue un hipervínculo a una celda.
1. Establezca el Comando del hipervínculo en cualquier valor deseado.
 El controlador de eventos del hipervínculo utiliza el valor para reconocerlo.
1. Establezca una información sobre herramientas, si lo desea.
1. Establezca la URL de la imagen que se mostrará como un hipervínculo.

**Se ha agregado un hipervínculo de comando de celda a la hoja de trabajo** 

![todo:imagen_alternativa_texto](manage-hyperlinks-in-worksheet_4.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AddHyperlinks.aspx-AddCellCommandHyperlinks.cs" >}}
##### **Manejo de eventos de hipervínculos de comando Cell**
Los desarrolladores deben crear un controlador de eventos para el evento CellCommand del control GridWeb para realizar tareas específicas cuando se hace clic en un hipervínculo de comando de celda específico. El controlador de eventos del evento CellCommand proporciona un objeto del tipo CellEventArgs que ofrece la propiedad Argument. Utilice la propiedad Argument para identificar un hipervínculo específico comparando su valor CellCommand.

El siguiente ejemplo crea un controlador de eventos para el hipervínculo del comando de celda creado en el código anterior. El CellCommand del hipervínculo se estableció en Click. Entonces, en el controlador de eventos, primero verifíquelo y luego agregue el código que muestra un mensaje en la celda A6.

El controlador de eventos se invoca cuando se hace clic en el hipervínculo.

**Salida: texto agregado a la celda A6 cuando se hace clic en el hipervínculo** 

![todo:imagen_alternativa_texto](manage-hyperlinks-in-worksheet_5.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AddHyperlinks.aspx-HandleCellCommandHyperlinkEvent.cs" >}}
### **Acceso a hipervínculos**
Para acceder a un hipervínculo existente:

1. Accede a la celda que lo contiene.
1. Obtenga la referencia de la celda.
1. Pase la referencia al método GetHyperlink de la colección Hyperlinks para acceder al hipervínculo.
1. Modifique las propiedades del hipervínculo.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ManageHyperlinks.aspx-AccessHyperlinks.cs" >}}
### **Eliminación de hipervínculos**
Para eliminar un hipervínculo:

1. Accede a la hoja de trabajo activa.
1. Quite un hipervínculo mediante el método Quitar de la colección Hipervínculos.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ManageHyperlinks.aspx-RemoveHyperlink.cs" >}}
