---
title: Удалить существующие настройки принтера для рабочих листов в файле Excel
type: docs
weight: 60
url: /ru/net/remove-existing-printersettings-of-worksheets-in-excel-file/
description: В этой статье вы узнаете, как программно удалить существующие настройки принтера рабочего листа внутри файла Excel с помощью объекта «Параметры страницы» с помощью примера кода с использованием библиотеки C# API или .NET.
keywords: remove printer settings of worksheet c#, remove printer settings of excel worksheet c#
---
##  **Возможные сценарии использования**
Иногда разработчики хотят запретить Excel включать*.bin* файлы настроек принтера в сохраненных файлах XLSX. Файлы настроек принтера находятся в папке*«[файл «root»]\xl\printerSettings».* В этом документе объясняется, как удалить существующие настройки принтера с помощью API Aspose.Cells.
##  **Удалить существующие настройки принтера для рабочих листов в файле Excel**
Aspose.Cells позволяет удалить существующие настройки принтера, указанные для разных листов в файле Excel. В следующем примере кода показано, как удалить существующие параметры принтера для всех рабочих листов в книге. Пожалуйста, посмотрите его[образец файла Excel](45056020.xlsx), [выходной файл Excel](45056021.xlsx)консольный вывод, а также скриншот для справки.
##  **Скриншот**
![дело:image_alt_text](remove-existing-printersettings-of-worksheets-in-excel-file_1.png)
##  **Образец кода**
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-RemoveExistingPrinterSettingsOfWorksheets.cs" >}}
##  **Консольный вывод**
{{< highlight "java" >}}

 PrinterSettings of this worksheet exist.

Sheet Name: Sheet1

Paper Size: PaperLegal

Printer settings of this worksheet are now removed by setting it null.

PrinterSettings of this worksheet exist.

Sheet Name: Sheet2

Paper Size: PaperEnvelopeB5

Printer settings of this worksheet are now removed by setting it null.

PrinterSettings of this worksheet exist.

Sheet Name: Sheet3

Paper Size: PaperA6

Printer settings of this worksheet are now removed by setting it null.

PrinterSettings of this worksheet exist.

Sheet Name: Sheet4

Paper Size: PaperA3

Printer settings of this worksheet are now removed by setting it null.

{{< /highlight >}}
