---
title: Public API Changements dans Aspose.Cells 8.8.2
type: docs
weight: 290
url: /fr/java/public-api-changes-in-aspose-cells-8-8-2/
---
{{% alert color="primary" %}} 

Ce document décrit les modifications apportées au Aspose.Cells API de la version 8.8.1 à 8.8.2 qui peuvent intéresser les développeurs de modules/applications. Il inclut non seulement les méthodes publiques nouvelles et mises à jour, les classes ajoutées et supprimées, etc., mais également une description de tout changement de comportement dans les coulisses de Aspose.Cells.

{{% /alert %}} 
## **API ajoutées**
### **Mettre à jour automatiquement les références lors de la suppression de lignes et de colonnes vides**
 Aspose.Cells for Java 8.8.2 a exposé les versions surchargées des méthodes Cells.deleteBlankRows & Cells.deleteBlankColumns. Les nouvelles méthodes peuvent accepter une instance de la classe DeleteOptions et peuvent être utilisées pour surmonter les situations qui pourraient survenir en raison des références brisées dans les formules, les données des séries de graphiques, etc. La classe DeleteOptions n'a actuellement qu'un seul membre, une propriété de type booléen nommée UpdateReference. Si ladite propriété est définie sur true et que l'instance de la classe DeleteOptions est transmise aux méthodes Cells.deleteBlankRows & Cells.deleteBlankColumns, le API ajustera en interne les références de formule (le cas échéant) pour s'adapter aux modifications.

{{% alert color="primary" %}} 

 Pour plus de détails sur cette fonctionnalité, veuillez consulter l'article détaillé sur[Suppression de lignes et de colonnes vides avec des références mises à jour](/cells/fr/java/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/).

{{% /alert %}} 

Voici le scénario d'utilisation simple.

**Java**

{{< highlight "csharp" >}}

 //Create an instance of Workbook & load an existing spreadsheet

Workbook book = new Workbook(dir + "sample.xlsx");

//Access worksheet from which blank rows/columns have to be deleted

Worksheet sheet = book.getWorksheets().get(0);

//Access cells of the desired worksheet

Cells cells = sheet.getCells();

//Create an instance of DeleteOptions class

DeleteOptions options = new DeleteOptions();

//Set UpdateReference property to true;

options.setUpdateReference(true);

//Delete all blank rows and columns

cells.deleteBlankColumns(options);

cells.deleteBlankRows(options);

{{< /highlight >}}
