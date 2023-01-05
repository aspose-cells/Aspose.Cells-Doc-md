---
title: Public API Changements dans Aspose.Cells 8.6.3
type: docs
weight: 220
url: /fr/net/public-api-changes-in-aspose-cells-8-6-3/
---
{{% alert color="primary" %}} 

Ce document décrit les modifications apportées au Aspose.Cells API de la version 8.6.2 à 8.6.3 qui peuvent intéresser les développeurs de modules/applications. Il comprend non seulement des méthodes publiques nouvelles et mises à jour, des classes ajoutées, mais également une description de tout changement de comportement en coulisse dans Aspose.Cells.

{{% /alert %}} 
## **API ajoutées**
### **Prise en charge de l'analyse HTML lors de l'importation de données**
Cette version de Aspose.Cells for .NET API a exposé la propriété ImportTableOptions.IsHtmlString qui ordonne au API d'analyser les balises HTML lors de l'importation de données dans la feuille de calcul et de définir le résultat analysé comme valeur de cellule. Veuillez noter que les API Aspose.Cells fournissent déjà le Cell.HtmlString pour effectuer cette tâche pour une seule cellule, cependant, lors de l'importation de données en bloc, comme à partir d'un DataTable, la propriété ImportTableOptions.IsHtmlString (lorsqu'elle est définie sur true) essaie d'analyser tous les pris en charge HTML marque et définit les résultats analysés sur les cellules correspondantes.

Voici le scénario d'utilisation le plus simple.

**C#**

{{< highlight "csharp" >}}

 //create an instance of ImportTableOptions

var importOptions = new ImportTableOptions();

//Set IsHtmlString to true so that the API can parse the HTML

importOptions.IsHtmlString = true;

//Import data from DataTable while passing instance of ImportTableOptions

cells.ImportData(table, 0, 0, importOptions);

{{< /highlight >}}


### **Méthode Workbook.CreateBuiltinStyle ajouté**
 Aspose.Cells for .NET 8.6.3 a exposé la méthode Workbook.CreateBuiltinStyle qui peut être utilisée pour créer un objet de la classe Style qui correspond à l'un des[styles intégrés offerts par l'application Excel](/cells/fr/net/using-built-in-styles/)La méthode Workbook.CreateBuiltinStyle accepte une constante de l'énumération BuiltinStyleType. Veuillez noter qu'avec les versions précédentes des API Aspose.Cells, la même tâche pouvait être accomplie via la méthode StyleCollection.CreateBuiltinStyle, mais comme les versions récentes des API Aspose.Cells ont supprimé la classe StyleCollection, la méthode Workbook.CreateBuiltinStyle nouvellement exposée peut être considérée comme une approche alternative pour réaliser la même chose.

Voici le scénario d'utilisation simple.

**C#**

{{< highlight "csharp" >}}

 //Create an instance of Workbook

//Optionally load a spreadsheet

var book = new Workbook();

//Create a built-in style of type Title

var style = book.CreateBuiltinStyle(BuiltinStyleType.Title);

{{< /highlight >}}


### **Méthode Cells.ImportGridView ajoutée**
Aspose.Cells for .NET 8.6.3 a exposé une version surchargée de Cells.ImportGridView qui peut désormais accepter une instance de ImportTableOptions pour donner plus de contrôle sur le processus d'importation.

Voici le scénario d'utilisation simple.

**C#**

{{< highlight "csharp" >}}

 //Create an instance of Workbook

//Optionally load a spreadsheet

var book = new Workbook();

//Retrieve the Cells collection of first Worksheet in Workbook

var cells = book.Worksheets[0].Cells;

//create an instance of ImportTableOptions & set its various properties

var importOptions = new ImportTableOptions();

importOptions.IsHtmlString = true;

importOptions.IsFieldNameShown = true;

//Import data from GridView while passing instance of ImportTableOptions

cells.ImportGridView(gridView, 0, 0, importOptions);

{{< /highlight >}}


### **Propriété ImportTableOptions.ConvertGridStyle ajoutée**
En référence aux améliorations mentionnées ci-dessus, la dernière version de Aspose.Cells for .NET API a également exposé la propriété ImportTableOptions.ConvertGridStyle. Cette propriété de type booléen permet aux développeurs de contrôler l'apparence des données importées, où la définition de la propriété ImportTableOptions.ConvertGridStyle sur true indique que le API appliquera le style de GridView aux cellules où les données ont été importées.

Voici le scénario d'utilisation simple.

**C#**

{{< highlight "csharp" >}}

 //Create an instance of Workbook

//Optionally load a spreadsheet

var book = new Workbook();

//Retrieve the Cells collection of first Worksheet in Workbook

var cells = book.Worksheets[0].Cells;

//create an instance of ImportTableOptions

var importOptions = new ImportTableOptions();

//Set ConvertGridStyle property to true

importOptions.ConvertGridStyle = true;



//Import data from GridView while passing instance of ImportTableOptions

cells.ImportGridView(gridView, 0, 0, importOptions);

{{< /highlight >}}


### **Propriété LoadDataOption.OnlyVisibleWorksheet ajoutée**
 Aspose.Cells for .NET 8.6.3 a exposé la propriété LoadDataOption.OnlyVisibleWorksheet qui, lorsqu'elle est définie sur true, influencera le mécanisme de chargement de Aspose.Cells for .NET API, par conséquent, seules les feuilles de calcul visibles d'une feuille de calcul donnée seront chargées. S'il vous plaît, vérifiez le[article détaillé](/cells/fr/net/different-ways-to-open-files/) à propos de ce sujet.

Voici le scénario d'utilisation simple.

**C#**

{{< highlight "csharp" >}}

 //Create an instance of LoadDataOption

var loadDataOptions = new LoadDataOption();

//Set OnlyVisibleWorksheet property to true

loadDataOptions.OnlyVisibleWorksheet = true;

//Create an instance of LoadOptions

var loadOptions = new LoadOptions();

//Set LoadDataOptions property to the instance of LoadDataOption created earlier

loadOptions.LoadDataOptions = loadDataOptions;



//Create an instance of Workbook & load an existing spreadsheet

//while passing the instance of LoadOptions created earlier

var book = new Workbook(inputFilePath, loadOptions);

{{< /highlight >}}
## **API obsolètes**
### **Méthode Worksheet.CopyConditionalFormatting obsolète**
Comme alternative à la méthode Worksheet.CopyConditionalFormatting, il est conseillé d'utiliser l'une des méthodes Cells.CopyRows ou Range.Copy.
### **Propriété Cells.Fin Obsolète**
Veuillez utiliser la propriété Cells.LastCell comme alternative à la propriété Cells.End.
