---
title: Habilitar el cuadro de edición de GridWeb
type: docs
weight: 110
url: /es/net/enable-gridweb-editbox/
---
{{% alert color="primary" %}} 

El cuadro de edición de GridWeb es una barra de herramientas que se representa en la parte superior del control que puede usar para ver/ingresar o copiar datos/fórmulas en las celdas. También muestra el nombre de la celda que está editando. Después de hacer clic en el marco o cuando comience a escribir datos o escriba un símbolo igual (=), se activará el cuadro de edición.

{{% /alert %}} 
## **Configuración del cuadro de edición de Aspose.Cells.GridWeb**
El control GridWeb proporciona la propiedad ShowCellEditBox a la que los desarrolladores pueden asignarla a "Verdadero" para activar la barra de herramientas. El valor predeterminado del atributo es Falso. Cuando establece su valor en "Verdadero", el cuadro de edición aparecerá en la parte superior del control GridWeb.

{{% alert color="primary" %}} 

 Para habilitar esta función, debe importar el archivo "jquery.js" a su proyecto y consultarlo en sus páginas .aspx para que funcione. Puede descargar el archivo jQuery de<https://jqueryui.com/download/all/> y coloque los archivos de la biblioteca en alguna carpeta del proyecto y agregue una referencia al archivo de la biblioteca a través de<script> etiqueta en su formulario web .aspx de la siguiente manera. Todas las últimas versiones de jQuery están bien.

{{< highlight "csharp" >}}

 <head id="Head1" runat="server">

  <title>Untitled Page</title>

  <script type="text/javascript" src="/jquery/jquery.js"></script>

</head>



{{< /highlight >}}

{{% /alert %}} 

**Control GridWeb con cuadro de edición** 

![todo:imagen_alternativa_texto](enable-gridweb-editbox_1.png)
### **Ejemplo**


{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-DisplayCellEditBox.aspx-DisplayCellEditBox.cs" >}}
