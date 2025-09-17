##Limitations and API Differences
"Aspose.Cells for Python via Java limitations and api differences."
## **Public API Differences**
### **Example**
**Aspose.Cells for Java**
import com.aspose.cells.*;
public class Test1 {
public static void main(String[] args) throws Exception {
Workbook workbook = new Workbook(FileFormatType.XLSX);
workbook.getWorksheets().get(0).getCells().get("A1").putValue("testing...");
workbook.save("wb.xlsx");
}
}
**Aspose.Cells for Python via Java**
import jpype
import asposecells
def run():
kwargs = dict(convertStrings=True)
jpype.startJVM(**kwargs)
from asposecells.api import Workbook, CellsHelper, FileFormatType, License
workbook = Workbook(FileFormatType.XLSX)
workbook .getWorksheets().get(0).getCells().get("A1").putValue("testing...")
workbook .save("wb.xlsx")
jpype.shutdownJVM()
