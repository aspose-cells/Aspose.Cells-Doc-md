---
title: Modifications de l API publique dans Aspose.Cells 8.6.3
type: docs
weight: 220
url: /fr/net/public-api-changes-in-aspose-cells-8-6-3/
---

{{% alert color="primary" %}} 

Ce document décrit les changements apportés à l'API Aspose.Cells de la version 8.6.2 à la version 8.6.3 qui pourraient intéresser les développeurs de modules/applications. Il inclut non seulement les nouvelles méthodes publiques et mises à jour, les classes ajoutées, mais aussi une description de tout changement dans le comportement en arrière-plan dans Aspose.Cells.

{{% /alert %}} 
## **APIs ajoutées**
### **Prise en charge de l'analyse HTML lors de l'importation de données**
Cette version de l'API Aspose.Cells for .NET a exposé la propriété ImportTableOptions.IsHtmlString qui dirige l'API pour analyser les balises HTML lors de l'importation des données sur la feuille de calcul et définir le résultat analysé comme valeur de la cellule. Veuillez noter que les API Aspose.Cells fournissent déjà Cell.HtmlString pour effectuer cette tâche pour une seule cellule, cependant, lors de l'importation de données en masse telles que d'un DataTable, la propriété ImportTableOptions.IsHtmlString (lorsqu'elle est définie sur true) tente d'analyser toutes les balises HTML prises en charge et définit les résultats analysés dans les cellules correspondantes.

Voici le scénario d'utilisation le plus simple.

**C#**

{{< highlight csharp >}}

 //create an instance of ImportTableOptions

var importOptions = new ImportTableOptions();

//Set IsHtmlString to true so that the API can parse the HTML

importOptions.IsHtmlString = true;

//Import data from DataTable while passing instance of ImportTableOptions

cells.ImportData(table, 0, 0, importOptions);

{{< /highlight >}}


### **Méthode Workbook.CreateBuiltinStyle ajoutée**
La version 8.6.3 de Aspose.Cells for .NET a exposé la méthode Workbook.CreateBuiltinStyle qui peut être utilisée pour créer un objet de la classe Style qui correspond à l'un des [styles intégrés offerts par l'application Excel](/cells/fr/net/using-built-in-styles/). La méthode Workbook.CreateBuiltinStyle accepte une constante de l'énumération BuiltinStyleType. Veuillez noter qu'avec les versions précédentes des API Aspose.Cells, la même tâche pouvait être accomplie via la méthode StyleCollection.CreateBuiltinStyle, mais comme les versions récentes des API Aspose.Cells ont supprimé la classe StyleCollection, la méthode Workbook.CreateBuiltinStyle nouvellement exposée peut être considérée comme une approche alternative pour réaliser la même tâche.

Voici le scénario d'utilisation simple.

**C#**

{{< highlight csharp >}}

 //Create an instance of Workbook

//Optionally load a spreadsheet

var book = new Workbook();

//Create a built-in style of type Title

var style = book.CreateBuiltinStyle(BuiltinStyleType.Title);

{{< /highlight >}}


### **Méthode Cells.ImportGridView ajoutée**
Aspose.Cells for .NET 8.6.3 a exposé une version surchargée de Cells.ImportGridView qui peut maintenant accepter une instance de ImportTableOptions pour donner plus de contrôle sur le processus d'importation.

Voici le scénario d'utilisation simple.

**C#**

{{< highlight csharp >}}

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
En référence aux améliorations mentionnées ci-dessus, la dernière version de l'API Aspose.Cells for .NET a également exposé la propriété ImportTableOptions.ConvertGridStyle. Cette propriété de type booléen permet aux développeurs de contrôler l'apparence des données importées, où le fait de paramétrer la propriété ImportTableOptions.ConvertGridStyle sur true indique que l'API appliquera le style de la GridView aux cellules où les données ont été importées.

Voici le scénario d'utilisation simple.

**C#**

{{< highlight csharp >}}

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
Aspose.Cells for .NET 8.6.3 a exposé la propriété LoadDataOption.OnlyVisibleWorksheet qui, lorsqu'elle est réglée sur true, influencera le mécanisme de chargement de l'API Aspose.Cells for .NET, en conséquence seules les feuilles de calcul visibles d'une feuille de calcul donnée seront chargées. Veuillez consulter l'article détaillé sur ce sujet.

Voici le scénario d'utilisation simple.

**C#**

{{< highlight csharp >}}

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
## **APIs obsolètes**
### **Méthode Worksheet.CopyConditionalFormatting obsolète**
En alternative à la méthode Worksheet.CopyConditionalFormatting, il est conseillé d'utiliser l'une des méthodes Cells.CopyRows ou Range.Copy.
### **Propriété Cells.End obsolète**
Veuillez utiliser la propriété Cells.LastCell en remplacement de la propriété Cells.End.
