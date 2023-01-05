---
title: Public API Changements dans Aspose.Cells 8.7.1
type: docs
weight: 240
url: /fr/net/public-api-changes-in-aspose-cells-8-7-1/
---
{{% alert color="primary" %}} 

Ce document décrit les modifications apportées au Aspose.Cells API de la version 8.7.0 à 8.7.1 qui peuvent intéresser les développeurs de modules/applications. Il inclut non seulement les méthodes publiques nouvelles et mises à jour, les classes ajoutées et supprimées, etc., mais également une description de tout changement de comportement dans les coulisses de Aspose.Cells.

{{% /alert %}} 
## **API ajoutées**
### **Ajout de la propriété LookInType.OriginalValues**
 Aspose.Cells Les API prennent déjà en charge le[Rechercher ou rechercher des données](/cells/fr/net/find-or-search-data/)fonctionnalité pour les feuilles de calcul afin de trouver un contenu particulier dans la valeur et la formule de la cellule. Cependant, il manquait à cette fonctionnalité l'aspect du formatage appliqué à la cellule qui peut modifier l'apparence ainsi que la valeur du contenu, rendant par conséquent le texte impossible à rechercher en utilisant la valeur d'origine. Avec cette version des API Aspose.Cells, une autre constante du nom LookInType.OriginalValues a été exposée au public API, ce qui permet de surmonter la situation décrite ci-dessus.

{{% alert color="primary" %}} 

 Pour plus de détails sur cette fonctionnalité, veuillez consulter l'article détaillé sur[Rechercher des données à l'aide des valeurs d'origine](/cells/fr/net/search-data-using-original-values/)

{{% /alert %}} 

Voici le scénario d'utilisation simple.

**C#**

{{< highlight "csharp" >}}

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


### **Ajout de l'événement OnBeforeColumnFilter pour GridWeb**
Aspose.Cells.GridWeb for .NET 8.7.1 a exposé l'événement OnBeforeColumnFilter qui sert de rappel au mécanisme de filtrage effectué via l'interface utilisateur GridWeb. Comme son nom l'indique, l'événement est déclenché avant l'application du filtrage de colonne et peut être utilisé pour obtenir les informations de filtrage telles que l'index de colonne et la valeur sur laquelle le filtre doit être appliqué.

Le scénario d'utilisation simple se présente comme suit.

**C#**

{{< highlight "csharp" >}}

 protected void GridWeb1_ColumnFilter(object sender, Aspose.Cells.GridWeb.RowColumnEventArgs e)

{

    string msg = "Column index: " + (e.Num) + ", Filtered Value:" + e.Argument;

}

{{< /highlight >}}

{{% alert color="primary" %}} 

N'oubliez pas d'enregistrer l'événement au contrôle GridWeb<acw:gridweb OnBeforeColumnFilter="GridWeb1_ColumnFilter"/>

{{% /alert %}}
