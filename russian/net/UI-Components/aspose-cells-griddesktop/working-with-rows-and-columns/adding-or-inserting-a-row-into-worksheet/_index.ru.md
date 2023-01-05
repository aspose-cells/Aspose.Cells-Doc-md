---
title: Добавление или вставка строки в рабочий лист
type: docs
weight: 30
url: /ru/net/adding-or-inserting-a-row-into-worksheet/
---
{{% alert color="primary" %}} 

Как и в одном из наших предыдущих разделов, в этом разделе описывается функция добавления и вставки строк на рабочие листы во время выполнения с использованием API из Aspose.Cells.GridDesktop. Основное различие между добавлением и вставкой заключается в том, что, кроме того, строка добавляется в конец коллекции строк рабочего листа, где, как и при вставке, строка может быть добавлена в любую указанную позицию на рабочем листе.

{{% /alert %}} 
## **Добавление строки на лист**
Чтобы добавить новую строку на лист, выполните следующие действия:

-  Добавьте элемент управления Aspose.Cells.GridDesktop в свой**Форма**
-  Доступ к любому желаемому**Рабочий лист**
-  Добавлять**Строка** к**Рабочий лист**



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-AddInsertRow-AddRow.cs" >}}
## **Вставка строки в рабочий лист**
Чтобы вставить новую строку в лист в указанном месте, выполните следующие действия:

-  Добавьте элемент управления Aspose.Cells.GridDesktop в свой**Форма**
-  Доступ к любому желаемому**Рабочий лист**
-  Вставлять**Строка** в**Рабочий лист**(в определенной позиции, указав индекс строки, куда ее вставить)

{{< highlight "java" >}}

 // Accessing first worksheet of the Grid

Aspose.Cells.GridDesktop.Worksheet sheet = gridDesktop1.Worksheets[0];

// Inserting row to the worksheet to the first position.

sheet.Cells.InsertRow(0);

{{< /highlight >}}
