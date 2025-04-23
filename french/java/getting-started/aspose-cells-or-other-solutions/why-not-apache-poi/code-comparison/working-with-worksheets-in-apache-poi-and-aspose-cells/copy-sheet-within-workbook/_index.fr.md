---
title: Copier une feuille dans le classeur
type: docs
weight: 40
url: /fr/java/copy-sheet-within-workbook/
---

## **Microsoft Excel - Déplacer ou copier des feuilles dans un classeur**
Voici les étapes à suivre pour copier et déplacer des feuilles de calcul au sein d'un classeur ou entre des classeurs.

1. Pour déplacer ou copier des feuilles au sein ou entre des classeurs, ouvrez le classeur qui recevra les feuilles.
1. Basculez vers le classeur contenant les feuilles que vous souhaitez déplacer ou copier, puis sélectionnez les feuilles.
1. Dans le menu **Édition**, cliquez sur **Déplacer ou copier la feuille**.
1. Dans la zone Vers le classeur, cliquez sur le classeur pour recevoir les feuilles.
1. Pour déplacer ou copier les feuilles sélectionnées dans un nouveau classeur, cliquez sur **nouveau classeur**.
1. Dans la zone **Avant la feuille**, cliquez sur la feuille avant laquelle vous souhaitez insérer les feuilles déplacées ou copiées.
1. Pour copier les feuilles au lieu de les déplacer, sélectionnez la case à cocher **Créer une copie**.
## **Aspose.Cells - Copier une feuille dans un classeur**
{{% alert color="primary" %}} 

Aspose.Cells fournit une méthode surchargée, WorksheetCollection.addCopy(), qui est utilisée pour ajouter une feuille de calcul à la collection et copier des données à partir d'une feuille de calcul existante. Une version de la méthode prend l'index de la feuille source en paramètre. L'autre version prend le nom de la feuille source.

L'exemple suivant montre comment copier une feuille existante dans un classeur.

{{% /alert %}} 

Copiez des feuilles avec Aspose.Cells

**Java**

{{< highlight java >}}

 //Create a new Workbook by excel file path

Workbook wb = new Workbook(dataDir + "workbook.xls");

//Create a Worksheets object with reference to the sheets of the Workbook.

WorksheetCollection sheets = wb.getWorksheets();

//Copy data to a new sheet from an existing sheet within the Workbook.

sheets.addCopy("Sheet1");

{{< /highlight >}}
## **Apache POI SS - Copier une feuille dans un classeur**
{{% alert color="primary" %}} 

Workbook.cloneSheet() est utilisé pour copier des feuilles avec le classeur.

{{% /alert %}} 

Copiez des feuilles avec Apache POI SS

**Java**

{{< highlight java >}}

 Workbook wb = new HSSFWorkbook();

wb.createSheet("new sheet");

wb.createSheet("second sheet");

Sheet cloneSheet = wb.cloneSheet(0);

{{< /highlight >}}
## **Télécharger le code en cours d'exécution**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Télécharger le code source d'exemple**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/worksheets/copysheetwithinworkbook)

{{% alert color="primary" %}} 

Pour plus de détails, visitez [Copier et déplacer les feuilles de calcul](/cells/fr/java/copying-and-moving-worksheets).

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
