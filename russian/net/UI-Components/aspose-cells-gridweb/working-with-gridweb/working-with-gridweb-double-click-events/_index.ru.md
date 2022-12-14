---
title: Работа с событиями двойного щелчка GridWeb
type: docs
weight: 80
url: /ru/net/working-with-gridweb-double-click-events/
---
{{% alert color="primary" %}} 

Aspose.Cells.GridWeb содержит три типа событий двойного щелчка:

- CellDoubleClick, срабатывает при двойном щелчке по ячейке.
- ColumnDoubleClick, срабатывает при двойном щелчке заголовка столбца.
- RowDoubleClick, срабатывает при двойном щелчке заголовка строки.

В этом разделе обсуждается, как включить события двойного щелчка в Aspose.Cells.GridWeb. Также обсуждается создание обработчиков событий для этих событий.

{{% /alert %}} 
## **Включение событий двойного щелчка**
Все типы событий двойного щелчка можно включить на стороне клиента, задав для свойства EnableDoubleClickEvent элемента управления GridWeb значение true.

{{% alert color="primary" %}} 

По умолчанию для свойства EnableDoubleClickEvent установлено значение false. Это означает, что события двойного щелчка не включены по умолчанию. Чтобы реализовать такие события, сначала включите эту функцию.

{{% /alert %}} 

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-HandleDoubleClickEvents.aspx-EnableDoubleClickEvents.cs" >}}



После включения событий двойного щелчка можно создавать обработчики событий для любых событий двойного щелчка. Эти обработчики событий выполняют определенные задачи, когда запускается данное событие двойного щелчка.
## **Обработка событий двойного щелчка**
Чтобы создать обработчик событий в Visual Studio:

1.  Дважды щелкните событие в**События** список на панели свойств.

В этом примере мы реализовали обработчики событий для различных событий двойного щелчка.
### **Двойной щелчок Cell**
Обработчик события CellDoubleClick предоставляет аргумент типа CellEventArgs, предоставляющий полную информацию о ячейке, по которой выполняется двойной щелчок.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-HandleDoubleClickEvents.aspx-CellDoubleClickEvent.cs" >}}
### **Двойной щелчок по заголовку столбца**
Обработчик событий для события ColumnDoubleClick предоставляет аргумент типа RowColumnEventArgs, предоставляющий порядковый номер столбца для заголовка, по которому был выполнен двойной щелчок, и другую информацию.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-HandleDoubleClickEvents.aspx-ColumnDoubleClickEvent.cs" >}}
### **Двойной щелчок по заголовку строки**
Обработчик событий для события RowDoubleClick предоставляет аргумент типа RowColumnEventArgs, предоставляющий порядковый номер строки для заголовка, по которому был выполнен двойной щелчок, и другую связанную информацию.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-HandleDoubleClickEvents.aspx-RowDoubleClickEvent.cs" >}}
