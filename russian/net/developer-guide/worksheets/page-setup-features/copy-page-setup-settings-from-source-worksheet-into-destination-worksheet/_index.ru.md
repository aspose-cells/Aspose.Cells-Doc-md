---
title: Скопировать настройки страницы из исходного листа в назначенный лист
type: docs
weight: 80
url: /ru/net/copy-page-setup-settings-from-source-worksheet-into-destination-worksheet/
description: Эта статья объясняет, как использовать примерный код C# API или библиотеки .NET для копирования настроек страницы от исходного листа в конечный лист программно.
keywords: копировать настройки страницы c#, копировать настройки страницы на конечный лист c#
---

## **Возможные сценарии использования**

При добавлении нового листа в книгу, он содержит настройки *Параметры страницы* по умолчанию. Иногда может возникнуть необходимость передать настройки ([**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup)) с одного листа на другой. В этом документе объясняется, как скопировать настройки Параметры страницы с одного листа на другой с использованием API Aspose.Cells.

## **Копирование настроек страницы с исходного листа на целевой лист**

Следующий образец кода иллюстрирует, как скопировать *Параметры страницы* с одного листа на другой с использованием метода [**PageSetup.Copy()**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/methods/copy). Обратитесь к следующему образцу кода и его выводу консоли для справки.

## **Образец кода**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-CopyPageSetupSettingsFromSourceWorksheetToDestinationWorksheet.cs" >}}

## **Вывод в консоль**

{{< highlight java >}}

Before Paper Size: PaperA3ExtraTransverse

Before Paper Size: PaperLetter

After Paper Size: PaperA3ExtraTransverse

After Paper Size: PaperA3ExtraTransverse

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
