---
title: Recherche des antécédents et des personnes à charge au Aspose.Cells
type: docs
weight: 130
url: /fr/net/tracing-precedents-and-dependents-in-aspose-cells/
---
{{% alert color="primary" %}} 

Les feuilles de calcul financières complexes, en particulier celles développées en collaboration, peuvent cacher les erreurs les plus embarrassantes. Vérifier l'exactitude des formules et trouver la source d'une erreur peut être difficile lorsque la formule utilise des cellules précédentes et des cellules dépendantes.

- **Cellules précédentes** sont des cellules référencées par une formule dans un autre Cell. Par exemple, si la cellule D10 contient la formule =B5, la cellule B5 est un précédent de la cellule D10.
- **Cellules dépendantes** contiennent des formules faisant référence à d'autres cellules. Par exemple, si la cellule D10 contient la formule =B5, la cellule D10 dépend de la cellule B5.

Pour faciliter la lecture de la feuille de calcul, vous souhaiterez peut-être indiquer clairement quelles cellules d'une feuille de calcul sont utilisées dans une formule. De même, vous souhaiterez peut-être extraire les cellules dépendantes d'autres cellules.

Aspose.Cells vous permet de tracer des cellules et de découvrir lesquelles sont liées.

{{% /alert %}} 
## **Traçage précédent et dépendant Cells : Microsoft Excel**
Les formules peuvent changer en fonction des modifications apportées par un client. Par exemple, si la cellule C1 dépend de C3 et C4 contenant une formule et que C1 est modifiée (la formule est donc remplacée), C3 et C4, ou d'autres cellules, doivent être modifiées pour équilibrer la feuille de calcul en fonction des règles métier.

De même, supposons que C1 contienne la formule "=(B1*22)/(M2*N32)". Je veux trouver les cellules dont dépend C1, c'est-à-dire les cellules précédentes B1, M2 et N32.

Vous devrez peut-être tracer la dépendance d'une cellule particulière à d'autres cellules. Si des règles métier sont intégrées dans des formules, nous aimerions découvrir la dépendance et exécuter certaines règles basées sur celle-ci. De même, si la valeur d'une cellule particulière est modifiée, quelles cellules de la feuille de calcul sont impactées par ce changement ?

Microsoft Excel permet aux utilisateurs de retracer les antécédents et les personnes à charge.

1.  Sur le**Afficher la barre d'outils** , sélectionner**Audit de formule**.
 La boîte de dialogue Audit de formule s'affiche.
   **La boîte de dialogue Audit de formule** 

![tâche : image_autre_texte](tracing-precedents-and-dependents-in-aspose-cells_1.png)

1. Tracez des précédents :
1. Sélectionnez la cellule contenant la formule pour laquelle vous souhaitez rechercher des cellules précédentes.
 1. Pour afficher une flèche de suivi sur chaque cellule qui fournit directement des données à la cellule active, cliquez sur**Tracer des précédents** sur le**Audit de formule** barre d'outils.
1. Formules de trace qui font référence à une cellule particulière (dépendants)
 1. Sélectionnez la cellule pour laquelle vous souhaitez identifier les cellules dépendantes.
 1. Pour afficher une flèche de suivi sur chaque cellule qui dépend de la cellule active, cliquez sur Tracer les dépendants dans la barre d'outils Audit de formule.
## **Recherche de précédent et de personne à charge Cells : Aspose.Cells**
### **Retrouver les précédents**
Aspose.Cells facilite l'obtention de cellules précédentes. Non seulement il peut récupérer des cellules qui fournissent des données à des précédents de formules simples, mais également trouver des cellules qui fournissent des données à des précédents de formules complexes avec des plages nommées.

Dans l'exemple ci-dessous, un modèle de fichier Excel, Book1.xls, est utilisé. La feuille de calcul contient des données et des formules sur la première feuille de calcul.

**La feuille de calcul d'entrée** 

![tâche : image_autre_texte](tracing-precedents-and-dependents-in-aspose-cells_2.png)

Aspose.Cells fournit la méthode GetPrecedents de la classe Cell utilisée pour tracer les précédents d'une cellule. Elle renvoie une ReferredAreaCollection. Comme vous pouvez le voir ci-dessus, dans Book1.xls, la cellule B7 contient une formule "=SUM(A1:A3)". Ainsi, les cellules A1: A3 sont les cellules précédentes à la cellule B7. L'exemple suivant illustre la fonctionnalité de suivi des précédents à l'aide du fichier de modèle Book1.xls.

**C#**

{{< highlight "csharp" >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook("book1.xls");

Cells cells = workbook.Worksheets[0].Cells;

Aspose.Cells.Cell cell = cells["B7"];

//Tracing precedents of the cell B7.

//The return array contains ranges and cells.

ReferredAreaCollection ret = cell.GetPrecedents();

//Printing all the precedent cells' name.

if(ret != null)

{

  for(int m = 0 ; m < ret.Count; m++)

  {

    ReferredArea area = ret[m];

    StringBuilder stringBuilder = new StringBuilder();

    if (area.IsExternalLink)

    {

        stringBuilder.Append("[");

        stringBuilder.Append(area.ExternalFileName);

        stringBuilder.Append("]");

     }

     stringBuilder.Append(area.SheetName);

     stringBuilder.Append("!");

     stringBuilder.Append(CellsHelper.CellIndexToName(area.StartRow, area.StartColumn));

     if (area.IsArea)

      {

          stringBuilder.Append(":");

          stringBuilder.Append(CellsHelper.CellIndexToName(area.EndRow, area.EndColumn));

      }


      Console.WriteLine(stringBuilder.ToString());

   }

}



{{< /highlight >}}
### **Recherche des personnes à charge**
Aspose.Cells vous permet d'obtenir des cellules dépendantes dans des feuilles de calcul. Aspose.Cells peut non seulement récupérer des cellules qui fournissent des données concernant une formule simple, mais également trouver des cellules qui fournissent des données à une formule complexe dépendante avec des plages nommées.

Aspose.Cells fournit la méthode GetDependents de la classe Cell utilisée pour tracer les personnes à charge d'une cellule. Par exemple, dans Book1.xlsx, il existe des formules : "=A1+20" et "=A1+30" dans les cellules B2 et C2 respectivement. L'exemple suivant montre comment tracer les personnes à charge pour la cellule A1 à l'aide du fichier de modèle Book1.xlsx.

**C#**

{{< highlight "csharp" >}}

 string path = "Book1.xlsx";

Workbook workbook = new Workbook(path);

Worksheet worksheet = workbook.Worksheets[0];

var c = worksheet.Cells["A1"];

var dependents = c.GetDependents(true);

foreach (var dependent in dependents)

{

     Debug.WriteLine(string.Format("{0} ---- {1} : {2}", dependent.Worksheet.Name, dependent.Name, dependent.Value));

}

{{< /highlight >}}
## **Télécharger le code d'exécution**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Tracing%20Precedents%20and%20Dependents)
## **Télécharger l'exemple de code**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)

