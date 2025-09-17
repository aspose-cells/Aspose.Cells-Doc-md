##Hello World
## **Aspose.Cells - Hello World**
To Write anything in the Spreadsheet Document using Aspose.Cells for Java in PHP, simply invoke HelloWorld module.
**PHP Code**
# Instantiating a Workbook object that represents a Microsoft Excel file.
$workbook = new Workbook();
\# Note when you create a new workbook, a default worksheet,
\# "Sheet1", is by default added to the workbook.
\# Accessing the first worksheet in the book ("Sheet1").
$sheet = $workbook->getWorksheets()->get(0);
\# Access cell "A1" in the sheet.
$cell = $sheet->getCells()->get("A1");
\# Input the "Hello World!" text into the "A1" cell
$cell->setValue("Hello World!");
\# Saving the modified Excel file in default (that is Excel 2003) format
$file_format_type = new FileFormatType();
$workbook.save($data_dir . "HelloWorld.xls", $file_format_type->EXCEL_97_TO_2003);
print "Document has been saved, please check the output file.";
## **Download Running Code**
Download **Hello World (Aspose.Cells)** from any of the below mentioned social coding sites:
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/quickstart/HelloWorld.php)
