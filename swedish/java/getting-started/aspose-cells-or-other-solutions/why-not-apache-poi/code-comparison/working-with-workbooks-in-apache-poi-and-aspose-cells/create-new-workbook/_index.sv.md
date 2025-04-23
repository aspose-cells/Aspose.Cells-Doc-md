---
title: Skapa ny arbetsbok
type: docs
weight: 20
url: /sv/java/create-new-workbook/
---

## **Aspose.Cells - Skapa ny arbetsbok**
Workbook-klass är tillgänglig för enkel användning

**Java**

{{< highlight java >}}

 Workbook workbook = new Workbook(); // Creating a Workbook object

workbook.save("newWorkBook.xlsx", SaveFormat.XLSX); //Workbooks can be saved in many formats

{{< /highlight >}}
## **Apache POI SS - HSSF XSSF - Skapa ny arbetsbok**
Skapa ny arbetsbok med hjälp av Workbook-klassen och spara med FileOutputStream.

**Java**

{{< highlight java >}}

 Workbook wb = new HSSFWorkbook();

FileOutputStream fileOut;

fileOut = new FileOutputStream("newWorkbook.xls");

wb.write(fileOut);

fileOut.close();

{{< /highlight >}}
## **Ladda ned körbar kod**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Ladda ned provkoden**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/workbook/createnewworkbook)
{{< app/cells/assistant language="java" >}}
