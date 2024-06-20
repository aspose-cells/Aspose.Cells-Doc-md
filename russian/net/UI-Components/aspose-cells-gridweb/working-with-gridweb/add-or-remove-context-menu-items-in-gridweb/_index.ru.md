---
title: Добавление или удаление пунктов контекстного меню в GridWeb
type: docs
weight: 130
url: /ru/net/aspose-cells-gridweb/add-or-remove-context-menu-items-in-gridweb/
keywords: GridWeb, контекстное меню, меню
description: В этой статье рассматривается способ добавления или удаления пунктов контекстного меню в GridWeb.
---

{{% alert color="primary" %}} 

Вы можете добавлять элементы контекстного меню с использованием разметки ASP.NET или с помощью кода .NET. Вы также можете удалять элементы контекстного меню с использованием кода .NET. Для этого используйте методы GridWeb.CustomCommandButtons.Add() и GridWeb.CustomCommandButtons.Remove() или RemoveAt().

{{% /alert %}} 
## **Добавить элемент контекстного меню с использованием разметки ASP.NET**
Следующая разметка ASP.NET добавляет элемент контекстного меню в GridWeb.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-AddRemoveContextMenuItem-InitContextMenuItem.aspx" >}}



Вот полная разметка ASP.NET, создающая GridWeb с указанным элементом контекстного меню. Обратите внимание на атрибут OnCustomCommand="GridWeb1_CustomCommand". Это имя обработчика событий, которое будет вызвано при щелчке на ваш элемент контекстного меню.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-InitContextMenuItem-InitContextMenuItem.aspx" >}}



Так выглядит элемент контекстного меню после добавления с использованием указанной разметки ASP.NET.

![todo:image_alt_text](add-or-remove-context-menu-items-in-gridweb_1.png)

Это код обработчика событий, который выполняется при щелчке на элемент контекстного меню. Сначала код проверяет имя команды, если оно соответствует нашей команде, то добавляет текст в ячейку A1 активного листа GridWeb и устанавливает ширину первого столбца равной 40 единицам, чтобы текст был видимым.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-InitContextMenuItem.aspx-HandleContextMenuItemCommand.cs" >}}


Вот как выглядит GridWeb после щелчка на элемент контекстного меню.

![todo:image_alt_text](add-or-remove-context-menu-items-in-gridweb_2.png)
## **Добавление элементов контекстного меню в Aspose.Cells.GridWeb с использованием кода**
Этот код показывает, как добавить элемент контекстного меню в GridWeb с помощью кода.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-AddRemoveContextMenuItem.aspx-AddContextMenuItem.cs" >}}
## **Удаление элементов контекстного меню в Aspose.Cells.GridWeb с использованием кода**
Этот код показывает, как удалить элемент контекстного меню с помощью методов CustomCommandButtons.Remove() и CustomCommandButtons.RemoveAt().



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-AddRemoveContextMenuItem.aspx-RemoveContextMenuItem.cs" >}}
