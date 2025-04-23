---
title: Скопировать настройки страницы из исходного листа в назначенный лист
type: docs
weight: 80
url: /ru/python-net/copy-page-setup-settings-from-source-worksheet-into-destination-worksheet/
description: В этой статье объясняется, как с помощью примера кода Aspose.Cells для Python via .NET скопировать настройки Page Setup из исходного листа в целевой лист программно.
keywords: Библиотека Excel на Python, копирование настроек страницы, копировать настройки страницы в целевой лист в Python.
---

## **Возможные сценарии использования**

При добавлении нового листа в рабочую книгу он содержит настройки *Page Setup* по умолчанию. Иногда необходимо перенести эти настройки ([**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup)) с одного листа на другой. В этом документе объясняется, как копировать настройки Page Setup с помощью API Aspose.Cells для Python via .NET.

## **Копирование настроек страницы с исходного листа на целевой лист**

Следующий образец кода иллюстрирует, как скопировать *Параметры страницы* с одного листа на другой с использованием метода [**PageSetup.copy()**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/copy/#aspose.cells.PageSetup-aspose.cells.CopyOptions). Обратитесь к следующему образцу кода и его выводу консоли для справки.

## **Образец кода**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-CopyPageSetupSettingsFromSourceWorksheetToDestinationWorksheet.py" >}}

## **Вывод в консоль**

{{< highlight java >}}

Before Paper Size: PaperA3ExtraTransverse

Before Paper Size: PaperLetter

After Paper Size: PaperA3ExtraTransverse

After Paper Size: PaperA3ExtraTransverse

{{< /highlight >}}
