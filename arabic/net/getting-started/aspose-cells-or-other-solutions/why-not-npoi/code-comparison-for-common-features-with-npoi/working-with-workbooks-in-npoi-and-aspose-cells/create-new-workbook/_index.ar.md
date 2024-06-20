---
title: إنشاء سجل عمل جديد
type: docs
weight: 20
url: /ar/net/create-new-workbook/
---

## **Aspose.Cells - إنشاء سجل عمل جديد**
تتوفر فئة Workbook للاستخدام البسيط

**C#**

{{< highlight cs >}}

 Workbook workbook = new Workbook(); // Creating a Workbook object

workbook.Save("test.xlsx", SaveFormat.Xlsx); //Workbooks can be saved in many formats

{{< /highlight >}}
## **NPOI - HSSF XSSF - إنشاء سجل عمل جديد**
إنشاء سجل عمل جديد باستخدام فئة Workbook وحفظه باستخدام FileOutputStream

**C#**

{{< highlight cs >}}

 IWorkbook workbook = new XSSFWorkbook();

workbook.CreateSheet("Sheet A1");

workbook.CreateSheet("Sheet A2");

workbook.CreateSheet("Sheet A3");

FileStream sw = File.Create("test.xlsx");

workbook.Write(sw);

sw.Close();

{{< /highlight >}}
## **تحميل رمز التشغيل**
تحميل **إنشاء سجل عمل جديد** من أي من مواقع التعديل الاجتماعي المذكورة أدناه:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/Aspose.Cells_vs_NPOI_1.0/Create.New.Workbook.Aspose.Cells.zip)
