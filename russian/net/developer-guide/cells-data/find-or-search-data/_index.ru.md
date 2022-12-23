---
title: Поиск или поиск данных
type: docs
weight: 50
url: /ru/net/find-or-search-data/
---
{{% alert color="primary" %}}

Microsoft Excel позволяет пользователям находить ячейки на листе, содержащие указанные данные.

{{% /alert %}}

## **Обнаружение Cells, содержащее указанные данные**

### **Использование Microsoft Excel**

 Microsoft Excel позволяет пользователям находить ячейки на листе, содержащие указанные данные. Если вы выберете**Редактировать** от**Находить** меню в Microsoft Excel, вы увидите диалоговое окно, в котором вы можете указать значение поиска.

Здесь мы ищем значение «Апельсины». Aspose.Cells также позволяет разработчикам находить ячейки на листе, содержащие указанные значения.

### **Использование Aspose.Cells**

 Aspose.Cells предоставляет класс,[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , представляющий файл Excel Microsoft.[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook) класс содержит[**Рабочие листы**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) коллекция, которая обеспечивает доступ к каждому рабочему листу в файле Excel. Рабочий лист представлен[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) учебный класс.[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) класс предоставляет[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) коллекция, представляющая все ячейки рабочего листа.[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)collection предоставляет несколько методов для поиска ячеек на листе, содержащих указанные пользователем данные. Некоторые из этих методов обсуждаются ниже более подробно.

{{% alert color="primary" %}}

Все методы Find возвращают ссылки на ячейки, содержащие указанные данные для поиска.

{{% /alert %}}

## **Находка Cells, содержащая формулу**

 Разработчики могут найти указанную формулу на листе, вызвав метод[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) коллекция[**Находить**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index) метод. Как правило,[**Находить**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index)метод принимает три параметра:

- **Объект:**Объект для поиска. Тип должен быть int, double, DateTime, string, bool.
- **Предыдущая ячейка:**Предыдущая ячейка с тем же объектом. Этот параметр может быть установлен равным нулю, если поиск выполняется с самого начала.
- FindOptions: Варианты поиска нужного объекта.

В приведенных ниже примерах данные рабочего листа используются для отработки методов поиска:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Find-FindingCellsContainingFormula-1.cs" >}}

## **Поиск данных или формул с помощью FindOptions**

 Можно найти заданные значения с помощью[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) коллекция[**Находить**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index) метод с различными[**FindOptions**](https://reference.aspose.com/cells/net/aspose.cells/findoptions) . Как правило,[**Находить**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index)метод принимает следующие параметры:

- **Значение поиска**, данные или значение для поиска.
- **Предыдущая ячейка**, последняя ячейка, содержащая такое же значение. Этот параметр может быть установлен равным нулю при поиске с самого начала.
- **Найти варианты**, параметры поиска.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Find-FindingDataOrFormulasUsingFindOptions-1.cs" >}}

## **Поиск Cells, содержащего указанное строковое значение или число**

 Можно найти заданные строковые значения, вызвав тот же[**Находить**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index) метод, найденный в[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) коллекция с различными[**FindOptions**](https://reference.aspose.com/cells/net/aspose.cells/findoptions).

 Укажите[**FindOptions.LookInType**](https://reference.aspose.com/cells/net/aspose.cells/findoptions/properties/lookintype) и[**FindOptions.LookAtType**](https://reference.aspose.com/cells/net/aspose.cells/findoptions/properties/lookattype) характеристики. В следующем примере кода показано, как использовать эти свойства для поиска ячеек с различным количеством строк в**начало** или в**центр** или в**конец** строки ячейки.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Find-FindingCellsContainingStringValueOrNumber-1.cs" >}}

## **Предварительные темы**
- [Найти Cells с определенным стилем](/cells/ru/net/find-cells-with-specific-style/)
- [Найдите, начинается ли значение ячейки с одинарной кавычки](/cells/ru/net/find-if-the-cell-value-starts-with-single-quote-mark/)
- [Поиск данных с использованием исходных значений](/cells/ru/net/search-data-using-original-values/)
