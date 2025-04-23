---
title: Définir les titres d impression dans xlsx4j
type: docs
weight: 40
url: /fr/java/set-print-titles-in-xlsx4j/
---

## **Aspose.Cells - Définir les titres à imprimer**
Aspose.Cells vous permet de désigner des en-têtes de lignes et de colonnes à répéter sur toutes les pages d'une feuille de calcul imprimée. Pour ce faire, utilisez les propriétés setPrintTitleColumns et setPrintTitleRows de la classe [PageSetup](/java/PageSetup).

Les lignes ou colonnes qui seront répétées sont définies en passant leurs numéros de ligne ou de colonne. Par exemple, les lignes sont définies comme $1:$2 et les colonnes sont définies comme $A:$B.

**Java**

{{< highlight java >}}

 //Obtaining the reference of the PageSetup of the worksheet

PageSetup pageSetup = sheet.getPageSetup();

//Defining column numbers A & B as title columns

pageSetup.setPrintTitleColumns("$A:$B");

//Defining row numbers 1 & 2 as title rows

pageSetup.setPrintTitleRows("$1:$2");

{{< /highlight >}}
## **Télécharger le code en cours d'exécution**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **Télécharger le code source d'exemple**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/print/setprinttitles/AsposeSetPrintTitles.java)

{{% alert color="primary" %}} 

Pour plus de détails, visitez [Paramétrer les options d'impression](/cells/fr/java/page-setup-features/#setting-print-options).

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
