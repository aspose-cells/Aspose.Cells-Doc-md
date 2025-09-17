##Removing Worksheets Using Sheet Index in PHP
## **Removing Worksheets Using Sheet Index**
Removing Worksheets Using Sheet Index
**PHP Code**
$dataDir = '';
/ Create Aspose.Cells Helper Object
$ptr = new \COM('Aspose.Cells.Interop.InteropHelper');
// Opening through Path
// Creating a Workbook object and opening an Excel file using its file path
$workbook = $ptr->New("Aspose.Cells.Workbook",array($dataDir . '/book1.xls'));
$worksheets = $ptr->Get($workbook,"Worksheets",array());
$ptr->Call($worksheets,"RemoveAt",array(0));
$ptr->Call($workbook,"Save",array($dataDir."/output.xls"));
## **Download Running Code**
Download **Removing Worksheets Using Sheet Index (Aspose.Cells)** from any of the below mentioned social coding sites:
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Plugins/Aspose_Cells_NET_for_PHP/src/aspose/cells/WorkingWithWorksheets/ManagementFeatures/ManagingWorksheets/RemovingWorksheetsUsingSheetIndex.php)
