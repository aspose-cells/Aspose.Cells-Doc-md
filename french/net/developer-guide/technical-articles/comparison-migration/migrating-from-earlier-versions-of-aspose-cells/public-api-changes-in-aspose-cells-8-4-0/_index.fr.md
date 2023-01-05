---
title: Public API Changements dans Aspose.Cells 8.4.0
type: docs
weight: 130
url: /fr/net/public-api-changes-in-aspose-cells-8-4-0/
---
{{% alert color="primary" %}} 

Ce document décrit les modifications apportées au Aspose.Cells API de la version 8.3.2 à 8.4.0 qui peuvent intéresser les développeurs de modules/applications. Il comprend non seulement des méthodes publiques nouvelles et mises à jour,[classes ajoutées, etc.](/cells/fr/net/public-api-changes-in-aspose-cells-8-4-0/) et[classes supprimées, etc.](/cells/fr/net/public-api-changes-in-aspose-cells-8-4-0/), mais aussi une description de tout changement de comportement dans les coulisses du Aspose.Cells.

{{% /alert %}} 
## **API ajoutées**
### **Mécanisme pour modifier le code VBA/Macro dans les feuilles de calcul**
 Afin de fournir la fonctionnalité de[Manipulation de code VBA/macro](/cells/fr/net/modifying-vba-or-macro-code-using-aspose-cells/), le Aspose.Cells for .NET 8.4.0 a exposé une série de nouvelles classes et propriétés dans l'espace de noms Aspose.Cells.Vba. Voici quelques-uns des détails importants de ces nouvelles classes.

- La classe VbaProject peut être utilisée pour récupérer le projet VBA à partir d'une feuille de calcul donnée.
- La classe VbaModuleCollection représente la collection de modules VBA qui font partie d'un VbaProject donné.
- La classe VbaModule représente un seul module de VbaModuleCollection.

L'extrait de code suivant montre comment modifier dynamiquement les segments de code VBA.

**C#**

{{< highlight "csharp" >}}

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


### **Possibilité de supprimer le tableau croisé dynamique**
Aspose.Cells for .NET 8.4.0 a exposé deux méthodes pour la PivotTableCollection afin de fournir la fonctionnalité de suppression du tableau croisé dynamique d'une feuille de calcul donnée. Les détails des procédés susmentionnés sont les suivants.

- La méthode PivotTableCollection.Remove accepte un objet de PivotTable et le supprime de la collection.
- La méthode PivotTableCollection.RemoveAt accepte une valeur entière basée sur un index zéro et supprime le tableau croisé dynamique particulier de la collection.

L'extrait de code suivant montre comment supprimer le tableau croisé dynamique à l'aide des deux méthodes mentionnées ci-dessus.

**C#**

{{< highlight "csharp" >}}

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


### **Prise en charge de différentes dispositions de tableau croisé dynamique**
Aspose.Cells for .NET 8.4.0 prend en charge différentes dispositions prédéfinies pour les tableaux croisés dynamiques. Afin de fournir cette fonctionnalité, les API Aspose.Cells ont exposé trois méthodes pour la classe PivotTable, comme détaillé ci-dessous.

- La méthode PivotTable.ShowInCompactForm restitue le tableau croisé dynamique dans la disposition compacte.
- La méthode PivotTable.ShowInOutlineForm restitue le tableau croisé dynamique dans la disposition Plan.
- La méthode PivotTable.ShowInTabularForm restitue le tableau croisé dynamique dans la disposition tabulaire.

{{% alert color="primary" %}} 

Il est important d'appeler PivotTable.RefreshData & PivotTable.CalculateData après avoir défini l'une des dispositions mentionnées ci-dessus.

{{% /alert %}} 

L'exemple de code suivant définit différentes dispositions pour un tableau croisé dynamique et stocke le résultat sur disque.

**C#**

{{< highlight "csharp" >}}

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


### **Classe TxtLoadStyleStrategy et propriété TxtLoadOptions.LoadStyleStrategy ajoutée**
Aspose.Cells for .NET 8.4.0 a exposé la classe TxtLoadStyleStrategy et la propriété TxtLoadOptions.LoadStyleStrategy afin de spécifier la stratégie de formatage des valeurs analysées lors de la conversion de la valeur de chaîne en nombre ou en date/heure.
### **Méthode DataBar.ToImage ajoutée**
Avec la version v8.4.0, le Aspose.Cells API a fourni la méthode DataBar.ToImage pour enregistrer les DataBars formatés de manière conditionnelle au format image. La méthode {DataBar.ToImage}} accepte deux paramètres comme détaillé ci-dessous.

- Le premier paramètre est de type Aspose.Cells.Cell sur lequel une mise en forme conditionnelle a été appliquée.
- Le deuxième paramètre est de type Aspose.Cells.Rendering.ImageOrPrintOptions afin de définir différents paramètres de l'image résultante.

L'exemple de code suivant illustre l'utilisation de la méthode DataBar.ToImage pour restituer la DataBar au format image.

**C#**

{{< highlight "csharp" >}}

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

byte[]imgBytes = dbar.ToImage(cell, opts);

//Write image bytes on the disk

File.WriteAllBytes("databar.png", imgBytes);

{{< /highlight >}}


### **Propriété Border.ThemeColor ajoutée**
Aspose.Cells Les API permettent d'extraire des données de formatage liées au thème des feuilles de calcul. Avec la sortie de Aspose.Cells for .NET 8.4.0, le API a exposé la propriété Border.ThemeColor qui peut être utilisée pour récupérer les attributs de couleur de thème des bordures Cell.
### **Propriété DrawObject.ImageBytes ajoutée**
Aspose.Cells for .NET 8.4.0 a exposé la propriété DrawObject.ImageBytes pour obtenir les données d'image de Chart ou Shape.
### **Propriété HtmlSaveOptions.ExportBogusRowData ajoutée**
Aspose.Cells for .NET 8.4.0 a fourni la propriété {HtmlSaveOptions.ExportBogusRowData}}. La propriété de type booléen détermine si API injectera de fausses données de ligne inférieure lors de l'exportation de la feuille de calcul au format HTML.

{{% alert color="primary" %}} 

La valeur par défaut est true.

{{% /alert %}} 

L'exemple de code suivant illustre l'utilisation de la propriété susmentionnée.

**C#**

{{< highlight "csharp" >}}

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
La propriété nouvellement ajoutée HtmlSaveOptions.CellCssPrefix permet de définir le préfixe pour les fichiers CSS lors de l'exportation des feuilles de calcul au format HTML.

{{% alert color="primary" %}} 

La valeur par défaut est "" (chaîne vide).

{{% /alert %}}
## **API obsolètes**
### **Méthodes Cells.GetCellByIndex & Row.GetCellByIndex Obsolète**
Utilisez la méthode GetEnumerator pour itérer toutes les cellules à la place.
### **Propriété DrawObject.Image Obsolète**
Utilisez plutôt la propriété DrawObject.ImageBytes pour obtenir des données d'image.
