---
title: Hide and Unhide Cells
type: docs
weight: 30
url: /fr/java/hide-and-unhide-cells/
---

## **Aspose.Cells - Masquer et afficher des lignes et des colonnes**
Aspose.Cells fournit une classe, [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook), qui représente un fichier Microsoft Excel. La classe Workbook contient une WorksheetCollection qui permet d'accéder à chaque feuille de calcul dans le fichier Excel. Une feuille de calcul est représentée par la classe [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet). La classe Worksheet fournit une collection de Cells qui représente toutes les cellules de la feuille de calcul. La collection de Cells fournit plusieurs méthodes pour gérer les lignes ou les colonnes dans une feuille de calcul. 

**Java**

{{< highlight java >}}

 Workbook workbook = new Workbook("workbook.xls");

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.getWorksheets().get(0);

Cells cells = worksheet.getCells();

cells.hideRow(2); //Hiding the 3rd row of the worksheet

cells.hideColumn(1); //Hiding the 2nd column of the worksheet

{{< /highlight >}}
## **Apache POI SS - HSSF XSSF - Masquer / Afficher des cellules**
Pour masquer une ligne ou une colonne, Apache POI SS fournit la méthode Row.setZeroHeight(boolean).

**Java**

{{< highlight java >}}

 InputStream inStream = new FileInputStream("workbook.xls");

Workbook workbook = WorkbookFactory.create(inStream);

Sheet sheet = workbook.createSheet();

Row row = sheet.createRow(0);

row.setZeroHeight(true);

{{< /highlight >}}
## **Télécharger le code en cours d'exécution**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Télécharger le code source d'exemple**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/cellsrowscolumns/hideunhidecells)

{{% alert color="primary" %}} 

Pour plus de détails, visitez [Masquer et afficher des lignes et des colonnes](/java/hiding-and-showing-rows-and-columns).

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
