---
title: Копирование строк и столбцов
type: docs
weight: 40
url: /ru/net/copying-rows-and-columns/
description: В этой статье показано, как копировать строки и столбцы через Aspose.Cells for .NET API.
keywords: C# How to Copy Rows and Columns, Copy Rows in C#, Copy Columns using C#, How to Paste Rows and Columns using Aspose.Cells for .NET, Paste multiple rows and columns, How to Copy and paste Single Row or Column.
---
##  **Введение**

Иногда вам нужно скопировать строки и столбцы на листе, не копируя весь лист. С помощью Aspose.Cells можно копировать строки и столбцы внутри книг или между ними.
При копировании строки (или столбца) содержащиеся в ней данные, включая формулы (с обновленными ссылками) и значения, комментарии, форматирование, скрытые ячейки, изображения и другие объекты рисования, также копируются.

##  **Как скопировать строки и столбцы с помощью Microsoft Excel**

1. Выберите строку или столбец, который вы хотите скопировать.
1.  Чтобы скопировать строки или столбцы, нажмите**Копировать** на**Стандартный** панель инструментов или нажмите**CTRL**+*С**.
1. Выберите строку или столбец ниже или справа от того места, куда вы хотите скопировать свой выбор.
1.  При копировании строк или столбцов нажмите кнопку**Скопировано Cells** на**Вставлять** меню.

{{% alert color="primary" %}}

 Если вы нажмете**Вставить** на**Стандартный** панель инструментов или нажмите**CTRL**+**V** вместо нажатия команды на **Вставить**меню, любое содержимое ячеек назначения заменяется.

{{% /alert %}}

##  **Как вставить строки и столбцы с помощью параметров вставки в Excel Microsoft**

1. Выберите ячейки, содержащие данные или другие атрибуты, которые вы хотите скопировать.
1. На вкладке «Главная» нажмите *Копировать**.
1.  Щелкните первую ячейку в области, в которой вы хотите**вставить** то, что ты скопировал.
1.  На вкладке Главная щелкните стрелку рядом с надписью**Вставить**, а затем выберите **Вставить.** Особенный.
1.  Выберите**параметры** вы хотите.

##  **Как скопировать строки и столбцы с помощью Aspose.Cells for .NET**

##  **Как скопировать отдельные строки**

 Aspose.Cells обеспечивает[**Копироватьстроку**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrow) метод[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)сорт. Этот метод копирует все типы данных, включая формулы, значения, комментарии, форматы ячеек, скрытые ячейки, изображения и другие объекты рисования, из исходной строки в целевую строку.

[**Копироватьстроку**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrow)метод принимает следующие параметры:

-  источник[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)объект,
- индекс исходной строки и
- индекс строки назначения.

 Используйте этот метод, чтобы скопировать строку на листе или на другой лист.[**Копироватьстроку**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrow)Метод работает аналогично Microsoft Excel. Так, например, вам не нужно явно задавать высоту целевой строки, это значение тоже копируется.

В следующем примере показано, как скопировать строку на листе. Он использует файл Excel шаблона Microsoft и копирует вторую строку (вместе с данными, форматированием, комментариями, изображениями и т. д.) и вставляет ее в 12-ю строку на том же листе.

 Вы можете пропустить шаг, который получает высоту исходной строки, используя[**Cells.GetRowHeight**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/getrowheight) метод, а затем устанавливает высоту строки назначения, используя метод[**Cells.SetRowHeight**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setrowheight) метод как[**Копироватьстроку**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrow)метод автоматически заботится о высоте строки.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Copying-CopyingRows-1.cs" >}}

{{% alert color="primary" %}}

При копировании строк важно отмечать связанные изображения, диаграммы или другие объекты рисования, так как это то же самое, что и Microsoft Excel:

1. Если индекс исходной строки равен 5, изображение, диаграмма и т. д. копируются, если они содержатся в трех строках (индекс начальной строки — 4, а индекс конечной строки — 6).
1. Существующие изображения, диаграммы и т. д. в целевой строке не будут удалены.

{{% /alert %}}

##  **Как скопировать несколько строк**

Вы также можете скопировать несколько строк в новое место назначения, используя[**Cells.CopyRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrows/index)метод, который принимает дополнительный параметр целочисленного типа, чтобы указать количество копируемых исходных строк.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CopyRowsColumns-CopyingMultipleRows-1.cs" >}}


##  **Как скопировать столбцы**

 Aspose.Cells обеспечивает[**Копироватьколонку**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copycolumn) метод[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)class, этот метод копирует все типы данных, включая формулы (с обновленными ссылками) и значениями, комментариями, форматами ячеек, скрытыми ячейками, изображениями и другими объектами рисования из исходного столбца в целевой столбец.

[**Копироватьколонку**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copycolumn)метод принимает следующие параметры:

-  источник[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)объект,
- индекс исходного столбца и
- индекс столбца назначения.

 Использовать[**Копироватьколонку**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copycolumn)метод для копирования столбца на листе или на другой лист.

В этом примере столбец копируется с листа и вставляется на лист другой книги.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Copying-CopyingColumns-1.cs" >}}

##  **Как скопировать несколько столбцов**

 Похожий на[**Cells.CopyRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrows/index) API Aspose.Cells также предоставляют[**Cells.CopyColumns**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copycolumns/index)метод, чтобы скопировать несколько исходных столбцов в новое место.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CopyRowsColumns-CopyingMultipleColumns-1.cs" >}}


##  **Как вставить строки и столбцы с помощью параметров вставки**

 Aspose.Cells теперь предоставляет[**Параметры вставки**](https://reference.aspose.com/cells/net/aspose.cells/pasteoptions) при использовании функций[**КопироватьРовс**](https://reference.aspose.com/cells/net/aspose.cells.cells/copyrows/methods/2) и[**Копировать столбцы**](https://reference.aspose.com/cells/net/aspose.cells.cells/copycolumns/methods/1). Это позволяет установить соответствующий параметр вставки, аналогичный Excel.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Copying-PastingRowsColumnsWithPasteOptions-1.cs" >}}

