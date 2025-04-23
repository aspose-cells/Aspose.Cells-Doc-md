---
title: Fusionner ou scinder des cellules dans une feuille de calcul
type: docs
weight: 40
url: /fr/net/merge-or-unmerge-cells-in-a-worksheet/
---

{{% alert color="primary" %}}

Lorsque vous travaillez avec des feuilles de calcul, vous avez souvent besoin de créer un titre / en-tête dans une seule cellule qui s'étend sur le dessus de votre feuille de calcul. Vous pourriez être en train de créer une facture et vouloir moins de colonnes pour le total ou les valeurs de résumé. Lorsque vous souhaitez fusionner une cellule à partir de deux cellules ou plus, vous fusionnez les cellules. Nous effectuons la tâche à l'aide de VSTO et Aspose.Cells for .NET de manière indépendante.

{{% /alert %}}

## **Description**

Ouvrir un fichier Excel existant, fusionner certaines cellules dans la première feuille de calcul du classeur et enregistrer le fichier Excel.

## **Fusion de cellules**

Voici les extraits de code parallèles pour VSTO (C#, VB) et Aspose.Cells for .NET (C#, VB).

### **1) VSTO**

**C#**

{{< highlight csharp >}}

 .......



using Microsoft.VisualStudio.Tools.Applications.Runtime;

using Excel = Microsoft.Office.Interop.Excel;

using Office = Microsoft.Office.Core;

using System.Reflection;

.......

//Instantiate the Application object.

Excel.Application excelApp = new Excel.ApplicationClass();

//Specify the template excel file path.

string myPath=@"d:\test\MyBook.xls";

//Open the excel file.

excelApp.Workbooks.Open(myPath, Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value);

//Get the range of cells i.e.., A1:C1.

Excel.Range rng1 = excelApp.get_Range("A1", "C1");

//Merge the cells.

rng1.Merge(Missing.Value);

//Save the file.

excelApp.ActiveWorkbook.Save();

//Quit the Application.

excelApp.Quit();



{{< /highlight >}}

### **2) Aspose.Cells for .NET**

**C#**

{{< highlight csharp >}}

 .......

using Aspose.Cells;

.......

//Instantiate a new Workbook.

Workbook workbook = new Workbook();

//Specify the template excel file path.

string myPath=@"d:\test\MyBook.xls";

//Open the excel file.

workbook.Open(myPath);

//Get the range of cells i.e.., A1:C1.

Aspose.Cells.Range rng1 = workbook.Worksheets[0].Cells.CreateRange("A1", "C1");

//Merge the cells.

rng1.Merge();

//Save the file.

workbook.Save(@"d:\test\MyBook.xls");



{{< /highlight >}}

## **Défusionner les cellules**

Pour défusionner la ou les cellule(s), utilisez les lignes de code suivantes pour VSTO (C#, VB) et Aspose.Cells for .NET (C#, VB).

### **1) VSTO**

**C#**

{{< highlight csharp >}}

 //Get the A1 cell (Merged Cell).

Excel.Range rng1 = excelApp.get_Range("A1", Missing.Value);

//UnMerge the cell.

rng1.UnMerge();     



{{< /highlight >}}

### **2) Aspose.Cells for .NET**

**C#**

{{< highlight csharp >}}

 //Get the A1 cell (Merged Cell).

Cells rng1 = workbook.Worksheets[0].Cells;

//UnMerge the cell.

rng1.UnMerge(0, 0, 1, 3); 

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
