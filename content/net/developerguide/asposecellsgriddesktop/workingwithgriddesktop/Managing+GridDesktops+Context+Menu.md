+++
title = "Managing GridDesktops Context Menu" 
description = "" 
weight = 16599 
+++

Aspose.Cells for .NET : Managing GridDesktops Context Menu  

# Aspose.Cells for .NET : Managing GridDesktops Context Menu


Aspose.Cells.GridDesktop has a context menu which has all the commonly used commands. The control allows you to hide/show menu items. Moreover, it is possible to add new menu items with event handlers to the menu.

{{< panel title="Contents Summary" style="primary" >}}
*   1 [Introduction](#ManagingGridDesktopsContextMenu-Introduction)
*   2 [Managing the Context Menu](#ManagingGridDesktopsContextMenu-ManagingtheContextMenu)
    *   2.1 [Hiding Context Menu Items](#ManagingGridDesktopsContextMenu-HidingContextMenuItems)
    *   2.2 [Adding New Menu Items](#ManagingGridDesktopsContextMenu-AddingNewMenuItems)
{{< /panel >}}
 

 

## Introduction

The `ContextMenuManager` class is used to manage the context menu items. The `GridDesktop.ContextMenuManager` attribute gets the instance of `ContextMenuManager` object. For example, the `ContextMenuManager.MenuItemAvailable_Copy` attribute gets or sets a value indicating whether the context menu item **Copy** is available or not. Similarly, we have all the corresponding attributes for different context menu items.

**IMPORTANT:** By default, all the context menu items are visible in the list.

## Managing the Context Menu

### Hiding Context Menu Items

To perform this task, we first take a look the default context menu the GridDesktop has.

**GridDeskop's default menu**  
![](https://docs2.aspose.com/cells/net/attachments/5017852/5113856.png)

Now, hide some menu items using the code below:

After executing the above code, some menu items will not be visible for the users:

**Some menu items are hidden**  
![](https://docs2.aspose.com/cells/net/attachments/5017852/5113857.png)

### Adding New Menu Items

Add a new context menu item to the list using the following code snippet.

  
We also specify an event handler for the new command/option.

After executing the above code, a new menu item can be seen in the context menu. A message will also appear when cell is clicked.

**A new menu item is added to the list**  
![](https://docs2.aspose.com/cells/net/attachments/5017852/5113858.png)

## Attachments:

![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Managing GridDesktops Context Menu-001.png](https://docs2.aspose.com/cells/net/attachments/5017852/5115170.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Managing GridDesktops Context Menu-002.png](https://docs2.aspose.com/cells/net/attachments/5017852/5115171.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Managing GridDesktops Context Menu-003.png](https://docs2.aspose.com/cells/net/attachments/5017852/5115172.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Managing GridDesktops Context Menu-004.png](https://docs2.aspose.com/cells/net/attachments/5017852/5113859.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Managing GridDesktops Context Menu-003.png](https://docs2.aspose.com/cells/net/attachments/5017852/5113858.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Managing GridDesktops Context Menu-002.png](https://docs2.aspose.com/cells/net/attachments/5017852/5113857.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Managing GridDesktops Context Menu-001.png](https://docs2.aspose.com/cells/net/attachments/5017852/5113856.png) (image/png)  

