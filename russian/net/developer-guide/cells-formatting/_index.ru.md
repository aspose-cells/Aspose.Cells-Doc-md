---
title: Форматировать ячейки
description: Изучите, как форматировать и стилизовать ячейки в Aspose.Cells for .NET, включая форматирование чисел, форматирование дат, стили шрифтов и другие опции стиля ячейки. Наш руководство поможет вам создавать привлекательные и профессионально выглядящие электронные таблицы.
keywords: Aspose.Cells for .NET, форматирование ячеек, стилизация, форматирование чисел, форматирование дат, стиль шрифта, опции стиля ячейки, электронная таблица, создание, профессиональный вид, форматировать строки и столбцы.
linktitle: Форматировать ячейки
type: docs
weight: 120
url: /ru/net/cells-formatting/
---

## **Введение**

{{% alert color="primary" %}}

Aspose.Cells предоставляет методы [**GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle) и [**SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle) класса [Cell](https://reference.aspose.com/cells/net/aspose.cells/cell), используемые для получения/установки стиля форматирования ячейки. Aspose.Cells также предоставляет класс [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style).

{{% /alert %}}

## **Как форматировать ячейки с помощью методов GetStyle и SetStyle**

Применить различные виды стилей форматирования на ячейки для установки цветов фона или переднего плана, границ, шрифтов, горизонтальных и вертикальных выравниваний, уровня отступа, направления текста, угла поворота и многое другое.

### **Как использовать методы GetStyle и SetStyle**

Если разработчикам нужно применить различные стили форматирования к различным ячейкам, то лучше получить [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) ячейки с помощью метода [**Cell.GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle), указать атрибуты стиля, а затем применить форматирование с помощью метода [**Cell.SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle). Приведен пример, демонстрирующий этот подход к применению различного форматирования к ячейке.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ApproachesToFormatData-UsingGetStyleSetStyle-1.cs" >}}

### **Как использовать объект стиля для форматирования различных ячеек**

Если разработчикам нужно применить одинаковый стиль форматирования к различным ячейкам, то они могут использовать [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) объект. Пожалуйста, выполните следующие шаги для использования объекта [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style):

1. Добавьте объект [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style), вызвав метод [**CreateStyle**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/createstyle) класса [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)
1. Получите только что добавленный объект [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style)
1. Установите желаемые свойства/атрибуты объекта [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style), чтобы применить желаемые настройки форматирования
1. Присвойте настроенный объект [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) вашим желаемым ячейкам

Этот подход может значительно повысить эффективность ваших приложений и сэкономить память.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ApproachesToFormatData-UsingStyleObject-1.cs" >}}

### **Как использовать предопределенные стили Microsoft Excel 2007**

Если вам необходимо применить различные стили форматирования для Microsoft Excel 2007, примените стили с использованием API Aspose.Cells. Приведен пример, демонстрирующий этот подход к применению предопределенного стиля к ячейке.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ApproachesToFormatData-UsingExcelPredefinedStyles-1.cs" >}}



## **Как форматировать выбранные символы в ячейке**

Работа со настройками шрифта объясняет, как форматировать текст в ячейках, но это объясняет только, как форматировать весь содержимое ячейки. Что, если вы хотите отформатировать только выбранные символы?

Aspose.Cells также поддерживает эту функцию. В этой теме объясняется, как использовать эту функцию эффективно.

### **Как форматировать выбранные символы**

Aspose.Cells предоставляет класс, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) который представляет файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) содержит коллекцию [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets), которая позволяет получить доступ к каждому листу в файле Excel. Лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). Класс [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) обеспечивает коллекцию [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells). Каждый элемент в коллекции [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) представляет объект класса [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell).

Класс [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) предоставляет метод [**Characters**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/characters), который принимает следующие параметры для выбора диапазона символов внутри ячейки:

- **Индекс начала**, индекс символа, с которого начинается выбор.
- **Количество символов**, количество выбираемых символов.

Метод [**Characters**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/characters) возвращает экземпляр класса [**FontSetting**](https://reference.aspose.com/cells/net/aspose.cells/fontsetting), который позволяет разработчикам форматировать символы таким же образом, как они бы это сделали с ячейкой, как показано ниже в примере кода. В выходном файле в ячейке A1 слово 'Visit' будет отформатировано шрифтом по умолчанию, но 'Aspose!' будет жирным и синим.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-FormattingSelectedCharacters-1.cs" >}}

{{% alert color="primary" %}}

Если вас интересует форматирование части Rich Text в ячейке, рассмотрите использование методов [**Cell.GetCharacters**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getcharacters) и [**Cell.SetCharacters**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setcharacters). Метод [[**Cell.GetCharacters**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getcharacters) служит для доступа к частям текста, а затем изменения можно вносить с помощью метода [**Cell.SetCharacters**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setcharacters), в то время как метод **Get** возвращает массив объектов [**FontSetting**](https://reference.aspose.com/cells/net/aspose.cells/fontsetting), которые могут быть настроены для установки различных свойств, таких как имя шрифта, цвет шрифта, жирность и т. д., а метод **Set** можно использовать для применения изменений.

{{% /alert %}}

## **Как форматировать строки и столбцы**

Иногда разработчику требуется применить одно и то же форматирование на строки или столбцы. Применение форматирования к ячейкам одну за другой часто занимает больше времени и не является хорошим решением.
Для решения этой проблемы Aspose.Cells предоставляет простой и быстрый способ, который подробно рассматривается в данной статье.

### **Форматирование строк и столбцов**

Aspose.Cells предоставляет класс, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) который представляет файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)содержит коллекцию [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets), которая позволяет получить доступ к каждому листу в файле Excel. Лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). Класс [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) предоставляет коллекцию [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells). Коллекция [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) предоставляет коллекцию [**Rows**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/rows).

### **Как форматировать строку**

Каждый элемент в коллекции {0} представляет объект {1}. Объект {2} предлагает метод {3, используемый для установки форматирования строки. Для применения одного и того же форматирования к строке используйте объект {4}. Ниже приведены шаги, как его использовать.

1. Добавьте объект [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) в класс [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), вызвав его метод [**CreateStyle**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/createstyle).
1. Установите свойства объекта [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style), чтобы применить настройки форматирования.
1. Включите соответствующие атрибуты для объекта [**StyleFlag**](https://reference.aspose.com/cells/net/aspose.cells/styleflag).
1. Назначьте настроенный объект [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) на объект [**Row**](https://reference.aspose.com/cells/net/aspose.cells/row).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-FormatRowsColumns-FormattingARow-1.cs" >}}

### **Как форматировать столбец**

Коллекция [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) также предоставляет коллекцию [**Columns**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/columns). Каждый элемент в коллекции [**Columns**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/columns) представляет объект [**Column**](https://reference.aspose.com/cells/net/aspose.cells/column). Аналогично объекту [**Row**](https://reference.aspose.com/cells/net/aspose.cells/row), объект [**Column**](https://reference.aspose.com/cells/net/aspose.cells/column) также предлагает метод [**ApplyStyle**](https://reference.aspose.com/cells/net/aspose.cells/row/methods/applystyle) для форматирования столбца.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-FormatRowsColumns-FormattingAColumn-1.cs" >}}

## **Продвинутые темы**
- [Настройки выравнивания](/cells/ru/net/cells-alignment-settings/)
- [Настройки границ](/cells/ru/net/cells-border-settings/)
- [Установить условные форматы для файлов Excel и ODS.](/cells/ru/net/conditional-formatting/)
- [Темы и цвета Excel](/cells/ru/net/excel-themes-and-colors/)
- [Настройки заливки](/cells/ru/net/cells-fill-settings/)
- [Настройки шрифта](/cells/ru/net/cells-font-settings/)
- [Форматирование ячеек листа в книге Excel](/cells/ru/net/format-worksheet-cells-in-a-workbook/)
- [Реализация системы дат 1904 года](/cells/ru/net/implement-1904-date-system/)
- [Объединение и разъединение ячеек](/cells/ru/net/merging-and-unmerging-cells/)
- [Настройки чисел](/cells/ru/net/cells-number-settings/)
- [Получение и установка стиля ячеек](/cells/ru/net/evaluating-cell-getstyle-and-setstyle-methods-against-cell-style-property/)

{{< app/cells/assistant language="csharp" >}}
