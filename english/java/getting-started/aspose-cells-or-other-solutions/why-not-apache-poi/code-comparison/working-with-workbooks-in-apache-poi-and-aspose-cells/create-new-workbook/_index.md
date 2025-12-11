---
title: Create New Workbook
type: docs
weight: 20
url: /java/create-new-workbook/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Aspose.Cells - Create New Workbook**
The Workbook class is available for simple use.

**Java**

{{< highlight java >}}
Workbook workbook = new Workbook(); // Creating a Workbook object

workbook.save("newWorkBook.xlsx", SaveFormat.XLSX); // Workbooks can be saved in many formats
{{< /highlight >}}

## **Apache POI SS - HSSF XSSF - Create New Workbook**
Create a new workbook using the Workbook class and save it using `FileOutputStream`.

**Java**

{{< highlight java >}}
Workbook wb = new HSSFWorkbook();

FileOutputStream fileOut;

fileOut = new FileOutputStream("newWorkbook.xls");

wb.write(fileOut);

fileOut.close();
{{< /highlight >}}

## **Download Running Code**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)

## **Download Sample Code**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/workbook/createnewworkbook)

{{< app/cells/assistant language="java" >}}
