##Split Panes in Php
## **Aspose.Cells - Split Panes**
To Split Panes using **Aspose.Cells Java for PHP**, simply invoke **SplitPanes** module.
**PHP Code**
$saveFormat = new SaveFormat();
//Instantiate a new workbook
//Open a template file
$book = new Workbook($dataDir . "book.xls");
//Set the active cell
$book->getWorksheets()->get(0)->setActiveCell("A20");
//Split the worksheet window
$book->getWorksheets()->get(0)->split();
//Save the excel file
$book->save($dataDir . "book.out.xls", $saveFormat->EXCEL_97_TO_2003);
## **Download Running Code**
Download **Split Panes (Aspose.Cells)** from any of the below mentioned social coding sites:
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/DisplayFeatures/SplitPanes.php)
