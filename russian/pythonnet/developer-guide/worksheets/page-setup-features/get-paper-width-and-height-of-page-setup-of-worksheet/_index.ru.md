---
title: Получить ширину и высоту бумаги параметров страницы листа
type: docs
weight: 50
url: /ru/python-net/get-paper-width-and-height-of-page-setup-of-worksheet/
description: Вы узнаете в этой статье, как получить Ширину и Высоту бумаги страницы листа Excel с использованием програмного кода на Python с помощью API или библиотеки Aspose.Cells для Python via .NET.
keywords: Библиотека Python Excel, ширина бумаги страницы Excel в Python, высота бумаги страницы Excel в Python.
---

## **Возможные сценарии использования**

Иногда вам нужно знать ширину и высоту размера бумаги, установленного в параметрах страницы листа. Пожалуйста, используйте свойства [**PageSetup.paper_width**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/paper_width) и [**PageSetup.paper_height**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/paper_height) для этой цели.

## **Получение ширины и высоты бумаги на листе Excel**

В следующем образце кода объясняется использование свойств [**PageSetup.paper_width**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/paper_width) и [**PageSetup.paper_height**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/paper_height). Сначала он изменяет размер бумаги на *A2*, затем находит ширину и высоту бумаги, затем меняет на *A3*, *A4*, *Letter* и соответственно находит ширину и высоту бумаги.

### **Образец кода**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-GetPageDimensions.py" >}}

### **Вывод в консоль**

Вот вывод в консоль вышеуказанного образца кода.

{{< highlight java >}}

PaperA2: 16.54x23.39

PaperA3: 11.69x16.54

PaperA4: 8.27x11.69

PaperLetter: 8.5x11

{{< /highlight >}}
