---
title: Скопировать настройки страницы из исходного листа в назначенный лист
type: docs
weight: 10
url: /ru/java/copy-page-setup-settings-from-source-worksheet-into-destination-worksheet/
---

## **Возможные сценарии использования**

Когда вы добавляете новый лист в книгу Excel, он содержит настройки страницы по умолчанию. Иногда возникает необходимость передать настройки ([**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/PageSetup)) с одного листа на другой. В данном документе объясняется, как скопировать настройки страницы с одного листа на другой с использованием API Aspose.Cells.

## **Копирование настроек страницы с исходного листа на целевой лист**

Нижеприведенный образец кода показывает, как скопировать параметры Печати страницы с одного листа на другой с помощью метода [**PageSetup.Copy()**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#copy-com.aspose.cells.PageSetup-com.aspose.cells.CopyOptions-). Пожалуйста, ознакомьтесь с приведенным ниже образцом кода и его выводом в консоли в качестве справки.

## **Образец кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Worksheets-PageSetupFeatures-CopyPageSetupSettingsFromSourceWorksheetToDestinationWorksheet.java" >}}

## **Вывод в консоль**

{{< highlight java >}}

Before Paper Size: PAPER_A_3_EXTRA_TRANSVERSE

Before Paper Size: PAPER_LETTER

After Paper Size: PAPER_A_3_EXTRA_TRANSVERSE

After Paper Size: PAPER_A_3_EXTRA_TRANSVERSE

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
