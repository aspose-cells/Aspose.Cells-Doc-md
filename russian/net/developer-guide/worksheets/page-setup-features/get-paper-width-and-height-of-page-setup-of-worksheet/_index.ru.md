---
title: Получить ширину и высоту бумаги параметров страницы листа
type: docs
weight: 50
url: /ru/net/get-paper-width-and-height-of-page-setup-of-worksheet/
description: В этой статье вы узнаете, как получить ширину и высоту бумаги параметров страницы листа Excel с помощью кода на C# программным образом с использованием .NET API или Library.
keywords: ширина листа страницы настройки Excel на C#, высота листа страницы настройки Excel на C#
---

## **Возможные сценарии использования**

Иногда вам нужно знать ширину и высоту размера бумаги, установленного в параметрах страницы листа. Пожалуйста, используйте свойства [**PageSetup.PaperWidth**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/paperwidth) и [**PageSetup.PaperHeight**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/paperheight) для этой цели.

## **Получение ширины и высоты бумаги на листе Excel**

В следующем образце кода объясняется использование свойств [**PageSetup.PaperWidth**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/paperwidth) и [**PageSetup.PaperHeight**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/paperheight). Сначала он изменяет размер бумаги на *A2* и затем находит ширину и высоту бумаги, затем он изменяет его на *A3*, *A4*, *Letter* и находит ширину и высоту бумаги соответственно.

### **Образец кода**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-GetPageDimensions.cs" >}}

### **Вывод в консоль**

Вот вывод в консоль вышеуказанного образца кода.

{{< highlight java >}}

PaperA2: 16.54x23.39

PaperA3: 11.69x16.54

PaperA4: 8.27x11.69

PaperLetter: 8.5x11

{{< /highlight >}}
