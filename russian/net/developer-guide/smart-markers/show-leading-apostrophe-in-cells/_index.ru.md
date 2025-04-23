---
title: Показывать ведущий апостроф в ячейках
type: docs
weight: 70
url: /ru/net/show-leading-apostrophe-in-cells/
---

В Microsoft Excel ведущий апостроф в значении ячейки скрыт. Aspose.Cells предоставляет функцию отображения апострофа по умолчанию. Для этого API предоставляет свойство [Workbook.Settings.QuotePrefixToStyle](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/quoteprefixtostyle). Это свойство показывает, установлено ли свойство [QuotePrefix](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix) при вводе строки, начинающейся с одиночного апострофа, в ячейку. Установка свойства [Workbook.Settings.QuotePrefixToStyle](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/quoteprefixtostyle) на **false** отобразит ведущий апостроф в выходном файле Excel.

На следующем снимке экрана показан выходной файл Excel с видимым апострофом.

![todo:image_alt_text](show-leading-apostrophe-in-cells_1.jpg)

Ниже приведен фрагмент кода, демонстрирующий это путем добавления данных с интеллектуальными маркерами в исходный файл Excel. В качестве справки прилагаются исходный и выходной файлы Excel.

[Исходный файл](98107425.xlsx)

[Файл вывода](98107426.xlsx)
## **Образец кода**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-AllowLeadingApostrophe-1.cs" >}}

Реализация класса *DataObject* представлена ниже

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-AllowLeadingApostrophe-2.cs" >}}
{{< app/cells/assistant language="csharp" >}}
