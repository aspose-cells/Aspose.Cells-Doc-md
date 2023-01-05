---
title: Создать новую книгу
type: docs
weight: 20
url: /ru/java/create-new-workbook/
---
## **Aspose.Cells - Создать новую книгу**
Класс Workbook доступен для простого использования

**Java**

{{< highlight "java" >}}

 Workbook workbook = new Workbook(); // Creating a Workbook object

workbook.save("newWorkBook.xlsx", SaveFormat.XLSX); //Workbooks can be saved in many formats

{{< /highlight >}}
## **Apache POI SS — HSSF XSSF — Создать новую книгу**
Создайте новую книгу с помощью класса Workbook и сохраните с помощью FileOutputStream.

**Java**

{{< highlight "java" >}}

 Workbook wb = new HSSFWorkbook();

FileOutputStream fileOut;

fileOut = new FileOutputStream("newWorkbook.xls");

wb.write(fileOut);

fileOut.close();

{{< /highlight >}}
## **Скачать рабочий код**
- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Скачать пример кода**
- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/workbook/createnewworkbook)
