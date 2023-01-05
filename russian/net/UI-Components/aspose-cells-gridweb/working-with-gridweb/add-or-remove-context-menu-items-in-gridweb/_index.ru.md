---
title: Добавление или удаление элементов контекстного меню в GridWeb
type: docs
weight: 130
url: /ru/net/add-or-remove-context-menu-items-in-gridweb/
---
{{% alert color="primary" %}} 

Вы можете добавить элементы контекстного меню, используя разметку ASP.NET или код .NET. Вы также можете удалить пункты контекстного меню, используя код .NET. Для этих целей используйте методы GridWeb.CustomCommandButtons.Add() и GridWeb.CustomCommandButtons.Remove() или RemoveAt().

{{% /alert %}} 
## **Добавить пункт контекстного меню с помощью разметки ASP.NET**
Следующая разметка ASP.NET добавляет элемент контекстного меню в GridWeb.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-AddRemoveContextMenuItem-InitContextMenuItem.aspx" >}}



Вот полная разметка ASP.NET, которая создает GridWeb с указанным выше элементом контекстного меню. Обратите внимание на атрибут OnCustomCommand="GridWeb1_CustomCommand". Это имя обработчика события, которое будет вызываться при нажатии на элемент контекстного меню.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-InitContextMenuItem-InitContextMenuItem.aspx" >}}



Вот как выглядит элемент контекстного меню после добавления с использованием приведенной выше разметки ASP.NET.

![дело:изображение_альтернативный_текст](add-or-remove-context-menu-items-in-gridweb_1.png)

Это код обработчика событий, который выполняется при нажатии на элемент контекстного меню. Код сначала проверяет имя команды, и если оно соответствует нашей команде, он добавляет текст в ячейку A1 активного рабочего листа GridWeb и устанавливает ширину первого столбца на 40 единиц, чтобы сделать текст видимым.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-InitContextMenuItem.aspx-HandleContextMenuItemCommand.cs" >}}


Вот как выглядит GridWeb, когда вы щелкаете пункт контекстного меню.

![дело:изображение_альтернативный_текст](add-or-remove-context-menu-items-in-gridweb_2.png)
## **Добавить элементы контекстного меню в Aspose.Cells.GridWeb с помощью кода**
В этом коде показано, как добавить элемент контекстного меню в GridWeb с помощью кода.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-AddRemoveContextMenuItem.aspx-AddContextMenuItem.cs" >}}
## **Удалить элементы контекстного меню в Aspose.Cells.GridWeb с помощью кода**
Этот код показывает, как удалить элемент контекстного меню с помощью методов CustomCommandButtons.Remove() и CustomCommandButtons.RemoveAt().



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-AddRemoveContextMenuItem.aspx-RemoveContextMenuItem.cs" >}}
