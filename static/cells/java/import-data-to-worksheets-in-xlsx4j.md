##Import Data to Worksheets in xlsx4j
## **Aspose.Cells - Import Data to Worksheets**
Import Data from Arrays
**Java**
//Instantiating a Workbook object
Workbook workbook = new Workbook();
//Obtaining the reference of the newly added worksheet by passing its sheet index
int sheetIndex = workbook.getWorksheets().add();
Worksheet worksheet= workbook.getWorksheets().get(sheetIndex);
//==================================================
//Creating an array containing names as string values
String[] names = new String[]{"laurence chen", "roman korchagin", "kyle huang"};
//Importing the array of names to 1st row and first column vertically
Cells cells = worksheet.getCells();
cells.importArray(names,0,0,false);
Import Data from ArrayList
**Java**
ArrayList<String> list = new ArrayList<String>();
//Add few names to the list as string values
list.add("laurence chen");
list.add("roman korchagin");
list.add("kyle huang");
//Importing the contents of ArrayList to 1st row and first column vertically
cells.importArrayList(list,2,0,true);
//==================================================
//Saving the Excel file
workbook.save(dataDir + "AsposeDataImport.xls");
## **Download Running Code**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **Download Sample Code**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/datahandling/importdatatoworksheets/AsposeImportDataToWorksheets.java)
