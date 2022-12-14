---
title: Управление контекстным меню GridDesktops
type: docs
weight: 40
url: /ru/net/managing-griddesktops-context-menu/
---
{{% alert color="primary" %}} 

Aspose.Cells.GridDesktop имеет контекстное меню, в котором есть все часто используемые команды. Элемент управления позволяет скрывать/показывать пункты меню. Более того, в меню можно добавлять новые пункты меню с обработчиками событий.

{{% /alert %}} 
## **Введение**
Класс ContextMenuManager используется для управления элементами контекстного меню. Атрибут GridDesktop.ContextMenuManager получает экземпляр объекта ContextMenuManager. Например, атрибут ContextMenuManager.MenuItemAvailable_Copy получает или задает значение, указывающее, доступен ли элемент контекстного меню **Копировать**. Точно так же у нас есть все соответствующие атрибуты для разных пунктов контекстного меню.

**ВАЖНЫЙ:** По умолчанию в списке видны все пункты контекстного меню.
## **Управление контекстным меню**
### **Скрытие пунктов контекстного меню**
Чтобы выполнить эту задачу, мы сначала рассмотрим контекстное меню по умолчанию, которое есть в GridDesktop.

**Меню GridDeskop по умолчанию** 

![дело:изображение_альтернативный_текст](managing-griddesktops-context-menu_1.png)

Теперь скройте некоторые пункты меню, используя приведенный ниже код:



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-ManagingContextMenu-HideContextMenuItem.cs" >}}



После выполнения приведенного выше кода некоторые пункты меню не будут видны пользователям:

**Некоторые пункты меню скрыты** 

![дело:изображение_альтернативный_текст](managing-griddesktops-context-menu_2.png)
### **Добавление новых пунктов меню**
Добавьте в список новый элемент контекстного меню, используя следующий фрагмент кода.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-ManagingContextMenu-AddContextMenuItem.cs" >}}


Мы также указываем обработчик событий для новой команды/параметра.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-ManagingContextMenu-EventHandler.cs" >}}



После выполнения приведенного выше кода в контекстном меню можно увидеть новый пункт меню. Сообщение также появится при нажатии на ячейку.

**В список добавлен новый пункт меню** 

![дело:изображение_альтернативный_текст](managing-griddesktops-context-menu_3.png)
