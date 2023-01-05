---
title: Nouvelle ligne au Cells
type: docs
weight: 30
url: /fr/net/new-line-in-cells/
---
## **Aspose.Cells - Nouvelle ligne en Cells**
Pour s'assurer que le texte d'une cellule peut être lu, des sauts de ligne et des retours à la ligne explicites peuvent être appliqués. L'habillage du texte transforme une ligne en plusieurs dans une cellule, que les sauts de ligne explicites placent exactement là où vous le souhaitez.

Pour envelopper du texte dans une cellule, utilisez la propriété Aspose.Cells.Style.IsTextWrapped.

**C#**

{{< highlight "cs" >}}

 Workbook workbook = new Workbook(); // Creating a Workbook object

Worksheet sheet = workbook.Worksheets[0];

sheet.Cells[2,2].Value = "Use \n with word wrap on to create a new line";

//Get Cell's Style

Style style = sheet.Cells[2, 2].GetStyle();

//Set Text Wrap property to true

style.IsTextWrapped = true;

//Set Cell's Style

sheet.Cells[2, 2].SetStyle(style);

workbook.Save("test.xlsx");

{{< /highlight >}}
## **NPOI - HSSF XSSF - Nouvelle ligne au Cells**
CellStyle.setWrapText doit être vrai pour le texte enveloppé.

**C#**

{{< highlight "cs" >}}

 IWorkbook workbook = new XSSFWorkbook();

ISheet sheet = workbook.CreateSheet("Sheet1");

IRow row = sheet.CreateRow(2);

ICell cell = row.CreateCell(2);

cell.SetCellValue("Use \n with word wrap on to create a new line");

//to enable newlines you need set a cell styles with wrap=true

ICellStyle cs = workbook.CreateCellStyle();

cs.WrapText = true;

cell.CellStyle = cs;

FileStream sw = File.Create("test.xlsx");

workbook.Write(sw);

sw.Close();

{{< /highlight >}}
## **Télécharger le code d'exécution**
 Télécharger**Nouvelle ligne au Cells** forment l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/Aspose.Cells_vs_NPOI_1.0/New.Line.In.Cells.Aspose.Cells.zip)

{{% alert color="primary" %}} 

 Pour plus de détails, visitez[Sauts de ligne et retour à la ligne](/cells/fr/net/line-breaks-and-text-wrapping/).

{{% /alert %}}
