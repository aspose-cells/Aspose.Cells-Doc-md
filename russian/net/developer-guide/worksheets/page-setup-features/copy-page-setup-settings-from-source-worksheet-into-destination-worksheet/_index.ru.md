---
title: Скопируйте настройки параметров страницы из исходного листа в рабочий лист назначения
type: docs
weight: 80
url: /ru/net/copy-page-setup-settings-from-source-worksheet-into-destination-worksheet/
description: В этой статье объясняется, как использовать образец кода библиотеки C# API или .NET для программного копирования параметров настройки страницы из исходного рабочего листа в целевой рабочий лист.
keywords: copy page setup settings c#, copy page setup settings to target worksheet c#
---
##  **Возможные сценарии использования**

Когда вы добавляете новый лист в книгу, он содержит *параметры параметров страницы* по умолчанию. Могут быть случаи, когда вам нужно перенести настройки ([**Настройка страницы**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup)) с одного листа на другой лист. В этом документе объясняется, как копировать настройки параметров страницы с одного рабочего листа на другой с помощью API-интерфейсов Aspose.Cells.

##  **Скопируйте настройки параметров страницы из исходного листа в рабочий лист назначения**

В следующем примере кода показано, как скопировать*Параметры настройки страницы*с одного рабочего листа на другой с помощью[**PageSetup.Копировать()**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/methods/copy)метод. Для справки см. следующий пример кода и вывод его консоли.

##  **Образец кода**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-CopyPageSetupSettingsFromSourceWorksheetToDestinationWorksheet.cs" >}}

##  **Консольный вывод**

{{< highlight "java" >}}

Before Paper Size: PaperA3ExtraTransverse

Before Paper Size: PaperLetter

After Paper Size: PaperA3ExtraTransverse

After Paper Size: PaperA3ExtraTransverse

{{< /highlight >}}
