---
title: Neue Arbeitsmappe erstellen
type: docs
weight: 20
url: /de/java/create-new-workbook/
---
## **Aspose.Cells – Neue Arbeitsmappe erstellen**
Die Workbook-Klasse ist für die einfache Verwendung verfügbar

**Java**

{{< highlight "java" >}}

 Workbook workbook = new Workbook(); // Creating a Workbook object

workbook.save("newWorkBook.xlsx", SaveFormat.XLSX); //Workbooks can be saved in many formats

{{< /highlight >}}
## **Apache POI SS - HSSF XSSF - Neue Arbeitsmappe erstellen**
Erstellen Sie eine neue Arbeitsmappe mit der Workbook-Klasse und speichern Sie sie mit FileOutputStream.

**Java**

{{< highlight "java" >}}

 Workbook wb = new HSSFWorkbook();

FileOutputStream fileOut;

fileOut = new FileOutputStream("newWorkbook.xls");

wb.write(fileOut);

fileOut.close();

{{< /highlight >}}
## **Laufcode herunterladen**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Beispielcode herunterladen**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/workbook/createnewworkbook)
