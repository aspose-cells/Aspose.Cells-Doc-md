---
title: Habillage du texte Cell
type: docs
weight: 130
url: /fr/net/wrapping-cell-text/
---
{{% alert color="primary" %}}

L'habillage du texte facilite la lecture : une cellule avec du texte enveloppé s'agrandit pour s'adapter au texte afin que le texte ne s'affiche pas par-dessus d'autres cellules.

Avec Aspose.Cells for .NET, les développeurs peuvent effectuer la plupart des tâches dans leurs applications que les utilisateurs peuvent effectuer avec Microsoft Excel, y compris l'habillage du texte dans les cellules. Cet article explique comment et compare la tâche en utilisant VSTO et Aspose.Cells. Aspose.Cells est optimisé pour un codage efficace et fonctionne sans Microsoft Automation.

{{% /alert %}}

## **Habillage du texte Cell**

Pour créer une feuille de calcul avec deux cellules, une avec du texte enveloppé et une sans :

1. Configurez la feuille de calcul :
 1. Créez un classeur.
 1. Accédez à la première feuille de calcul.
1. Ajouter du texte:
 1. Ajoutez du texte à la cellule A1.
 1. Ajoutez du texte enveloppé à la cellule A5.
1. Enregistrez la feuille de calcul.

 Les exemples de code ci-dessous montrent comment effectuer ces étapes à l'aide de[VSTO](/cells/fr/net/wrapping-cell-text/) avec C# ou Visual Basic. Exemples de code qui montrent comment faire la même chose en utilisant[Aspose.Cells for .NET](/cells/fr/net/wrapping-cell-text/), en utilisant à nouveau C# ou Visual Basic suivre immédiatement après.

L'exécution du code donne une feuille de calcul avec deux cellules, une avec du texte qui n'a pas été encapsulé et une avec :

|<p>**Sortie du texte de cellule d'habillage avec VSTO** </p><p>![tâche : image_autre_texte](wrapping-cell-text_1.png)</p>|<p>**Texte de cellule d'emballage de sortie avec Aspose.Cells for .NET** </p><p>![tâche : image_autre_texte](wrapping-cell-text_2.png)</p>|
|:- |:- |

### **Habillage du texte Cell à l'aide de VSTO**

**C#**

{{< highlight "csharp" >}}

 //Note: To help you better, the code uses full namespacing

void WrappingCellText()

{

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

    workbook.SaveAs("f:\\downloads\\OutputVsto.xlsx");

    //Quit the application

    app.Quit();

}

{{< /highlight >}}

### **Habillage du texte Cell avec Aspose.Cells for .NET**

**C#**

{{< highlight "csharp" >}}

 void WrappingCellText()

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

    workbook.Save("f:\\downloads\\OutputAspose.xlsx", SaveFormat.Xlsx);

}

{{< /highlight >}}
