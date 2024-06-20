---
title: Управление контекстным меню GridDesktop
type: docs
weight: 40
url: /ru/net/aspose-cells-griddesktop/manage-griddesktops-context-menu/
keywords: GridDesktop,контекст,контекстное меню
description: В этой статье представлено, как настраивать контекстное меню в GridDesktop.
---

{{% alert color="primary" %}} 

У Aspose.Cells.GridDesktop есть контекстное меню, в котором содержатся все часто используемые команды. Элемент управления позволяет скрывать/показывать пункты меню. Кроме того, возможно добавление новых пунктов меню с обработчиками событий в меню.

{{% /alert %}} 
## **Введение**
Класс ContextMenuManager используется для управления пунктами контекстного меню. Атрибут GridDesktop.ContextMenuManager получает экземпляр объекта ContextMenuManager. Например, атрибут ContextMenuManager.MenuItemAvailable_Copy получает или устанавливает значение, указывающее, доступен ли пункт меню контекстного меню **Копировать** или нет. Аналогично у нас есть все соответствующие атрибуты для различных пунктов контекстного меню.

**ВАЖНО:** По умолчанию все элементы контекстного меню видны в списке.
## **Управление контекстным меню**
### **Скрытие элементов контекстного меню**
Для выполнения этой задачи мы сначала рассмотрим контекстное меню по умолчанию, которое есть у GridDesktop.

**Команды меню по умолчанию GridDeskop** 

![todo:image_alt_text](managing-griddesktops-context-menu_1.png)

Теперь скроем некоторые пункты меню, используя следующий код:



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-ManagingContextMenu-HideContextMenuItem.cs" >}}



После выполнения вышеуказанного кода некоторые пункты меню не будут видны для пользователей:

**Некоторые пункты меню скрыты** 

![todo:image_alt_text](managing-griddesktops-context-menu_2.png)
### **Добавление новых пунктов меню**
Добавьте новый пункт контекстного меню в список, используя следующий фрагмент кода.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-ManagingContextMenu-AddContextMenuItem.cs" >}}


Мы также указываем обработчик событий для новой команды/опции.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-ManagingContextMenu-EventHandler.cs" >}}



После выполнения вышеуказанного кода новый пункт меню можно увидеть в контекстном меню. Также появится сообщение при щелчке на ячейке.

**Новый пункт меню добавлен в список** 

![todo:image_alt_text](managing-griddesktops-context-menu_3.png)
