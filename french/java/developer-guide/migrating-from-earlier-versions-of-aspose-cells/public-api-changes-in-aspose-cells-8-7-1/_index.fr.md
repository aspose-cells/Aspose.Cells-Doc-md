---
title: Changements dans l API publique dans Aspose.Cells 8.7.1
type: docs
weight: 250
url: /fr/java/public-api-changes-in-aspose-cells-8-7-1/
---

{{% alert color="primary" %}} 

Ce document décrit les changements apportés à l'API Aspose.Cells de la version 8.7.0 à la version 8.7.1 qui peuvent intéresser les développeurs de modules/applications. Il comprend non seulement les nouvelles méthodes publiques et mises à jour, les classes ajoutées et supprimées, mais aussi une description de tout changement dans le comportement en coulisses dans Aspose.Cells.

{{% /alert %}} 
## **APIs ajoutées**
### **Propriété LookInType.ORIGINAL_VALUES ajoutée**
Les APIs Aspose.Cells prennent déjà en charge la fonction [Rechercher ou Rechercher des Données](/cells/fr/java/find-or-search-data/) pour les feuilles de calcul afin de trouver un contenu particulier dans la valeur de la cellule et la formule. Cependant, cette fonctionnalité était dépourvue de l'aspect de mise en forme appliquée à la cellule qui peut modifier l'apparence ainsi que la valeur du contenu, rendant ainsi le texte non recherchable en utilisant la valeur d'origine. Avec cette version des APIs Aspose.Cells, une autre constante du nom de LookInType.ORIGINAL_VALUES a été exposée à l'API publique, ce qui permet de surmonter la situation discutée ci-dessus. 

{{% alert color="primary" %}} 

Pour plus de détails sur cette fonctionnalité, veuillez consulter l'article détaillé sur [Rechercher des Données en Utilisant les Valeurs d'Origine](https://docs.aspose.com/cells/java/search-data-using-original-values/)

{{% /alert %}} 

Voici le scénario d'utilisation simple.

**Java**

{{< highlight csharp >}}

 //Create workbook object

Workbook workbook = new Workbook();

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Add 10 in cell A1 and A2

worksheet.getCells().get("A1").putValue(10);

worksheet.getCells().get("A2").putValue(10);

//Add Sum formula in cell D4 but customize it as ---

Cell cell = worksheet.getCells().get("D4");

Style style = cell.getStyle();

style.setCustom("---");

cell.setStyle(style);

//The result of formula will be 20

//but 20 will not be visible because

//the cell is formated as ---

cell.setFormula("=Sum(A1:A2)");

//Calculate the workbook

workbook.calculateFormula();

//Create find options

FindOptions options = new FindOptions();

options.setLookInType(LookInType.ORIGINAL_VALUES);

options.setLookAtType(LookAtType.ENTIRE_CONTENT);

Cell foundCell = null;

Object obj = 20;

//Find 20 which is Sum(A1:A2) and formatted as ---

foundCell = worksheet.getCells().find(obj, foundCell, options);

//Print the found cell

System.out.println(foundCell);

{{< /highlight >}}
