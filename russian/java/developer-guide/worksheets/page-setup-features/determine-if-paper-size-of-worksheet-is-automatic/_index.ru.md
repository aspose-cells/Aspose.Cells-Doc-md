---
title: Определение автоматического размера бумаги листа
type: docs
weight: 20
url: /ru/java/determine-if-paper-size-of-worksheet-is-automatic/
---

## **Возможные сценарии использования**

В большинстве случаев размер бумаги листа устанавливается автоматически. Когда это происходит, он часто устанавливается как *Letter*. Иногда пользователь устанавливает размер бумаги листа в соответствии с их требованиями. В этом случае размер бумаги не является автоматическим. Вы можете определить, является ли размер бумаги листа автоматическим или нет, используя метод [**Worksheet.getPageSetup().isAutomaticPaperSize()**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#IsAutomaticPaperSize).

## **Определение автоматического размера бумаги листа**

В приведенном ниже образце кода загружаются следующие два файлы Excel

- [samplePageSetupIsAutomaticPaperSize-False.xlsx](48496700.xlsx)
- [samplePageSetupIsAutomaticPaperSize-True.xlsx](48496701.xlsx)

и определяется, является ли размер бумаги их первого листа автоматическим или нет. В Microsoft Excel вы можете проверить, является ли размер бумаги автоматическим или нет, через окно настройки страницы, как показано на этом скриншоте.

![todo:image_alt_text](determine-if-paper-size-of-worksheet-is-automatic_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Worksheets-PageSetupFeatures-DetermineIfPaperSizeOfWorksheetIsAutomatic.java" >}}

## **Вывод в консоль**

Вот вывод в консоль приведенного выше образца кода при выполнении с данными образцами файлов Excel.

{{< highlight java >}}

First Worksheet of First Workbook - IsAutomaticPaperSize: false

First Worksheet of Second Workbook - IsAutomaticPaperSize: true

{{< /highlight >}}
