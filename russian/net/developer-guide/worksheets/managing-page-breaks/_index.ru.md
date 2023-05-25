---
title: Управление разрывами страниц
type: docs
weight: 30
url: /ru/net/managing-page-breaks/
description: В этой статье представлен пример кода и объясняется, как добавлять разрывы страниц, удалять разрывы страниц или удалять определенные разрывы страниц на листах Excel программным путем с помощью библиотеки C# API или .NET.
keywords: page breaks c#, excel page breaks c#, clear page break c#, delete specific page break c#
---
{{% alert color="primary" %}}

Согласно определению, разрыв страницы — это место в потоке текста, где заканчивается одна страница и начинается следующая. Microsoft Excel позволяет пользователям добавлять разрывы страниц в любую выбранную ячейку рабочего листа.

Расположение ячейки, в которой добавлен разрыв страницы, страница заканчивается, а остальные данные после разрыва страницы печатаются на следующей странице во время печати. Проще говоря, разрывы страниц делят ваш рабочий лист на несколько страниц в соответствии с вашими требованиями. Вы также можете добавлять разрывы страниц на свои рабочие листы во время выполнения, используя Aspose.Cells. Aspose.Cells позволяет разработчикам добавлять два типа разрывов страниц:

- Горизонтальный разрыв страницы
- Вертикальный разрыв страницы

В оставшейся части обсуждения мы опишем, как вы можете добавить горизонтальные или вертикальные разрывы страниц в свои рабочие листы, используя Aspose.Cells.

{{% /alert %}}

##  **Разрывы страниц**

Aspose.Cells предоставляет[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook) класс, представляющий файл Excel.[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook) класс содержит[**Рабочие листы**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)коллекция, которая обеспечивает доступ к каждому рабочему листу в файле Excel.

 Рабочий лист представлен[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) сорт.[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)Класс предоставляет широкий спектр свойств и методов, используемых для управления рабочим листом.

Чтобы добавить разрывы страниц, используйте[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) сорт'[**ГоризонтальныйPageBreaks**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/horizontalpagebreaks) и[**Вертикальные разрывы страниц**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/verticalpagebreaks)характеристики.

[**ГоризонтальныйPageBreaks**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/horizontalpagebreaks) и[**Вертикальные разрывы страниц**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/verticalpagebreaks)свойства — это наборы, которые могут содержать несколько разрывов страниц. Каждая коллекция содержит несколько методов управления горизонтальными и вертикальными разрывами страниц.

###  **Добавление разрывов страниц**

 Чтобы добавить разрыв страницы на листе, вставьте вертикальные и горизонтальные разрывы страниц в указанной ячейке, вызвав метод[**Коллекция HorizontalPageBreakCollection.Добавить()**](https://reference.aspose.com/cells/net/aspose.cells/horizontalpagebreakcollection/methods/add/index) и[**Коллекция VerticalPageBreakCollection.Добавить()**](https://reference.aspose.com/cells/net/aspose.cells/verticalpagebreakcollection/methods/add/index) методы. Каждый**Добавлять** Метод принимает имя ячейки, в которую следует добавить разрыв.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Value-AddingPageBreaks-1.cs" >}}

{{% alert color="primary" %}}

В режимах предварительного просмотра разрывов страниц или предварительного просмотра печати вы можете увидеть, как работают эти разрывы страниц.

{{% /alert %}}

###  **Удаление всех разрывов страниц**

 Чтобы удалить все разрывы страниц на листе, вызовите метод[**HorizontalPageBreakCollection**](https://reference.aspose.com/cells/net/aspose.cells/horizontalpagebreakcollection) и[**ВертикальнаяPageBreakCollection**](https://reference.aspose.com/cells/net/aspose.cells/verticalpagebreakcollection) коллекции[**Clear()**](https://docs.microsoft.com/en-us/dotnet/api/system.collections.collectionbase.clear?redirectedfrom=MSDN&view=netframework-4.7.2#System_Collections_CollectionBase_Clear)методы.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Value-ClearAllPageBreaks-1.cs" >}}

###  **Удаление определенного разрыва страницы**

 Чтобы удалить определенный разрыв страницы, вызовите[**HorizontalPageBreakCollection.RemoveAt()**](https://reference.aspose.com/cells/net/aspose.cells/horizontalpagebreakcollection/methods/removeat) и[**Коллекция VerticalPageBreakCollection.RemoveAt()**](https://reference.aspose.com/cells/net/aspose.cells/verticalpagebreakcollection/methods/removeat) методы. Каждый**RemoveAt**Метод принимает индекс разрыва страницы, который нужно удалить.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Value-RemoveSpecificPageBreak-1.cs" >}}

##  **Важно знать**

 Когда вы устанавливаете**Подгонка по страницам** свойства (т.[**FitToPagesTall**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/fittopagestall) и[**FitToPagesWide**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/fittopageswide)) в параметрах настройки страницы затрагиваются параметры разрыва страницы, поэтому при печати рабочего листа параметры разрыва страницы не учитываются, хотя они все еще установлены.
