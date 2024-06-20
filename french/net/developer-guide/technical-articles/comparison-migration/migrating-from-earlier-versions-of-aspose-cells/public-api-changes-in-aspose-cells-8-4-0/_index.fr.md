---
title: Modifications de l API publique dans Aspose.Cells 8.4.0
type: docs
weight: 130
url: /fr/net/public-api-changes-in-aspose-cells-8-4-0/
---

{{% alert color="primary" %}} 

Ce document décrit les changements de l'API Aspose.Cells de la version 8.3.2 à la 8.4.0 qui peuvent être intéressants pour les développeurs de modules/applications. Il inclut non seulement les nouvelles méthodes publiques et mises à jour, les classes ajoutées, etc., mais aussi une description de tout changement dans le comportement en coulisses dans Aspose.Cells.

{{% /alert %}} 
## **APIs ajoutées**
### **Mécanisme pour modifier le code VBA/Macro dans les feuilles de calcul**
Afin de fournir la fonctionnalité de Manipulation du Code VBA/Macro, le Aspose.Cells for .NET 8.4.0 a exposé une série de nouvelles classes et propriétés dans l'espace de noms Aspose.Cells.Vba. Quelques détails importants de ces nouvelles classes sont les suivants.

- La classe VbaProject peut être utilisée pour récupérer le projet VBA à partir d'une feuille de calcul donnée.
- La classe VbaModuleCollection représente la collection de modules VBA qui font partie d'un VbaProject donné.
- La classe VbaModule représente un seul module de la VbaModuleCollection.

Le code suivant montre comment modifier dynamiquement les segments de code VBA.

**C#**

{{< highlight csharp >}}

 //Create workbook object from source Excel file

Workbook workbook = new Workbook("source.xlsm");

//Change the VBA Module Code

foreach (VbaModule module in workbook.VbaProject.Modules)

{

    string code = module.Codes;

    //Replace the original message with the modified message

    if (code.Contains("This is test message."))

    {

        code = code.Replace("This is test message.", "This is Aspose.Cells message.");

        module.Codes = code;

    }

}

//Save the output Excel file

workbook.Save("output.xlsm");

{{< /highlight >}}


### **Capacité de supprimer une table de pivot**
Aspose.Cells for .NET 8.4.0 a exposé deux méthodes pour la PivotTableCollection afin de fournir la fonctionnalité de suppression du TCD d'une feuille de calcul donnée. Les détails des méthodes susmentionnées sont les suivants.

- La méthode PivotTableCollection.Remove accepte un objet PivotTable et le supprime de la collection.
- La méthode PivotTableCollection.RemoveAt accepte une valeur entière basée sur un index zéro et supprime le PivotTable particulier de la collection.

Le code suivant montre comment supprimer la table de pivot en utilisant les deux méthodes mentionnées ci-dessus.

**C#**

{{< highlight csharp >}}

 //Create workbook object from source Excel file

Workbook workbook = new Workbook("source.xlsx");

//Access the first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access the first pivot table object

PivotTable pivotTable = worksheet.PivotTables[0];

//Remove pivot table using pivot table object

worksheet.PivotTables.Remove(pivotTable);

//Remove pivot table using pivot table position

worksheet.PivotTables.RemoveAt(0);

//Save the workbook

workbook.Save("output.xlsx");

{{< /highlight >}}


### **Support pour différents agencements de table de pivot**
Aspose.Cells for .NET 8.4.0 fournit le support pour différents mises en page prédéfinies pour les tableaux croisés dynamiques. Pour fournir cette fonctionnalité, les APIs Aspose.Cells ont exposé trois méthodes pour la classe PivotTable comme détaillé ci-dessous.

- La méthode PivotTable.ShowInCompactForm rend le tableau croisé dynamique en disposition compacte.
- La méthode PivotTable.ShowInOutlineForm rend le tableau croisé dynamique en disposition de plan.
- La méthode PivotTable.ShowInTabularForm rend le tableau croisé dynamique en disposition tabulaire.

{{% alert color="primary" %}} 

Il est important d'appeler les méthodes PivotTable.RefreshData & PivotTable.CalculateData après avoir défini l'une des mises en page mentionnées ci-dessus.

{{% /alert %}} 

Le code d'exemple suivant définit différents agencements pour une table de pivot et stocke le résultat sur le disque.

**C#**

{{< highlight csharp >}}

 //Create workbook object from source excel file

Workbook workbook = new Workbook("source.xlsx");

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access first pivot table

PivotTable pivotTable = worksheet.PivotTables[0];

//Render the pivot table in compact form

pivotTable.ShowInCompactForm();

//Refresh the pivot table

pivotTable.RefreshData();

pivotTable.CalculateData();

//Save the output

workbook.Save("CompactForm.xlsx");

//Render the pivot table in outline form

pivotTable.ShowInOutlineForm();

//Refresh the pivot table

pivotTable.RefreshData();

pivotTable.CalculateData();

//Save the output

workbook.Save("OutlineForm.xlsx");

//Render the pivot table in tabular form

pivotTable.ShowInTabularForm();

//Refresh the pivot table

pivotTable.RefreshData();

pivotTable.CalculateData();

//Save the output

workbook.Save("TabularForm.xlsx");

{{< /highlight >}}


### **Classe TxtLoadStyleStrategy & Propriété TxtLoadOptions.LoadStyleStrategy Ajoutées**
Aspose.Cells for .NET 8.4.0 a exposé la classe TxtLoadStyleStrategy et la propriété TxtLoadOptions.LoadStyleStrategy afin de spécifier la stratégie de formatage des valeurs analysées lors de la conversion de valeur de chaîne en nombre ou en date.
### **Méthode DataBar.ToImage ajoutée**
Avec la sortie de la version 8.4.0, l'API Aspose.Cells a fourni la méthode DataBar.ToImage pour enregistrer les barres de données conditionnellement formatées au format image. La méthode {DataBar.ToImage}} accepte deux paramètres comme détaillé ci-dessous.

- Le premier paramètre est de type Cellule Aspose.Cells sur laquelle le formatage conditionnel a été appliqué.
- Le second paramètre est de type ImageOrPrintOptions Aspose.Cells.Rendering pour définir différents paramètres de l'image résultante.

Le code d'exemple suivant montre l'utilisation de la méthode DataBar.ToImage pour rendre la barre de données au format image.

**C#**

{{< highlight csharp >}}

 //Create workbook object from source excel file

Workbook workbook = new Workbook("source.xlsx");

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access the cell which contains conditional formatting databar

Cell cell = worksheet.Cells["C1"];

//Get the conditional formatting of the cell

FormatConditionCollection fcc = cell.GetFormatConditions();

//Access the conditional formatting databar

DataBar dbar = fcc[0].DataBar;

//Create image or print options

ImageOrPrintOptions opts = new ImageOrPrintOptions();

opts.ImageFormat = ImageFormat.Png;

//Get the image bytes of the databar

byte[] imgBytes = dbar.ToImage(cell, opts);

//Write image bytes on the disk

File.WriteAllBytes("databar.png", imgBytes);

{{< /highlight >}}


### **Propriété Border.ThemeColor ajoutée**
Les APIs Aspose.Cells permettent d'extraire des données de formatage liées au thème des feuilles de calcul. Avec la sortie de Aspose.Cells for .NET 8.4.0, l'API a exposé la propriété Border.ThemeColor qui peut être utilisée pour récupérer les attributs de couleur de thème des bordures de cellules.
### **Propriété DrawObject.ImageBytes ajoutée**
Aspose.Cells for .NET 8.4.0 a exposé la propriété DrawObject.ImageBytes pour obtenir les données d'image du graphique ou de la forme.
### **Propriété HtmlSaveOptions.ExportBogusRowData ajoutée**
Aspose.Cells for .NET 8.4.0 a fourni la {HtmlSaveOptions.ExportBogusRowData}} propriété. La propriété de type booléen détermine si l'API injectera des données de ligne basse factice lors de l'exportation de feuilles de calcul au format HTML.

{{% alert color="primary" %}} 

La valeur par défaut est true.

{{% /alert %}} 

L'exemple de code suivant illustre l'utilisation de la propriété susmentionnée.

**C#**

{{< highlight csharp >}}

 //Create an object of HtmlSaveOptions class

HtmlSaveOptions options = new HtmlSaveOptions();

//Set the ExportBogusRowData to true

options.ExportBogusRowData = true;

//Create workbook object from source excel file

Workbook workbook = new Workbook("source.xlsx");

//Save the workbook

workbook.Save("output.xlsx");

{{< /highlight >}}


### **Propriété HtmlSaveOptions.CellCssPrefix ajoutée**
La nouvelle propriété ajoutée HtmlSaveOptions.CellCssPrefix permet de définir le préfixe des fichiers CSS lors de l'exportation des feuilles de calcul au format HTML.

{{% alert color="primary" %}} 

La valeur par défaut est "" (chaîne vide).

{{% /alert %}}
## **API obsolètes**
### **Méthodes Cells.GetCellByIndex & Row.GetCellByIndex obsolètes**
Utilisez la méthode GetEnumerator pour parcourir toutes les cellules à la place.
### **La propriété DrawObject.Image obsolète**
Utilisez la propriété DrawObject.ImageBytes pour obtenir les données de l'image à la place.
