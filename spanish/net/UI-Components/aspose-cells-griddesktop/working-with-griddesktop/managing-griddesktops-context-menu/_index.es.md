---
title: Gestionar Menús Contextuales de GridDesktop
type: docs
weight: 40
url: /es/net/aspose-cells-griddesktop/manage-griddesktops-context-menu/
keywords: GridDesktop, contexto, menú contextual
description: Este artículo presenta cómo personalizar el menú contextual en GridDesktop.
---

{{% alert color="primary" %}} 

Aspose.Cells.GridDesktop tiene un menú contextual que cuenta con todos los comandos comúnmente utilizados. El control permite ocultar/mostrar elementos de menú. Además, es posible añadir nuevos elementos de menú con controladores de eventos al menú.

{{% /alert %}} 
## **Introducción**
La clase ContextMenuManager se utiliza para gestionar los elementos del menú contextual. El atributo GridDesktop.ContextMenuManager obtiene la instancia del objeto ContextMenuManager. Por ejemplo, el atributo ContextMenuManager.MenuItemAvailable_Copy obtiene o establece un valor que indica si el elemento del menú contextual **Copiar** está disponible o no. De manera similar, tenemos todos los atributos correspondientes para diferentes elementos del menú contextual.

**IMPORTANTE:** Por defecto, todos los elementos del menú contextual son visibles en la lista.
## **Gestionando el Menú Contextual**
### **Ocultar Elementos del Menú Contextual**
Para realizar esta tarea, primero echamos un vistazo al menú contextual predeterminado que tiene GridDesktop.

**Menú predeterminado de GridDesktop** 

![todo:image_alt_text](managing-griddesktops-context-menu_1.png)

Ahora, ocultar algunos elementos del menú utilizando el código a continuación:



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-ManagingContextMenu-HideContextMenuItem.cs" >}}



Después de ejecutar el código anterior, algunos elementos del menú no serán visibles para los usuarios:

**Algunos elementos del menú están ocultos** 

![todo:image_alt_text](managing-griddesktops-context-menu_2.png)
### **Añadiendo nuevos elementos de menú**
Agregue un nuevo elemento al menú contextual a la lista utilizando el siguiente fragmento de código.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-ManagingContextMenu-AddContextMenuItem.cs" >}}


También especificamos un controlador de eventos para el nuevo comando/opción.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-ManagingContextMenu-EventHandler.cs" >}}



Después de ejecutar el código anterior, se podrá ver un nuevo elemento de menú en el menú contextual. También aparecerá un mensaje cuando se haga clic en la celda.

**Se añade un nuevo elemento de menú a la lista** 

![todo:image_alt_text](managing-griddesktops-context-menu_3.png)
