+++
title = "Create New Workbook" 
description = "" 
weight = 20602 
+++

Aspose.Cells for Java : Create New Workbook  

# Aspose.Cells for Java : Create New Workbook


## Aspose.Cells - Create New Workbook

`Workbook` class is available for simple use

**Java**

{{< code lang="java" >}}
Workbook workbook = new Workbook(); // Creating a Workbook object
workbook.save("newWorkBook.xlsx", SaveFormat.XLSX); //Workbooks can be saved in many formats
{{< /code >}}

## Apache POI SS - HSSF XSSF - Create New Workbook

Create new Workbook using `Workbook` class and save using `FileOutputStream`.

**Java**

{{< code lang="java" >}}
Workbook wb = new HSSFWorkbook();

FileOutputStream fileOut;
fileOut = new FileOutputStream("newWorkbook.xls");
wb.write(fileOut);
fileOut.close();
{{< /code >}}

## Download Running Code

*   [CodePlex](https://asposecellsjavaapachepoi.codeplex.com/releases/view/618615)
*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)

## Download Sample Code

*   [CodePlex](https://asposecellsjavaapachepoi.codeplex.com/SourceControl/latest#src/main/java/com/aspose/cells/examples/featurescomparison/workbook/createnewworkbook/)
*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/src/main/java/com/aspose/cells/examples/featurescomparison/workbook/createnewworkbook)

For more details, visit [File Handling Features](http://docs.aspose.com:8082/docs/display/cellsjava/File+Handling+Features).

