---
title: Добавление или вставка рабочего листа
type: docs
weight: 20
url: /ru/net/aspose-cells-griddesktop/add-or-insert-a-worksheet/
keywords: GridDesktop,insert,worksheet,insert worksheet
description: Эта статья рассказывает о том, как добавить или вставить рабочий лист в GridDesktop.
---

{{% alert color="primary" %}} 

В этой теме мы обсудим техники добавления или вставки рабочих листов в файл Excel с помощью Aspose.Cells.GridDesktop. Разница между добавлением и вставкой рабочих листов заключается в том, что при добавлении рабочий лист просто добавляется в конец коллекции рабочих листов файла Excel, тогда как вставка означает добавление рабочего листа на определенную позицию в коллекции рабочих листов.

{{% /alert %}} 
## **Добавление рабочего листа**
Чтобы добавить лист книги Excel с помощью Aspose.Cells.GridDesktop, выполните указанные ниже шаги:

1. Добавить элемент управления Aspose.Cells.GridDesktop на форму.
1. Вызовите метод Add коллекции Worksheet в элементе управления GridDesktop.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddInsertWorksheet-AddingWorksheet.cs" >}}


Множество перегруженных версий метода Add доступно. Используя вышеприведенную перегруженную версию, например, лист добавляется в файл Excel с именем листа по умолчанию. При использовании других перегруженных версий метода Add можно определить имя, как показано в следующем примере.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddInsertWorksheet-AddingWorksheetWithName.cs" >}}
## **Вставка листа**
Чтобы вставить лист с помощью Aspose.Cells.GridDesktop, выполните указанные ниже шаги:

1. Добавьте элемент управления Aspose.Cells.GridDesktop на форму.
1. Вызовите метод Insert коллекции Worksheets в элементе управления GridDesktop.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddInsertWorksheet-InsertingWorksheet.cs" >}}

{{% alert color="primary" %}} 

ВАЖНО: Microsoft Excel (97-2003 XLS) поддерживает листы Excel с количеством строк до 65 536 и 256 столбцов. Aspose.Cells.GridDesktop следует тем же стандартам. В элементе управления Aspose.Cells.GridDesktop разработчики могут добавлять или вставлять листы с большим количеством строк и столбцов, чем стандартный предел, но при попытке сохранить данные элемента управления Grid в файл Excel, будет сгенерироваться исключение. Это означает, что только данные, содержащиеся в 65 536 строках и 256 столбцах, могут быть сохранены в файл Excel XLS с использованием Aspose.Cells.GridDesktop. Если используется формат файла XLSX (MS Excel 2007/2010), такого ограничения нет.

{{% /alert %}}
