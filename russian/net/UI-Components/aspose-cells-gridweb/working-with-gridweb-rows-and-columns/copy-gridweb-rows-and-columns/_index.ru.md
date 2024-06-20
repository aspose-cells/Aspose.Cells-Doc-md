---
title: Копирование строк и столбцов GridWeb
type: docs
weight: 80
url: /ru/net/aspose-cells-gridweb/copy-gridweb-rows-and-columns/
keywords: GridWeb, копировать
description: В этой статье рассматривается способ копирования строк и столбцов в GridWeb.
---

{{% alert color="primary" %}} 

Компонент Aspose.Cells.GridWeb предлагает способ копирования строк и столбцов при использовании класса GridCells. В этой статье демонстрируется использование API, предоставленного компонентом Aspose.Cells.GridWeb, для копирования строк и столбцов на интерфейсе GridWeb. 

Методы GridCells.CopyRow, GridCells.CopyColumn, GridCells.CopyRows и GridCells.CopyColumns будут копировать содержимое, стили и формулы из исходной строки и столбца в назначение.

{{% /alert %}} 
## **Копирование строк и столбцов**
Если вы еще не знакомы с компонентом Aspose.Cells.GridWeb, мы настоятельно рекомендуем вам ознакомиться с [Введение в Aspose.Cells.GridWeb](https://docs.aspose.com/cells/net/aspose-cells-gridweb/browsers-capabilities/) и подробной статьей о [Как добавить компонент Aspose.Cells.GridWeb в веб-приложение WebForms](https://docs.aspose.com/cells/net/aspose-cells-gridweb/add-gridweb-to-web-form/).
### **Копирование одной строки**
Для того чтобы привести пример копирования строки, в этой статье используется существующая электронная таблица с одной строкой и простой формулой, суммирующей все значения в строке. Вот как электронная таблица отображается в интерфейсе Aspose.Cells.GridWeb перед копированием строки.

![todo:image_alt_text](copy-gridweb-rows-and-columns_1.png)

Фрагмент кода прост, как показано ниже. Он обращается к объекту GridCells активного рабочего листа для создания копии первой строки в последующую строку.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-CopyRowsColumns.aspx-CopyRow.cs" >}}


Вот как выглядит Aspose.Cells.GridWeb после операции копирования строки.

![todo:image_alt_text](copy-gridweb-rows-and-columns_2.png)
### **Копирование одного столбца**
В следующем примере используется существующая электронная таблица с одним столбцом и простой формулой, которая суммирует все значения в столбце. Вот как электронная таблица отображается в интерфейсе Aspose.Cells.GridWeb до копирования столбца.

![todo:image_alt_text](copy-gridweb-rows-and-columns_3.png)

Аналогично предыдущему примеру, следующий фрагмент кода обращается к объекту GridCells активного рабочего листа для создания копии первого столбца в последующем столбце.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-CopyRowsColumns.aspx-CopyColumn.cs" >}}



Вот как выглядит Aspose.Cells.GridWeb после операции копирования столбца.

![todo:image_alt_text](copy-gridweb-rows-and-columns_4.png)

{{% alert color="primary" %}} 

Вы можете использовать методы GridCells.CopyRow & GridCells.CopyColumn в цикле для копирования исходной строки & столбца в несколько строк & столбцов соответственно.

{{% /alert %}} 
### **Копирование нескольких строк**
Также можно скопировать несколько строк в новое место с использованием метода GridCells.CopyRows, который принимает дополнительный параметр типа integer для указания количества копируемых исходных строк.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-CopyRowsColumns.aspx-CopyMultipleRows.cs" >}}



Вот как выглядит Aspose.Cells.GridWeb до & после операции копирования столбцов.

![todo:image_alt_text](copy-gridweb-rows-and-columns_5.png)

![todo:image_alt_text](copy-gridweb-rows-and-columns_6.png)
### **Копирование нескольких столбцов**
Класс GridCells также предоставляет метод CopyColumns, который принимает дополнительный параметр типа integer для указания количества копируемых исходных столбцов.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-CopyRowsColumns.aspx-CopyMultipleColumns.cs" >}}



Вот как выглядит Aspose.Cells.GridWeb до & после операции копирования столбцов.

![todo:image_alt_text](copy-gridweb-rows-and-columns_7.png)

![todo:image_alt_text](copy-gridweb-rows-and-columns_8.png)
