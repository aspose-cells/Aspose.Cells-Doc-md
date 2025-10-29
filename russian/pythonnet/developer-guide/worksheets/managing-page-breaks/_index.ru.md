---
title: Управление разрывами страниц
type: docs
weight: 30
url: /ru/python-net/managing-page-breaks/
description: Эта статья содержит пример кода и объясняет, как добавлять, очищать или удалять разрывы страниц в листах Excel программным способом с использованием API Aspose.Cells для Python via .NET.
keywords: Библиотека Python для Excel, разрывы страниц, разрывы страниц в Excel в Python, очищение разрывов страниц в Python.
---

{{% alert color="primary" %}}

Согласно определению, перерыв страницы - это место в текучем тексте, где заканчивается одна страница, и начинается другая. Microsoft Excel позволяет пользователям добавлять перерывы страницы в любую выбранную ячейку листа.

Место расположения ячейки, в которую добавляется разрыв страницы. Страница заканчивается, и оставшиеся данные после разрыва страницы выводятся на следующей. Проще говоря, разрывы страниц делят ваш лист на несколько страниц согласно вашим настройкам. Также, вы можете добавлять разрывы страниц в ваши листы во время выполнения с помощью Aspose.Cells для Python via .NET. Aspose.Cells для Python via .NET позволяет разработчикам добавлять два типа разрывов страниц:

- Горизонтальный перерыв страницы
- Вертикальный перерыв страницы

В дальнейшем мы опишем, как можно добавлять горизонтальные или вертикальные разрывы страниц в ваши листы с помощью Aspose.Cells для Python via .NET.

{{% /alert %}}

## **Разрывы страниц**

Aspose.Cells для Python via .NET предоставляет класс [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), который представляет собой Excel файл. Класс [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) содержит коллекцию [**Worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets), позволяющую доступ к каждому листу в Excel файле.

Лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). Класс [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) предоставляет широкий спектр свойств и методов, используемых для управления листом.

Для добавления перерывов страниц используйте свойства класса [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) и методы [**horizontal_page_breaks**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/horizontal_page_breaks) и [**vertical_page_breaks**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/vertical_page_breaks).

Свойства [**horizontal_page_breaks**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/horizontal_page_breaks) и [**vertical_page_breaks**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/vertical_page_breaks) являются коллекциями, которые могут содержать несколько перерывов страницы. Каждая коллекция содержит несколько методов для управления горизонтальными и вертикальными перерывами страниц.

## **Как добавить разрыв страницы**

Чтобы добавить разрыв страницы в лист, вставьте вертикальные и горизонтальные разрывы страниц в указанную ячейку, вызвав методы [**HorizontalPageBreakCollection.add()**](https://reference.aspose.com/cells/python-net/aspose.cells/horizontalpagebreakcollection/add/#str) и [**VerticalPageBreakCollection.add()**](https://reference.aspose.com/cells/python-net/aspose.cells/verticalpagebreakcollection/add/#str). Каждый метод **add** принимает название ячейки, в которую необходимо вставить разрыв.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Value-AddingPageBreaks-1.py" >}}

{{% alert color="primary" %}}

В режиме предварительного просмотра разрывов страниц или предварительного просмотра печати можно увидеть, как работают эти разрывы страниц.

{{% /alert %}}


## **Важно знать**

Когда вы устанавливаете свойства **FitToPages** (то есть [**fit_to_pages_tall**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/fit_to_pages_tall) и [**fit_to_pages_wide**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/fit_to_pages_wide)) в настройках страницы, настройки перерывов страницы также влияют на них, поэтому, если вы печатаете лист, настройки перерывов страницы не учитываются, хотя они все еще заданы.
{{< app/cells/assistant language="python-net" >}}
