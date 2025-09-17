##Add Worksheets to New Excel File in PHP
## **Add Worksheets to New Excel File**
Add Worksheets to New Excel File
**PHP Code**
$dataDir = '';
// Create Aspose.Cells Helper Object
$ptr = new \COM('Aspose.Cells.Interop.InteropHelper');
// Opening through Path
// Creating a Workbook object and opening an Excel file using its file path
$workbook = $ptr->New("Aspose.Cells.Workbook",array());
$worksheets = $ptr->Get($workbook,"Worksheets",array());
$worksheet_index = $ptr->Call($worksheets,"Add_2",array());
$worksheet = $ptr->Get($worksheets,"Item",array($worksheet_index));
$ptr->Set($worksheet,"Name","My Worksheet",array());
$ptr->Call($workbook,"Save",array($dataDir."/output.xls"));
print "Completed." . PHP_EOL;
## **Download Running Code**
Download **Add Worksheets to New Excel File (Aspose.Cells)** from any of the below mentioned social coding sites:
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Plugins/Aspose_Cells_NET_for_PHP/src/aspose/cells/WorkingWithWorksheets/ManagementFeatures/ManagingWorksheets/AddingWorksheetsToNewExcelFile.php)
