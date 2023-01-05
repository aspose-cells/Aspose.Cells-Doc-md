---
title: Показать начальный апостроф в ячейках
type: docs
weight: 20
url: /ru/java/show-leading-apostrophe-in-cells/
---
## **Показать начальный апостроф в ячейках**

В Microsoft Excel начальный апостроф в значении ячейки скрыт. Aspose.Cells предоставляет возможность отображать апостроф по умолчанию. Для этого API предоставляет[**Workbook.Settings.QuotePrefixToStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#QuotePrefixToStyle)имущество. Это свойство указывает, следует ли устанавливать[**ЦитатаПрефикс**](https://reference.aspose.com/cells/java/com.aspose.cells/Style#QuotePrefix)свойство при вводе строкового значения, начинающегося с одинарной кавычки в ячейку. Настройка[**Workbook.Settings.QuotePrefixToStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#QuotePrefixToStyle)собственность на**ЛОЖЬ**отобразит начальный апостроф в выходном файле Excel.

На следующем снимке экрана показан выходной файл Excel с видимым апострофом.

![дело:изображение_альтернативный_текст](show-leading-apostrophe-in-cells_1.jpg)

Следующий фрагмент кода демонстрирует это, добавляя данные со смарт-маркерами в исходный файл Excel. Исходный и выходной файлы Excel прилагаются для ознакомления.

[Исходный файл](AllowLeadingApostropheSample.xlsx)

[Выходной файл](AllowLeadingApostropheSample_out.xlsx)

## **Образец кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-AllowLeadingApostrophe-1.java" >}}

Реализация*Объект данных*класс указан ниже

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-HelperClasses-DataObject-1.java" >}}
