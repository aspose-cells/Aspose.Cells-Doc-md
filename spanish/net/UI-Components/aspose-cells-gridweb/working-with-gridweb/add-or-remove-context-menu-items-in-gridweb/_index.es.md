---
title: Agregar o Quitar Elementos del Menú Contextual en GridWeb
type: docs
weight: 130
url: /es/net/aspose-cells-gridweb/add-or-remove-context-menu-items-in-gridweb/
keywords: GridWeb, menú contextual, menú
description: Este artículo presenta cómo agregar o quitar elementos del menú contextual en GridWeb.
---

{{% alert color="primary" %}} 

Puedes agregar elementos al menú contextual usando la marcación de ASP.NET o utilizando el código .NET. También puedes quitar elementos del menú contextual usando el código .NET. Por favor, usa los métodos GridWeb.CustomCommandButtons.Add() y GridWeb.CustomCommandButtons.Remove() o RemoveAt() para estos propósitos.

{{% /alert %}} 
## **Agregar Elemento al Menú Contextual usando la Marcación de ASP.NET**
El siguiente marcado de ASP.NET agrega un elemento de menú contextual en GridWeb.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-AddRemoveContextMenuItem-InitContextMenuItem.aspx" >}}



Aquí está el marcado completo de ASP.NET que crea un GridWeb con el elemento de menú contextual anterior. Por favor, tenga en cuenta el atributo OnCustomCommand="GridWeb1_CustomCommand". Es el nombre del controlador de eventos que se llamará cuando se haga clic en su elemento de menú contextual.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-InitContextMenuItem-InitContextMenuItem.aspx" >}}



Así es como se ve el elemento de menú contextual después de ser agregado usando el marcado de ASP.NET anterior.

![todo:image_alt_text](add-or-remove-context-menu-items-in-gridweb_1.png)

Este es el código del controlador de eventos que se ejecuta cuando se hace clic en el elemento de menú contextual. El código primero verifica el nombre del comando, si coincide con nuestro comando, agrega un texto en la celda A1 de la hoja de cálculo activa de GridWeb y ajusta el ancho de la primera columna a 40 unidades para que el texto sea visible.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-InitContextMenuItem.aspx-HandleContextMenuItemCommand.cs" >}}


Así es como se ve el GridWeb cuando se hace clic en el elemento de menú contextual.

![todo:image_alt_text](add-or-remove-context-menu-items-in-gridweb_2.png)
## **Agregar elementos de menú contextual en Aspose.Cells.GridWeb usando código**
Este código muestra cómo agregar un elemento de menú contextual dentro de un GridWeb usando código.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-AddRemoveContextMenuItem.aspx-AddContextMenuItem.cs" >}}
## **Eliminar elementos de menú contextual en Aspose.Cells.GridWeb usando código**
Este código muestra cómo eliminar un elemento de menú contextual utilizando los métodos CustomCommandButtons.Remove() y CustomCommandButtons.RemoveAt().



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-AddRemoveContextMenuItem.aspx-RemoveContextMenuItem.cs" >}}
