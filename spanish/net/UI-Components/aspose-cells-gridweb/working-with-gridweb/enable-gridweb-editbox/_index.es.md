---
title: Habilitar cuadro de edición de GridWeb
type: docs
weight: 110
url: /es/net/aspose-cells-gridweb/enable-gridweb-editbox/
keywords: GridWeb, cuadro de edición, barra de fórmulas
description: Este artículo introduce cómo trabajar con la barra de fórmulas o el cuadro de edición en GridWeb.
---

{{% alert color="primary" %}} 

El Cuadro de Edición de GridWeb (llamado barra de fórmulas en Excel) es una barra de herramientas que se renderiza en la parte superior del control y que puedes usar para mostrar o ingresar valores o copiar datos/fórmulas para la celda enfocada. También muestra el nombre de la celda que estás editando. Después de hacer clic en el marco o al comenzar a escribir datos o al escribir un signo igual (=), el Cuadro de Edición se activará.

{{% /alert %}} 
## **Configurando el Cuadro de Edición de Aspose.Cells.GridWeb**
El control GridWeb proporciona la propiedad ShowCellEditBox a la cual los desarrolladores pueden asignarle "True" para mostrar la barra de herramientas. El valor predeterminado del atributo es Falso. Cuando se establece su valor en "True", el Cuadro de Edición aparecerá en la parte superior del control GridWeb.

{{% alert color="primary" %}} 

To enable this feature, you need to import "jquery.js" file to your project and refer it in your .aspx page(s) to make it work. You may download the jQuery archive from <https://jqueryui.com/download/all/> and put the library file(s) into some folder in the project and add reference to the library file via <script> tag in your .aspx web form as following. All the latest jQuery versions are OK.

{{< highlight csharp >}}

 <head id="Head1" runat="server">

  <title>Untitled Page</title>

  <script type="text/javascript" src="/jquery/jquery.js"></script>

</head>



{{< /highlight >}}

{{% /alert %}} 

**Control GridWeb con Cuadro de Edición** 

![todo:image_alt_text](enable-gridweb-editbox_1.png)
### **Ejemplo**


{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-DisplayCellEditBox.aspx-DisplayCellEditBox.cs" >}}
