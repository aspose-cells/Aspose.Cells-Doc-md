---
title: Gestionar hipervínculos en la hoja de trabajo
type: docs
weight: 100
url: /es/net/aspose-cells-gridweb/manage-hyperlinks-in-worksheet/
keywords: GridWeb,hipervínculo
description: Este artículo presenta cómo trabajar con hipervínculos en GridWeb.
---

{{% alert color="primary" %}} 

Este tema discute qué tipos de hipervínculos son admitidos en Aspose.Cells.GridWeb y cómo gestionarlos programáticamente. Los hipervínculos se pueden utilizar para crear enlaces a URL web o para realizar una devolución de llamada a un servidor.

{{% /alert %}} 
## **Trabajando con hipervínculos**
### **Tipos de hipervínculos**
Generalmente, los siguientes hipervínculos son compatibles con Aspose.Cells.GridWeb:

- [Hipervínculos de URL](/cells/es/net/aspose-cells-gridweb/manage-hyperlinks-in-worksheet/), hipervínculos que se pueden vincular a URLs web.
- [Hipervínculos de texto](/cells/es/net/aspose-cells-gridweb/manage-hyperlinks-in-worksheet/), hipervínculos de URL aplicados al texto.
- [Hipervínculos de imagen](/cells/es/net/aspose-cells-gridweb/manage-hyperlinks-in-worksheet/), hipervínculos de URL aplicados a imágenes.
- [Hipervínculos de comando de celda](/cells/es/net/aspose-cells-gridweb/manage-hyperlinks-in-worksheet/), hipervínculos que envían datos a un servidor. Tales hipervínculos actúan más como un botón que desencadena un evento del lado del servidor al hacer clic.

Las siguientes secciones describen el uso de todos los tipos de hipervínculos en detalle. También se discute cómo acceder o eliminar enlaces.
### **Añadiendo hipervínculos**

#### **Hipervínculos de URL**
Los URL de hipervínculo se parecen más a hipervínculos simples que normalmente se ven en sitios web. Un URL de hipervínculo funciona como un ancla en una celda. Cuando se hace clic en él, navega a una página web o abre una nueva ventana del navegador.

Existen diferentes tipos de URL de hipervínculo:

- Hipervínculos de texto.
- Hipervínculos de imagen.

Los desarrolladores pueden especificar una imagen para el hipervínculo. Si no se especifica una imagen, se crea un hipervínculo de texto; de lo contrario, se crea un hipervínculo de imagen.


##### **Hipervínculos de texto**
Para agregar un hipervínculo de texto a una hoja de cálculo:

1. Agrega el control Aspose.Cells.GridWeb a tu Formulario Web.
1. Acceder a una hoja de cálculo.
1. Agregar un hipervínculo a una celda en la hoja de cálculo.
1. Establecer el texto que se mostrará en la celda.
1. Establecer el URL del hipervínculo.
1. Establecer el destino del hipervínculo, si se desea.
1. Establecer una descripción, si se desea.

{{% alert color="primary" %}} 

NOTA: El destino del hipervínculo puede definirse como _self, _top o _parent para abrir URL web en una ventana nueva, la actual o en la superior respectivamente.

{{% /alert %}} 

El siguiente ejemplo añade dos hipervínculos a una hoja de cálculo. Uno sin destino y el otro con destino a _parent.

**Resultado: hipervínculos de texto agregados a la hoja de cálculo** 

![todo:image_alt_text](manage-hyperlinks-in-worksheet_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AddHyperlinks.aspx-AddTextHyperlinks.cs" >}}


##### **Hipervínculos de imagen**
Para añadir un hipervínculo de imagen:

1. Agrega el control Aspose.Cells.GridWeb a tu Formulario Web.
1. Acceder a una hoja de cálculo.
1. Agregar un hipervínculo a una celda.
1. Establecer la URL de la imagen que se mostrará como hipervínculo.
1. Establecer la URL del hipervínculo.
1. Establecer una descripción, si se desea.
1. Establecer el texto del hipervínculo, si se desea.

**Salida: hipervínculos de imagen agregados a la hoja de cálculo** 

![todo:image_alt_text](manage-hyperlinks-in-worksheet_2.png)

{{% alert color="primary" %}} 

Setting the image hyperlink's AltText fills a similar function as setting an <ALT> tag in HTML. The text is displayed only if the hyperlinked image is not displayed. (For example, if the image isn't at the specified location.) If the image of the second hyperlink is not found, the output of the code snippet below would look as follows.

**La imagen para la URL de la imagen no se pudo encontrar** 

![todo:image_alt_text](manage-hyperlinks-in-worksheet_3.png)

{{% /alert %}} 

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AddHyperlinks.aspx-AddImageHyperlinks.cs" >}}


#### **Hipervínculos de Comando de Celda**
Un hipervínculo de comando de celda es un tipo especial de hipervínculo que activa un evento del lado del servidor en lugar de abrir una página web. Los desarrolladores pueden agregar código al evento del lado del servidor y realizar cualquier tarea cuando se hace clic en el hipervínculo. Esta característica permite a los desarrolladores crear aplicaciones más interactivas.

Para agregar un hipervínculo de comando de celda:

1. Agrega el control Aspose.Cells.GridWeb a tu Formulario Web.
1. Acceder a una hoja de cálculo.
1. Agregar un hipervínculo a una celda.
1. Establecer el comando del hipervínculo al valor deseado.
   El valor es utilizado por el manejador de eventos del hipervínculo para reconocerlo.
1. Establecer una descripción, si se desea.
1. Establecer la URL de la imagen que se mostrará como hipervínculo.

**Se ha agregado un hipervínculo de comando de celda a la hoja de cálculo** 

![todo:image_alt_text](manage-hyperlinks-in-worksheet_4.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AddHyperlinks.aspx-AddCellCommandHyperlinks.cs" >}}
##### **Manejo de Eventos de Hipervínculos de Comando de Celda**
Los desarrolladores necesitan crear un controlador de eventos para el evento CellCommand del control GridWeb para realizar tareas específicas cuando se hace clic en un hipervínculo de comando de celda específico. El controlador de eventos del evento CellCommand proporciona un objeto del tipo CellEventArgs que ofrece la propiedad Argument. Use la propiedad Argument para identificar un hipervínculo específico comparando su valor CellCommand.

El ejemplo a continuación crea un controlador de eventos para el hipervínculo de comando de celda creado en el código anterior. El CellCommand del hipervínculo se estableció en Click. Entonces, en el controlador de eventos, primero verifíquelo y luego agregue código que muestre un mensaje en la celda A6.

El controlador de eventos se invoca cuando se hace clic en el hipervínculo.

**Salida: texto agregado a la celda A6 cuando se hace clic en el hipervínculo** 

![todo:image_alt_text](manage-hyperlinks-in-worksheet_5.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AddHyperlinks.aspx-HandleCellCommandHyperlinkEvent.cs" >}}
### **Accediendo a los hipervínculos**
Para acceder a un hipervínculo existente:

1. Acceda a la celda que lo contiene.
1. Obtenga la referencia de la celda.
1. Pase la referencia al método GetHyperlink de la colección Hyperlinks para acceder al hipervínculo.
1. Modifique las propiedades del hipervínculo.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ManageHyperlinks.aspx-AccessHyperlinks.cs" >}}
### **Eliminando hipervínculos**
Para eliminar un hipervínculo:

1. Accede a la hoja de cálculo activa.
1. Elimine un hipervínculo utilizando el método Remove de la colección Hyperlinks.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ManageHyperlinks.aspx-RemoveHyperlink.cs" >}}
