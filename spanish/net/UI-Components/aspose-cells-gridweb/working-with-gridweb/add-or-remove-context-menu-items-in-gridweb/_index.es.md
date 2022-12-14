---
title: Agregar o quitar elementos del menú contextual en GridWeb
type: docs
weight: 130
url: /es/net/add-or-remove-context-menu-items-in-gridweb/
---
{{% alert color="primary" %}} 

Puede agregar elementos del menú contextual usando el marcado ASP.NET o usando el código .NET. También puede eliminar elementos del menú contextual utilizando el código .NET. Utilice los métodos GridWeb.CustomCommandButtons.Add() y GridWeb.CustomCommandButtons.Remove() o RemoveAt() para estos fines.

{{% /alert %}} 
## **Agregue el elemento del menú contextual usando el marcado ASP.NET**
El siguiente marcado ASP.NET agrega un elemento de menú contextual en GridWeb.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-AddRemoveContextMenuItem-InitContextMenuItem.aspx" >}}



Aquí está el marcado ASP.NET completo que crea un GridWeb con el elemento de menú contextual anterior. Tenga en cuenta el atributo OnCustomCommand="GridWeb1_CustomCommand". Es el nombre del controlador de eventos que se llamará cuando se haga clic en el elemento del menú contextual.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-InitContextMenuItem-InitContextMenuItem.aspx" >}}



Así es como se ve el elemento del menú contextual después de agregarlo usando el marcado ASP.NET anterior.

![todo:imagen_alternativa_texto](add-or-remove-context-menu-items-in-gridweb_1.png)

Este es el código del controlador de eventos que se ejecuta cuando se hace clic en el elemento del menú contextual. El código primero verifica el nombre del comando, si coincide con nuestro comando, agrega un texto en la celda A1 de la hoja de trabajo GridWeb activa y establece el ancho de la primera columna en 40 unidades para que el texto sea visible.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-InitContextMenuItem.aspx-HandleContextMenuItemCommand.cs" >}}


Así es como se ve GridWeb cuando hace clic en el elemento del menú contextual.

![todo:imagen_alternativa_texto](add-or-remove-context-menu-items-in-gridweb_2.png)
## **Agregar elementos del menú contextual en Aspose.Cells.GridWeb usando código**
Este código muestra cómo agregar un elemento de menú contextual dentro de GridWeb usando código.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-AddRemoveContextMenuItem.aspx-AddContextMenuItem.cs" >}}
## **Eliminar elementos del menú contextual en Aspose.Cells.GridWeb usando código**
Este código muestra cómo eliminar un elemento del menú contextual mediante los métodos CustomCommandButtons.Remove() y CustomCommandButtons.RemoveAt().



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-AddRemoveContextMenuItem.aspx-RemoveContextMenuItem.cs" >}}
