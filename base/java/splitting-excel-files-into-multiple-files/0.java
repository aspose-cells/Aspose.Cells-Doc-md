import com.aspose.cells.*;

String dataDir = "data/";
Workbook workbook = new Workbook(dataDir + "book1.xls");

for (int i = 0; i < workbook.getWorksheets().getCount(); i++)
{
    Worksheet sourceSheet = workbook.getWorksheets().get(i);
    String sheetName = sourceSheet.getName();
    
    Workbook destWorkbook = new Workbook();
    int destIndex = destWorkbook.getWorksheets().add();
    Worksheet destSheet = destWorkbook.getWorksheets().get(destIndex);
    destSheet.setName(sheetName);
    
    destSheet.copy(sourceSheet);
    
    String destFile = dataDir + sheetName + ".xls";
    destWorkbook.save(destFile, SaveFormat.EXCEL_97_TO_2003);
}