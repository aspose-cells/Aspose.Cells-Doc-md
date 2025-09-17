##Unprotect a Worksheet in Php
## **Aspose.Cells - Unprotect a Worksheet**
To protect worksheet using **Aspose.Cells Java for PHP**, call **unprotect_worksheet** method of **protection** module.
**PHP Code**
$filesFormatType = new FileFormatType();
//Instantiating a Workbook object
$workbook = new Workbook($dataDir . "book1.xls");
$worksheets = $workbook->getWorksheets();
$worksheet = $worksheets->get(0);
$protection = $worksheet->getProtection();
//Unprotecting the worksheet with a password
$worksheet->unprotect("aspose");
// Save the excel file.
$workbook->save($dataDir . "output.xls", $filesFormatType->EXCEL_97_TO_2003);
## **Download Running Code**
Download **Unprotect a Worksheet (Aspose.Cells)** from any of the below mentioned social coding sites:
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/SecurityFeatures/UnprotectingPasswordProtectedWorksheet.php)
