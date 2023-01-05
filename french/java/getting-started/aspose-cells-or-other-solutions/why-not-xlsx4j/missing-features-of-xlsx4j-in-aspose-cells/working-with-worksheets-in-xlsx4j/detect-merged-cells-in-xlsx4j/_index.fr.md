---
title: Détecter fusionné Cells dans xlsx4j
type: docs
weight: 20
url: /fr/java/detect-merged-cells-in-xlsx4j/
---
## **Aspose.Cells - Détecter fusionné Cells**
Dans Microsoft Excel, plusieurs cellules peuvent être fusionnées en une seule. Ceci est souvent utilisé pour créer des tableaux complexes ou pour créer une cellule contenant un en-tête qui s'étend sur plusieurs colonnes.
Aspose.Cells vous permet d'identifier les zones de cellules fusionnées dans une feuille de calcul. Vous pouvez également les dissocier.

**Java**

{{< highlight "java" >}}

 //Get the merged cells list to put it into the arraylist object

ArrayList<CellArea> al = worksheet.getCells().getMergedCells();

//Define cellarea

CellArea ca;

//Define some variables

int frow, fcol, erow, ecol;

// Print Message

System.out.println("Merged Areas: \n"+ al.toString());

//Loop through the arraylist and get each cellarea to unmerge it

for(int i = al.size()-1 ; i > -1; i--)

{

	ca = new CellArea();

	ca = (CellArea)al.get(i);

	frow = ca.StartRow;

	fcol = ca.StartColumn;

	erow = ca.EndRow;

	ecol = ca.EndColumn;

	System.out.println((i+1) + ". [" + fcol +"," + frow +"] " + "[" + ecol +"," + erow +"]");

	worksheet.getCells().unMerge(frow, fcol, erow, ecol);

}

{{< /highlight >}}
## **Télécharger le code d'exécution**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **Télécharger l'exemple de code**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/detectmergecells/AsposeDetectMergeCells.java)

{{% alert color="primary" %}} 

 Pour plus de détails, visitez[Détecter fusionné Cells dans une feuille de calcul](/cells/fr/java/detect-merged-cells-in-a-worksheet).

{{% /alert %}}
