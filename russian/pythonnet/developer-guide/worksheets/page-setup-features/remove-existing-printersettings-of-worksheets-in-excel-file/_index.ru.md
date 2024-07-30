---
title: Удаление существующих настроек принтера листов в файле Excel
type: docs
weight: 60
url: /ru/python-net/remove-existing-printersettings-of-worksheets-in-excel-file/
description: В данной статье вы узнаете, как удалить существующие параметры принтера рабочего листа в файле Excel через объект настройки страницы программно с образцовым кодом, используя библиотеку Python Excel Aspose.Cells.
keywords: Библиотека Python Excel, удаление параметров принтера рабочего листа на Python, Удаление параметров принтера рабочего листа Excel.
---

## **Возможные сценарии использования**
Иногда разработчики хотят предотвратить Excel от включения файлов настроек принтера *.bin* в сохраненные файлы XLSX. Файлы настроек принтера находятся в папке *“[file "root"]\xl\printerSettings”.* В этом документе объясняется, как удалить существующие настройки принтера с использованием API Aspose.Cells для Python via .NET.

## **Удаление текущих настроек принтера на листах Excel**
Aspose.Cells для Python via .NET позволяет удалять существующие настройки принтера, указанные для разных листов в файле Excel. Приведенный ниже образец кода показывает, как удалить существующие настройки принтера для всех листов в рабочей книге. Пожалуйста, смотрите [образец файла Excel](45056020.xlsx), [файл Excel с результатом](45056021.xlsx), вывод в консоль, а также скриншот для справки.

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
