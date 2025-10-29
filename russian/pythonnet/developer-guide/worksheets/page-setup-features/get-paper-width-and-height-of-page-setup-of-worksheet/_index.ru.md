---
title: Получить ширину и высоту бумаги параметров страницы листа
type: docs
weight: 50
url: /ru/python-net/get-paper-width-and-height-of-page-setup-of-worksheet/
description: Вы узнаете, как программно получить ширину и высоту бумаги настройки страницы листа Excel с помощью кода Python и API Aspose.Cells для Python via .NET.
keywords: Библиотека Excel на Python, ширина бумаги настройки страницы Excel, высота бумаги настройки страницы в Python.
---

## **Возможные сценарии использования**

Иногда вам нужно знать ширину и высоту размера бумаги, установленного в параметрах страницы листа. Пожалуйста, используйте свойства [**PageSetup.paper_width**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/paper_width) и [**PageSetup.paper_height**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/paper_height) для этой цели.

## **Получение ширины и высоты бумаги на листе Excel**

Следующий пример кода демонстрирует использование свойств [**PageSetup.paper_width**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/paper_width) и [**PageSetup.paper_height**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/paper_height). Он сначала изменяет размер бумаги на *A2*, затем находит ширину и высоту бумаги, после чего изменяет их на *A3*, *A4*, *Letter* и соответственно находит ширину и высоту бумаги.

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
{{< app/cells/assistant language="python-net" >}}
