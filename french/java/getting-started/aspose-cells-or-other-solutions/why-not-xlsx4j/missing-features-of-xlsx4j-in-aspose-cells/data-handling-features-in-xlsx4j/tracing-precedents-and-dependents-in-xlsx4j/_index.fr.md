---
title: Traçage des précédents et des personnes à charge dans xlsx4j
type: docs
weight: 70
url: /fr/java/tracing-precedents-and-dependents-in-xlsx4j/
---
## **Aspose.Cells - Recherche des antécédents et des personnes à charge**
Les feuilles de calcul financières complexes, en particulier celles développées en collaboration, peuvent cacher les erreurs les plus embarrassantes. Vérifier l'exactitude des formules et trouver la source d'une erreur peut être difficile lorsque la formule utilise des cellules précédentes et des cellules dépendantes.

- **Cellules précédentes**sont des cellules référencées par une formule dans un autre Cell. Par exemple, si la cellule D10 contient la formule =B5, la cellule B5 est un précédent de la cellule D10.
- **Cellules dépendantes**contiennent des formules faisant référence à d'autres cellules. Par exemple, si la cellule D10 contient la formule =B5, la cellule D10 dépend de la cellule B5.

Pour faciliter la lecture de la feuille de calcul, vous souhaiterez peut-être indiquer clairement quelles cellules d'une feuille de calcul sont utilisées dans une formule. De même, vous souhaiterez peut-être extraire les cellules dépendantes d'autres cellules.

Aspose.Cells vous permet de tracer des cellules et de découvrir lesquelles sont liées.

Retrouver les précédents

**Java**

{{< highlight "java" >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook(dataDir + "workbook.xls");

Cells cells = workbook.getWorksheets().get(0).getCells();

Cell cell = cells.get("A12");

//Tracing precedents of the cell A12.

//The return array contains ranges and cells.

ReferredAreaCollection ret = cell.getPrecedents();

//Printing all the precedent cells' name.

if(ret != null)

{

  for(int m = 0 ; m < ret.getCount(); m++)

  {

    ReferredArea area = ret.get(m);

    StringBuilder stringBuilder = new StringBuilder();

    if (area.isExternalLink())

    {

        stringBuilder.append("[");

        stringBuilder.append(area.getExternalFileName());

        stringBuilder.append("]");

     }

     stringBuilder.append(area.getSheetName());

     stringBuilder.append("!");

     stringBuilder.append(CellsHelper.cellIndexToName(area.getStartRow(), area.getStartColumn()));

     if (area.isArea())

      {

          stringBuilder.append(":");

          stringBuilder.append(CellsHelper.cellIndexToName(area.getEndRow(), area.getEndColumn()));

      }

      System.out.println("Tracing Precedents: " + stringBuilder.toString());

   }

}

{{< /highlight >}}

Recherche des personnes à charge

**Java**

{{< highlight "java" >}}

 // Récupère la cellule A1

Cell c = cellules.get("A5");

// Récupère toutes les personnes à charge de la cellule A5

Cell[]dépendants = c.getDependents(true);

pour (int je = 0; je< dependents.length; i++)

{

     System.out.println("Tracing Dependents: " + dependents[i].getWorksheet().getName() +dependents[i].getName() + ":" + dependents[i].getIntValue());

}

{{< /highlight >}}
## **Télécharger le code d'exécution**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **Télécharger l'exemple de code**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/datahandling/tracingprecedentsanddependents/AsposeTracingPrecedentsAndDependents.java)

{{% alert color="primary" %}} 

 Pour plus de détails, visitez[Recherche des antécédents et des personnes à charge](/java/tracing-precedents-and-dependents).

{{% /alert %}}
