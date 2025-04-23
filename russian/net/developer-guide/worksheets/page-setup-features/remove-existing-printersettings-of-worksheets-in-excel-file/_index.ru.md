---
title: Удаление существующих настроек принтера листов в файле Excel
type: docs
weight: 60
url: /ru/net/remove-existing-printersettings-of-worksheets-in-excel-file/
description: В этой статье вы узнаете, как удалить существующие настройки принтера на листе в файле Excel через объект параметров страницы программным способом с образцом кода с использованием API на C# или .NET Library.
keywords: удалить настройки принтера листа на C#, удалить настройки принтера листа Excel на C#
---

## **Возможные сценарии использования**
Иногда разработчики хотят предотвратить Excel от включения файлов настроек принтера *.bin* в сохраненные файлы XLSX. Файлы настроек принтера расположены в папке *“[file "root"]\xl\printerSettings”.* В этом документе объясняется, как удалить существующие настройки принтера с использованием Aspose.Cells APIs.
## **Удаление текущих настроек принтера на листах Excel**
Aspose.Cells позволяет удалять существующие настройки принтера, указанные для различных листов в файле Excel. В приведенном ниже образце кода показано, как удалить существующие настройки принтера для всех листов в книге. Пожалуйста, ознакомьтесь с [образцом файла Excel](45056020.xlsx), [выходным файлом Excel](45056021.xlsx), выводом консоли, а также скриншотами для справки.
## **Снимок экрана**
![todo:image_alt_text](remove-existing-printersettings-of-worksheets-in-excel-file_1.png)
## **Образец кода**
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-RemoveExistingPrinterSettingsOfWorksheets.cs" >}}
## **Вывод в консоль**
{{< highlight java >}}

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
{{< app/cells/assistant language="csharp" >}}
