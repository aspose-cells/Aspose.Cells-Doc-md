---
title: Gestión del menú contextual de GridDesktops
type: docs
weight: 40
url: /es/net/managing-griddesktops-context-menu/
---
{{% alert color="primary" %}} 

Aspose.Cells.GridDesktop tiene un menú contextual que tiene todos los comandos de uso común. El control le permite ocultar/mostrar elementos del menú. Además, es posible agregar nuevos elementos de menú con controladores de eventos al menú.

{{% /alert %}} 
## **Introducción**
La clase ContextMenuManager se utiliza para administrar los elementos del menú contextual. El atributo GridDesktop.ContextMenuManager obtiene la instancia del objeto ContextMenuManager. Por ejemplo, el atributo ContextMenuManager.MenuItemAvailable_Copy obtiene o establece un valor que indica si el elemento del menú contextual **Copiar** está disponible o no. Del mismo modo, tenemos todos los atributos correspondientes para diferentes elementos del menú contextual.

**IMPORTANTE:** De forma predeterminada, todos los elementos del menú contextual están visibles en la lista.
## **Gestión del menú contextual**
### **Ocultar elementos del menú contextual**
Para realizar esta tarea, primero echamos un vistazo al menú contextual predeterminado que tiene GridDesktop.

**Menú predeterminado de GridDeskop** 

![todo:imagen_alternativa_texto](managing-griddesktops-context-menu_1.png)

Ahora, oculta algunos elementos del menú usando el siguiente código:



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-ManagingContextMenu-HideContextMenuItem.cs" >}}



Después de ejecutar el código anterior, algunos elementos del menú no serán visibles para los usuarios:

**Algunos elementos del menú están ocultos** 

![todo:imagen_alternativa_texto](managing-griddesktops-context-menu_2.png)
### **Adición de nuevos elementos de menú**
Agregue un nuevo elemento de menú contextual a la lista mediante el siguiente fragmento de código.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-ManagingContextMenu-AddContextMenuItem.cs" >}}


También especificamos un controlador de eventos para el nuevo comando/opción.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-ManagingContextMenu-EventHandler.cs" >}}



Después de ejecutar el código anterior, se puede ver un nuevo elemento de menú en el menú contextual. También aparecerá un mensaje cuando se haga clic en la celda.

**Se agrega un nuevo elemento de menú a la lista.** 

![todo:imagen_alternativa_texto](managing-griddesktops-context-menu_3.png)
