---
title: Определение автоматического размера бумаги листа
type: docs
weight: 90
url: /ru/python-net/determine-if-paper-size-of-worksheet-is-automatic/
description: В этой статье объясняется, как использовать пример кода Aspose.Cells для Python via .NET для определения, является ли размер бумаги листа автоматическим программно.
keywords: Библиотека Excel на Python, определить, является ли размер бумаги листа автоматическим.
---

## **Возможные сценарии использования**

Большую часть времени размер бумаги листа устанавливается автоматически. Когда он устанавливается автоматически, он часто устанавливается *Letter*. Иногда пользователь устанавливает размер бумаги листа в соответствии с их потребностями. В этом случае размер бумаги не является автоматическим. Вы можете определить, является ли размер бумаги листа автоматическим или нет, используя свойство [**Worksheet.page_setup.IsAutomaticPaperSize**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/is_automatic_paper_size/).

## **Определение автоматического размера бумаги листа**

В приведенном ниже образце кода загружаются следующие два файлы Excel

- [samplePageSetupIsAutomaticPaperSize-False.xlsx](48496681.xlsx)
- [samplePageSetupIsAutomaticPaperSize-True.xlsx](48496682.xlsx)

и определяется, является ли размер бумаги их первого листа автоматическим или нет. В Microsoft Excel вы можете проверить, является ли размер бумаги автоматическим или нет, через окно настройки страницы, как показано на этом скриншоте.

![todo:image_alt_text](determine-if-paper-size-of-worksheet-is-automatic_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-DetermineIfPaperSizeOfWorksheetIsAutomatic.py" >}}

## **Вывод в консоль**

Вот вывод в консоль приведенного выше образца кода при выполнении с данными образцами файлов Excel.

{{< highlight java >}}

First Worksheet of First Workbook - IsAutomaticPaperSize: False

First Worksheet of Second Workbook - IsAutomaticPaperSize: True

{{< /highlight >}}
{{< app/cells/assistant language="python-net" >}}
