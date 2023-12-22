---
title: Формат ячеек
description: Узнайте, как форматировать и стилизовать ячейки в Aspose.Cells for .NET, включая форматирование чисел, форматирование даты, стили шрифтов и другие параметры стиля ячеек. Наше руководство поможет вам создавать привлекательные и профессионально выглядящие таблицы.
keywords: Aspose.Cells for .NET, cell formatting, styling, number formatting, date formatting, font style, cell style options, spreadsheet, create, professional look, format rows and columns.
linktitle: Формат ячеек
type: docs
weight: 120
url: /ru/net/cells-formatting/
---
##  **Введение**

{{% alert color="primary" %}}

 Aspose.Cells обеспечивает[**GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle) и[**SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle) методы[Cell](https://reference.aspose.com/cells/net/aspose.cells/cell) класс, используемый для получения/установки стиля форматирования ячейки. Aspose.Cells также предоставляет[**Стиль**](https://reference.aspose.com/cells/net/aspose.cells/style)сорт.

{{% /alert %}}

##  **Как отформатировать Cells с помощью методов GetStyle и SetStyle**

Применяйте различные стили форматирования к ячейкам, чтобы установить цвета фона или переднего плана, границы, шрифты, горизонтальное и вертикальное выравнивание, уровень отступов, направление текста, угол поворота и многое другое.

###  **Как использовать методы GetStyle и SetStyle**

 Если разработчикам необходимо применять разные стили форматирования к разным ячейкам, лучше получить[**Стиль**](https://reference.aspose.com/cells/net/aspose.cells/style) клетки с помощью[**Cell.GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle) метод, укажите атрибуты стиля, а затем примените форматирование, используя[**Cell.SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle)метод. Ниже приведен пример, демонстрирующий этот подход к применению различного форматирования к ячейке.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ApproachesToFormatData-UsingGetStyleSetStyle-1.cs" >}}

###  **Как использовать объект стиля для форматирования разных форматов Cells**

 Если разработчикам необходимо применить один и тот же стиль форматирования к разным ячейкам, они могут использовать[**Стиль**](https://reference.aspose.com/cells/net/aspose.cells/style) объект. Пожалуйста, следуйте инструкциям ниже, чтобы использовать[**Стиль**](https://reference.aspose.com/cells/net/aspose.cells/style)объект:

1.  Добавить[**Стиль**](https://reference.aspose.com/cells/net/aspose.cells/style) объект, вызвав[**Создать стиль**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/createstyle) метод[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook)сорт
1.  Доступ к недавно добавленным[**Стиль**](https://reference.aspose.com/cells/net/aspose.cells/style) object
1.  Установите нужные свойства/атрибуты[**Стиль**](https://reference.aspose.com/cells/net/aspose.cells/style)объект для применения желаемых настроек форматирования
1.  Назначьте настроенное[**Стиль**](https://reference.aspose.com/cells/net/aspose.cells/style)возражайте против нужных ячеек

Этот подход может значительно повысить эффективность ваших приложений, а также сэкономить память.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ApproachesToFormatData-UsingStyleObject-1.cs" >}}

###  **Как использовать Microsoft Предопределенные стили Excel 2007**

Если вам нужно применить разные стили форматирования для Microsoft Excel 2007, примените стили, используя Aspose.Cells API. Ниже приведен пример, демонстрирующий этот подход для применения предопределенного стиля к ячейке.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ApproachesToFormatData-UsingExcelPredefinedStyles-1.cs" >}}



##  **Как отформатировать выбранные символы в коде Cell**

В разделе «Настройки шрифта» объясняется, как форматировать текст в ячейках, но объясняется только, как форматировать все содержимое ячейки. Что делать, если вы хотите отформатировать только выбранные символы?

Aspose.Cells также поддерживает эту функцию. В этом разделе объясняется, как эффективно использовать эту функцию.

###  **Как форматировать выбранные символы**

 Aspose.Cells предоставляет класс,[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook) который представляет файл Excel Microsoft.[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook) класс содержит[**Рабочие листы**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)коллекция, которая обеспечивает доступ к каждому листу в файле Excel. Рабочий лист представлен[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) сорт.[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) класс обеспечивает[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) коллекция. Каждый предмет в[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) коллекция представляет собой объект[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)сорт.

[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) класс обеспечивает[**Персонажи**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/characters)метод, который принимает следующие параметры для выбора диапазона символов внутри ячейки:

- *Начальный индекс** — индекс символа, с которого начинается выделение.
- *Количество символов** — количество символов для выбора.

[**Персонажи**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/characters) метод возвращает экземпляр[**Настройка шрифта**](https://reference.aspose.com/cells/net/aspose.cells/fontsetting)класс, который позволяет разработчикам форматировать символы так же, как и ячейку, как показано ниже в примере кода. В выходном файле в ячейке A1 слово «Посетить» будет отформатировано шрифтом по умолчанию, но «Aspose!» жирный и синий.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-FormattingSelectedCharacters-1.cs" >}}

{{% alert color="primary" %}}

Если вы хотите отформатировать часть форматированного текста в ячейке, рассмотрите возможность использования[**Cell.GetCharacters**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getcharacters) & [**Cell.SetCharacters**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setcharacters) методы.[[**Cell.GetCharacters**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getcharacters) метод следует использовать для доступа к частям текста, а затем можно внести поправки с помощью метода[**Cell.SetCharacters**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setcharacters) метод, тогда как**Получать** метод возвращает массив[**Настройка шрифта**](https://reference.aspose.com/cells/net/aspose.cells/fontsetting) объекты, которыми можно манипулировать для установки различных свойств, таких как имя шрифта, цвет шрифта, жирность и т. д., а также**Набор** метод можно использовать для применения изменений.

{{% /alert %}}

##  **Как форматировать строки и столбцы**

Иногда разработчикам необходимо применить одинаковое форматирование к строкам или столбцам. Применение форматирования к ячейкам по одной часто занимает больше времени и не является хорошим решением.
Чтобы решить эту проблему, Aspose.Cells предлагает простой и быстрый способ, подробно описанный в этой статье.

###  **Форматирование строк и столбцов**

 Aspose.Cells предоставляет класс,[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook) который представляет файл Excel Microsoft.[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook) класс содержит[**Рабочие листы**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) коллекция, которая обеспечивает доступ к каждому листу в файле Excel. Рабочий лист представлен[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) сорт.[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) класс обеспечивает[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) коллекция.[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) коллекция представляет собой[**Строки**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/rows)коллекция.

###  **Как отформатировать строку**

 Каждый предмет в[**Строки**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/rows) коллекция представляет собой[**Ряд**](https://reference.aspose.com/cells/net/aspose.cells/row) объект.[**Ряд**](https://reference.aspose.com/cells/net/aspose.cells/row)объект предлагает[**Применить стиль**](https://reference.aspose.com/cells/net/aspose.cells/row/methods/applystyle) метод, используемый для установки форматирования строки. Чтобы применить то же форматирование к строке, используйте[**Стиль**](https://reference.aspose.com/cells/net/aspose.cells/style)объект. Шаги ниже показывают, как его использовать.

1.  Добавить[**Стиль**](https://reference.aspose.com/cells/net/aspose.cells/style) возражать против[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook) класс, вызвав его[**Создать стиль**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/createstyle)метод.
1.  Установить[**Стиль**](https://reference.aspose.com/cells/net/aspose.cells/style)свойства объекта, чтобы применить настройки форматирования.
1.  Включите соответствующие атрибуты для[**СтильФлаг**](https://reference.aspose.com/cells/net/aspose.cells/styleflag)объект.
1.  Назначьте настроенное[**Стиль**](https://reference.aspose.com/cells/net/aspose.cells/style) возражать против[**Ряд**](https://reference.aspose.com/cells/net/aspose.cells/row)объект.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-FormatRowsColumns-FormattingARow-1.cs" >}}

###  **Как отформатировать столбец**

[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) коллекция также предоставляет[**Столбцы**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/columns) коллекция. Каждый предмет в[**Столбцы**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/columns) коллекция представляет собой[**Столбец**](https://reference.aspose.com/cells/net/aspose.cells/column) объект. Похоже на[**Ряд**](https://reference.aspose.com/cells/net/aspose.cells/row) объект,[**Столбец**](https://reference.aspose.com/cells/net/aspose.cells/column) объект также предлагает[**Применить стиль**](https://reference.aspose.com/cells/net/aspose.cells/row/methods/applystyle)метод форматирования столбца.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-FormatRowsColumns-FormattingAColumn-1.cs" >}}

##  **Предварительные темы**
- [Настройки выравнивания](/cells/ru/net/cells-alignment-settings/)
- [Настройки границ](/cells/ru/net/cells-border-settings/)
- [Установите условные форматы файлов Excel и ODS.](/cells/ru/net/conditional-formatting/)
- [Темы и цвета Excel](/cells/ru/net/excel-themes-and-colors/)
- [Заполнить настройки](/cells/ru/net/cells-fill-settings/)
- [Настройки шрифта](/cells/ru/net/cells-font-settings/)
- [Форматирование листа Cells в рабочей книге](/cells/ru/net/format-worksheet-cells-in-a-workbook/)
- [Внедрить систему дат 1904 года](/cells/ru/net/implement-1904-date-system/)
- [Слияние и разъединение Cells](/cells/ru/net/merging-and-unmerging-cells/)
- [Настройки номера](/cells/ru/net/cells-number-settings/)
- [Получить и установить стиль для ячеек](/cells/ru/net/evaluating-cell-getstyle-and-setstyle-methods-against-cell-style-property/)

