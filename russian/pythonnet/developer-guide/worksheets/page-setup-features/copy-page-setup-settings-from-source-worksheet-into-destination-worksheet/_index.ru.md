---
title: Скопировать настройки страницы из исходного листа в назначенный лист
type: docs
weight: 80
url: /ru/python-net/copy-page-setup-settings-from-source-worksheet-into-destination-worksheet/
description: Эта статья объясняет, как использовать пример кода Aspose.Cells для Python via .NET, чтобы программно скопировать настройки настройки страницы из исходного рабочего листа в целевой рабочий лист.
keywords: Библиотека Excel для Python, копирование настроек страницы в Python, копирование настроек страницы в целевой рабочий лист в Python.
---

## **Возможные сценарии использования**

Когда вы добавляете новый лист в книгу, он содержит настройки по умолчанию *настройки страницы*. Возможно, вам потребуется перенести настройки ([**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup)) с одного рабочего листа на другой. Этот документ объясняет, как копировать настройки страницы с одного рабочего листа на другой с помощью Aspose.Cells для Python via .NET API.

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
