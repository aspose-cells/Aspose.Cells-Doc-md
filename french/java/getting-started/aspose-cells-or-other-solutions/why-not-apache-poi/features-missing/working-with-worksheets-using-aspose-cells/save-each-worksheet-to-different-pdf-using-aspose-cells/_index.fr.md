---
title: Enregistrer chaque feuille de calcul au format PDF différent à l aide d Aspose.Cells
type: docs
weight: 80
url: /fr/java/save-each-worksheet-to-different-pdf-using-aspose-cells/
---

## **Aspose.Cells - Enregistrer chaque feuille de calcul au format PDF différent**
Aspose.Cells prend en charge la conversion de fichiers XLS (contenant des images, des graphiques, etc.) en documents PDF. Aspose.Cells for Java peut travailler de manière indépendante pour convertir une feuille de calcul en document Pdf et vous n'avez plus besoin d'utiliser Aspose.Pdf for Java pour la conversion. La conversion ne nécessite pas de créer/utiliser de fichier(s) temporaire(s) car tout le processus peut être effectué en mémoire.

**Java**

{{< highlight java >}}

 //Get the Excel file path

String filePath = dataDir + "workbook.xlsx";

//Instantiate a new workbook and open the Excel

//File from its location

Workbook workbook = new Workbook(filePath);

//Get the count of the worksheets in the workbook

int sheetCount = workbook.getWorksheets().getCount();

//Make all sheets invisible except first worksheet

for (int i = 1; i < workbook.getWorksheets().getCount(); i++)

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
## **Télécharger le code en cours d'exécution**
## **Télécharger le code source d'exemple**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/SaveEachWorksheetToDifferentPDF.java)

{{% alert color="primary" %}} 

Pour plus de détails, visitez [Enregistrer chaque feuille de calcul dans un fichier PDF différent](/cells/fr/java/enregistrer-chaque-feuille-de-calcul-dans-un-fichier-pdf-different).

{{% /alert %}}
