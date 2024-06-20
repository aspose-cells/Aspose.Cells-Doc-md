---
title: Нахождение или Поиск Данных
type: docs
weight: 50
url: /ru/python-net/find-or-search-data/
description: Узнайте, как найти или найти ячейки в листе, которые содержат указанные данные через Aspose.Cells для Python via .NET API.
keywords: Python библиотека для Excel, поиск данных в Python, поиск данных в Python, поиск ячеек с формулой в Python, поиск ячеек с формулой в Python, поиск данных или формул в Python с использованием FindOptions, поиск данных или формул в Python с использованием FindOptions, поиск или поиск ячеек, содержащих указанное строковое значение или число в Python, поиск или поиск ячеек, содержащих указанные данные в Python
---

{{% alert color="primary" %}}

Microsoft Excel позволяет пользователям находить ячейки в листе, содержащие указанные данные.

{{% /alert %}}

## **Поиск ячеек, содержащих указанные данные**

### **Использование Microsoft Excel**

Microsoft Excel позволяет пользователям находить ячейки в листе, содержащие указанные данные. Если выбрать **Редактировать** в меню **Поиск** в Microsoft Excel, откроется диалоговое окно, в котором можно указать значение для поиска.

Здесь мы ищем значение "Апельсины". Aspose.Cells также позволяет разработчикам находить ячейки в листе с указанными значениями.

### **Использование Aspose.Cells**

Aspose.Cells предоставляет класс [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), который представляет файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) содержит коллекцию [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets), которая позволяет получить доступ к каждому листу в файле Excel. Лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). Класс [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) предоставляет коллекцию [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells), которая представляет все ячейки в листе. Коллекция [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) предоставляет несколько методов для поиска ячеек в листе, содержащих указанные данные. Ниже подробно описаны несколько из этих методов.

{{% alert color="primary" %}}

Все методы поиска возвращают ссылки на ячейки, содержащие указанные искомые данные.

{{% /alert %}}

## **Поиск ячеек, содержащих формулу**

Разработчики могут найти указанную формулу на листе, вызвав метод [**find**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/find/#any-aspose.cells.Cell-aspose.cells.FindOptions) коллекции [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells). Обычно метод [**find**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/find/#any-aspose.cells.Cell-aspose.cells.FindOptions) принимает три параметра:

- **что:** Объект для поиска. Тип должен быть int, double, DateTime, string, bool.
- **предыдущая_ячейка:** Предыдущая ячейка с тем же объектом. Этот параметр может быть установлен в null при поиске с начала.
- **find_options:** Опции для поиска необходимого объекта.

Ниже приведены примеры использования данных листа для тренировки методов поиска:

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FindingCellsContainingFormula-1.py" >}}

## **Поиск данных или формул с использованием FindOptions**

Можно найти указанные значения, используя метод [**find**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/find/#any-aspose.cells.Cell-aspose.cells.FindOptions) коллекции [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) с различными [**FindOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/findoptions). Обычно метод [**find**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/find/#any-aspose.cells.Cell-aspose.cells.FindOptions) принимает следующие параметры:

- **что:** данные или значение для поиска.
- **предыдущая_ячейка:** последняя ячейка, содержавшая то же значение. Этот параметр можно установить в null при поиске с начала.
- **find_options:** варианты поиска.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FindingDataOrFormulasUsingFindOptions-1.py" >}}

## **Поиск ячеек, содержащих указанное строковое значение или число**

Можно найти указанные строковые значения, вызвав тот же метод [**find**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/find/#any-aspose.cells.Cell-aspose.cells.FindOptions), найденный в коллекции [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells), с различными [**FindOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/findoptions).

Укажите свойства [**FindOptions.look_in_type**](https://reference.aspose.com/cells/python-net/aspose.cells/findoptions/look_in_type/) и [**FindOptions.look_at_type**](https://reference.aspose.com/cells/python-net/aspose.cells/findoptions/look_at_type/). В следующем примере кода показано, как использовать эти свойства для поиска ячеек с различным количеством строк в **начале** или в **центре** или в **конце** строки ячейки.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FindingCellsContainingStringValueOrNumber-1.py" >}}

## **Продвинутые темы**
- [Нахождение ячеек с определенным стилем](/cells/ru/python-net/find-cells-with-specific-style/)
- [Определите, начинается ли значение ячейки с одинарной кавычки](/cells/ru/python-net/find-if-the-cell-value-starts-with-single-quote-mark/)
- [Поиск данных с использованием исходных значений](/cells/ru/python-net/search-data-using-original-values/)
