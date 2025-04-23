---
title: Форматировать ячейки
description: Узнайте как форматировать и стилизовать ячейки в Aspose.Cells for Python via .NET, включая числовое форматирование, форматирование дат, стили шрифтов и другие параметры стилей ячеек. Наше руководство поможет вам создавать привлекательные и профессиональные таблицы.
keywords: Aspose.Cells for Python via .NET, форматирование ячеек, стилизация, числовое форматирование, форматирование даты, стиль шрифта, параметры стилей ячеек, электронная таблица, создание, профессиональный вид, форматирование строк и столбцов.
linktitle: Форматировать ячейки
type: docs
weight: 120
url: /ru/python-net/cells-formatting/
---

## **Введение**

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET предоставляет методы [**get_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_style) и [**set_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_style) класса [Cell](https://reference.aspose.com/cells/python-net/aspose.cells/cell), используемые для получения/установки стиля форматирования ячейки. Также предоставляется класс [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style).

{{% /alert %}}

## **Как форматировать ячейки с помощью методов GetStyle и SetStyle**

Применить различные виды стилей форматирования на ячейки для установки цветов фона или переднего плана, границ, шрифтов, горизонтальных и вертикальных выравниваний, уровня отступа, направления текста, угла поворота и многое другое.

### **Как использовать методы GetStyle и SetStyle**

Если разработчикам нужно применить различные стили форматирования к различным ячейкам, то лучше получить [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) ячейки с помощью метода [**Cell.get_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_style), указать атрибуты стиля, а затем применить форматирование с помощью метода [**Cell.set_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_style). Приведен пример, демонстрирующий этот подход к применению различного форматирования к ячейке.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ApproachesToFormatData-UsingGetStyleSetStyle-1.py" >}}

### **Как использовать объект стиля для форматирования различных ячеек**

Если разработчикам нужно применить одинаковый стиль форматирования к различным ячейкам, то они могут использовать [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) объект. Пожалуйста, выполните следующие шаги для использования объекта [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style):

1. Добавьте объект [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style), вызвав метод [**create_style**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/create_style) класса [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)
1. Получите только что добавленный объект [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style)
1. Установите желаемые свойства/атрибуты объекта [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style), чтобы применить желаемые настройки форматирования
1. Присвойте настроенный объект [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) вашим желаемым ячейкам

Этот подход может значительно повысить эффективность ваших приложений и сэкономить память.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ApproachesToFormatData-UsingStyleObject-1.py" >}}

### **Как использовать предопределенные стили Microsoft Excel 2007**

Если вам необходимо применять разные стили форматирования для Microsoft Excel 2007, используйте стили с помощью API Aspose.Cells for Python via .NET. Ниже приведен пример, демонстрирующий этот подход для применения предопределенного стиля к ячейке.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ApproachesToFormatData-UsingExcelPredefinedStyles-1.py" >}}



## **Как форматировать выбранные символы в ячейке**

Работа со настройками шрифта объясняет, как форматировать текст в ячейках, но это объясняет только, как форматировать весь содержимое ячейки. Что, если вы хотите отформатировать только выбранные символы?

Aspose.Cells for Python via .NET также поддерживает эту функцию. Эта тема объясняет, как эффективно использовать эту функцию.

### **Как форматировать выбранные символы**

Aspose.Cells for Python via .NET предоставляет класс [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), который представляет файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) содержит коллекцию [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets), которая обеспечивает доступ к каждому листу в файле Excel. Лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). Класс [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) предоставляет коллекцию [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells). Каждый элемент коллекции [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) представляет объект класса [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell).

Класс [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) предоставляет метод [**characters**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/characters), который принимает следующие параметры для выбора диапазона символов внутри ячейки:

- **Индекс начала**, индекс символа, с которого начинается выбор.
- **Количество символов**, количество выбираемых символов.

Метод [**characters**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/characters) возвращает экземпляр класса [**FontSetting**](https://reference.aspose.com/cells/python-net/aspose.cells/fontsetting), который позволяет разработчикам форматировать символы таким же образом, как они бы это сделали с ячейкой, как показано ниже в примере кода. В выходном файле в ячейке A1 слово 'Visit' будет отформатировано шрифтом по умолчанию, но 'Aspose!' будет жирным и синим.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-FormattingSelectedCharacters-1.py" >}}

{{% alert color="primary" %}}

Если вы хотите отформатировать часть богатого текста в ячейке, используйте методы [**Cell.get_characters**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_characters) и [**Cell.set_characters**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_characters). Метод [**Cell.get_characters**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_characters) используется для доступа к частям текста, а затем изменения можно делать с помощью метода [**Cell.set_characters**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_characters), в то время как метод **Get** возвращает массив объектов [**FontSetting**](https://reference.aspose.com/cells/python-net/aspose.cells/fontsetting), которыми можно управлять для установки различных свойств, таких как название шрифта, цвет шрифта, полужирность и т. д., а метод **Set** применяется для применения изменений.

{{% /alert %}}

## **Как форматировать строки и столбцы**

Иногда разработчику требуется применить одно и то же форматирование на строки или столбцы. Применение форматирования к ячейкам одну за другой часто занимает больше времени и не является хорошим решением.
Чтобы решить эту проблему, Aspose.Cells for Python via .NET предоставляет простой быстрый способ, подробно описанный в этой статье.

### **Форматирование строк и столбцов**

Aspose.Cells for Python via .NET предоставляет класс [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), который представляет файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) содержит коллекцию [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets), которая обеспечивает доступ к каждому листу в Excel файле. Лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). Класс [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) предоставляет коллекцию [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells). Коллекция [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) содержит коллекцию [**rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/rows).

### **Как форматировать строку**

Каждый элемент в коллекции {0} представляет объект {1}. Объект {2} предлагает метод {3, используемый для установки форматирования строки. Для применения одного и того же форматирования к строке используйте объект {4}. Ниже приведены шаги, как его использовать.

1. Добавьте объект [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) в класс [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), вызвав его метод [**create_style**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/create_style).
1. Установите свойства объекта [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style), чтобы применить настройки форматирования.
1. Включите соответствующие атрибуты для объекта [**StyleFlag**](https://reference.aspose.com/cells/python-net/aspose.cells/styleflag).
1. Назначьте настроенный объект [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) на объект [**Row**](https://reference.aspose.com/cells/python-net/aspose.cells/row).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-FormatRowsColumns-FormattingARow-1.py" >}}

### **Как форматировать столбец**

Коллекция [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) также предоставляет коллекцию [**columns**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/columns). Каждый элемент в коллекции [**columns**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/columns) представляет объект [**Column**](https://reference.aspose.com/cells/python-net/aspose.cells/column). Аналогично объекту [**Row**](https://reference.aspose.com/cells/python-net/aspose.cells/row), объект [**Column**](https://reference.aspose.com/cells/python-net/aspose.cells/column) также предлагает метод [**apply_style**](https://reference.aspose.com/cells/python-net/aspose.cells/row/apply_style) для форматирования столбца.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-FormatRowsColumns-FormattingAColumn-1.py" >}}

## **Продвинутые темы**
- [Настройки выравнивания](/cells/ru/python-net/cells-alignment-settings/)
- [Настройки границ](/cells/ru/python-net/cells-border-settings/)
- [Установить условные форматы для файлов Excel и ODS.](/cells/ru/python-net/conditional-formatting/)
- [Темы и цвета Excel](/cells/ru/python-net/excel-themes-and-colors/)
- [Настройки заливки](/cells/ru/python-net/cells-fill-settings/)
- [Настройки шрифта](/cells/ru/python-net/cells-font-settings/)
- [Форматирование ячеек листа в книге Excel](/cells/ru/python-net/format-worksheet-cells-in-a-workbook/)
- [Реализация системы дат 1904 года](/cells/ru/python-net/implement-1904-date-system/)
- [Объединение и разъединение ячеек](/cells/ru/python-net/merging-and-unmerging-cells/)
- [Настройки чисел](/cells/ru/python-net/cells-number-settings/)
- [Получение и установка стиля ячеек](/cells/ru/python-net/evaluating-cell-getstyle-and-setstyle-methods-against-cell-style-property/)

