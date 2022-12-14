---
title: Enregistrer chaque feuille de calcul dans un PDF différent
type: docs
weight: 10
url: /fr/net/save-each-worksheet-to-different-pdf/
---
## **Aspose.Cells - Enregistrer chaque feuille de calcul dans un PDF différent**
Aspose.Cells prend en charge la conversion de fichiers XLS (contenant des images, des graphiques, etc.) en documents PDF. Aspose.Cells for .NET peut fonctionner indépendamment pour convertir une feuille de calcul en document PDF et vous n'avez plus besoin d'utiliser Aspose.Pdf for .NET pour la conversion. La conversion ne nécessite pas non plus de créer/utiliser de fichier(s) temporaire(s) car l'ensemble du processus peut être effectué dans la mémoire.

**C#**

{{< highlight "cs" >}}

 //Instancier un nouveau classeur et ouvrir Excel

//Fichier depuis son emplacement

Classeur classeur = nouveau classeur("../../data/test.xlsx");

// Récupère le nombre de feuilles de calcul dans le classeur

int sheetCount = workbook.Worksheets.Count ;

//Rend toutes les feuilles invisibles sauf la première feuille de calcul

 pour (int je = 1; je< workbook.Worksheets.Count; i++)

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
## **Télécharger le code d'exécution**
 Télécharger**Enregistrer chaque feuille de calcul dans un PDF différent** forment l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Save.Each.Worksheet.to.Different.PDF.Aspose.Cells.zip)

{{% alert color="primary" %}} 

 Pour plus de détails, visitez[Enregistrer chaque feuille de calcul dans un fichier PDF différent](https://docs.aspose.com/cells/net/save-each-worksheet-to-a-different-pdf-file/).

{{% /alert %}}
