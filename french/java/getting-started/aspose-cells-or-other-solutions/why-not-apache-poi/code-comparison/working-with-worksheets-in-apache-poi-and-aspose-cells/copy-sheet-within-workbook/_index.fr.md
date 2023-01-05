---
title: Copier la feuille dans le classeur
type: docs
weight: 40
url: /fr/java/copy-sheet-within-workbook/
---
## **Microsoft Excel - Déplacer ou copier des feuilles dans le classeur**
Voici les étapes à suivre pour copier et déplacer des feuilles de calcul dans ou entre des classeurs.

1. Pour déplacer ou copier des feuilles dans ou entre des classeurs, ouvrez le classeur qui recevra les feuilles.
1. Basculez vers le classeur contenant les feuilles que vous souhaitez déplacer ou copier, puis sélectionnez les feuilles.
1.  Sur le**Éditer** menu, cliquez sur**Déplacer ou copier une feuille**.
1. Dans la zone À réserver, cliquez sur le classeur pour recevoir les feuilles.
1.  Pour déplacer ou copier les feuilles sélectionnées dans un nouveau classeur, cliquez sur**nouveau livre**.
1.  Dans le**Avant feuille** , cliquez sur la feuille devant laquelle vous souhaitez insérer les feuilles déplacées ou copiées.
1.  Pour copier les feuilles au lieu de les déplacer, sélectionnez le**Créer une copie** case à cocher.
## **Aspose.Cells - Copier la feuille dans le classeur**
{{% alert color="primary" %}} 

Aspose.Cells fournit une méthode surchargée, WorksheetCollection.addCopy(), qui est utilisée pour ajouter une feuille de calcul à la collection et copier les données d'une feuille de calcul existante. Une version de la méthode prend l'index de la feuille de calcul source comme paramètre. L'autre version prend le nom de la feuille de calcul source.

L'exemple suivant montre comment copier une feuille de calcul existante dans un classeur.

{{% /alert %}} 

Copiez les feuilles en utilisant Aspose.Cells

**Java**

{{< highlight "java" >}}

 //Create a new Workbook by excel file path

Workbook wb = new Workbook(dataDir + "workbook.xls");

//Create a Worksheets object with reference to the sheets of the Workbook.

WorksheetCollection sheets = wb.getWorksheets();

//Copy data to a new sheet from an existing sheet within the Workbook.

sheets.addCopy("Sheet1");

{{< /highlight >}}
## **Apache POI SS - Copier la feuille dans le classeur**
{{% alert color="primary" %}} 

Workbook.cloneSheet() est utilisé pour copier des feuilles avec un classeur.

{{% /alert %}} 

Copier des feuilles à l'aide d'Apache POI SS

**Java**

{{< highlight "java" >}}

 Workbook wb = new HSSFWorkbook();

wb.createSheet("new sheet");

wb.createSheet("second sheet");

Sheet cloneSheet = wb.cloneSheet(0);

{{< /highlight >}}
## **Télécharger le code d'exécution**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Télécharger l'exemple de code**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/worksheets/copysheetwithinworkbook)

{{% alert color="primary" %}} 

 Pour plus de détails, visitez[Copier et déplacer des feuilles de calcul](/cells/fr/java/copying-and-moving-worksheets).

{{% /alert %}}
