---
title: Figer les volets dans Apache POI et Aspose.Cells
type: docs
weight: 80
url: /fr/java/freeze-panes-in-apache-poi-and-aspose-cells/
---
## **Aspose.Cells - Figer les volets**
Aspose.Cells fournit une classe,[Cahier](http://docs.aspose.com:8082/docs/display/cellsjava/Workbook)qui représente un fichier Excel Microsoft. La classe Workbook contient une WorksheetCollection qui permet d'accéder à chaque feuille de calcul dans un fichier Excel.

Une feuille de calcul est représentée par le[Feuille de travail](http://docs.aspose.com:8082/docs/display/cellsjava/Worksheet)classer. La classe Worksheet fournit un large éventail de propriétés et de méthodes pour gérer les feuilles de calcul. Pour configurer les volets de gel, appelez la méthode freezePanes de la classe Worksheet. La méthode FreezePanes prend les paramètres suivants :

- **Ligne**, l'index de ligne de la cellule à partir de laquelle le gel commencera.
- **Colonne**, l'index de colonne de la cellule à partir de laquelle le gel commencera.
- **Lignes gelées**, le nombre de lignes visibles dans le volet supérieur.
- **Colonnes gelées**, le nombre de colonnes visibles dans le volet de gauche

**Java**

{{< highlight "java" >}}

 worksheet1.freezePanes(0,2,0,2); // Freezing Columns

worksheet2.freezePanes(2,0,2,0); // Freezing Rows

{{< /highlight >}}
## **Apache POI SS - HSSF XSSF - Figer les volets**
sheet.createFreezePane est disponible pour obtenir la fonctionnalité FreezePane tout en utilisant Apache POI SS - HSSF et XSSF

**Java**

{{< highlight "java" >}}

 // Freeze just one row

sheet1.createFreezePane( 0, 2, 0, 2 );

// Freeze just one column

sheet2.createFreezePane( 2, 0, 2, 0 );

// Freeze the columns and rows (forget about scrolling position of the lower right quadrant).

sheet3.createFreezePane( 2, 2 );

{{< /highlight >}}
## **Télécharger le code d'exécution**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Télécharger l'exemple de code**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/cellsrowscolumns/freezepanes)

{{% alert color="primary" %}} 

 Pour plus de détails, visitez[Figer les volets](http://docs.aspose.com:8082/docs/display/cellsjava/Freeze+Panes).

{{% /alert %}}
