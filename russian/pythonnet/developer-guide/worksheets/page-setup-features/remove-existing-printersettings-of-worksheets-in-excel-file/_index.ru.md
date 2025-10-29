---
title: Удаление существующих настроек принтера листов в файле Excel
type: docs
weight: 60
url: /ru/python-net/remove-existing-printersettings-of-worksheets-in-excel-file/
description: В этой статье вы узнаете, как программно удалить существующие настройки принтера листа внутри файла Excel через объект Page Setup, используя пример кода с библиотекой Aspose.Cells for Python Excel.
keywords: Библиотека Python Excel, удаление настроек принтера листа на Python, удаление настроек принтера в Excel листе на Python.
---

## **Возможные сценарии использования**
Иногда разработчики хотят предотвратить включение файлов *.bin* настроек принтера в сохраняемые файлы XLSX. Файлы настроек принтера расположены в папке *“[файл "root"]\xl\printerSettings”.* Этот документ объясняет, как удалить существующие настройки принтера с помощью API Aspose.Cells for Python via .NET.

## **Удаление текущих настроек принтера на листах Excel**
Aspose.Cells for Python via .NET позволяет удалить существующие настройки принтера, заданные для различных листов в файле Excel. Ниже приведен пример кода, который показывает, как удалить текущие настройки принтера для всех листов в рабочей книге. Также смотрите [пример файла Excel](45056020.xlsx), [выходной файл Excel](45056021.xlsx), вывод в консоль и скриншот для справки.

## **Снимок экрана**
![todo:image_alt_text](remove-existing-printersettings-of-worksheets-in-excel-file_1.png)

## **Образец кода**
{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-RemoveExistingPrinterSettingsOfWorksheets.py" >}}

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
{{< app/cells/assistant language="python-net" >}}
