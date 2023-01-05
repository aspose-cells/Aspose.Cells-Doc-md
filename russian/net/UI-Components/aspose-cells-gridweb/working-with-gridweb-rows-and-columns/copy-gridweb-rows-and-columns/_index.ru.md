---
title: Копирование строк и столбцов GridWeb
type: docs
weight: 80
url: /ru/net/copy-gridweb-rows-and-columns/
---
{{% alert color="primary" %}} 

 Aspose.Cells. Компонент GridWeb предлагает средства для копирования строки и столбца при использовании класса GridCells. В этой статье демонстрируется использование API-интерфейсов, предоставляемых Aspose.Cells.GridWeb, для копирования строк и столбцов в интерфейсе GridWeb.

Методы GridCells.CopyRow, GridCells.CopyColumn, GridCells.CopyRows и GridCells.CopyColumns копируют содержимое, стили и формулы из исходной строки и столбца в место назначения.

{{% /alert %}} 
## **Копирование строк и столбцов**
 Если вы еще не знакомы с компонентом Aspose.Cells.GridWeb, мы настоятельно рекомендуем вам проверить[Введение в Aspose.Cells.GridWeb](https://docs.aspose.com/cells/net/browsers-capabilities/) и подробная статья о[Как добавить компонент Aspose.Cells.GridWeb в приложение WebForms](https://docs.aspose.com/cells/net/add-gridweb-to-web-form/).
### **Копирование одной строки**
Для простоты примера в статье используется существующая электронная таблица с одной строкой и простая формула, которая суммирует все значения в строке. Вот как электронная таблица отображается в интерфейсе Aspose.Cells.GridWeb перед копированием строки.

![дело:изображение_альтернативный_текст](copy-gridweb-rows-and-columns_1.png)

Фрагмент кода прост, как показано ниже. Он обращается к объекту GridCells активного рабочего листа, чтобы сделать копию первой строки в последующую строку.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-CopyRowsColumns.aspx-CopyRow.cs" >}}


Вот как выглядит Aspose.Cells.GridWeb после операции копирования строки.

![дело:изображение_альтернативный_текст](copy-gridweb-rows-and-columns_2.png)
### **Копирование одного столбца**
В следующем примере используется существующая электронная таблица с одним столбцом и простая формула, которая суммирует все значения в столбце. Вот как электронная таблица отображается в интерфейсе Aspose.Cells.GridWeb перед копированием столбца.

![дело:изображение_альтернативный_текст](copy-gridweb-rows-and-columns_3.png)

Как и в приведенном выше примере, следующий фрагмент кода обращается к объекту GridCells в порядке активного рабочего листа, чтобы сделать копию первого столбца в последующий столбец.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-CopyRowsColumns.aspx-CopyColumn.cs" >}}



Вот как выглядит Aspose.Cells.GridWeb после операции копирования столбца.

![дело:изображение_альтернативный_текст](copy-gridweb-rows-and-columns_4.png)

{{% alert color="primary" %}} 

Вы можете использовать методы GridCells.CopyRow и GridCells.CopyColumn в цикле, чтобы скопировать исходную строку и столбец в несколько строк и столбцов соответственно.

{{% /alert %}} 
### **Копирование нескольких строк**
Также можно скопировать несколько строк в новое место назначения при использовании метода GridCells.CopyRows, который принимает дополнительный параметр типа integer, чтобы указать количество копируемых исходных строк.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-CopyRowsColumns.aspx-CopyMultipleRows.cs" >}}



Вот как выглядит Aspose.Cells.GridWeb до и после операции копирования строк.

![дело:изображение_альтернативный_текст](copy-gridweb-rows-and-columns_5.png)

![дело:изображение_альтернативный_текст](copy-gridweb-rows-and-columns_6.png)
### **Копирование нескольких столбцов**
Класс GridCells также предоставляет метод CopyColumns, который принимает дополнительный параметр типа integer, чтобы указать количество копируемых исходных столбцов.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-CopyRowsColumns.aspx-CopyMultipleColumns.cs" >}}



Вот как выглядит Aspose.Cells.GridWeb до и после операции копирования строк.

![дело:изображение_альтернативный_текст](copy-gridweb-rows-and-columns_7.png)

![дело:изображение_альтернативный_текст](copy-gridweb-rows-and-columns_8.png)
