---
title: Формат ячеек
linktitle: Формат ячеек
type: docs
weight: 120
url: /ru/net/cells-formatting/
description: Установите числовой формат, цвет рамки и фона для файлов Excel на платформах .NET Framework, .NET Core, Mono или Xamarin.
---
## **Вступление**

{{% alert color="primary" %}}

 Aspose.Cells обеспечивает[**GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle) и[**SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle) методы[Cell](https://reference.aspose.com/cells/net/aspose.cells/cell) класс, используемый для получения/установки стиля форматирования ячейки. Aspose.Cells также предоставляет[**Стиль**](https://reference.aspose.com/cells/net/aspose.cells/style)учебный класс.

{{% /alert %}}

## **Формат Cells с использованием методов GetStyle и SetStyle**

Применяйте различные стили форматирования к ячейкам, чтобы установить цвета фона или переднего плана, границы, шрифты, горизонтальное и вертикальное выравнивание, уровень отступа, направление текста, угол поворота и многое другое.

### **Использование методов GetStyle и SetStyle**

 Если разработчикам нужно применить разные стили форматирования к разным ячейкам, лучше получить[**Стиль**](https://reference.aspose.com/cells/net/aspose.cells/style) клетки с помощью[**Cell.GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle) метод, укажите атрибуты стиля, а затем примените форматирование, используя[**Cell.SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle)метод. Ниже приведен пример, демонстрирующий этот подход для применения различного форматирования к ячейке.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ApproachesToFormatData-UsingGetStyleSetStyle-1.cs" >}}

### **Использование объекта стиля для различного форматирования Cells**

 Если разработчикам необходимо применить один и тот же стиль форматирования к разным ячейкам, они могут использовать[**Стиль**](https://reference.aspose.com/cells/net/aspose.cells/style) объект. Пожалуйста, следуйте инструкциям ниже, чтобы использовать[**Стиль**](https://reference.aspose.com/cells/net/aspose.cells/style)объект:

1.  Добавить[**Стиль**](https://reference.aspose.com/cells/net/aspose.cells/style) объект, позвонив в[**Создать стиль**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/createstyle) метод[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook)учебный класс
1.  Доступ к недавно добавленным[**Стиль**](https://reference.aspose.com/cells/net/aspose.cells/style)объект
1.  Установите желаемые свойства/атрибуты[**Стиль**](https://reference.aspose.com/cells/net/aspose.cells/style)объект для применения желаемых настроек форматирования
1. Назначьте настроенный[**Стиль**](https://reference.aspose.com/cells/net/aspose.cells/style)возражать против желаемых ячеек

Такой подход может значительно повысить эффективность ваших приложений и сэкономить память.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ApproachesToFormatData-UsingStyleObject-1.cs" >}}

### **Использование предопределенных стилей Microsoft Excel 2007**

Если вам нужно применить разные стили форматирования для Microsoft Excel 2007, примените стили, используя Aspose.Cells API. Ниже приведен пример, демонстрирующий этот подход для применения предопределенного стиля к ячейке.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ApproachesToFormatData-UsingExcelPredefinedStyles-1.cs" >}}



## **Форматирование выбранных символов в Cell**

Работа с настройками шрифта объясняет, как форматировать текст в ячейках, но только объясняет, как форматировать все содержимое ячейки. Что делать, если вы хотите отформатировать только выбранные символы?

Aspose.Cells также поддерживает эту функцию. В этом разделе объясняется, как эффективно использовать эту функцию.

### **Форматирование выбранных символов**

 Aspose.Cells предоставляет класс,[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook) который представляет собой файл Excel Microsoft.[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook) класс содержит[**Рабочие листы**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) коллекция, которая обеспечивает доступ к каждому рабочему листу в файле Excel. Рабочий лист представлен[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) учебный класс.[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) класс предоставляет[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) коллекция. Каждый элемент в[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) коллекция представляет собой объект[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)учебный класс.

[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) класс обеспечивает[**Символы**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/characters)метод, который принимает следующие параметры для выбора диапазона символов внутри ячейки:

- **Начальный индекс**, индекс символа, с которого начинается выделение.
- **Количество символов**, количество символов для выбора.

[**Символы**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/characters) метод возвращает экземпляр[**Настройка шрифта**](https://reference.aspose.com/cells/net/aspose.cells/fontsetting)класс, который позволяет разработчикам форматировать символы так же, как и ячейку, как показано ниже в примере кода. В выходном файле в ячейке A1 слово «Посетить» будет отформатировано шрифтом по умолчанию, но «Aspose!» жирный и синий.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-FormattingSelectedCharacters-1.cs" >}}

{{% alert color="primary" %}}

 Если вы хотите отформатировать часть форматированного текста в ячейке, рассмотрите возможность использования[**Cell.GetCharacters**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getcharacters) & [**Cell.SetCharacters**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setcharacters) методы.[[**Cell.GetCharacters**]](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getcharacters) метод должен использоваться для доступа к частям текста, а затем можно вносить поправки с помощью[**Cell.SetCharacters**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setcharacters) метод, тогда как**Получать**метод возвращает массив[**Настройка шрифта**](https://reference.aspose.com/cells/net/aspose.cells/fontsetting) объекты, которыми можно манипулировать для установки различных свойств, таких как имя шрифта, цвет шрифта, жирность и т. д. и**Установлен** можно использовать для применения изменений.

{{% /alert %}}

## **Форматирование строк и столбцов**

Иногда разработчикам необходимо применить одинаковое форматирование к строкам или столбцам. Применение форматирования к ячейкам по одной часто занимает больше времени и не является хорошим решением.
Чтобы решить эту проблему, Aspose.Cells предоставляет простой и быстрый способ, подробно описанный в этой статье.

### **Форматирование строк и столбцов**

 Aspose.Cells предоставляет класс,[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook) который представляет собой файл Excel Microsoft.[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook) класс содержит[**Рабочие листы**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) коллекция, которая обеспечивает доступ к каждому рабочему листу в файле Excel. Рабочий лист представлен[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) учебный класс.[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) класс предоставляет[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) коллекция.[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)коллекция обеспечивает[**Ряды**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/rows)коллекция.

### **Форматирование строки**

 Каждый элемент в[**Ряды**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/rows) коллекция представляет собой[**Строка**](https://reference.aspose.com/cells/net/aspose.cells/row) объект.[**Строка**](https://reference.aspose.com/cells/net/aspose.cells/row)объект предлагает[**Применить стиль**](https://reference.aspose.com/cells/net/aspose.cells/row/methods/applystyle) метод, используемый для установки форматирования строки. Чтобы применить такое же форматирование к строке, используйте[**Стиль**](https://reference.aspose.com/cells/net/aspose.cells/style)объект. Шаги ниже показывают, как его использовать.

1.  Добавить[**Стиль**](https://reference.aspose.com/cells/net/aspose.cells/style) возражать против[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook) класс, вызвав его[**Создать стиль**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/createstyle)метод.
1.  Установить[**Стиль**](https://reference.aspose.com/cells/net/aspose.cells/style)свойства объекта для применения параметров форматирования.
1.  Включите соответствующие атрибуты для[**СтильФлаг**](https://reference.aspose.com/cells/net/aspose.cells/styleflag)объект.
1. Назначьте настроенный[**Стиль**](https://reference.aspose.com/cells/net/aspose.cells/style) возражать против[**Строка**](https://reference.aspose.com/cells/net/aspose.cells/row)объект.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-FormatRowsColumns-FormattingARow-1.cs" >}}

### **Форматирование столбца**

[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) коллекция также обеспечивает[**Столбцы**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/columns) коллекция. Каждый элемент в[**Столбцы**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/columns) коллекция представляет собой[**Столбец**](https://reference.aspose.com/cells/net/aspose.cells/column) объект. Похоже на[**Строка**](https://reference.aspose.com/cells/net/aspose.cells/row) объект,[**Столбец**](https://reference.aspose.com/cells/net/aspose.cells/column) объект также предлагает[**Применить стиль**](https://reference.aspose.com/cells/net/aspose.cells/row/methods/applystyle)метод форматирования столбца.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-FormatRowsColumns-FormattingAColumn-1.cs" >}}

## **Предварительные темы**
- [Настройки выравнивания](/cells/ru/net/cells-alignment-settings/)
- [Настройки границы](/cells/ru/net/cells-border-settings/)
- [Установите условные форматы файлов Excel и ODS.](/cells/ru/net/conditional-formatting/)
- [Темы и цвета Excel](/cells/ru/net/excel-themes-and-colors/)
- [Настройки заполнения](/cells/ru/net/cells-fill-settings/)
- [Настройки шрифта](/cells/ru/net/cells-font-settings/)
- [Формат рабочего листа Cells в рабочей книге](/cells/ru/net/format-worksheet-cells-in-a-workbook/)
- [Внедрить систему дат 1904 года](/cells/ru/net/implement-1904-date-system/)
- [Объединение и разделение Cells](/cells/ru/net/merging-and-unmerging-cells/)
- [Настройки номера](/cells/ru/net/cells-number-settings/)
- [Получить и установить стиль для ячеек](/cells/ru/net/evaluating-cell-getstyle-and-setstyle-methods-against-cell-style-property/)

