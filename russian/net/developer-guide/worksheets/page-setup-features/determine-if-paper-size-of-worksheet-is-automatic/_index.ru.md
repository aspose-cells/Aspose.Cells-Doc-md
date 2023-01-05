---
title: Определите, является ли размер бумаги рабочего листа автоматическим
type: docs
weight: 90
url: /ru/net/determine-if-paper-size-of-worksheet-is-automatic/
---
## **Возможные сценарии использования**

 В большинстве случаев размер бумаги рабочего листа устанавливается автоматически. Когда он автоматический, он часто устанавливается как*Письмо* . Иногда пользователь устанавливает размер бумаги рабочего листа в соответствии со своими требованиями. В этом случае размер бумаги не задается автоматически. Вы можете узнать, является ли размер бумаги рабочего листа автоматическим или нет, используя[**Рабочий лист.PageSetup.IsAutomaticPaperSize**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/isautomaticpapersize)имущество.

## **Определите, является ли размер бумаги рабочего листа автоматическим**

Пример кода, приведенный ниже, загружает следующие два файла Excel.

- [SamplePageSetupIsAutomaticPaperSize-False.xlsx](48496681.xlsx)
- [SamplePageSetupIsAutomaticPaperSize-True.xlsx](48496682.xlsx)

и выяснить, является ли размер бумаги их первого рабочего листа автоматическим или нет. В Microsoft Excel вы можете проверить, является ли размер бумаги автоматическим или нет, через окно «Параметры страницы», как показано на этом снимке экрана.

![дело:изображение_альтернативный_текст](determine-if-paper-size-of-worksheet-is-automatic_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-DetermineIfPaperSizeOfWorksheetIsAutomatic.cs" >}}

## **Консольный вывод**

Вот вывод консоли приведенного выше примера кода при выполнении с заданными примерами файлов Excel.

{{< highlight "java" >}}

First Worksheet of First Workbook - IsAutomaticPaperSize: False

First Worksheet of Second Workbook - IsAutomaticPaperSize: True

{{< /highlight >}}
