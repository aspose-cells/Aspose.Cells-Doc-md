---
title: Exporter des données à partir de feuilles de calcul au format xlsx4j
type: docs
weight: 20
url: /fr/java/export-data-from-worksheets-in-xlsx4j/
---
## **Aspose.Cells - Exporter des données à partir de feuilles de calcul**
Aspose.Cells permet non seulement à ses utilisateurs d'importer des données dans des feuilles de calcul à partir de sources de données externes, mais leur permet également d'exporter des données de feuille de calcul vers un tableau.

**Java**

{{< highlight "java" >}}

 //Création d'un flux de fichier contenant le fichier Excel à ouvrir

FileInputStream fstream = new FileInputStream(dataDir + "workbook.xls");

//Instanciation d'un objet Workbook

Classeur classeur = nouveau classeur(fstream);

//Accéder à la première feuille de calcul du fichier Excel

feuille de calcul feuille de calcul = workbook.getWorksheets().get(0);

// Exportation du contenu de 7 lignes et 2 colonnes à partir de la 1ère cellule vers Array.

Table de données d'objet [][]= worksheet.getCells().exportArray(4,0,7,8);

 pour (int je = 0 ; je< dataTable.length ; i++)

{

	System.out.println("["+ i +"]: "+ Arrays.toString(dataTable[i]));

}

{{< /highlight >}}
## **Télécharger le code d'exécution**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **Télécharger l'exemple de code**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/datahandling/exportdatafromworksheets/AsposeExportDataFromWorksheets.java)

{{% alert color="primary" %}} 

 Pour plus de détails, visitez[Exportation de données à partir de feuilles de calcul](/java/exporting-data-from-worksheets).

{{% /alert %}}
