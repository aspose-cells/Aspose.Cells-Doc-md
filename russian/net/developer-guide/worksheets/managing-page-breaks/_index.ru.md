---
title: Управление разрывами страниц
type: docs
weight: 30
url: /ru/net/managing-page-breaks/
description: В данной статье предоставляется образец кода и объясняется, как добавлять разрывы страниц, очищать разрывы страниц или удалять конкретные разрывы страниц в листах книги Excel программно с использованием API C# или .NET Library.
keywords: перерывы страниц c#, excel перерывы страницы c#, очистить перерыв страницы c#, удалить конкретный перерыв странице c#
---

{{% alert color="primary" %}}

Согласно определению, перерыв страницы - это место в текучем тексте, где заканчивается одна страница, и начинается другая. Microsoft Excel позволяет пользователям добавлять перерывы страницы в любую выбранную ячейку листа.

Местоположение ячейки, в которую добавлен перерыв страницы, страница заканчивается, и оставшиеся данные после перерыва странице печатаются на следующей странице во время печати. Проще говоря, перерывы страницы делят ваш лист на несколько страниц в соответствии с вашими спецификациями. Вы также можете добавлять перерывы страниц в свои листы во время выполнения с использованием Aspose.Cells. Aspose.Cells позволяет разработчикам добавлять два вида перерывов страницы:

- Горизонтальный перерыв страницы
- Вертикальный перерыв страницы

В остальной части обсуждения мы опишем, как вы можете добавить горизонтальные или вертикальные перерывы страниц в свои листы с использованием Aspose.Cells.

{{% /alert %}}

## **Разрывы страниц**

Aspose.Cells предоставляет класс [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), представляющий файл Excel. Класс [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) содержит коллекцию [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets), позволяющую получить доступ к каждому листу в файле Excel.

Лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). Класс [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) предоставляет широкий спектр свойств и методов, используемых для управления листом.

Для добавления перерывов страниц используйте свойства класса [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) и методы [**HorizontalPageBreaks**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/horizontalpagebreaks) и [**VerticalPageBreaks**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/verticalpagebreaks).

Свойства [**HorizontalPageBreaks**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/horizontalpagebreaks) и [**VerticalPageBreaks**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/verticalpagebreaks) являются коллекциями, которые могут содержать несколько перерывов страницы. Каждая коллекция содержит несколько методов для управления горизонтальными и вертикальными перерывами страниц.

### **Добавление разрывов страниц**

Чтобы добавить перерыв страницы в лист, вставьте вертикальные и горизонтальные перерывы в указанную ячейку, вызвав методы [**HorizontalPageBreakCollection.Add()**](https://reference.aspose.com/cells/net/aspose.cells/horizontalpagebreakcollection/methods/add/index) и [**VerticalPageBreakCollection.Add()**](https://reference.aspose.com/cells/net/aspose.cells/verticalpagebreakcollection/methods/add/index). Каждый метод **Add** принимает имя ячейки, в которую следует добавить перерыв.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Value-AddingPageBreaks-1.cs" >}}

{{% alert color="primary" %}}

В режиме предварительного просмотра разрывов страниц или предварительного просмотра печати можно увидеть, как работают эти разрывы страниц.

{{% /alert %}}

### **Очистка всех разрывов страниц**

Чтобы удалить все перерывы страницы в листе, вызовите методы [**Clear()**](https://docs.microsoft.com/en-us/dotnet/api/system.collections.collectionbase.clear?redirectedfrom=MSDN&view=netframework-4.7.2#System_Collections_CollectionBase_Clear) коллекций [**HorizontalPageBreakCollection**](https://reference.aspose.com/cells/net/aspose.cells/horizontalpagebreakcollection) и [**VerticalPageBreakCollection**](https://reference.aspose.com/cells/net/aspose.cells/verticalpagebreakcollection).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Value-ClearAllPageBreaks-1.cs" >}}

### **Удаление определенного разрыва страницы**

Чтобы удалить конкретный перерыв страницы, вызовите методы [**HorizontalPageBreakCollection.RemoveAt()**](https://reference.aspose.com/cells/net/aspose.cells/horizontalpagebreakcollection/methods/removeat) и [**VerticalPageBreakCollection.RemoveAt()**](https://reference.aspose.com/cells/net/aspose.cells/verticalpagebreakcollection/methods/removeat). Каждый метод **RemoveAt** принимает индекс удаляемого перерыва страницы.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Value-RemoveSpecificPageBreak-1.cs" >}}

## **Важно знать**

Когда вы устанавливаете свойства **FitToPages** (то есть [**FitToPagesTall**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/fittopagestall) и [**FitToPagesWide**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/fittopageswide)) в настройках страницы, настройки перерывов страницы также влияют на них, поэтому, если вы печатаете лист, настройки перерывов страницы не учитываются, хотя они все еще заданы.
{{< app/cells/assistant language="csharp" >}}
