---
title: إنشاء سجل عمل جديد
type: docs
weight: 20
url: /ar/java/create-new-workbook/
---

## **Aspose.Cells - إنشاء سجل عمل جديد**
تتوفر فئة Workbook للاستخدام البسيط

**Java**

{{< highlight java >}}

 Workbook workbook = new Workbook(); // Creating a Workbook object

workbook.save("newWorkBook.xlsx", SaveFormat.XLSX); //Workbooks can be saved in many formats

{{< /highlight >}}
## **Apache POI SS - HSSF XSSF - إنشاء سجل عمل جديد**
إنشاء سجل عمل جديد باستخدام فئة Workbook وحفظه باستخدام FileOutputStream

**Java**

{{< highlight java >}}

 Workbook wb = new HSSFWorkbook();

FileOutputStream fileOut;

fileOut = new FileOutputStream("newWorkbook.xls");

wb.write(fileOut);

fileOut.close();

{{< /highlight >}}
## **تحميل رمز التشغيل**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **تحميل رمز عينة**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/workbook/createnewworkbook)
