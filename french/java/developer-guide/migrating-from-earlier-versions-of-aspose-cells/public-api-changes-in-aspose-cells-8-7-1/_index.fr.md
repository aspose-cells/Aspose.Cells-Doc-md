---
title: Public API Changements dans Aspose.Cells 8.7.1
type: docs
weight: 250
url: /fr/java/public-api-changes-in-aspose-cells-8-7-1/
---
{{% alert color="primary" %}} 

Ce document décrit les modifications apportées au Aspose.Cells API de la version 8.7.0 à 8.7.1 qui peuvent intéresser les développeurs de modules/applications. Il inclut non seulement les méthodes publiques nouvelles et mises à jour, les classes ajoutées et supprimées, etc., mais également une description de tout changement de comportement dans les coulisses de Aspose.Cells.

{{% /alert %}} 
## **API ajoutées**
### **Ajout de la propriété LookInType.ORIGINAL_VALUES**
 Aspose.Cells Les API prennent déjà en charge le[Rechercher ou rechercher des données](/cells/fr/java/find-or-search-data/)fonctionnalité pour les feuilles de calcul afin de trouver un contenu particulier dans la valeur et la formule de la cellule. Cependant, il manquait à cette fonctionnalité l'aspect du formatage appliqué à la cellule qui peut modifier l'apparence ainsi que la valeur du contenu, rendant par conséquent le texte impossible à rechercher en utilisant la valeur d'origine. Avec cette version des API Aspose.Cells, une autre constante du nom LookInType.ORIGINAL_VALUES a été exposée au public API, ce qui permet de surmonter la situation décrite ci-dessus.

{{% alert color="primary" %}} 

 Pour plus de détails sur cette fonctionnalité, veuillez consulter l'article détaillé sur[Rechercher des données à l'aide des valeurs d'origine](https://docs.aspose.com/cells/java/search-data-using-original-values/)

{{% /alert %}} 

Voici le scénario d'utilisation simple.

**Java**

{{< highlight "csharp" >}}

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
