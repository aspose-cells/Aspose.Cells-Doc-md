---
title: Définir la zone d impression
type: docs
weight: 40
url: /fr/java/set-print-area/
---

## **Aspose.Cells - Définir la zone d'impression**
Par défaut, seule la zone d'impression intègre toutes les zones de la feuille de calcul contenant des données. Les développeurs peuvent définir une zone d'impression spécifique de la feuille de calcul.

Pour sélectionner une zone d'impression spécifique, utilisez la méthode setPrintArea de la classe [PageSetup](/java/pagesetup). Attribuez une plage de cellules qui définit la zone d'impression à cette propriété.

**Java**

{{< highlight java >}}

 // Instantiating a Workbook object

Workbook workbook = new Workbook();

// Accessing the first worksheet in the Workbook file

WorksheetCollection worksheets = workbook.getWorksheets();

Worksheet sheet = worksheets.get(0);

// Obtaining the reference of the PageSetup of the worksheet

PageSetup pageSetup = sheet.getPageSetup();

// Specifying the cells range (from A1 cell to F20 cell) of the print area

pageSetup.setPrintArea("A1:F20");

{{< /highlight >}}
## **Apache POI SS - HSSF XSSF - Définir la zone d'impression**
La méthode Workbook.setPrintArea est disponible pour définir les propriétés de la zone d'impression.

**Java**

{{< highlight java >}}

 Workbook wb = new HSSFWorkbook();

Sheet sheet = wb.createSheet("Sheet1");

//sets the print area for the first sheet

wb.setPrintArea(0, "$A$1:$C$2");

//Alternatively:

wb.setPrintArea(

        0, //sheet index

        0, //start column

        1, //end column

        0, //start row

        0  //end row

);

{{< /highlight >}}
## **Télécharger le code en cours d'exécution**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Télécharger le code source d'exemple**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/workbook/setprintarea)

{{% alert color="primary" %}} 

Pour plus de détails, visitez [Paramétrer les options d'impression](/cells/fr/java/page-setup-features/#setting-print-options).

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
