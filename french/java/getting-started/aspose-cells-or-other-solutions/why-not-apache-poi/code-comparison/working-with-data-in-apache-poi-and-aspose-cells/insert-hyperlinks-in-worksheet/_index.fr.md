---
title: Insérer des liens hypertexte dans la feuille de calcul
type: docs
weight: 20
url: /fr/java/insert-hyperlinks-in-worksheet/
---
## **Aspose.Cells - Insérer des hyperliens dans la feuille de calcul**
**Ajout d'un lien vers un Cell dans le même fichier**

Il est possible d'ajouter des liens hypertexte aux cellules d'un même fichier Excel en appelant la méthode Add de la collection Hyperlink. La méthode Add fonctionne pour les liens hypertexte internes et externes.

**Java**

{{< highlight "java" >}}

 //Obtaining the reference of the first worksheet.

WorksheetCollection worksheets = workbook.getWorksheets();

Worksheet sheet = worksheets.get(0);

HyperlinkCollection hyperlinks = sheet.getHyperlinks();

//Adding a hyperlink to a URL at "A1" cell

hyperlinks.add("A1",1,1,"http://www.aspose.com");

//============ Link to Cell =================

//Setting a value to the "A1" cell

Cells cells = sheet.getCells();

Cell cell = cells.get("A2");

cell.setValue("Link to B9");

setFormatting(cell);

hyperlinks = sheet.getHyperlinks();

//Adding an internal hyperlink to the "B9" cell of the other worksheet "Sheet1" in

//the same Excel file

hyperlinks.add("A2",1 ,1, "Sheet1!B9");


{{< /highlight >}}

**Ajouter un lien vers un fichier externe**

Il est possible d'ajouter des liens hypertexte vers des fichiers Excel externes en appelant la méthode Add de la collection Hyperlinks. La méthode Add prend les paramètres suivants :

- Cell nom, le nom de la cellule à laquelle le lien hypertexte sera ajouté.
- Nombre de lignes, le nombre de lignes dans cette plage de liens hypertexte.
- Nombre de colonnes, le nombre de colonnes dans cette plage de liens hypertexte.
- URL, l'adresse de la cible, fichier Excel externe.

**Java**

{{< highlight "java" >}}

 cell = cells.get("A3");

cell.setValue("External Link");

setFormatting(cell);

hyperlinks = sheet.getHyperlinks();

//Adding a link to the external file

hyperlinks.add("A3", 1, 1, "book1.xls");

{{< /highlight >}}
## **Apache POI SS - HSSF XSSF - Insérer des hyperliens dans la feuille de calcul**
**Java**

{{< highlight "java" >}}

 CellStyle hlink_style = wb.createCellStyle();

Font hlink_font = wb.createFont();

hlink_font.setUnderline(Font.U_SINGLE);

hlink_font.setColor(IndexedColors.BLUE.getIndex());

hlink_style.setFont(hlink_font);

Cell cell;

Sheet sheet = wb.createSheet("Hyperlinks");

//URL

cell = sheet.createRow(0).createCell((short)0);

cell.setCellValue("URL Link");

Hyperlink link = createHelper.createHyperlink(Hyperlink.LINK_URL);

link.setAddress("http://poi.apache.org/");

cell.setHyperlink(link);

cell.setCellStyle(hlink_style);

//link to a file in the current directory

cell = sheet.createRow(1).createCell((short)0);

cell.setCellValue("File Link");

link = createHelper.createHyperlink(Hyperlink.LINK_FILE);

link.setAddress("link1.xls");

cell.setHyperlink(link);

cell.setCellStyle(hlink_style);

//e-mail link

cell = sheet.createRow(2).createCell((short)0);

cell.setCellValue("Email Link");

link = createHelper.createHyperlink(Hyperlink.LINK_EMAIL);

//note, if subject contains white spaces, make sure they are url-encoded

link.setAddress("mailto:poi@apache.org?subject=Hyperlinks");

cell.setHyperlink(link);

cell.setCellStyle(hlink_style);

//link to a place in this workbook

//create a target sheet and cell

Sheet sheet2 = wb.createSheet("Target Sheet");

sheet2.createRow(0).createCell((short)0).setCellValue("Target Cell");

cell = sheet.createRow(3).createCell((short)0);

cell.setCellValue("Worksheet Link");

Hyperlink link2 = createHelper.createHyperlink(Hyperlink.LINK_DOCUMENT);

link2.setAddress("'Target Sheet'!A1");

cell.setHyperlink(link2);

cell.setCellStyle(hlink_style);

{{< /highlight >}}
## **Télécharger le code d'exécution**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Télécharger l'exemple de code**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/datahandling/hyperlien)

