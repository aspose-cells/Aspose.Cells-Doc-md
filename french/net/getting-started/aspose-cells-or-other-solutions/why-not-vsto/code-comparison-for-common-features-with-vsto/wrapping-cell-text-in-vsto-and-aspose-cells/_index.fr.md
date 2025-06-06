---
title: Envelopper le texte de la cellule dans VSTO et Aspose.Cells
type: docs
weight: 250
url: /fr/net/wrapping-cell-text-in-vsto-and-aspose-cells/
---

Pour créer une feuille de calcul avec deux cellules, une avec du texte enveloppé et une sans:

1. Mettez en place la feuille de calcul: 
   1. Créer un classeur.
   1. Accédez à la première feuille de calcul.
1. Ajoutez du texte: 
   1. Ajoutez du texte à la cellule A1.
   1. Ajoutez du texte enveloppé à la cellule A5.
1. Enregistrez la feuille de calcul.
   Les exemples de code ci-dessous montrent comment exécuter ces étapes à l'aide de VSTO avec C#. Des échantillons de code montrant comment faire la même chose en utilisant Aspose.Cells for .NET, encore une fois en utilisant C#, suivent immédiatement après.

L'exécution du code donne comme résultat une feuille de calcul avec deux cellules, l'une ayant un texte qui n'a pas été enveloppé et l'autre qui l'a été:

## **Sortie utilisant VSTO Excel**

![todo:image_alt_text](picture1.png)

## **Sortie en utilisant Aspose.Cells for .NET**

![todo:image_alt_text](picture2.png)

## **VSTO**

{{< highlight csharp >}}

 //Access vsto application

Microsoft.Office.Interop.Excel.Application app = Globals.ThisAddIn.Application;

//Access workbook

Microsoft.Office.Interop.Excel.Workbook workbook = app.ActiveWorkbook;

//Access worksheet

Microsoft.Office.Interop.Excel.Worksheet m_sheet = workbook.Worksheets[1];

//Access vsto worksheet

Microsoft.Office.Tools.Excel.Worksheet sheet = Globals.Factory.GetVstoObject(m_sheet);

//Place some text in cell A1 without wrapping

Microsoft.Office.Interop.Excel.Range cellA1 = sheet.Cells.get_Range("A1");

cellA1.Value = "Sample Text Unwrapped";

//Place some text in cell A5 with wrapping

Microsoft.Office.Interop.Excel.Range cellA5 = sheet.Cells.get_Range("A5");

cellA5.Value = "Sample Text Wrapped";

cellA5.WrapText = true;

//Save the workbook

workbook.SaveAs("OutputVsto.xlsx");

//Quit the application

app.Quit();

{{< /highlight >}}

## **Aspose.Cells**

{{< highlight csharp >}}

 private static void WrappingCellText()

{

	//Create workbook

	Workbook workbook = new Workbook();

	//Access worksheet

	Worksheet worksheet = workbook.Worksheets[0];

	//Place some text in cell A1 without wrapping

	Cell cellA1 = worksheet.Cells["A1"];

	cellA1.PutValue("Some Text Unwrapped");

	//Place some text in cell A5 wrapping

	Cell cellA5 = worksheet.Cells["A5"];

	cellA5.PutValue("Some Text Wrapped");

	Style style = cellA5.GetStyle();

	style.IsTextWrapped = true;

	cellA5.SetStyle(style);

	//Autofit rows

	worksheet.AutoFitRows();

	//Save the workbook

	workbook.Save("OutputAspose.xlsx", SaveFormat.Xlsx);

}

{{< /highlight >}}

## **Télécharger le code source d'exemple**

- [Github](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/Wrapping.Cell.Text.Aspose.Cells.zip)
- [Sourceforge](https://sourceforge.net/projects/asposevsto/files/Aspose.Cells%20Vs%20VSTO%20Excel/Wrapping%20Cell%20Text%20\(Aspose.Cells\).zip/download)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Wrapping%20Cell%20Text%20\(Aspose.Cells\).zip)
{{< app/cells/assistant language="csharp" >}}
