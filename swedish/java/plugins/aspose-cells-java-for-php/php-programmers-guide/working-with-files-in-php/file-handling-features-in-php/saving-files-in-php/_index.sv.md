---
title: Spara filer i PHP
type: docs
weight: 20
url: /sv/java/saving-files-in-php/
---

## **Aspose.Cells - Spara filer**
### **Spara filen på en viss plats**
Om utvecklare behöver spara sina filer med **Aspose.Cells Java för PHP** till en lagringsplats kan de helt enkelt specificera filnamnet (med dess kompletta lagringsväg) och önskat filformat (genom att använda **FileFormatType**-uppräkningen) vid anropet av **spara**-metoden för **Workbook**-objektet.

**PHP-kod**

{{< highlight php >}}

 $fileFormatType = new FileFormatType();

//Creating an Workbook object with an Excel file path

$workbook = new Workbook($dataDir . "book.xls");

//Save in default (Excel2003) format

$workbook->save($dataDir . "book.default.out.xls");

//Save in Excel2003 format

$workbook->save($dataDir . "book.out.xls",$fileFormatType->EXCEL_97_TO_2003);

//Save in Excel2007 xlsx format

$workbook->save($dataDir . "book.out.xlsx", $fileFormatType->XLSX);

//Save in SpreadsheetML format

$workbook->save($dataDir . "book.out.xml", $fileFormatType->EXCEL_2003_XML);

{{< /highlight >}}
## **Ladda ned körbar kod**
Ladda ner **Sparar filer (Aspose.Cells)** från någon av de nedan nämnda sociala kodningssidorna:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithFiles/FileHandlingFeatures/SavingFiles.php)
