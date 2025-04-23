---
title: Copier la feuille de calcul
type: docs
weight: 40
url: /fr/net/copy-worksheet/
---

## **Aspose.Cells - Copier la feuille de calcul**
**C#**

{{< highlight cs >}}

 //Create a new Workbook by excel file path

Workbook wb = new Workbook("../../data/workbook.xlsx");

//Create a Worksheets object with reference to the sheets of the Workbook.

WorksheetCollection sheets = wb.Worksheets;

//Copy data to a new sheet from an existing sheet within the Workbook.

sheets.AddCopy("Sheet1");

wb.Save("../../data/workbook.xlsx");


{{< /highlight >}}
## **NPOI - HSSF XSSF - Copier la feuille de calcul**
**C#**

{{< highlight cs >}}

 IWorkbook wb = new XSSFWorkbook();

wb.CreateSheet("new sheet");

wb.CreateSheet("second sheet");

ISheet cloneSheet = wb.CloneSheet(0);

FileStream sw = File.Create("newWorksheet.xls");

wb.Write(sw);

sw.Close();


{{< /highlight >}}
## **Télécharger le code en cours d'exécution**
Télécharger le formulaire **Copier la feuille de calcul** à partir de l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/Aspose.Cells_Vs_NPOI_HWPF_and_XWPF_v1.2/Copy.Worksheet.zip)

{{% alert color="primary" %}} 

Pour plus de détails, visitez [Travailler avec les feuilles de calcul](/cells/fr/net/working-with-worksheets-in-npoi-and-aspose-cells/).

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
