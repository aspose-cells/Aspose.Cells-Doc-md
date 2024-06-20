---
title: Changements d API publics dans Aspose.Cells 8.8.2
type: docs
weight: 290
url: /fr/java/public-api-changes-in-aspose-cells-8-8-2/
---

{{% alert color="primary" %}} 

Ce document décrit les changements de l'API Aspose.Cells de la version 8.8.1 à la 8.8.2 qui peuvent être d'intérêt pour les développeurs de modules/applications. Il comprend non seulement les nouvelles méthodes publiques et mises à jour, les classes ajoutées et supprimées, etc., mais aussi une description de tout changement dans le comportement en coulisses dans Aspose.Cells.

{{% /alert %}} 
## **APIs ajoutées**
### **Mise à jour automatique des références lors de la suppression des lignes et colonnes vides**
Aspose.Cells for Java 8.8.2 a exposé les versions surchargées des méthodes Cells.deleteBlankRows & Cells.deleteBlankColumns. Les nouvelles méthodes peuvent accepter une instance de la classe DeleteOptions et peuvent être utilisées pour surmonter les situations qui pourraient survenir en raison de références rompues dans les formules, les données des séries de graphiques, et ainsi de suite. La classe DeleteOptions a actuellement seulement un membre, une propriété de type booléen nommée UpdateReference. Si ladite propriété est définie sur vrai et que l'instance de la classe DeleteOptions est passée aux méthodes Cells.deleteBlankRows & Cells.deleteBlankColumns, l'API ajustera internalement les références de formule (le cas échéant) pour accommoder les changements. 

{{% alert color="primary" %}} 

Pour plus de détails sur cette fonctionnalité, veuillez consulter l'article détaillé sur [Suppression des lignes et colonnes vides avec des références mises à jour](/cells/fr/java/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/).

{{% /alert %}} 

Voici le scénario d'utilisation simple.

**Java**

{{< highlight csharp >}}

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
