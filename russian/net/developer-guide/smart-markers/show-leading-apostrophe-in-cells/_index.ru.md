---
title: Показать начальный апостроф в ячейках
type: docs
weight: 70
url: /ru/net/show-leading-apostrophe-in-cells/
---
 В Microsoft Excel начальный апостроф в значении ячейки скрыт. Aspose.Cells предоставляет возможность отображать апостроф по умолчанию. Для этого API предоставляет[Workbook.Settings.QuotePrefixToStyle](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/quoteprefixtostyle) имущество. Это свойство указывает, следует ли устанавливать[ЦитатаПрефикс](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix)свойство при вводе строкового значения, начинающегося с одинарной кавычки в ячейку. Настройка[Workbook.Settings.QuotePrefixToStyle](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/quoteprefixtostyle) собственность на**ЛОЖЬ**отобразит начальный апостроф в выходном файле Excel.

На следующем снимке экрана показан выходной файл Excel с видимым апострофом.

![дело:изображение_альтернативный_текст](show-leading-apostrophe-in-cells_1.jpg)

Следующий фрагмент кода демонстрирует это, добавляя данные со смарт-маркерами в исходный файл Excel. Исходный и выходной файлы Excel прилагаются для ознакомления.

[Исходный файл](98107425.xlsx)

[Выходной файл](98107426.xlsx)
## **Образец кода**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-AllowLeadingApostrophe-1.cs" >}}

Реализация*Объект данных*класс указан ниже

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-AllowLeadingApostrophe-2.cs" >}}
