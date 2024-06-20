---
title: Changements dans l API publique dans Aspose.Cells 8.7.1
type: docs
weight: 240
url: /fr/net/public-api-changes-in-aspose-cells-8-7-1/
---

{{% alert color="primary" %}} 

Ce document décrit les changements apportés à l'API Aspose.Cells de la version 8.7.0 à la version 8.7.1 qui peuvent intéresser les développeurs de modules/applications. Il comprend non seulement les nouvelles méthodes publiques et mises à jour, les classes ajoutées et supprimées, mais aussi une description de tout changement dans le comportement en coulisses dans Aspose.Cells.

{{% /alert %}} 
## **APIs ajoutées**
### **Propriété LookInType.OriginalValues ajoutée**
Les API Aspose.Cells prennent déjà en charge la fonctionnalité de [Recherche de données](/cells/fr/net/find-or-search-data/) pour les feuilles de calcul afin de trouver un élément particulier dans la valeur de la cellule et la formule. Cependant, cette fonctionnalité manquait l'aspect de mise en forme appliquée à la cellule qui peut changer l'apparence ainsi que la valeur des contenus, rendant ainsi le texte non recherchable en utilisant la valeur originale. Avec cette version des API Aspose.Cells, une autre constante nommée LookInType.OriginalValues a été exposée à l'API publique ce qui permet de surmonter la situation discutée ci-dessus.

{{% alert color="primary" %}} 

Pour plus de détails sur cette fonctionnalité, veuillez consulter l'article détaillé sur [Recherche de données en utilisant les valeurs originales](/cells/fr/net/search-data-using-original-values/)

{{% /alert %}} 

Voici le scénario d'utilisation simple.

**C#**

{{< highlight csharp >}}

 //Create workbook object

Workbook workbook = new Workbook();

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Add 10 in cell A1 and A2

worksheet.Cells["A1"].PutValue(10);

worksheet.Cells["A2"].PutValue(10);

//Add Sum formula in cell D4 but customize it as ---

Cell cell = worksheet.Cells["D4"];

Style style = cell.GetStyle();

style.Custom = "---";

cell.SetStyle(style);

//The result of formula will be 20

//but 20 will not be visible because

//the cell is formatted as ---

cell.Formula = "=Sum(A1:A2)";

//Calculate the workbook

workbook.CalculateFormula();

//Create find options

FindOptions options = new FindOptions();

options.LookInType = LookInType.OriginalValues;

options.LookAtType = LookAtType.EntireContent;

Cell foundCell = null;

object obj = 20;

//Find 20 which is Sum(A1:A2) and formatted as ---

foundCell = worksheet.Cells.Find(obj, foundCell, options);

//Print the found cell

Console.WriteLine(foundCell);

{{< /highlight >}}


### **Événement OnBeforeColumnFilter ajouté pour GridWeb**
Aspose.Cells.GridWeb pour .NET 8.7.1 a exposé l'événement OnBeforeColumnFilter qui sert de rappel au mécanisme de filtrage effectué à travers l'interface utilisateur de GridWeb. Comme son nom l'indique, l'événement est déclenché avant l'application du filtrage de colonne et peut être utilisé pour obtenir les informations de filtrage telles que l'index de colonne et la valeur sur laquelle le filtre doit être appliqué.

Le scénario d'utilisation simple ressemble à ce qui suit.

**C#**

{{< highlight csharp >}}

 protected void GridWeb1_ColumnFilter(object sender, Aspose.Cells.GridWeb.RowColumnEventArgs e)

{

    string msg = "Column index: " + (e.Num) + ", Filtered Value:" + e.Argument;

}

{{< /highlight >}}

{{% alert color="primary" %}} 

Do not forget to register the event to GridWeb control <acw:gridweb OnBeforeColumnFilter="GridWeb1_ColumnFilter"/>

{{% /alert %}}
