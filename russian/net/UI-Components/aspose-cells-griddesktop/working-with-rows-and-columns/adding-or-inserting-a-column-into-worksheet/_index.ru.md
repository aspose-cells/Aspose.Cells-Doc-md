---
title: Добавление или вставка столбца в рабочий лист
type: docs
weight: 10
url: /ru/net/adding-or-inserting-a-column-into-worksheet/
---
{{% alert color="primary" %}} 

В этом разделе мы опишем основную функцию добавления и вставки столбцов на рабочие листы во время выполнения с помощью API из Aspose.Cells.GridDesktop. Основное различие между добавлением и вставкой заключается в том, что, кроме того, столбец добавляется в конец коллекции столбцов рабочего листа, где, как и при вставке, столбец может быть добавлен в любую указанную позицию на рабочем листе.

{{% /alert %}} 
## **Добавление столбца на лист**
Чтобы добавить новый столбец на лист, выполните следующие действия:

-  Добавьте элемент управления Aspose.Cells.GridDesktop в свой**Форма**
-  Доступ к любому желаемому**Рабочий лист**
-  Добавлять**Столбец** к**Рабочий лист**



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-AddInsertColumn-AddColumn.cs" >}}
## **Вставка столбца в рабочий лист**
Чтобы вставить новый столбец в таблицу в указанном месте, выполните следующие действия:

-  Добавьте элемент управления Aspose.Cells.GridDesktop в свой**Форма**
-  Доступ к любому желаемому**Рабочий лист**
-  Вставлять**Столбец** в**Рабочий лист** (в определенной позиции, указав индекс столбца, куда его вставить)

{{< highlight "java" >}}

 // Accessing first worksheet of the Grid

Aspose.Cells.GridDesktop.Worksheet sheet = gridDesktop1.Worksheets[0];

// Inserting column to the worksheet to the first position.

sheet.Cells.InsertColumn(0);

{{< /highlight >}}
