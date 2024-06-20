---
title: Нахождение или Поиск Данных
type: docs
weight: 50
url: /ru/net/find-or-search-data/
description: Узнайте, как найти или найти ячейки в рабочем листе, содержащие указанные данные через Aspose.Cells for .NET API.
keywords: Найти данные, найти ячейки, содержащие формулу, найти ячейки, содержащие формулу, найти данные или формулы с помощью FindOptions, найти данные или формулы с помощью FindOptions, найти или найти ячейки, содержащие указанное строковое значение или число, найти или найти ячейки, содержащие указанные данные
---

{{% alert color="primary" %}}

Microsoft Excel позволяет пользователям находить ячейки в листе, содержащие указанные данные.

{{% /alert %}}

## **Поиск ячеек, содержащих указанные данные**

### **Использование Microsoft Excel**

Microsoft Excel позволяет пользователям находить ячейки в листе, содержащие указанные данные. Если выбрать **Редактировать** в меню **Поиск** в Microsoft Excel, откроется диалоговое окно, в котором можно указать значение для поиска.

Здесь мы ищем значение "Апельсины". Aspose.Cells также позволяет разработчикам находить ячейки в листе с указанными значениями.

### **Использование Aspose.Cells**

Aspose.Cells предоставляет класс [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), который представляет файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) содержит коллекцию [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets), которая позволяет получить доступ к каждому листу в файле Excel. Лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). Класс [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) предоставляет коллекцию [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells), которая представляет все ячейки в листе. Коллекция [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) предоставляет несколько методов для поиска ячеек в листе, содержащих указанные данные. Ниже подробно описаны несколько из этих методов.

{{% alert color="primary" %}}

Все методы поиска возвращают ссылки на ячейки, содержащие указанные искомые данные.

{{% /alert %}}

## **Поиск ячеек, содержащих формулу**

Разработчики могут найти указанную формулу на листе, вызвав метод [**Find**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index) коллекции [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells). Обычно метод [**Find**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index) принимает три параметра:

- **Объект:** Объект для поиска. Тип должен быть int, double, DateTime, string, bool.
- **Предыдущая ячейка:** Предыдущая ячейка с тем же объектом. Этот параметр может быть установлен в null, если поиск начинается с начала.
- ПараметрыПоиска: Параметры поиска требуемого объекта.

Ниже приведены примеры использования данных листа для тренировки методов поиска:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Find-FindingCellsContainingFormula-1.cs" >}}

## **Поиск данных или формул с использованием FindOptions**

Можно найти указанные значения, используя метод [**Find**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index) коллекции [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) с различными [**FindOptions**](https://reference.aspose.com/cells/net/aspose.cells/findoptions). Обычно метод [**Find**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index) принимает следующие параметры:

- **Значение поиска**, данные или значение для поиска.
- **Предыдущая ячейка**, последняя ячейка, содержавшая то же значение. Этот параметр может быть установлен в null при поиске с начала.
- **Параметры поиска**, параметры поиска.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Find-FindingDataOrFormulasUsingFindOptions-1.cs" >}}

## **Поиск ячеек, содержащих указанное строковое значение или число**

Можно найти указанные строковые значения, вызвав тот же метод [**Find**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index), найденный в коллекции [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells), с различными [**FindOptions**](https://reference.aspose.com/cells/net/aspose.cells/findoptions).

Укажите свойства [**FindOptions.LookInType**](https://reference.aspose.com/cells/net/aspose.cells/findoptions/properties/lookintype) и [**FindOptions.LookAtType**](https://reference.aspose.com/cells/net/aspose.cells/findoptions/properties/lookattype). В следующем примере кода показано, как использовать эти свойства для поиска ячеек с различным количеством строк в **начале** или в **центре** или в **конце** строки ячейки.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Find-FindingCellsContainingStringValueOrNumber-1.cs" >}}

## **Продвинутые темы**
- [Нахождение ячеек с определенным стилем](/cells/ru/net/find-cells-with-specific-style/)
- [Определите, начинается ли значение ячейки с одинарной кавычки](/cells/ru/net/find-if-the-cell-value-starts-with-single-quote-mark/)
- [Поиск данных с использованием исходных значений](/cells/ru/net/search-data-using-original-values/)
