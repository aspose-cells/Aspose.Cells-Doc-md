---
title: إنشاء مصنف جديد
type: docs
weight: 20
url: /ar/net/create-new-workbook/
---
## **Aspose.Cells - إنشاء مصنف جديد**
فئة المصنف متاحة للاستخدام البسيط

**C#**

{{< highlight "cs" >}}

 Workbook workbook = new Workbook(); // Creating a Workbook object

workbook.Save("test.xlsx", SaveFormat.Xlsx); //Workbooks can be saved in many formats

{{< /highlight >}}
## **NPOI - HSSF XSSF - إنشاء كتاب عمل جديد**
قم بإنشاء مصنف جديد باستخدام فئة المصنف وحفظه باستخدام FileOutputStream.

**C#**

{{< highlight "cs" >}}

 IWorkbook workbook = new XSSFWorkbook();

workbook.CreateSheet("Sheet A1");

workbook.CreateSheet("Sheet A2");

workbook.CreateSheet("Sheet A3");

FileStream sw = File.Create("test.xlsx");

workbook.Write(sw);

sw.Close();

{{< /highlight >}}
## **قم بتنزيل كود التشغيل**
 تحميل**إنشاء مصنف جديد** من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/Aspose.Cells_vs_NPOI_1.0/Create.New.Workbook.Aspose.Cells.zip)
