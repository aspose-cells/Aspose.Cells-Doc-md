---
title: Добавление или вставка столбца в Лист
type: docs
weight: 10
url: /ru/net/aspose-cells-griddesktop/add-or-insert-a-column-into-worksheet/
keywords: GridDesktop,вставить,добавить,столбец,вставить столбец,вставить строку
description: В этой статье рассматривается способ вставки или добавления столбца в GridDesktop.
---

{{% alert color="primary" %}} 

В этой теме мы опишем основную функцию добавления и вставки столбцов в Листы во время выполнения с использованием API Aspose.Cells.GridDesktop. Основное различие между добавлением и вставкой заключается в том, что при добавлении столбец добавляется в конец коллекции столбцов Листа, а при вставке столбец можно добавить в любую указанную позицию в Листе.

{{% /alert %}} 
## **Добавление столбца в Лист**
Чтобы добавить новый столбец в Лист, выполните следующие шаги:

- Добавьте элемент управления Aspose.Cells.GridDesktop на ваш **Форм**
- Получить доступ к любому желаемому **Рабочему листу**
- Добавить **столбец** в **Worksheet**



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-AddInsertColumn-AddColumn.cs" >}}
## **Вставка столбца в Лист**
Чтобы вставить новый столбец в лист по указанной позиции, выполните следующие шаги:

- Добавьте элемент управления Aspose.Cells.GridDesktop на ваш **Форм**
- Получить доступ к любому желаемому **Рабочему листу**
- Вставьте **Столбец** в **Лист** (в определенное положение, указав индекс столбца, куда его вставить)

{{< highlight java >}}

 // Accessing first worksheet of the Grid

Aspose.Cells.GridDesktop.Worksheet sheet = gridDesktop1.Worksheets[0];

// Inserting column to the worksheet to the first position.

sheet.Cells.InsertColumn(0);

{{< /highlight >}}
