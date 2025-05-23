---
title: Mise en page  Réglage ajusté à la page
type: docs
weight: 30
url: /fr/java/page-setup-fit-to-page-setting/
---

## **Aspose.Cells - Mise en page - Réglage ajusté à la page**
Pour ajuster le contenu de la feuille de calcul à un nombre spécifique de pages, utilisez les méthodes setFitToPagesTall et setFitToPagesWide de la classe [PageSetup](/cells/fr/java/page-setup-fit-to-page-setting/). Ces méthodes sont également utilisées pour mettre à l'échelle les feuilles de calcul.

**Java**

{{< highlight java >}}

 // Instantiating a Workbook object

Workbook workbook = new Workbook();

// Accessing the first worksheet in the Excel file

WorksheetCollection worksheets = workbook.getWorksheets();

int sheetIndex = worksheets.add();

Worksheet sheet = worksheets.get(sheetIndex);

PageSetup pageSetup = sheet.getPageSetup();

// Setting the number of pages to which the length of the worksheet will

// be spanned

pageSetup.setFitToPagesTall(1);

// Setting the number of pages to which the width of the worksheet will be spanned

pageSetup.setFitToPagesWide(1);

{{< /highlight >}}
## **Apache POI SS - HSSF & XSSF - Mise en page - Réglage ajusté à la page**
Apache POI SS utilise les méthodes setFitHeight et setFitWidth pour les réglages ajustés à la page.

**Java**

{{< highlight java >}}

 Workbook wb = new XSSFWorkbook();  //or new HSSFWorkbook();

Sheet sheet = wb.createSheet("format sheet");

PrintSetup ps = sheet.getPrintSetup();

sheet.setAutobreaks(true);

ps.setFitHeight((short) 1);

ps.setFitWidth((short) 1);

{{< /highlight >}}
## **Télécharger le code en cours d'exécution**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Télécharger le code source d'exemple**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/workbook/fittoonepage)

{{% alert color="primary" %}} 

Pour plus de détails, visitez [Définition des options de page](http://www.aspose.com/docs/display/cellsjava/Setting+Page+Options).

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
