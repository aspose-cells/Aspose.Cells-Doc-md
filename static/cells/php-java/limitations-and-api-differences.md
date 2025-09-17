##Limitations and API Differences
"Aspose.Cells for PHP via Java limitations and api differences."
## **Public API Differences**
The following list (with sample code segments) shows some differences between Aspose.Cells for Java and Aspose.Cells for PHP via Java APIs.
### **Importing library (Package Comparisons)**
**Aspose.Cells for Java**
import com.aspose.cells.*;
**Aspose.Cells for PHP via Java**
require_once("Java.inc");
require_once("lib/aspose.cells.php");
use aspose\cells;
use aspose\cells\Workbook;
### **Instantiating a new Workbook**
**Aspose.Cells for Java**
Workbook workbook = new Workbook();
**Aspose.Cells for PHP via Java**
$workbook = new Workbook();
### **Enums or Constants**
**Aspose.Cells for Java**
arc2.getLineFormat().setDashStyle(MsoLineDashStyle.SOLID);
**Aspose.Cells for PHP via Java**
$arc2->getLineFormat()->setDashStyle(cells\MsoLineDashStyle::SOLID);
### **Example**
**Aspose.Cells for Java**
import com.aspose.cells.*;
public class Test1 {
/**
* @param args
*/
public static void main(String[] args) throws Exception {
Workbook workbook = new Workbook();
WorksheetCollection worksheets = workbook.getWorksheets();
Worksheet worksheet = worksheets.get(0);
Cell cell = worksheet.getCells().get("A1");
cell.putValue("Hello World!");
workbook.save("out1.xlsx");
}
}
**Aspose.Cells for PHP via Java**
require_once("Java.inc");
require_once("lib/aspose.cells.php");
use aspose\cells;
use aspose\cells\Workbook;
use aspose\cells\WorsheetCollection;
use aspose\cells\Worksheet;
use aspose\cells\Cell;
$workbook = new Workbook();
$worksheets = $workbook->getWorksheets();
$worksheet = $worksheets->get(0);
$cell = $worksheet->getCells()->get("A1");
$cell->putValue("Hello World!");
$workbook->save("out1.xlsx");
?>
## **Other Limitations of Aspose.Cells for PHP via Java API compared to Aspose.Cells for Java API**
1. Importing/exporting data from an Array, ArrayList, ResultSet etc. is not supported.
1. Printing is not supported.
