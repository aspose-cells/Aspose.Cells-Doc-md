---
title: Public API Changements dans Aspose.Cells 8.6.3
type: docs
weight: 230
url: /fr/java/public-api-changes-in-aspose-cells-8-6-3/
---
{{% alert color="primary" %}} 

Ce document décrit les modifications apportées au Aspose.Cells API de la version 8.6.2 à 8.6.3 qui peuvent intéresser les développeurs de modules/applications. Il comprend non seulement des méthodes publiques nouvelles et mises à jour, des classes ajoutées, mais également une description de tout changement de comportement en coulisse dans Aspose.Cells.

{{% /alert %}} 
## **API ajoutées**
### **Prise en charge de l'analyse HTML lors de l'importation de données**
Cette version de Aspose.Cells for Java API a exposé l'attribut ImportTableOptions.setHtmlString qui demande au API d'analyser les balises HTML lors de l'importation de données dans la feuille de calcul et de définir le résultat analysé comme valeur de cellule. Veuillez noter que les API Aspose.Cells fournissent déjà l'attribut Cell.setHtmlString pour effectuer cette tâche pour une seule cellule, cependant, lors de l'importation de données en bloc, l'attribut ImportTableOptions.setHtmlString (lorsqu'il est défini sur true) essaie d'analyser toutes les balises et ensembles HTML pris en charge. les résultats analysés dans les cellules correspondantes.

Voici le scénario d'utilisation le plus simple.

**Java**

{{< highlight "csharp" >}}

 //create an instance of ImportTableOptions

ImportTableOptions importOptions = new ImportTableOptions();

//Set IsHtmlString to true so that the API can parse the HTML

importOptions.setHtmlString(true);

//Import data from DataTable while passing instance of ImportTableOptions

cells.importData(iTable, 0, 0, importOptions);

{{< /highlight >}}
### **Méthode Workbook.createBuiltinStyle ajoutée**
Aspose.Cells for Java 8.6.3 a exposé la méthode Workbook.createBuiltinStyle qui peut être utilisée pour créer un objet de la classe Style qui correspond à l'un des[styles intégrés offerts par l'application Excel](/cells/fr/java/using-built-in-styles/). La méthode Workbook.createBuiltinStyle accepte une constante de l'énumération BuiltinStyleType. Veuillez noter qu'avec les versions précédentes des API Aspose.Cells, la même tâche pouvait être accomplie via la méthode StyleCollection.createBuiltinStyle, mais comme les versions récentes des API Aspose.Cells ont supprimé la classe StyleCollection, la méthode Workbook.createBuiltinStyle nouvellement exposée peut être considérée comme une approche alternative pour réaliser la même chose.

Voici le scénario d'utilisation simple.

**Java**

{{< highlight "csharp" >}}

 //Create an instance of Workbook

//Optionally load a spreadsheet

Workbook book = new Workbook();

//Create a built-in style of type Title

Style style = book.createBuiltinStyle(BuiltinStyleType.TITLE);

{{< /highlight >}}
### **Propriété LoadDataOption.OnlyVisibleWorksheet ajoutée**
Aspose.Cells for Java 8.6.3 a exposé la propriété LoadDataOption.OnlyVisibleWorksheet qui, lorsqu'elle est définie sur true, influencera le mécanisme de chargement de Aspose.Cells for Java API, par conséquent, seules les feuilles de calcul visibles d'une feuille de calcul donnée seront chargées.

Voici le scénario d'utilisation simple.

**Java**

{{< highlight "csharp" >}}

 //Create an instance of LoadDataOption

LoadDataOption loadDataOptions = new LoadDataOption();

//Set OnlyVisibleWorksheet property to true

loadDataOptions.setOnlyVisibleWorksheet(true);

//Create an instance of LoadOptions

LoadOptions loadOptions = new LoadOptions();

//Set LoadDataOptions property to the instance of LoadDataOption created earlier

loadOptions.setLoadDataOptions(loadDataOptions);

//Create an instance of Workbook & load an existing spreadsheet

//while passing the instance of LoadOptions created earlier

Workbook book = new Workbook(inputFilePath, loadOptions);

{{< /highlight >}}
## **API obsolètes**
### **Méthode Worksheet.copyConditionalFormatting obsolète**
Comme alternative à la méthode Worksheet.copyConditionalFormatting, il est conseillé d'utiliser l'une des méthodes Cells.copyRows ou Range.copy.
### **Propriété Cells.Fin Obsolète**
Veuillez utiliser la propriété Cells.LastCell comme alternative à la propriété Cells.End.
