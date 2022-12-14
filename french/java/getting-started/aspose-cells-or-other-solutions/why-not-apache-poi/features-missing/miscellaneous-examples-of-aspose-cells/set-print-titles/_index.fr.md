---
title: Définir les titres d'impression
type: docs
weight: 10
url: /fr/java/set-print-titles/
---
## **Aspose.Cells - Définir les titres d'impression**
Aspose.Cells vous permet de désigner des en-têtes de ligne et de colonne à répéter sur toutes les pages d'une feuille de calcul imprimée. Pour ce faire, utilisez le[Mise en page](/java/pagesetup)propriétés class'setPrintTitleColumns et setPrintTitleRows.

Les lignes ou les colonnes qui seront répétées sont définies en passant leurs numéros de ligne ou de colonne. Par exemple, les lignes sont définies comme $1:$2 et les colonnes sont définies comme $A:$B.

**Java**

{{< highlight "java" >}}

 //Obtaining the reference of the PageSetup of the worksheet

PageSetup pageSetup = sheet.getPageSetup();

//Defining column numbers A & B as title columns

pageSetup.setPrintTitleColumns("$A:$B");

//Defining row numbers 1 & 2 as title rows

pageSetup.setPrintTitleRows("$1:$2");

{{< /highlight >}}
## **Télécharger le code d'exécution**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Télécharger l'exemple de code**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/print/AsposePrintTitles.java)

{{% alert color="primary" %}} 

 Pour plus de détails, visitez[Définition des options d'impression](/cells/fr/java/page-setup-features/#setting-print-options).

{{% /alert %}}
