---
title: Получить ширину бумаги и высоту страницы настройки рабочего листа
type: docs
weight: 50
url: /ru/net/get-paper-width-and-height-of-page-setup-of-worksheet/
description: В этой статье вы узнаете, как получить ширину и высоту бумаги для настройки страницы рабочего листа Excel, используя код C# программно с .NET API или библиотекой.
keywords: excel page setup paper width c#, excel page setup paper height c#
---
##  **Возможные сценарии использования**

Иногда вам нужно знать ширину и высоту размера бумаги, поскольку они были установлены в настройках страницы рабочего листа. Пожалуйста, используйте[**PageSetup.PaperWidth**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/paperwidth)и[**PageSetup.PaperHeight**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/paperheight)свойств для этой цели.

##  **Получить ширину бумаги и высоту страницы настройки рабочего листа**

 В следующем примере кода объясняется использование[**PageSetup.PaperWidth**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/paperwidth) и[**PageSetup.PaperHeight**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/paperheight) характеристики. Сначала он изменяет размер бумаги на*A2*а затем находит ширину и высоту бумаги, затем меняет ее на*A3*, *A4*, *письмо*и находит ширину и высоту бумаги соответственно.

###  **Образец кода**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-GetPageDimensions.cs" >}}

###  **Консольный вывод**

Вот вывод консоли приведенного выше примера кода.

{{< highlight "java" >}}

PaperA2: 16.54x23.39

PaperA3: 11.69x16.54

PaperA4: 8.27x11.69

PaperLetter: 8.5x11

{{< /highlight >}}
