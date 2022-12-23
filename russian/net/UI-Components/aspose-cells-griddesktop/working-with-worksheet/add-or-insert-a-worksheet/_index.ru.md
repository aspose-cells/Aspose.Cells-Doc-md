---
title: Добавить или вставить рабочий лист
type: docs
weight: 20
url: /ru/net/add-or-insert-a-worksheet/
---
{{% alert color="primary" %}} 

В этом разделе мы обсудим методы добавления или вставки рабочих листов в файл Excel с помощью Aspose.Cells.GridDesktop. Разница между добавлением и вставкой рабочих листов заключается в том, что, кроме того, рабочий лист просто добавляется в конец коллекции рабочих листов файла Excel, однако вставка означает добавление рабочего листа в определенную позицию в коллекции рабочих листов.

{{% /alert %}} 
## **Добавление рабочего листа**
Чтобы добавить рабочий лист с помощью Aspose.Cells.GridDesktop, выполните следующие действия:

1. Добавьте в форму элемент управления Aspose.Cells.GridDesktop.
1. Вызовите метод Add коллекции Worksheet в элементе управления GridDesktop.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddInsertWorksheet-AddingWorksheet.cs" >}}


Доступно множество перегруженных версий метода Add. Например, при использовании приведенной выше перегруженной версии рабочий лист добавляется в файл Excel с именем листа по умолчанию. Используя другие перегруженные версии метода Add, можно определить имя, как показано ниже в примере.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddInsertWorksheet-AddingWorksheetWithName.cs" >}}
## **Вставка рабочего листа**
Чтобы вставить рабочий лист с помощью Aspose.Cells.GridDesktop, выполните следующие действия:

1. Добавьте в форму элемент управления Aspose.Cells.GridDesktop.
1. Вызовите метод Insert коллекции Worksheets в элементе управления GridDesktop.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddInsertWorksheet-InsertingWorksheet.cs" >}}

{{% alert color="primary" %}} 

ВАЖНО: Microsoft Excel (97-2003 XLS) поддерживает листы Excel, содержащие до 65 536 строк и 256 столбцов. Aspose.Cells.GridDesktop следует тем же стандартам. В элементе управления Aspose.Cells.GridDesktop разработчики могут добавлять или вставлять рабочие листы с большим количеством строк и столбцов, чем стандартное ограничение, но при попытке сохранить данные сетки в файл Excel будет выдано исключение. Это означает, что только данные, содержащиеся в 65 536 строках и 256 столбцах, могут быть сохранены в файле Excel XLS с использованием Aspose.Cells.GridDesktop, однако, если вы используете формат файла XLSX (MS Excel 2007/2010), такого ограничения нет.

{{% /alert %}}
