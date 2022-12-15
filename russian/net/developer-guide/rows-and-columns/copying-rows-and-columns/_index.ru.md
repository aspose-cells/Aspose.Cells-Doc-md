---
title: Копирование строк и столбцов
type: docs
weight: 40
url: /ru/net/copying-rows-and-columns/
---
## **Введение**

Иногда вам нужно скопировать строки и столбцы на листе, не копируя весь лист. С помощью Aspose.Cells можно копировать строки и столбцы внутри или между книгами.
При копировании строки (или столбца) содержащиеся в ней данные, включая формулы (с обновленными ссылками), а также значения, комментарии, форматирование, скрытые ячейки, изображения и другие объекты чертежа также копируются.

## **Копирование строк и столбцов с помощью Microsoft Excel**

1. Выберите строку или столбец, которые вы хотите скопировать.
1.  Чтобы скопировать строки или столбцы, щелкните**Копировать** на**Стандарт** панели инструментов или нажмите**CTRL**+**С**.
1. Выберите строку или столбец ниже или справа от того места, куда вы хотите скопировать свой выбор.
1.  При копировании строк или столбцов щелкните**Скопировано Cells** на**Вставлять** меню.

{{% alert color="primary" %}}

 Если вы нажмете**Вставить** на**Стандарт** панель инструментов или нажмите**CTRL**+** V** вместо нажатия команды на**В меню «Вставка**» любое содержимое ячеек назначения заменяется.

{{% /alert %}}

## **Вставка строк и столбцов с использованием параметров вставки с Microsoft Excel**

1. Выберите ячейки, содержащие данные или другие атрибуты, которые вы хотите скопировать.
1.  На вкладке Главная щелкните**Копировать**.
1.  Щелкните первую ячейку в области, где вы хотите**вставить** что ты скопировал.
1.  На вкладке Главная щелкните стрелку рядом с**Вставить** , а затем выберите**Вставить** Специальный.
1.  Выберите**опции** ты хочешь.

## **Использование Aspose.Cells**

## **Копирование отдельных строк**

 Aspose.Cells обеспечивает[**КопиРоу**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrow) метод[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)учебный класс. Этот метод копирует все типы данных, включая формулы, значения, комментарии, форматы ячеек, скрытые ячейки, изображения и другие объекты рисования из исходной строки в целевую строку.

[**КопиРоу**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrow)метод принимает следующие параметры:

-  источник[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)объект,
- индекс исходной строки и
- индекс строки назначения.

 Используйте этот метод, чтобы скопировать строку на листе или на другой лист.[**КопиРоу**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrow)метод работает аналогично Microsoft Excel. Так, например, вам не нужно явно задавать высоту строки назначения, это значение также копируется.

В следующем примере показано, как скопировать строку на листе. Он использует шаблон файла Excel Microsoft и копирует вторую строку (вместе с данными, форматированием, комментариями, изображениями и т. д.) и вставляет ее в 12-ю строку на том же рабочем листе.

 Вы можете пропустить шаг, который получает исходную высоту строки, используя[**Cells.GetRowHeight**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/getrowheight) метод, а затем устанавливает высоту строки назначения с помощью[**Cells.SetRowHeight**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setrowheight) метод как[**КопиРоу**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrow)метод автоматически заботится о высоте строки.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Copying-CopyingRows-1.cs" >}}

{{% alert color="primary" %}}

При копировании строк важно отметить связанные изображения, диаграммы или другие объекты рисования, так как это то же самое с Microsoft Excel:

1. Если индекс исходной строки равен 5, изображение, диаграмма и т. д. копируются, если они содержатся в трех строках (индекс начальной строки равен 4, а индекс конечной строки равен 6).
1. Существующие изображения, диаграммы и т. д. в строке назначения не будут удалены.

{{% /alert %}}

## **Копирование нескольких строк**

Вы также можете скопировать несколько строк в новое место назначения, используя[**Cells.CopyRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrows/index)метод, который принимает дополнительный параметр типа integer для указания количества копируемых исходных строк.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CopyRowsColumns-CopyingMultipleRows-1.cs" >}}


## **Копирование столбцов**

 Aspose.Cells обеспечивает[**КопиКолонка**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copycolumn) метод[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)class этот метод копирует все типы данных, включая формулы (с обновленными ссылками) и значения, комментарии, форматы ячеек, скрытые ячейки, изображения и другие объекты рисования из исходного столбца в целевой столбец.

[**КопиКолонка**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copycolumn)метод принимает следующие параметры:

-  источник[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)объект,
- индекс исходного столбца и
- индекс столбца назначения.

 Использовать[**КопиКолонка**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copycolumn)способ копирования столбца на листе или на другой лист.

В этом примере столбец копируется с листа и вставляется на лист в другой книге.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Copying-CopyingColumns-1.cs" >}}

## **Копирование нескольких столбцов**

 Похожий на[**Cells.CopyRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrows/index) метод, API-интерфейсы Aspose.Cells также предоставляют[**Cells.CopyColumns**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copycolumns/index)метод, чтобы скопировать несколько исходных столбцов в новое место.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CopyRowsColumns-CopyingMultipleColumns-1.cs" >}}


## **Вставка строк/столбцов с параметрами вставки**

 Aspose.Cells теперь обеспечивает[**Параметры вставки**](https://reference.aspose.com/cells/net/aspose.cells/pasteoptions) при использовании функций[**КопиРовс**](https://reference.aspose.com/cells/net/aspose.cells.cells/copyrows/methods/2) а также[**КопиКолонкс**](https://reference.aspose.com/cells/net/aspose.cells.cells/copycolumns/methods/1). Это позволяет установить соответствующий параметр вставки, аналогичный Excel.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Copying-PastingRowsColumnsWithPasteOptions-1.cs" >}}

