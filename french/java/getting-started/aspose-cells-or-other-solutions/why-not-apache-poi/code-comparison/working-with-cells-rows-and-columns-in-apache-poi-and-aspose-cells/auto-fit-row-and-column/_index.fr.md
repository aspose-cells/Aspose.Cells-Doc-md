---
title: Ajustement automatique de la ligne et de la colonne
type: docs
weight: 10
url: /fr/java/auto-fit-row-and-column/
description: Apprenez comment ajuster automatiquement la ligne et la colonne grâce à l API Aspose.Cells for Java.
keywords: Comment ajuster automatiquement la ligne et la colonne en Java, Données d ajustement automatique de ligne dans le classeur en utilisant Java, Données d ajustement automatique de colonne en Java. 
---

## **Comment adapter automatiquement la ligne et la colonne en utilisant Aspose.Cells for Java**
L'approche la plus simple pour redimensionner automatiquement la largeur et la hauteur d'une ligne est d'appeler la méthode Worksheet.autoFitRow. La méthode autoFitRow prend en paramètre l'index de la ligne (de la ligne à redimensionner).

**Notez s'il vous plaît:** Si vous souhaitez adapter automatiquement les lignes et colonnes dans les feuilles de calcul Excel en utilisant Java, veuillez visiter [Adapter les lignes et les colonnes](https://docs.aspose.com/cells/java/autofit-rows-and-columns/).

**Java**

{{< highlight java >}}

 Workbook workbook = new Workbook("workbook.xls");

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.getWorksheets().get(0);

worksheet.autoFitRow(1); //Auto-fitting the 2nd row of the worksheet

worksheet.autoFitColumn(0); //Auto-fitting the 1st column of the worksheet

//Saving the modified Excel file in default (that is Excel 2003) format

workbook.save("AutoFit_Aspose.xls");


{{< /highlight >}}
## **Apache POI SS - HSSF XSSF - Adaptation automatique de la ligne et de la colonne**
Apache POI SS - HSSF et XSSF fournit Sheet.autoSizeColumn pour adapter automatiquement les colonnes

**Java**

{{< highlight java >}}

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
## **Télécharger le code en cours d'exécution**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Télécharger le code source d'exemple**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/cellsrowscolumns/autofitrowandcolumn)
{{< app/cells/assistant language="java" >}}
