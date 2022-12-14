---
title: Определите, является ли размер бумаги рабочего листа автоматическим
type: docs
weight: 20
url: /ru/java/determine-if-paper-size-of-worksheet-is-automatic/
---
## **Возможные сценарии использования**

 В большинстве случаев размер бумаги рабочего листа устанавливается автоматически. Когда он автоматический, он часто устанавливается как*Письмо* . Иногда пользователь устанавливает размер бумаги рабочего листа в соответствии со своими требованиями. В этом случае размер бумаги не задается автоматически. Вы можете узнать, является ли размер бумаги рабочего листа автоматическим или нет, используя[**Рабочий лист.getPageSetup().isAutomaticPaperSize()**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#IsAutomaticPaperSize)метод.

## **Определите, является ли размер бумаги рабочего листа автоматическим**

Пример кода, приведенный ниже, загружает следующие два файла Excel.

- [SamplePageSetupIsAutomaticPaperSize-False.xlsx](48496700.xlsx)
- [SamplePageSetupIsAutomaticPaperSize-True.xlsx](48496701.xlsx)

и выяснить, является ли размер бумаги их первого рабочего листа автоматическим или нет. В Microsoft Excel вы можете проверить, является ли размер бумаги автоматическим или нет, через окно «Параметры страницы», как показано на этом снимке экрана.

![дело:изображение_альтернативный_текст](determine-if-paper-size-of-worksheet-is-automatic_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Worksheets-PageSetupFeatures-DetermineIfPaperSizeOfWorksheetIsAutomatic.java" >}}

## **Консольный вывод**

Вот вывод консоли приведенного выше примера кода при выполнении с заданными примерами файлов Excel.

{{< highlight "java" >}}

First Worksheet of First Workbook - IsAutomaticPaperSize: false

First Worksheet of Second Workbook - IsAutomaticPaperSize: true

{{< /highlight >}}
