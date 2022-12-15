---
title: قم بتعيين عامل تكبير ورقة العمل
type: docs
weight: 80
url: /ar/net/set-worksheet-zoom-factor/
---
## **Aspose.Cells - تعيين عامل تكبير ورقة العمل**
**C#**

{{< highlight "cs" >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Adding a new worksheet to the Workbook object

WorksheetCollection worksheets = workbook.Worksheets;

Worksheet worksheet = worksheets.Add("My Worksheet");

worksheet.Zoom = 75;

//Saving the Excel file

workbook.Save("../../data/newWorksheet.xls");


{{< /highlight >}}
## **NPOI - HSSF XSSF - تعيين عامل تكبير ورقة العمل**
**C#**

{{< highlight "cs" >}}

 IWorkbook wb = new XSSFWorkbook();

ISheet sheet1 = wb.CreateSheet("First Sheet");

sheet1.SetZoom(3, 4); // 75 percent

FileStream sw = File.Create("../../data/newWorksheet.xls");

wb.Write(sw);

sw.Close();

{{< /highlight >}}
## **تحميل كود الجري**
 تحميل**قم بتعيين عامل تكبير ورقة العمل** من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/Aspose.Cells_Vs_NPOI_HWPF_and_XWPF_v1.2/Zoom.Factor.zip)

{{% alert color="primary" %}} 

 لمزيد من التفاصيل ، قم بزيارة[العمل مع أوراق العمل](/cells/ar/net/working-with-worksheets-in-npoi-and-aspose-cells/).

{{% /alert %}}
