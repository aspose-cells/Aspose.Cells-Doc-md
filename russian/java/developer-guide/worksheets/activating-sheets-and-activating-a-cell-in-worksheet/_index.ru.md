---
title: Активация листов и активация Cell в рабочем листе
type: docs
weight: 5
url: /ru/java/activating-sheets-and-activating-a-cell-in-worksheet/
---
{{% alert color="primary" %}}

Иногда вам нужно, чтобы определенный рабочий лист был активным и отображался, когда пользователь открывает файл Excel Microsoft в Excel. Точно так же вы можете захотеть активировать определенную ячейку и настроить полосы прокрутки для отображения активной ячейки. Aspose.Cells способен выполнять все эти задачи, как показано ниже.

-  Ан**активный лист** — это лист, над которым вы работаете: имя активного листа на вкладке по умолчанию выделено полужирным шрифтом.
-  Ан**активная ячейка** — это выбранная ячейка, ячейка, в которую вводятся данные, когда вы начинаете печатать. Одновременно активна только одна ячейка. Активная ячейка выделена жирной рамкой.

{{% /alert %}}

## **Активация листов и активация Cell**

Aspose.Cells предоставляет специальные вызовы API для активации листа и ячейки. Например,[**WorksheetCollection.ActiveSheetIndex**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#ActiveSheetIndex)Свойство полезно для установки активного листа в книге. Точно так же[**Рабочий лист.ActiveCell**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#ActiveCell)Свойство можно использовать для установки и получения активной ячейки на листе.

Чтобы убедиться, что горизонтальные или вертикальные полосы прокрутки находятся в позиции индекса строки и столбца, в которой вы хотите отобразить определенные данные, используйте[**Лист.FirstVisibleRow**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#FirstVisibleRow)а также[**Рабочий лист.FirstVisibleColumn**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#FirstVisibleColumn)характеристики.

В следующем примере показано, как активировать рабочий лист и сделать в нем активную ячейку. При выполнении кода генерируется следующий вывод. Полосы прокрутки прокручиваются, чтобы сделать 2-ю строку и 2-й столбец их первой видимой строкой и столбцом.

**Установка ячейки B2 в качестве активной ячейки**

![дело:изображение_альтернативный_текст](activating-sheets-and-activating-a-cell-in-worksheet_1.png)

## Код Java для установки активного рабочего листа в Excel

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ActivatingSheetsandActivatingCell-ActivatingSheetsandActivatingCell.java" >}}

{{% alert color="primary" %}}

 В**оценка** режим, то есть; без установки действующей лицензии активным рабочим листом всегда будет тот, который содержит водяной знак оценки. Это поведение можно изменить, только установив лицензию при запуске приложения.

{{% /alert %}}
