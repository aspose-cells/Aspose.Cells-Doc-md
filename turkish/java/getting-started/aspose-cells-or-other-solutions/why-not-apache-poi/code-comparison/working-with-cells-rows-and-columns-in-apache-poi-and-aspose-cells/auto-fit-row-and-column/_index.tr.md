---
title: Satır ve Sütunu Otomatik Sığdır
type: docs
weight: 10
url: /tr/java/auto-fit-row-and-column/
---
## **Aspose.Cells - Satır ve Sütunu Otomatik Sığdır**
Bir satırın genişliğini ve yüksekliğini otomatik olarak boyutlandırmak için en basit yaklaşım, Worksheet.autoFitRow yöntemini çağırmaktır. autoFitRow yöntemi, parametre olarak bir satır dizini (yeniden boyutlandırılacak satırın) alır.

**Lütfen aklınızda bulundurun:**Java'i kullanarak Excel elektronik tablolarındaki satırları ve sütunları otomatik olarak sığdırmak istiyorsanız, lütfen şu adresi ziyaret edin:[Satırları ve Sütunları Otomatik Sığdır](https://docs.aspose.com/cells/java/autofit-rows-and-columns/).

**Java**

{{< highlight "java" >}}

 Workbook workbook = new Workbook("workbook.xls");

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.getWorksheets().get(0);

worksheet.autoFitRow(1); //Auto-fitting the 2nd row of the worksheet

worksheet.autoFitColumn(0); //Auto-fitting the 1st column of the worksheet

//Saving the modified Excel file in default (that is Excel 2003) format

workbook.save("AutoFit_Aspose.xls");


{{< /highlight >}}
## **Apache POI SS - HSSF XSSF - Satır ve Sütunu Otomatik Sığdır**
Apache POI SS - HSSF ve XSSF, sütunları otomatik sığdırmak için Sheet.autoSizeColumn sağlar

**Java**

{{< highlight "java" >}}

 InputStream inStream = new FileInputStream("workbook.xls");

Workbook workbook = WorkbookFactory.create(inStream);

Sheet sheet = workbook.createSheet("new sheet");

sheet.autoSizeColumn(0); //adjust width of the first column

sheet.autoSizeColumn(1); //adjust width of the second column

FileOutputStream fileOut;

fileOut = new FileOutputStream("AutoFit_Apache.xls");

workbook.write(fileOut);

fileOut.close();

{{< /highlight >}}
## **Çalışan Kodu İndir**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Örnek Kodu İndir**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/cellsrowscolumns/autofitrowandcolumn)
