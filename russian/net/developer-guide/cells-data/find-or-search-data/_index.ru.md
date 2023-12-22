---
title: Найти или найти данные
type: docs
weight: 50
url: /ru/net/find-or-search-data/
description: Узнайте, как найти или выполнить поиск ячеек на листе, содержащих указанные данные, с помощью Aspose.Cells for .NET API.
keywords: Find data, Search data, Find Cells Containing a Formula, Search Cells Containing a Formula, Find Data or Formulas using FindOptions, Search Data or Formulas using FindOptions, Find or Search Cells Containing Specified String Value or Number, Find or Search cells contains specified data
---
{{% alert color="primary" %}}

Microsoft Excel позволяет пользователям находить ячейки на листе, содержащие указанные данные.

{{% /alert %}}

##  **Нахождение Cells, содержащее указанные данные**

###  **Использование Microsoft Excel**

 Microsoft Excel позволяет пользователям находить ячейки на листе, содержащие указанные данные. Если вы выберете**Редактировать** из**Находить** меню в Microsoft Excel, вы увидите диалоговое окно, в котором можно указать значение поиска.

Здесь мы ищем значение «Апельсины». Aspose.Cells также позволяет разработчикам находить на листе ячейки, содержащие указанные значения.

###  **Использование Aspose.Cells**

 Aspose.Cells предоставляет класс,[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , который представляет файл Excel Microsoft.[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook) класс содержит[**Рабочие листы**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) коллекция, которая обеспечивает доступ к каждому листу в файле Excel. Рабочий лист представлен[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) сорт.[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) класс обеспечивает[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) коллекция, представляющая все ячейки на листе.[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)Коллекция предоставляет несколько методов поиска ячеек на листе, содержащих указанные пользователем данные. Некоторые из этих методов обсуждаются ниже более подробно.

{{% alert color="primary" %}}

Все методы Find возвращают ссылки на ячейки, содержащие указанные данные для поиска.

{{% /alert %}}

##  **Нахождение Cells, содержащего формулу**

 Разработчики могут найти указанную формулу на листе, вызвав метод[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) коллекция[**Находить**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index) метод. Как правило,[**Находить**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index)метод принимает три параметра:

- **Объект:**Объект для поиска. Тип должен быть int,double,DateTime,string,bool.
- **Предыдущая ячейка:**Предыдущая ячейка с тем же объектом. Для этого параметра можно установить значение null при поиске с самого начала.
- FindOptions: Параметры поиска нужного объекта.

В примерах ниже используются данные рабочих листов для отработки методов поиска:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Find-FindingCellsContainingFormula-1.cs" >}}

##  **Поиск данных или формул с помощью FindOptions**

 Найти указанные значения можно с помощью[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) коллекция[**Находить**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index) метод с различными[**Найти параметры**](https://reference.aspose.com/cells/net/aspose.cells/findoptions) . Как правило,[**Находить**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index)метод принимает следующие параметры:

- *Значение поиска**: данные или значение для поиска.
- *Предыдущая ячейка** — последняя ячейка, содержащая то же значение. Для этого параметра можно установить значение null при поиске с самого начала.
- *Параметры поиска**, параметры поиска.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Find-FindingDataOrFormulasUsingFindOptions-1.cs" >}}

##  **Поиск Cells, содержащий указанное строковое значение или число**

 Можно найти указанные строковые значения, вызвав тот же[**Находить**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index) метод, найденный в[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) коллекция с различными[**Найти параметры**](https://reference.aspose.com/cells/net/aspose.cells/findoptions).

 Укажите[**FindOptions.LookInType**](https://reference.aspose.com/cells/net/aspose.cells/findoptions/properties/lookintype) и[**FindOptions.LookAtType**](https://reference.aspose.com/cells/net/aspose.cells/findoptions/properties/lookattype) характеристики. В следующем примере кода показано, как использовать эти свойства для поиска ячеек с различным количеством строк в начале.**начало** или в**центр** или в**конец** строки ячейки.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Find-FindingCellsContainingStringValueOrNumber-1.cs" >}}

##  **Предварительные темы**
- [Найдите Cells с определенным стилем](/cells/ru/net/find-cells-with-specific-style/)
- [Найдите, начинается ли значение ячейки с одинарной кавычки](/cells/ru/net/find-if-the-cell-value-starts-with-single-quote-mark/)
- [Поиск данных с использованием исходных значений](/cells/ru/net/search-data-using-original-values/)
