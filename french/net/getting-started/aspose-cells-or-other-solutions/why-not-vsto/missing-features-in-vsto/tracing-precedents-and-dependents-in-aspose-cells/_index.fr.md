---
title: Suivi des précédents et des dépendances dans Aspose.Cells
type: docs
weight: 130
url: /fr/net/tracing-precedents-and-dependents-in-aspose-cells/
---

{{% alert color="primary" %}} 

Les feuilles de calcul financières complexes, en particulier celles développées en collaboration, peuvent cacher les erreurs les plus gênantes. Vérifier la précision des formules et trouver la source d'une erreur peut être difficile lorsque la formule utilise des cellules précédentes et des cellules dépendantes.

- **Cellules précédentes** sont des cellules auxquelles une formule d'une autre cellule fait référence. Par exemple, si la cellule D10 contient la formule =B5, la cellule B5 est une cellule précédente de la cellule D10.
- **Cellules dépendantes** contiennent des formules qui font référence à d'autres cellules. Par exemple, si la cellule D10 contient la formule =B5, la cellule D10 est une dépendance de la cellule B5.

Pour rendre la feuille de calcul facile à lire, vous voudrez peut-être clairement indiquer quelles cellules d'une feuille de calcul sont utilisées dans une formule. De même, vous voudrez peut-être extraire les cellules dépendantes d'autres cellules.

Aspose.Cells vous permet de tracer les cellules et de savoir lesquelles sont liées.

{{% /alert %}} 
## **Tracer les cellules précédentes et dépendantes : Microsoft Excel**
Les formules peuvent changer en fonction des modifications apportées par un client. Par exemple, si la cellule C1 dépend des cellules C3 et C4 contenant une formule, et que C1 est modifiée (de sorte que la formule est remplacée), C3 et C4, ou d'autres cellules, doivent changer pour équilibrer la feuille de calcul en fonction des règles commerciales.

De même, supposons que C1 contienne la formule "=(B1*22)/(M2*N32)". Je veux trouver les cellules dont C1 dépend, c'est-à-dire les cellules précédentes B1, M2 et N32.

Vous pourriez avoir besoin de tracer la dépendance d'une cellule particulière à d'autres cellules. Si les règles commerciales sont intégrées dans les formules, nous aimerions découvrir la dépendance et exécuter certaines règles en fonction de cela. De même, si la valeur d'une cellule particulière est modifiée, quelles cellules dans la feuille de calcul sont impactées par ce changement?

Microsoft Excel permet aux utilisateurs de tracer les cellules précédentes et dépendantes.

1. Sur la **Barre d'outils Affichage**, sélectionnez **Audit de formules**.
   La boîte de dialogue Audit de formules s'affiche. 
   **La boîte de dialogue Audit de formules** 

![todo:image_alt_text](tracing-precedents-and-dependents-in-aspose-cells_1.png)

1. Tracer les cellules précédentes :
   1. Sélectionnez la cellule contenant la formule pour laquelle vous souhaitez trouver les cellules précédentes.
   1. Pour afficher une flèche de traçage vers chaque cellule qui fournit directement des données à la cellule active, cliquez sur **Tracer les cellules précédentes** sur la **Barre d'outils Audit de formules**.
1. Tracer les formules qui référencent une cellule particulière (dépendantes)
   1. Sélectionnez la cellule pour laquelle vous souhaitez identifier les cellules dépendantes.
   1. Pour afficher une flèche de traçage vers chaque cellule qui dépend de la cellule active, cliquez sur Traçage des dépendances sur la barre d'outils d'Audit de formules.
## **Tracer les cellules précédentes et dépendantes : Aspose.Cells**
### **Tracer les cellules précédentes**
Aspose.Cells facilite l'obtention des cellules précédentes. Non seulement peut-il récupérer les cellules qui fournissent des données à des précédents de formule simples mais aussi trouver les cellules qui fournissent des données à des précédents de formule complexes avec des plages nommées.

Dans l'exemple ci-dessous, un fichier excel modèle, Book1.xls, est utilisé. La feuille de calcul contient des données et des formules sur la première feuille de calcul.

**La feuille de calcul d'entrée** 

![todo:image_alt_text](tracing-precedents-and-dependents-in-aspose-cells_2.png)

Aspose.Cells fournit la méthode GetPrecedents de la classe Cell utilisée pour tracer les précédents d'une cellule. Elle renvoie un ReferredAreaCollection. Comme vous pouvez le voir ci-dessus, dans Book1.xls, la cellule B7 contient la formule "=SUM(A1:A3)". Ainsi, les cellules A1:A3 sont les cellules précédentes de la cellule B7. L'exemple suivant présente la fonction de traçage des précédents en utilisant le fichier modèle Book1.xls.

**C#**

{{< highlight csharp >}}

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
### **Tracé des dépendances**
Aspose.Cells vous permet d'obtenir les cellules dépendantes dans des feuilles de calcul. Aspose.Cells peut non seulement récupérer les cellules fournissant des données concernant une formule simple, mais aussi trouver les cellules fournissant des données aux dépendances d'une formule complexe avec des plages nommées.

Aspose.Cells fournit la méthode GetDependents de la classe Cell utilisée pour tracer les dépendances d'une cellule. Par exemple, dans Book1.xlsx, il y a les formules : "=A1+20" et "=A1+30" dans les cellules B2 et C2 respectivement. L'exemple suivant démontre comment tracer les dépendances pour la cellule A1 en utilisant le fichier modèle Book1.xlsx.

**C#**

{{< highlight csharp >}}

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
## **Télécharger le code en cours d'exécution**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Tracing%20Precedents%20and%20Dependents)
## **Télécharger le code source d'exemple**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)

{{< app/cells/assistant language="csharp" >}}
