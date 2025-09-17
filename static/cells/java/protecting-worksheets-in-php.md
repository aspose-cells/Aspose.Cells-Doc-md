##Protecting Worksheets in Php
## **Aspose.Cells - Protecting Worksheets**
To protect worksheet using **Aspose.Cells Java for PHP**, call **protect_worksheet** method of **protection** module.
**PHP Code**
//Instantiating a Excel object by excel file path
$excel = new Workbook($dataDir . "book1.xls");
//Accessing the first worksheet in the Excel file
$worksheets = $excel->getWorksheets();
$worksheet = $worksheets->get(0);
$protection = $worksheet->getProtection();
//The following 3 methods are only for Excel 2000 and earlier formats
$protection->setAllowEditingContent(false);
$protection->setAllowEditingObject(false);
$protection->setAllowEditingScenario(false);
//Protects the first worksheet with a password "1234"
$protection->setPassword("1234");
//Saving the modified Excel file in default format
$excel->save($dataDir . "output.xls");
## **Download Running Code**
Download **Protecting Worksheets (Aspose.Cells)** from any of the below mentioned social coding sites:
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/SecurityFeatures/ProtectingWorksheet.php)
