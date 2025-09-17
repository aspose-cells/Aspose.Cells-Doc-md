##Worksheet to Image Conversion in PHP
## **Aspose.Cells - Convert Worksheet to Image**
Convert a Microsoft Excel Worksheet to Image File
**PHP Code**
$dataDir = '';
// Create Aspose.Cells Helper Object
$ptr = new \COM('Aspose.Cells.Interop.InteropHelper');
// Opening through Path
// Creating a Workbook object and opening an Excel file using its file path
$workbook = $ptr->New("Aspose.Cells.Workbook",array($dataDir . '/MyTestBook1.xls'));
$worksheets = $ptr->Get($workbook,"Worksheets",array());
$sheet = $ptr->Get($worksheets,'Item',array(0));
$imgOptions = $ptr->New("Aspose.Cells.Rendering.ImageOrPrintOptions",array());
$imageFormat = new \DOTNET('mscorlib', 'System.Drawing.Imaging.ImageFormat');
$ptr->Set($imgOptions,'ImageFormat',$imageFormat->Jpeg,array());
$ptr->Set($imgOptions,'OnePagePerSheet',true,array());
$sr = $ptr->New("Aspose.Cells.Rendering.SheetRender",array($sheet,$imgOptions));
$bitmap = new \DOTNET("mscorlib", "System.Drawing.Bitmap");
$bitmap->Save($dataDir . "./SheetImage.jpg");
print "Conversion to Image(s) completed!" . PHP_EOL;
## **Download Running Code**
Download **Worksheet to Image (Aspose.Cells)** from any of the below mentioned social coding sites:
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Plugins/Aspose_Cells_NET_for_PHP/src/aspose/cells/WorkingWithFiles/UtilityFeatures/WorksheetToImage.php)
