import com.aspose.cells.*;
import java.nio.file.Files;
import java.nio.file.Paths;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);

// Get the target cell C6
Cell cell = worksheet.getCells().get("C6");

// Read the image file into a byte array
byte[] imageData = Files.readAllBytes(Paths.get("logo.png"));

// Embed the image directly into the cell
cell.setEmbeddedImage(imageData);

// Optionally adjust row height and column width so the embedded image is more visible
worksheet.getCells().setColumnWidth(2, 30);   // Column C (index 2)
worksheet.getCells().setRowHeight(5, 100);     // Row 6 (index 5)

// Save the resulting workbook as an .xlsx file
workbook.save("output.xlsx", SaveFormat.XLSX);