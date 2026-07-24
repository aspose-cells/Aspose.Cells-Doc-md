import com.aspose.cells.*;
import java.io.File;
import java.util.GregorianCalendar;

String outputDir = "C:\\Output\\";
String filePath = new File(new File(outputDir), "output.dbf").getPath();

if (!new File(outputDir).exists())
{
    new File(outputDir).mkdirs();
}

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
Cells cells = worksheet.getCells();

// Column headers
cells.get(0, 0).putValue("ID");
cells.get(0, 1).putValue("Name");
cells.get(0, 2).putValue("Department");
cells.get(0, 3).putValue("Salary");
cells.get(0, 4).putValue("HireDate");

// Data row 1
cells.get(1, 0).putValue(101);
cells.get(1, 1).putValue("John Smith");
cells.get(1, 2).putValue("Engineering");
cells.get(1, 3).putValue(75000.50);
cells.get(1, 4).putValue(new GregorianCalendar(2020, 2, 15).getTime());

// Data row 2
cells.get(2, 0).putValue(102);
cells.get(2, 1).putValue("Jane Doe");
cells.get(2, 2).putValue("Marketing");
cells.get(2, 3).putValue(68000.75);
cells.get(2, 4).putValue(new GregorianCalendar(2019, 6, 22).getTime());

// Data row 3
cells.get(3, 0).putValue(103);
cells.get(3, 1).putValue("Bob Johnson");
cells.get(3, 2).putValue("Finance");
cells.get(3, 3).putValue(82000.00);
cells.get(3, 4).putValue(new GregorianCalendar(2021, 0, 10).getTime());

// Data row 4
cells.get(4, 0).putValue(104);
cells.get(4, 1).putValue("Alice Brown");
cells.get(4, 2).putValue("Human Resources");
cells.get(4, 3).putValue(71000.25);
cells.get(4, 4).putValue(new GregorianCalendar(2018, 10, 5).getTime());

// Data row 5
cells.get(5, 0).putValue(105);
cells.get(5, 1).putValue("Charlie Wilson");
cells.get(5, 2).putValue("Operations");
cells.get(5, 3).putValue(79500.80);
cells.get(5, 4).putValue(new GregorianCalendar(2022, 4, 30).getTime());

// Set column widths for better readability
worksheet.getCells().setColumnWidth(0, 8);
worksheet.getCells().setColumnWidth(1, 20);
worksheet.getCells().setColumnWidth(2, 20);
worksheet.getCells().setColumnWidth(3, 12);
worksheet.getCells().setColumnWidth(4, 14);

workbook.save(filePath, SaveFormat.DBF);