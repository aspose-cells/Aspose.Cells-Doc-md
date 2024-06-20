---
title: Diviser les volets dans Apache POI et Aspose.Cells
type: docs
weight: 70
url: /fr/java/split-panes-in-apache-poi-and-aspose-cells/
---

## **Aspose.Cells - Diviser les volets**
Aspose.Cells fournit une classe, Workbook qui représente un fichier Microsoft Excel. La classe Workbook offre une large gamme de propriétés et de méthodes pour gérer les fichiers Excel. Pour implémenter des vues divisées, utilisez la méthode split de la classe Worksheet. Pour supprimer les volets divisés, utilisez la méthode removeSplit.

**Java**

{{< highlight java >}}

 //Instantiate a new workbook / Open a template file

Workbook book = new Workbook(dataDir + "workbook.xls");

//Set the active cell

book.getWorksheets().get(0).setActiveCell("A20");

//Split the worksheet window

book.getWorksheets().get(0).split();

{{< /highlight >}}
## **Apache POI SS - HSSF & XSSF - Diviser les volets**
La fonctionnalité Split Panes peut être réalisée en utilisant la méthode createSplitPane avec l'API Apache POI SS (HSSF & XSSF)

**Java**

{{< highlight java >}}

 Workbook wb = new XSSFWorkbook();

Sheet sheet = wb.createSheet("new sheet");

// Create a split with the lower left side being the active quadrant

sheet.createSplitPane(2000, 2000, 0, 0, Sheet.PANE_LOWER_LEFT);

{{< /highlight >}}
## **Télécharger le code en cours d'exécution**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Télécharger le code source d'exemple**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/cellsrowscolumns/splitpanes)

{{% alert color="primary" %}} 

Pour plus de détails, visitez [Diviser les volets](http://docs.aspose.com:8082/docs/display/cellsjava/Split+Panes).

{{% /alert %}}
