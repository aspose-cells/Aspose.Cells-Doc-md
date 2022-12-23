---
title: Enregistrez chaque feuille de calcul dans différents PDF au format xlsx4j
type: docs
weight: 50
url: /fr/java/save-each-worksheet-to-different-pdf-in-xlsx4j/
---
## **Aspose.Cells - Enregistrer chaque feuille de calcul dans différents PDF**
Aspose.Cells prend en charge la conversion de fichiers XLS (contenant des images, des graphiques, etc.) en documents PDF. Aspose.Cells for Java peut fonctionner indépendamment pour convertir une feuille de calcul en document PDF et vous n'avez plus besoin d'utiliser Aspose.Pdf for Java pour la conversion. La conversion ne nécessite pas non plus de créer/utiliser de fichier(s) temporaire(s) car l'ensemble du processus peut être effectué dans la mémoire.

**Java**

{{< highlight "java" >}}

 // Récupère le chemin du fichier Excel

String filePath = dataDir + "workbook.xlsx" ;

//Instancier un nouveau classeur et ouvrir Excel

//Fichier depuis son emplacement

Classeur classeur = nouveau classeur (filePath);

// Récupère le nombre de feuilles de calcul dans le classeur

int sheetCount = classeur.getWorksheets().getCount();

//Rend toutes les feuilles invisibles sauf la première feuille de calcul

 pour (int je = 1; je< workbook.getWorksheets().getCount(); i++)

{

     workbook.getWorksheets().get(i).setVisible(false);

}

//Take Pdfs of each sheet

for (int j = 0; j < workbook.getWorksheets().getCount(); j++)

{

    Worksheet ws = workbook.getWorksheets().get(j);

    workbook.save(dataPath + ws.getName() + ".pdf");

    if (j < workbook.getWorksheets().getCount() - 1)

    {

       workbook.getWorksheets().get(j + 1).setVisible(true);

       workbook.getWorksheets().get(j).setVisible(false);

    }

}

{{< /highlight >}}
## **Télécharger le code d'exécution**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **Télécharger l'exemple de code**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/saveeachworksheettopdf/AsposeSaveEachWorksheetToDifferentPDF.java)

{{% alert color="primary" %}} 

 Pour plus de détails, visitez[Enregistrer chaque feuille de calcul dans un fichier PDF différent](/cells/fr/java/save-each-worksheet-to-a-different-pdf-file).

{{% /alert %}}
