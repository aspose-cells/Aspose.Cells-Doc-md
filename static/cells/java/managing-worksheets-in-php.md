##Managing Worksheets in Php
## **Aspose.Cells - Managing Worksheets**
### **Adding Worksheets to a New Excel File**
To add Worksheet to a new Excel file using **Aspose.Cells Java for PHP**, simply call **add_worksheet** method of **MangingWorksheets** module.
**PHP Code**
//Instantiating a Workbook object
$workbook = new Workbook();
//Adding a new worksheet to the Workbook object
$worksheets = $workbook->getWorksheets();
$sheetIndex = $worksheets->add();
$worksheet = $worksheets->get($sheetIndex);
//Setting the name of the newly added worksheet
$worksheet->setName("My Worksheet");
//Saving the Excel file
$workbook->save($dataDir . "book.out.xls");
### **Removing Worksheets using Sheet Name**
To remove worksheet by sheet name using **Aspose.Cells Java for PHP**, simply call **remove_worksheet_by_name** method of **MangingWorksheets** module.
**PHP Code**
//Creating a file stream containing the Excel file to be opened
$fstream = new FileInputStream($dataDir . "book.xls");
//Instantiating a Workbook object with the stream
$workbook = new Workbook($fstream);
//Removing a worksheet using its sheet name
$workbook->getWorksheets()->removeAt("Sheet1");
//Saving the Excel file
$workbook->save($dataDir . "book.out.xls");
//Closing the file stream to free all resources
$fstream->close();
### **Removing Worksheets using Sheet Index**
To remove worksheet by sheet index using **Aspose.Cells Java for PHP**, simply call **remove_worksheet_by_index** method of **MangingWorksheets** module.
**PHP Code**
//Creating a file stream containing the Excel file to be opened
$fstream=new FileInputStream($dataDir . "book.xls");
//Instantiating a Workbook object with the stream
$workbook = new Workbook($fstream);
//Removing a worksheet using its sheet index
$workbook->getWorksheets()->removeAt(0);
//Saving the Excel file
$workbook->save($dataDir . "book.out.xls");
//Closing the file stream to free all resources
$fstream->close();
## **Download Running Code**
Download **Managing Worksheets (Aspose.Cells)** from any of the below mentioned social coding sites:
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/ManagementFeatures/ManagingWorksheets)
