---
title: Удаление существующих настроек принтера листов в файле Excel
type: docs
weight: 40
url: /ru/java/remove-existing-printersettings-of-worksheets-in-excel-file/
---

## **Возможные сценарии использования**
Иногда разработчики хотят предотвратить включение файлов настроек принтера *.bin* в сохраненные файлы XLSX. Файлы настроек принтера располагаются в *"[файл"root"]\xl\printerSettings"*. В этом документе объясняется, как удалить существующие параметры печати с использованием API Aspose.Cells.
## **Удаление текущих настроек принтера на листах Excel**
Aspose.Cells позволяет удалять существующие параметры печати, указанные для различных листов в файле Excel. В следующем образце кода показано, как удалить существующие параметры печати для всех листов книги. Пожалуйста, ознакомьтесь с [образцовым файлом Excel](45056023.xlsx), [выходным файлом Excel](45056024.xlsx), выводом консоли, а также скриншотом для справки.
## **Снимок экрана**
![todo:image_alt_text](remove-existing-printersettings-of-worksheets-in-excel-file_1.png)
## **Образец кода**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Worksheets-PageSetupFeatures-RemoveExistingPrinterSettingsOfWorksheets.java" >}}
## **Вывод в консоль**
{{< highlight java >}}

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
