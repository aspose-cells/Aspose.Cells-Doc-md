import com.aspose.cells.*;
import java.io.File;

String dataDir = "Data/";
String filePath = new File(new File(dataDir), "example.dbf").getPath();

LoadOptions loadOptions = new LoadOptions(LoadFormat.DBF);

Workbook workbook = new Workbook(filePath, loadOptions);

Worksheet worksheet = workbook.getWorksheets().get(0);

Cells cells = worksheet.getCells();

StringBuilder sb = new StringBuilder();

int maxRow = cells.getMaxDataRow();
int maxCol = cells.getMaxDataColumn();

for (int i = 0; i <= maxRow; i++)
{
    for (int j = 0; j <= maxCol; j++)
    {
        Cell cell = cells.get(i, j);
        String value = cell.getStringValue();
        sb.append("|").append(value);
    }
    sb.append("|").append(System.lineSeparator());
}

System.out.println(sb.toString());

String outputPath = new File(new File(dataDir), "output.xlsx").getPath();
workbook.save(outputPath, SaveFormat.XLSX);

System.out.println("DBF file loaded successfully. Converted XLSX saved at: " + outputPath);