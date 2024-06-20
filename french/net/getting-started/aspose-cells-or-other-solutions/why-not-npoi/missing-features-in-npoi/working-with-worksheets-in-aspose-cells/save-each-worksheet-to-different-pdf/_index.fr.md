---
title: Enregistrer chaque feuille de calcul dans un fichier PDF différent
type: docs
weight: 10
url: /fr/net/save-each-worksheet-to-different-pdf/
---

## **Aspose.Cells - Enregistrer chaque feuille de calcul au format PDF différent**
Aspose.Cells prend en charge la conversion de fichiers XLS (contenant des images, des graphiques, etc.) en documents PDF. Aspose.Cells for .NET peut fonctionner de manière indépendante pour convertir une feuille de calcul en document Pdf et vous n'avez plus besoin d'utiliser Aspose.Pdf for .NET pour la conversion. La conversion ne nécessite pas non plus la création / l'utilisation de fichiers temporaires, car tout le processus peut être effectué en mémoire.

**C#**

{{< highlight cs >}}

 //Instantiate a new workbook and open the Excel

//File from its location

Workbook workbook = new Workbook("../../data/test.xlsx");

//Get the count of the worksheets in the workbook

int sheetCount = workbook.Worksheets.Count;

//Make all sheets invisible except first worksheet

for (int i = 1; i < workbook.Worksheets.Count; i++)

{

    workbook.Worksheets[i].IsVisible = false;

}

//Take Pdfs of each sheet

for (int j = 0; j < workbook.Worksheets.Count; j++)

{

    Worksheet ws = workbook.Worksheets[j];

    workbook.Save(ws.Name + ".pdf");

    if (j < workbook.Worksheets.Count - 1)

    {

        workbook.Worksheets[j + 1].IsVisible = true;

        workbook.Worksheets[j].IsVisible =false;

    }

}

{{< /highlight >}}
## **Télécharger le code en cours d'exécution**
Téléchargez le formulaire **Enregistrer chaque feuille de calcul dans un fichier PDF différent** sur l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Save.Each.Worksheet.to.Different.PDF.Aspose.Cells.zip)

{{% alert color="primary" %}} 

Pour plus de détails, visitez [Enregistrer chaque feuille de calcul dans un fichier PDF différent](https://docs.aspose.com/cells/net/save-each-worksheet-to-a-different-pdf-file/).

{{% /alert %}}
