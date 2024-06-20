---
title: Работа с событиями двойного щелчка GridWeb
type: docs
weight: 80
url: /ru/net/aspose-cells-gridweb/gridweb-double-click-event/
keywords: GridWeb, двойной щелчок, событие щелчка, событие
description: Эта статья представляет, как использовать событие двойного щелчка в GridWeb.
---

{{% alert color="primary" %}} 

Aspose.Cells.GridWeb содержит три типа событий двойного щелчка:

- CellDoubleClick, срабатывает, когда ячейка дважды щелкается.
- ColumnDoubleClick, срабатывает, когда дважды щелкается заголовок столбца.
- RowDoubleClick, срабатывает, когда дважды щелкается заголовок строки.

В этой статье обсуждается, как включить события двойного щелчка в Aspose.Cells.GridWeb. Она также обсуждает создание обработчиков событий для этих событий.

{{% /alert %}} 
## **Включение событий двойного щелчка**
Все типы событий двойного щелчка могут быть включены на стороне клиента, установив свойство EnableDoubleClickEvent элемента управления GridWeb в true.

{{% alert color="primary" %}} 

По умолчанию свойство EnableDoubleClickEvent установлено в false. Это означает, что события двойного щелчка по умолчанию отключены. Чтобы реализовать такие события, сначала включите функцию.

{{% /alert %}} 

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-HandleDoubleClickEvents.aspx-EnableDoubleClickEvents.cs" >}}



После включения событий двойного щелчка можно создать обработчики событий для любых событий двойного щелчка. Эти обработчики событий выполняют определенные задачи, когда данное событие двойного щелчка срабатывает.
## **Обработка событий двойного щелчка**
Чтобы создать обработчик событий в Visual Studio:

1. Дважды щелкните событие в списке **События** в панели свойств.

В данном примере мы реализовали обработчики событий для различных двойных щелчков.
### **Двойной щелчок по ячейке**
Обработчик события для события CellDoubleClick предоставляет аргумент типа CellEventArgs, который содержит полную информацию о ячейке, по которой был выполнен двойной щелчок.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-HandleDoubleClickEvents.aspx-CellDoubleClickEvent.cs" >}}
### **Двойной щелчок по заголовку столбца**
Обработчик события для события ColumnDoubleClick предоставляет аргумент типа RowColumnEventArgs, который содержит номер индекса столбца для заголовка, по которому был выполнен двойной щелчок, а также другую информацию.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-HandleDoubleClickEvents.aspx-ColumnDoubleClickEvent.cs" >}}
### **Двойной щелчок по заголовку строки**
Обработчик события для события RowDoubleClick предоставляет аргумент типа RowColumnEventArgs, который содержит номер индекса строки для заголовка, по которому был выполнен двойной щелчок, а также другую связанную информацию.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-HandleDoubleClickEvents.aspx-RowDoubleClickEvent.cs" >}}
