---
title: Conversion d'Excel au format OFD
linktitle: Conversion d'Excel au format OFD
description: Aspose.Cells est une bibliothèque Java destinée à la manipulation des fichiers de feuilles de calcul qui prend en charge la conversion de classeurs Excel au format OFD (Open Fixed-layout Document). Cet article montre comment créer du contenu Excel et l'exporter en OFD, ainsi que comment convertir des fichiers Excel existants en OFD à l'aide d'Aspose.Cells.
keywords: Aspose.Cells, bibliothèque Java, feuille de calcul, Excel vers OFD, conversion OFD, SaveFormat.Ofd, document à mise en page fixe, export de classeur
type: docs
weight: 195
url: /fr/java/converting-excel-to-ofd-format/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells prend en charge la conversion des classeurs Excel directement au format OFD (Open Fixed-layout Document) à l'aide de la valeur d'énumération `SaveFormat.Ofd`. Le document OFD obtenu préserve la mise en page visible du classeur, son contenu, les cellules fusionnées, les largeurs de colonnes, les hauteurs de lignes, les polices, les couleurs, les bordures et les formats de nombres. Aspose.Cells convient ainsi aux flux de travail d'archivage, d'impression, de dépôt réglementaire et de soumission aux autorités publiques qui nécessitent une sortie à mise en page fixe.

{{% /alert %}}
## **Introduction**
OFD (Open Fixed-layout Document) est une norme nationale chinoise (GB/T 33190-2016) destinée à représenter les documents numériques selon une mise en page fixe et paginée. Elle joue un rôle similaire à celui du PDF pour les cas d'utilisation où l'apparence visuelle du document source doit être conservée exactement telle qu'elle a été conçue. L'OFD est largement adopté pour les soumissions aux autorités publiques, les dépôts réglementaires, les factures électroniques et l'archivage à long terme en République populaire de Chine.

La conversion de classeurs Excel en OFD est une exigence fréquente dans les scénarios où le contenu d'une feuille de calcul doit être distribué sous forme d'artefact en lecture seule et à mise en page verrouillée, plutôt que comme une feuille de calcul éditable. Citons par exemple l'envoi d'une facture finalisée à un client, l'archivage d'un rapport financier trimestriel ou la soumission d'un tableur budgétaire à une autorité réglementaire. Aspose.Cells répond à cette exigence grâce à la valeur d'énumération `SaveFormat.Ofd`, qui écrit le classeur directement en OFD sans étape de conversion intermédiaire. La sortie OFD préserve les valeurs des cellules, les plages fusionnées, les polices, les couleurs, les bordures, les formats de nombres et les options de mise en page configurées dans le classeur.

{{% alert color="primary" %}}

La sortie OFD générée par Aspose.Cells préserve la mise en page visible du classeur source, y compris le contenu des cellules, les cellules fusionnées, les largeurs de colonnes et les hauteurs de lignes. La mise en forme des cellules, telles que les polices, les couleurs, les bordures, l'alignement et les formats de nombres, est également restituée dans la sortie à mise en page fixe. Les options de mise en page configurées sur la feuille de calcul, telles que le format du papier, l'orientation et la zone d'impression, influencent la mise en page du document OFD résultant.

{{% /alert %}}
## **Création d'un classeur Excel et enregistrement au format OFD**
Aspose.Cells vous permet de construire un classeur par programmation, de le remplir avec des données, puis de l'enregistrer directement au format OFD à l'aide de l'énumération `SaveFormat.Ofd`. L'exemple suivant crée une facture à partir de zéro. Il ajoute un logo d'entreprise, des informations d'en-tête, une section de facturation, des lignes de détail et des totaux calculés, puis exporte le classeur vers un document OFD.
### **Création d'une facture avec un logo**
L'exemple construit une feuille de calcul de facture en insérant une image de logo dans la zone supérieure gauche, en renseignant le nom de l'entreprise et les coordonnées, en ajoutant un titre « INVOICE » sur des cellules fusionnées, en enregistrant le numéro et la date de la facture, en listant le client facturé, en construisant un tableau de lignes de détail avec les colonnes description, quantité, prix unitaire et total, et en calculant le sous-total, la taxe et le total général à l'aide de formules de cellules. La mise en forme, telle que les en-têtes en gras, le format monétaire pour les prix, les bordures et les largeurs de colonnes, est appliquée à l'aide des objets `Style` et `Font`. Enfin, le classeur est enregistré avec l'extension `.ofd` à l'aide de `SaveFormat.Ofd`.

```java
import com.aspose.cells.*;
import java.text.SimpleDateFormat;
import java.util.Date;

String dataDir = "C:\\Temp\\";

// Créer un nouveau classeur
Workbook workbook = new Workbook();

// Obtenir la première feuille de calcul
Worksheet worksheet = workbook.getWorksheets().get(0);

// Définir la largeur des colonnes
worksheet.getCells().setColumnWidth(0, 5);
worksheet.getCells().setColumnWidth(1, 35);
worksheet.getCells().setColumnWidth(2, 12);
worksheet.getCells().setColumnWidth(3, 15);
worksheet.getCells().setColumnWidth(4, 15);
worksheet.getCells().setColumnWidth(5, 5);

// Insérer le logo de l'entreprise
worksheet.getPictures().add(1, 1, dataDir + "logo.png");

// Nom de l'entreprise et coordonnées
worksheet.getCells().get("B3").putValue("Acme Corporation");
worksheet.getCells().get("B4").putValue("123 Business Street");
worksheet.getCells().get("B5").putValue("City, State 12345");
worksheet.getCells().get("B6").putValue("Phone: (555) 123-4567");

// Titre FACTURE - fusionner les cellules
worksheet.getCells().merge(7, 1, 2, 4);
Cell titleCell = worksheet.getCells().get("B8");
titleCell.putValue("INVOICE");

Style titleStyle = workbook.createStyle();
titleStyle.getFont().setBold(true);
titleStyle.getFont().setSize(20);
titleStyle.setHorizontalAlignment(TextAlignmentType.CENTER);
titleCell.setStyle(titleStyle);

// Numéro et date de la facture
worksheet.getCells().get("B11").putValue("Invoice Number:");
worksheet.getCells().get("C11").putValue("INV-2024-001");
worksheet.getCells().get("B12").putValue("Date:");
worksheet.getCells().get("C12").putValue(new SimpleDateFormat("yyyy-MM-dd").format(new Date()));

// Section Facturer à
worksheet.getCells().get("B14").putValue("Bill To:");
worksheet.getCells().get("B15").putValue("Client Name");
worksheet.getCells().get("B16").putValue("Client Address");
worksheet.getCells().get("B17").putValue("Client City, State");

// En-tête des articles
Cell headerDesc = worksheet.getCells().get("B19");
Cell headerQty = worksheet.getCells().get("C19");
Cell headerPrice = worksheet.getCells().get("D19");
Cell headerTotal = worksheet.getCells().get("E19");

headerDesc.putValue("Description");
headerQty.putValue("Quantity");
headerPrice.putValue("Unit Price");
headerTotal.putValue("Total");

Style headerStyle = workbook.createStyle();
headerStyle.getFont().setBold(true);
headerStyle.getFont().setColor(Color.getWhite());
headerStyle.setBackgroundColor(Color.getNavy());
headerStyle.setHorizontalAlignment(TextAlignmentType.CENTER);
headerStyle.getBorders().getByBorderType(BorderType.TOP_BORDER).setLineStyle(CellBorderType.THIN);
headerStyle.getBorders().getByBorderType(BorderType.BOTTOM_BORDER).setLineStyle(CellBorderType.THIN);
headerStyle.getBorders().getByBorderType(BorderType.LEFT_BORDER).setLineStyle(CellBorderType.THIN);
headerStyle.getBorders().getByBorderType(BorderType.RIGHT_BORDER).setLineStyle(CellBorderType.THIN);

headerDesc.setStyle(headerStyle);
headerQty.setStyle(headerStyle);
headerPrice.setStyle(headerStyle);
headerTotal.setStyle(headerStyle);

// Style de devise avec bordures
Style currencyStyle = workbook.createStyle();
currencyStyle.setCustom("\"$\"#,##0.00");
currencyStyle.getBorders().getByBorderType(BorderType.TOP_BORDER).setLineStyle(CellBorderType.THIN);
currencyStyle.getBorders().getByBorderType(BorderType.BOTTOM_BORDER).setLineStyle(CellBorderType.THIN);
currencyStyle.getBorders().getByBorderType(BorderType.LEFT_BORDER).setLineStyle(CellBorderType.THIN);
currencyStyle.getBorders().getByBorderType(BorderType.RIGHT_BORDER).setLineStyle(CellBorderType.THIN);

// Style de bordure simple pour les cellules de description/quantité
Style borderStyle = workbook.createStyle();
borderStyle.getBorders().getByBorderType(BorderType.TOP_BORDER).setLineStyle(CellBorderType.THIN);
borderStyle.getBorders().getByBorderType(BorderType.BOTTOM_BORDER).setLineStyle(CellBorderType.THIN);
borderStyle.getBorders().getByBorderType(BorderType.LEFT_BORDER).setLineStyle(CellBorderType.THIN);
borderStyle.getBorders().getByBorderType(BorderType.RIGHT_BORDER).setLineStyle(CellBorderType.THIN);

// Lignes des articles
Object[][] lineItems = new Object[][] {
    {"Product A - Widget", 2, 50.00},
    {"Product B - Gadget", 3, 75.00},
    {"Product C - Service", 1, 100.00}
};

for (int i = 0; i < lineItems.length; i++)
{
    int row = 20 + i;
    Cell descCell = worksheet.getCells().get(row, 1);
    Cell qtyCell = worksheet.getCells().get(row, 2);
    Cell priceCell = worksheet.getCells().get(row, 3);
    Cell totalCell = worksheet.getCells().get(row, 4);

    descCell.putValue(lineItems[i][0]);
    qtyCell.putValue(lineItems[i][1]);
    priceCell.putValue(lineItems[i][2]);
    totalCell.setFormula("C" + row + "*D" + row);

    descCell.setStyle(borderStyle);
    qtyCell.setStyle(borderStyle);
    priceCell.setStyle(currencyStyle);
    totalCell.setStyle(currencyStyle);
}

// Sous-total, taxe, total général
worksheet.getCells().get("B24").putValue("Subtotal:");
Cell subtotalCell = worksheet.getCells().get("E24");
subtotalCell.setFormula("SUM(E20:E22)");

worksheet.getCells().get("B25").putValue("Tax (10%):");
Cell taxCell = worksheet.getCells().get("E25");
taxCell.setFormula("E24*0.1");

worksheet.getCells().get("B26").putValue("Grand Total:");
Cell grandTotalCell = worksheet.getCells().get("E26");
grandTotalCell.setFormula("E24+E25");

// Style gras + devise pour les valeurs totales
Style totalStyle = workbook.createStyle();
totalStyle.getFont().setBold(true);
totalStyle.setCustom("\"$\"#,##0.00");

subtotalCell.setStyle(totalStyle);
taxCell.setStyle(totalStyle);
grandTotalCell.setStyle(totalStyle);

// Style gras pour les étiquettes des totaux
Style boldStyle = workbook.createStyle();
boldStyle.getFont().setBold(true);

worksheet.getCells().get("B24").setStyle(boldStyle);
worksheet.getCells().get("B25").setStyle(boldStyle);
worksheet.getCells().get("B26").setStyle(boldStyle);

// Enregistrer le classeur en tant que fichier OFD
workbook.save(dataDir + "Invoice.ofd", SaveFormat.Ofd);
```
## **Conversion d'un fichier Excel existant en OFD**
Aspose.Cells peut également charger un classeur Excel existant depuis le disque et l'exporter directement au format OFD. Cela est utile pour les pipelines de conversion par lots, les flux d'archivage et les scénarios dans lesquels le classeur source a été produit par un autre outil et doit simplement être réémis en tant qu'artefact à mise en page fixe. L'exemple suivant charge un classeur `.xlsx` existant, lit les données de ses cellules, applique d'éventuels ajustements de mise en page, puis enregistre le résultat sous forme de document OFD.

```java
import com.aspose.cells.*;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

String dataDir = "C:\\Examples\\";

// Ouvrir un classeur Excel existant à partir du disque
Workbook workbook = new Workbook(dataDir + "SampleBook.xlsx");

// (1) Lire et afficher les valeurs des cellules sélectionnées pour confirmer que le fichier a été chargé
Worksheet firstSheet = workbook.getWorksheets().get(0);
System.out.println("First sheet name: " + firstSheet.getName());
System.out.println("Cell A1: " + firstSheet.getCells().get("A1").getStringValue());
System.out.println("Cell B1: " + firstSheet.getCells().get("B1").getStringValue());
System.out.println("Cell C1: " + firstSheet.getCells().get("C1").getStringValue());

// (2) Parcourir la collection Worksheets pour énumérer les feuilles disponibles
System.out.println("\nAvailable worksheets:");
for (int i = 0; i < workbook.getWorksheets().getCount(); i++)
{
    Worksheet ws = workbook.getWorksheets().get(i);
    System.out.println("  [" + i + "] " + ws.getName());
}

// (3) Optionnellement, mettre à jour une cellule d'horodatage pour refléter la conversion
String timestamp1 = LocalDateTime.now().format(DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss"));
firstSheet.getCells().get("A1").putValue("Converted on: " + timestamp1);

// Ajouter une ligne d'en-tête de résumé en haut du bloc de données
firstSheet.getCells().insertRow(0);
firstSheet.getCells().get("A1").putValue("Conversion Summary");

String timestamp2 = LocalDateTime.now().format(DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss"));
firstSheet.getCells().get("A2").putValue("Generated: " + timestamp2);

// (4) Configurer les propriétés PageSetup sur la feuille de calcul
PageSetup pageSetup = firstSheet.getPageSetup();
pageSetup.setOrientation(PageOrientationType.LANDSCAPE);
pageSetup.setPaperSize(PaperSizeType.PAPER_A_4);
pageSetup.setFitToPagesTall(1);
pageSetup.setFitToPagesWide(1);

// (5) Optionnellement, définir la zone d'impression pour la sortie OFD
int lastRow = firstSheet.getCells().getMaxDataRow();
int lastCol = firstSheet.getCells().getMaxDataColumn();
String lastColLetter = CellsHelper.columnIndexToName(lastCol);
String printArea = "A1:" + lastColLetter + (lastRow + 1);
firstSheet.getPageSetup().setPrintArea(printArea);
System.out.println("\nPrint area set to: " + printArea);

// (6) Enregistrer le classeur en tant que fichier OFD
workbook.save(dataDir + "SampleBook.ofd", SaveFormat.Ofd);
System.out.println("\nFile successfully converted to OFD format: " + dataDir + "SampleBook.ofd");
```

## **Articles connexes**
- [Fractionner des fichiers Excel en plusieurs fichiers](/cells/fr/java/splitting-excel-files-into-multiple-files/)
- [Insertion d'une image dans une cellule](/cells/fr/java/inserting-an-image-into-a-cell/)
- [Lecture et écriture de fichiers DBF](/cells/fr/java/dbf/)
- [Convertir un sparkline en image et HTML dans Aspose.Cells for Java](/cells/fr/java/convert-sparkline-to-image-and-html/)
{{< app/cells/assistant language="java" >}}