---
title: Travailler avec les en têtes et pieds de page
type: docs
weight: 110
url: /fr/net/working-with-headers-and-footers/
---

## **Aspose.Cells - Travailler avec les en-têtes et pieds de page**
**C#**

{{< highlight cs >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Adding a new worksheet to the Workbook object

WorksheetCollection worksheets = workbook.Worksheets;

Worksheet worksheet = worksheets.Add("My Worksheet");

//Obtaining the reference of the PageSetup of the worksheet

PageSetup pageSetup = worksheet.PageSetup;

//Setting worksheet name at the left  header

pageSetup.SetHeader(0, "&A");

//Setting current date and current time at the central header

//and changing the font of the header

pageSetup.SetHeader(1, "&\"Times New Roman,Bold\"&D-&T");

//Setting current file name at the right header and changing the font of the header

pageSetup.SetHeader(2, "&\"Times New Roman,Bold\"&12&F");

//Setting a string at the left footer and changing the font of the footer

pageSetup.SetFooter(0, "Hello World! &\"Courier New\"&14 123");

//Setting picture at the central footer

pageSetup.SetFooter(1, "&G");

workbook.Save("../../data/headerfooter.xlsx");


{{< /highlight >}}
## **NPOI - HSSF XSSF - Travailler avec les en-têtes et pieds de page**
**C#**

{{< highlight cs >}}

 IWorkbook wb = new XSSFWorkbook();

ISheet sheet1 = wb.CreateSheet("First Sheet");

IHeader header = sheet1.Header;

header.Center = "Center Header";

header.Left = "Left Header";

header.Right = "Right Header";            

FileStream sw = File.Create("../../data/header.xls");

wb.Write(sw);

sw.Close(); 

{{< /highlight >}}
## **Télécharger le code en cours d'exécution**
Téléchargez **Travailler avec les en-têtes et pieds de page** à partir de l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/Aspose.Cells_Vs_NPOI_HWPF_and_XWPF_v1.2/Headers.and.Footers.zip)

{{% alert color="primary" %}} 

Pour plus de détails, visitez [Travailler avec les feuilles de calcul](/cells/fr/net/working-with-worksheets-in-npoi-and-aspose-cells/).

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
