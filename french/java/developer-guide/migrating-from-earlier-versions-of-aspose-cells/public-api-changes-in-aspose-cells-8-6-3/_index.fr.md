---
title: Modifications de l API publique dans Aspose.Cells 8.6.3
type: docs
weight: 230
url: /fr/java/public-api-changes-in-aspose-cells-8-6-3/
---

{{% alert color="primary" %}} 

Ce document décrit les changements apportés à l'API Aspose.Cells de la version 8.6.2 à la version 8.6.3 qui pourraient intéresser les développeurs de modules/applications. Il inclut non seulement les nouvelles méthodes publiques et mises à jour, les classes ajoutées, mais aussi une description de tout changement dans le comportement en arrière-plan dans Aspose.Cells.

{{% /alert %}} 
## **APIs ajoutées**
### **Prise en charge de l'analyse HTML lors de l'importation de données**
Cette version de l'API Aspose.Cells for Java expose l'attribut ImportTableOptions.setHtmlString qui permet à l'API d'analyser les balises HTML lors de l'importation de données sur la feuille de calcul et de définir le résultat analysé comme valeur de cellule. Veuillez noter que les API Aspose.Cells fournissent déjà l'attribut Cell.setHtmlString pour effectuer cette tâche pour une seule cellule, cependant, lors de l'importation de données en vrac, l'attribut ImportTableOptions.setHtmlString (lorsqu'il est défini sur true) tente d'analyser toutes les balises HTML prises en charge et définit les résultats analysés dans les cellules correspondantes.

Voici le scénario d'utilisation le plus simple.

**Java**

{{< highlight csharp >}}

 //create an instance of ImportTableOptions

ImportTableOptions importOptions = new ImportTableOptions();

//Set IsHtmlString to true so that the API can parse the HTML

importOptions.setHtmlString(true);

//Import data from DataTable while passing instance of ImportTableOptions

cells.importData(iTable, 0, 0, importOptions);

{{< /highlight >}}
### **Ajout de la méthode Workbook.createBuiltinStyle**
Aspose.Cells for Java 8.6.3 a exposé la méthode Workbook.createBuiltinStyle qui peut être utilisée pour créer un objet de la classe Style correspondant à l'un des [styles intégrés offerts par l'application Excel](/cells/fr/java/using-built-in-styles/). La méthode Workbook.createBuiltinStyle accepte une constante de l'énumération BuiltinStyleType. Veuillez noter qu'avec les versions précédentes des API Aspose.Cells, la même tâche pouvait être accomplie via la méthode StyleCollection.createBuiltinStyle mais comme les versions récentes des API Aspose.Cells ont supprimé la classe StyleCollection, la méthode Workbook.createBuiltinStyle nouvellement exposée peut être considérée comme une approche alternative pour atteindre le même objectif.

Voici le scénario d'utilisation simple.

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook

//Optionally load a spreadsheet

Workbook book = new Workbook();

//Create a built-in style of type Title

Style style = book.createBuiltinStyle(BuiltinStyleType.TITLE);

{{< /highlight >}}
### **Ajout de la propriété LoadDataOption.OnlyVisibleWorksheet**
Aspose.Cells for Java 8.6.3 a exposé la propriété LoadDataOption.OnlyVisibleWorksheet qui, lorsqu'elle est définie sur true, influencera le mécanisme de chargement de l'API Aspose.Cells for Java, permettant ainsi de charger uniquement les feuilles de calcul visibles d'une feuille de calcul donnée.

Voici le scénario d'utilisation simple.

**Java**

{{< highlight csharp >}}

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
## **APIs obsolètes**
### **Méthode Worksheet.copyConditionalFormatting obsolète**
Comme alternative à la méthode Worksheet.copyConditionalFormatting, il est conseillé d'utiliser l'une des méthodes Cells.copyRows ou Range.copy.
### **Propriété Cells.End obsolète**
Veuillez utiliser la propriété Cells.LastCell en remplacement de la propriété Cells.End.
{{< app/cells/assistant language="java" >}}
