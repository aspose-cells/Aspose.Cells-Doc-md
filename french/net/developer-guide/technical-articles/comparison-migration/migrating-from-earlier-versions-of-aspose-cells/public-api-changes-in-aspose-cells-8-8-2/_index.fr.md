---
title: Changements d API publics dans Aspose.Cells 8.8.2
type: docs
weight: 280
url: /fr/net/public-api-changes-in-aspose-cells-8-8-2/
---

{{% alert color="primary" %}} 

Ce document décrit les changements de l'API Aspose.Cells de la version 8.8.1 à la 8.8.2 qui peuvent être d'intérêt pour les développeurs de modules/applications. Il comprend non seulement les nouvelles méthodes publiques et mises à jour, les classes ajoutées et supprimées, etc., mais aussi une description de tout changement dans le comportement en coulisses dans Aspose.Cells.

{{% /alert %}} 
## **APIs ajoutées**
### **Mise à jour automatique des références lors de la suppression des lignes et colonnes vides**
Aspose.Cells for .NET 8.8.2 a exposé les versions surchargées des méthodes Cells.DeleteBlankRows & Cells.DeleteBlankColumns. Les nouvelles méthodes peuvent accepter une instance de la classe DeleteOptions et peuvent être utilisées pour surmonter les situations qui pourraient survenir en raison des références brisées dans les formules, les données de séries de graphiques, etc. La classe DeleteOptions a actuellement un seul membre, une propriété de type Boolean nommée UpdateReference. Si ladite propriété est définie sur true et que l'instance de la classe DeleteOptions est passée aux méthodes Cells.DeleteBlankRows & Cells.DeleteBlankColumns, l'API ajustera automatiquement les références des formules (le cas échéant) pour accommoder les changements.

{{% alert color="primary" %}} 

Pour plus de détails sur cette fonction, veuillez consulter l'article détaillé sur [Suppression des lignes et colonnes vides avec des références mises à jour](/cells/fr/net/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/).

{{% /alert %}} 

Voici le scénario d'utilisation simple.

**C#**

{{< highlight csharp >}}

 //Create an instance of Workbook & load an existing spreadsheet

var book = new Workbook(dir + "sample.xlsx");

//Access worksheet from which blank rows/columns have to be deleted

var sheet = book.Worksheets[0];

//Access cells of the desired worksheet

var cells = sheet.Cells;

//Create an instance of DeleteOptions class

DeleteOptions options = new DeleteOptions();

//Set UpdateReference property to true;

options.UpdateReference = true;

//Delete all blank rows and columns

cells.DeleteBlankColumns(options);

cells.DeleteBlankRows(options);

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
