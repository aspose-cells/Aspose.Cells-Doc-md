---
title: Показывать ведущий апостроф в ячейках
type: docs
weight: 20
url: /ru/java/show-leading-apostrophe-in-cells/
---

## **Показывать ведущую апостроф в ячейках.**

В Microsoft Excel ведущий апостроф в значении ячейки скрыт. Aspose.Cells предоставляет возможность отображать апостроф по умолчанию. Для этого API предоставляет свойство, которое указывает, нужно ли устанавливать свойство при вводе строки, начинающейся с одинарной кавычки, в ячейку. Установка свойства в **false** будет показывать ведущий апостроф в выходном файле Excel.

На следующем снимке экрана показан выходной файл Excel с видимым апострофом.

![todo:image_alt_text](show-leading-apostrophe-in-cells_1.jpg)

Ниже приведен фрагмент кода, демонстрирующий это путем добавления данных с интеллектуальными маркерами в исходный файл Excel. В качестве справки прилагаются исходный и выходной файлы Excel.

[Исходный файл](AllowLeadingApostropheSample.xlsx)

[Выходной файл](AllowLeadingApostropheSample_out.xlsx)

## **Образец кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-AllowLeadingApostrophe-1.java" >}}

Реализация класса *DataObject* представлена ниже

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-HelperClasses-DataObject-1.java" >}}
