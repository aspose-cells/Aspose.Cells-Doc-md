---
title: Ajustement automatique des lignes et des colonnes
type: docs
weight: 10
url: /fr/java/auto-fit-row-and-column/
---
## **Aspose.Cells - Ligne et colonne d'ajustement automatique**
L'approche la plus simple pour dimensionner automatiquement la largeur et la hauteur d'une ligne consiste à appeler la méthode Worksheet.autoFitRow. La méthode autoFitRow prend un index de ligne (de la ligne à redimensionner) comme paramètre.

**Veuillez noter:** Si vous souhaitez ajuster automatiquement les lignes et les colonnes dans les feuilles de calcul Excel à l'aide de Java, veuillez visiter[Ajustement automatique des lignes et des colonnes](https://docs.aspose.com/cells/java/autofit-rows-and-columns/).

**Java**

{{< highlight "java" >}}

 Workbook workbook = new Workbook("workbook.xls");

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.getWorksheets().get(0);

worksheet.autoFitRow(1); //Auto-fitting the 2nd row of the worksheet

worksheet.autoFitColumn(0); //Auto-fitting the 1st column of the worksheet

//Saving the modified Excel file in default (that is Excel 2003) format

workbook.save("AutoFit_Aspose.xls");


{{< /highlight >}}
## **Apache POI SS - HSSF XSSF - Ajustement automatique des lignes et des colonnes**
Apache POI SS - HSSF et XSSF fournissent Sheet.autoSizeColumn pour ajuster automatiquement les colonnes

**Java**

{{< highlight "java" >}}

 InputStream inStream = new FileInputStream("workbook.xls");

Workbook workbook = WorkbookFactory.create(inStream);

Sheet sheet = workbook.createSheet("new sheet");

sheet.autoSizeColumn(0); //adjust width of the first column

sheet.autoSizeColumn(1); //adjust width of the second column

FileOutputStream fileOut;

fileOut = new FileOutputStream("AutoFit_Apache.xls");

workbook.write(fileOut);

fileOut.close();

{{< /highlight >}}
## **Télécharger le code d'exécution**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Télécharger l'exemple de code**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/cellsrowscolumns/autofitrowandcolumn)
