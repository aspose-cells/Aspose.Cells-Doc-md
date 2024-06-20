---
title: Добавление или вставка строки в лист
type: docs
weight: 30
url: /ru/net/aspose-cells-griddesktop/add-or-insert-a-row-into-worksheet/
keywords: GridDesktop,insert,add,row,insert row,add row
description: В этой статье рассматривается добавление или вставка строки в GridDesktop.
---

{{% alert color="primary" %}} 

Подобно одной из наших предыдущих тем, в этой статье описывается возможность добавления и вставки строк в листы во время выполнения с использованием API Aspose.Cells.GridDesktop. Основное различие между добавлением и вставкой заключается в том, что при добавлении строка добавляется в конец коллекции строк листа, в то время как при вставке строку можно добавить в любую указанную позицию в листе.

{{% /alert %}} 
## **Добавление строки в лист**
Чтобы добавить новую строку в лист, выполните следующие шаги:

- Добавьте элемент управления Aspose.Cells.GridDesktop на ваш **Форм**
- Получить доступ к любому желаемому **Рабочему листу**
- Добавьте **Строку** в **Лист**



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-AddInsertRow-AddRow.cs" >}}
## **Вставка строки в лист**
Чтобы вставить новую строку в лист по указанной позиции, выполните следующие шаги:

- Добавьте элемент управления Aspose.Cells.GridDesktop на ваш **Форм**
- Получить доступ к любому желаемому **Рабочему листу**
- Вставьте **Строку** в **Лист** (в определенное положение, указав индекс строки, куда ее вставить)

{{< highlight java >}}

 // Accessing first worksheet of the Grid

Aspose.Cells.GridDesktop.Worksheet sheet = gridDesktop1.Worksheets[0];

// Inserting row to the worksheet to the first position.

sheet.Cells.InsertRow(0);

{{< /highlight >}}
