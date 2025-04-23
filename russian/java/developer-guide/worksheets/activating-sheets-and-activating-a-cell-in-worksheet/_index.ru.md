---
title: Активация листов и активация ячейки в рабочем листе
type: docs
weight: 5
url: /ru/java/activating-sheets-and-activating-a-cell-in-worksheet/
---

{{% alert color="primary" %}}

Иногда вам нужно, чтобы определенный рабочий лист был активным и отображался, когда пользователь открывает файл Microsoft Excel в Excel. Точно так же вы можете активировать определенную ячейку и настроить полосы прокрутки для отображения активной ячейки. Aspose.Cells способен выполнять все эти задачи, как показано ниже.

- **Активный лист** - это лист, над которым вы работаете: имя активного листа на вкладке жирным шрифтом по умолчанию.
- **Активная ячейка** - это выбранная ячейка, в которую вводятся данные при начале ввода. Только одна ячейка активна в данный момент. Активная ячейка выделена толстой границей.

{{% /alert %}}

## **Активация листов и активация ячейки**

Aspose.Cells предоставляет конкретные вызовы API для активации листа и ячейки. Например, свойство [**WorksheetCollection.ActiveSheetIndex**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#ActiveSheetIndex) полезно для установки активного листа в книге. Точно так же свойство [**Worksheet.ActiveCell**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#ActiveCell) может быть использовано для установки и получения активной ячейки на листе.

Чтобы убедиться, что горизонтальные или вертикальные полосы прокрутки находятся в позиции номера строки и столбца, которые вы хотите показать конкретные данные, используйте свойства [**Worksheet.FirstVisibleRow**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#FirstVisibleRow) и [**Worksheet.FirstVisibleColumn**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#FirstVisibleColumn).

В следующем примере показано, как активировать лист и сделать активной ячейку в нем. Следующий вывод генерируется при выполнении кода. Полосы прокрутки прокручиваются для того, чтобы 2-я строка и 2-й столбец стали их первой видимой строкой и столбцом.

**Установить ячейку B2 в качестве активной ячейки**

![todo:image_alt_text](activating-sheets-and-activating-a-cell-in-worksheet_1.png)

## Код Java для установки активного листа в Excel

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ActivatingSheetsandActivatingCell-ActivatingSheetsandActivatingCell.java" >}}

{{% alert color="primary" %}}

В режиме **оценки**, то есть без установки действительной лицензии, активным листом будет всегда тот, который содержит водяной знак оценки. Это поведение можно изменить только путем установки лицензии в начале приложения.

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
