---
title: Группировка и разгруппировка строк и столбцов
type: docs
weight: 50
url: /ru/net/grouping-and-ungrouping-rows-and-columns/
---
## **Введение**

В файле Excel Microsoft можно создать структуру данных, позволяющую отображать и скрывать уровни детализации одним щелчком мыши.

 Нажмите на**Контурные символы**, 1,2,3, + и -, чтобы быстро отобразить только строки или столбцы, которые содержат сводки или заголовки для разделов на листе, или вы можете использовать символы, чтобы увидеть подробности под отдельной сводкой или заголовком, как показано ниже на рисунке. :

|**Группировка строк и столбцов.**|
|:- |
|![дело:изображение_альтернативный_текст](grouping-and-ungrouping-rows-and-columns_1.png)|

## **Групповое управление строками и столбцами**

 Aspose.Cells предоставляет класс,[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook) который представляет собой файл Excel Microsoft.[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook) класс содержит[**Рабочий листКоллекция**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) который позволяет получить доступ к каждому рабочему листу в файле Excel. Рабочий лист представлен[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) учебный класс.[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) класс предоставляет[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)коллекция, представляющая все ячейки рабочего листа.

[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)collection предоставляет несколько методов для управления строками или столбцами на листе, некоторые из них более подробно обсуждаются ниже.

### **Группировка строк и столбцов**

 Можно сгруппировать строки или столбцы, вызвав метод[**ГруппРовс**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/grouprows/index) а также[**Групповые столбцы**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/groupcolumns/index) методы[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) коллекция. Оба метода принимают следующие параметры:

- Индекс первой строки/столбца, первая строка или столбец в группе.
- Индекс последней строки/столбца, последняя строка или столбец в группе.
- Скрыт, логический параметр, указывающий, следует ли скрывать строки/столбцы после группировки или нет.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Grouping-GroupingRowsAndColumns-1.cs" >}}

#### **Настройки группы**

Microsoft Excel позволяет настроить параметры группы для отображения:

- Сводные строки под деталями.
- Сводные столбцы справа от подробностей.

 Разработчики могут настроить эти групповые параметры с помощью[**Контур**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/outline) собственность[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)учебный класс.

### **Сводные строки ниже детализации**

 Можно контролировать, будут ли сводные строки отображаться под деталями, установив параметр[**Контур**](https://reference.aspose.com/cells/net/aspose.cells/outline) учебный класс'[**РезюмеСтрокаНиже**](https://reference.aspose.com/cells/net/aspose.cells/outline/properties/summaryrowbelow) собственность на**истинный** или же**ЛОЖЬ**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Grouping-SummaryRowBelow-1.cs" >}}

### **Сводные столбцы справа от подробностей**

 Разработчики также могут управлять отображением сводных столбцов справа от подробностей, установив параметр[**РезюмеСтолбецПравый**](https://reference.aspose.com/cells/net/aspose.cells/outline/properties/summarycolumnright) свойство[**Контур**](https://reference.aspose.com/cells/net/aspose.cells/outline) класс для**истинный** или же**ЛОЖЬ**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Grouping-SummaryRowRight-1.cs" >}}

## **Разгруппировка строк и столбцов**

 Чтобы разгруппировать любые сгруппированные строки или столбцы, вызовите метод[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) коллекция[**Разгруппировать ряды**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/ungrouprows/index) а также[**Разгруппировать столбцы**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/ungroupcolumns)методы. Оба метода принимают два параметра:

- Индекс первой строки или столбца, первая строка/столбец, подлежащий разгруппировке.
- Индекс последней строки или столбца, последняя строка/столбец для разгруппировки.

[**Разгруппировать ряды**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/ungrouprows/index) имеет перегрузку, которая принимает логический третий параметр. Установка его на**истинный**удаляет всю сгруппированную информацию. В противном случае удаляется только информация о внешней группе.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Grouping-UngroupingRowsAndColumns-1.cs" >}}
