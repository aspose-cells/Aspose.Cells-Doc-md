---
title: Spara filer i PHP
type: docs
weight: 20
url: /sv/java/saving-files-in-php/
---
## **Aspose.Cells - Spara filer**
### **Sparar filen på någon plats**
 Om utvecklare behöver spara sina filer med**Aspose.Cells Java for PHP** till någon lagringsplats kan de helt enkelt ange filnamnet (med dess fullständiga lagringssökväg) och önskat filformat (med hjälp av**FileFormatType**uppräkning) medan du anropar**spara**metod av**Arbetsbok**objekt.

**PHP-kod**

{{< highlight "php" >}}

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
## **Ladda ner Running Code**
 Ladda ner**Spara filer (Aspose.Cells)**från någon av nedan nämnda webbplatser för social kodning:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithFiles/FileHandlingFeatures/SavingFiles.php)
