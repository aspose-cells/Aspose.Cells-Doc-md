---
title: Удалить существующие настройки принтера для рабочих листов в файле Excel
type: docs
weight: 40
url: /ru/java/remove-existing-printersettings-of-worksheets-in-excel-file/
---
## **Возможные сценарии использования**
Иногда разработчики хотят запретить Excel включать*.bin* файлы настроек принтера в сохраненных файлах XLSX. Файлы настроек принтера находятся в папке*«[файл «root»]\xl\printerSettings»*. В этом документе объясняется, как удалить существующие настройки принтера с помощью API Aspose.Cells.
## **Удалить существующие настройки принтера для рабочих листов в файле Excel**
Aspose.Cells позволяет удалить существующие настройки принтера, указанные для разных листов в файле Excel. В следующем примере кода показано, как удалить существующие параметры принтера для всех рабочих листов в книге. Пожалуйста, посмотрите его[образец файла Excel](45056023.xlsx), [выходной файл Excel](45056024.xlsx)консольный вывод, а также скриншот для справки.
## **Скриншот**
![дело:изображение_альтернативный_текст](remove-existing-printersettings-of-worksheets-in-excel-file_1.png)
## **Образец кода**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Worksheets-PageSetupFeatures-RemoveExistingPrinterSettingsOfWorksheets.java" >}}
## **Консольный вывод**
{{< highlight "java" >}}

 PrinterSettings of this worksheet exist.

Sheet Name: Sheet1

Paper Size: 5

Printer settings of this worksheet are now removed by setting it null.

PrinterSettings of this worksheet exist.

Sheet Name: Sheet2

Paper Size: 34

Printer settings of this worksheet are now removed by setting it null.

PrinterSettings of this worksheet exist.

Sheet Name: Sheet3

Paper Size: 70

Printer settings of this worksheet are now removed by setting it null.

PrinterSettings of this worksheet exist.

Sheet Name: Sheet4

Paper Size: 8

Printer settings of this worksheet are now removed by setting it null.

{{< /highlight >}}
