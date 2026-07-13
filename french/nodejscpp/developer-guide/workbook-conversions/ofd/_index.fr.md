---
title: Conversion d'Excel au format OFD
linktitle: Conversion d'Excel au format OFD
description: Aspose.Cells est une bibliothèque Node.js permettant de travailler avec des fichiers de tableurs qui prend en charge la conversion des classeurs Excel au format OFD (Open Fixed-layout Document). Cet article montre comment créer du contenu Excel et l'exporter en OFD, ainsi que comment convertir des fichiers Excel existants en OFD à l'aide d'Aspose.Cells.
keywords: Aspose.Cells, bibliothèque Node.js, tableur, Excel vers OFD, conversion OFD, SaveFormat.Ofd, document à mise en page fixe, export de classeur
type: docs
weight: 195
url: /fr/nodejs-cpp/converting-excel-to-ofd-format/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells prend en charge la conversion des classeurs Excel directement au format OFD (Open Fixed-layout Document) à l'aide de la valeur d'énumération `SaveFormat.Ofd`. Le document OFD résultant préserve la disposition visible du classeur, le contenu, les cellules fusionnées, les largeurs de colonnes, les hauteurs de lignes, les polices, les couleurs, les bordures et les formats numériques. Cela rend Aspose.Cells adapté aux flux de travail d'archivage, d'impression, de dépôt réglementaire et de soumission gouvernementale nécessitant une sortie à mise en page fixe.

{{% /alert %}}
## **Introduction**
OFD (Open Fixed-layout Document) est une norme nationale chinoise (GB/T 33190-2016) pour la représentation de documents numériques dans une mise en page fixe, basée sur les pages. Elle joue un rôle similaire à celui du PDF pour les cas d'utilisation où l'apparence visuelle du document source doit être préservée exactement comme elle a été conçue. Le format OFD est largement adopté pour les soumissions gouvernementales, les dépôts réglementaires, les factures électroniques et l'archivage à long terme en République populaire de Chine.

La conversion des classeurs Excel au format OFD est une exigence courante dans les scénarios où le contenu d'un tableur doit être distribué sous forme d'artefact en lecture seule, à mise en page verrouillée, plutôt que sous forme de tableur modifiable. Parmi les exemples, citons l'envoi d'une facture finalisée à un client, l'archivage d'un rapport financier trimestriel ou la soumission d'un tableur budgétaire à une autorité réglementaire. Aspose.Cells répond à cette exigence grâce à la valeur d'énumération `SaveFormat.Ofd`, qui écrit le classeur directement au format OFD sans nécessiter d'étape de conversion intermédiaire. La sortie OFD préserve les valeurs des cellules, les plages fusionnées, les polices, les couleurs, les bordures, les formats numériques et les options de mise en page configurées sur le classeur.

{{% alert color="primary" %}}

La sortie OFD générée par Aspose.Cells préserve la disposition visible du classeur source, y compris le contenu des cellules, les cellules fusionnées, les largeurs de colonnes et les hauteurs de lignes. La mise en forme des cellules telle que les polices, les couleurs, les bordures, l'alignement et les formats numériques est également rendue dans la sortie à mise en page fixe. Les options de mise en page configurées sur la feuille de calcul, telles que la taille du papier, l'orientation et la zone d'impression, influencent la mise en page du document OFD résultant.

{{% /alert %}}
## **Création d'un classeur Excel et enregistrement au format OFD**
Aspose.Cells vous permet de créer un classeur par programmation, de le remplir avec des données, puis de l'enregistrer directement au format OFD à l'aide de l'énumération `SaveFormat.Ofd`. L'exemple suivant crée une facture à partir de zéro. Il ajoute un logo d'entreprise, des informations d'en-tête, une section de facturation, des lignes d'articles et des totaux calculés, puis exporte le classeur vers un document OFD.
### **Création d'une facture avec un logo**
L'exemple construit une feuille de calcul de facture en insérant une image de logo dans la zone supérieure gauche, en remplissant le nom de l'entreprise et les coordonnées, en ajoutant un titre « INVOICE » sur des cellules fusionnées, en enregistrant le numéro et la date de la facture, en listant le client facturé, en construisant un tableau d'articles avec les colonnes de description, quantité, prix unitaire et total, et en calculant le sous-total, la taxe et le total général à l'aide de formules de cellules. La mise en forme telle que les en-têtes en gras, le format de devise pour les prix, les bordures et les largeurs de colonnes est appliquée à l'aide des objets `Style` et `Font`. Enfin, le classeur est enregistré avec l'extension `.ofd` en utilisant `SaveFormat.Ofd`.

```javascript
let dataDir = "C:\\Temp\\";

// Créer un nouveau classeur
let workbook = new AsposeCells.Workbook();

// Obtenir la première feuille de calcul
let worksheet = workbook.getWorksheets().get(0);

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
let titleCell = worksheet.getCells().get("B8");
titleCell.putValue("INVOICE");

let titleStyle = workbook.createStyle();
titleStyle.getFont().setIsBold(true);
titleStyle.getFont().setSize(20);
titleStyle.setHorizontalAlignment(AsposeCells.TextAlignmentType.Center);
titleCell.setStyle(titleStyle);

// Numéro et date de la facture
worksheet.getCells().get("B11").putValue("Invoice Number:");
worksheet.getCells().get("C11").putValue("INV-2024-001");
worksheet.getCells().get("B12").putValue("Date:");
let now = new Date();
let dateStr = `${now.getFullYear()}-${String(now.getMonth() + 1).padStart(2, '0')}-${String(now.getDate()).padStart(2, '0')}`;
worksheet.getCells().get("C12").putValue(dateStr);

// Section Facturation à
worksheet.getCells().get("B14").putValue("Bill To:");
worksheet.getCells().get("B15").putValue("Client Name");
worksheet.getCells().get("B16").putValue("Client Address");
worksheet.getCells().get("B17").putValue("Client City, State");

// En-tête des lignes d'articles
let headerDesc = worksheet.getCells().get("B19");
let headerQty = worksheet.getCells().get("C19");
let headerPrice = worksheet.getCells().get("D19");
let headerTotal = worksheet.getCells().get("E19");

headerDesc.putValue("Description");
headerQty.putValue("Quantity");
headerPrice.putValue("Unit Price");
headerTotal.putValue("Total");

let headerStyle = workbook.createStyle();
headerStyle.getFont().setIsBold(true);
headerStyle.getFont().setColor(AsposeCells.Color.White);
headerStyle.setBackgroundColor(AsposeCells.Color.Navy);
headerStyle.setHorizontalAlignment(AsposeCells.TextAlignmentType.Center);
headerStyle.getBorders().getByBorderType(AsposeCells.BorderType.TopBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
headerStyle.getBorders().getByBorderType(AsposeCells.BorderType.BottomBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
headerStyle.getBorders().getByBorderType(AsposeCells.BorderType.LeftBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
headerStyle.getBorders().getByBorderType(AsposeCells.BorderType.RightBorder).setLineStyle(AsposeCells.CellBorderType.Thin);

headerDesc.setStyle(headerStyle);
headerQty.setStyle(headerStyle);
headerPrice.setStyle(headerStyle);
headerTotal.setStyle(headerStyle);

// Style de devise avec bordures
let currencyStyle = workbook.createStyle();
currencyStyle.setCustom("\"$\"#,##0.00");
currencyStyle.getBorders().getByBorderType(AsposeCells.BorderType.TopBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
currencyStyle.getBorders().getByBorderType(AsposeCells.BorderType.BottomBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
currencyStyle.getBorders().getByBorderType(AsposeCells.BorderType.LeftBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
currencyStyle.getBorders().getByBorderType(AsposeCells.BorderType.RightBorder).setLineStyle(AsposeCells.CellBorderType.Thin);

// Style de bordure simple pour les cellules de description/quantité
let borderStyle = workbook.createStyle();
borderStyle.getBorders().getByBorderType(AsposeCells.BorderType.TopBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
borderStyle.getBorders().getByBorderType(AsposeCells.BorderType.BottomBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
borderStyle.getBorders().getByBorderType(AsposeCells.BorderType.LeftBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
borderStyle.getBorders().getByBorderType(AsposeCells.BorderType.RightBorder).setLineStyle(AsposeCells.CellBorderType.Thin);

// Lignes d'articles
let lineItems = [
    ["Product A - Widget", 2, 50.00],
    ["Product B - Gadget", 3, 75.00],
    ["Product C - Service", 1, 100.00]
];

for (let i = 0; i < lineItems.length; i++) {
    let row = 20 + i;
    let descCell = worksheet.getCells().get(row, 1);
    let qtyCell = worksheet.getCells().get(row, 2);
    let priceCell = worksheet.getCells().get(row, 3);
    let totalCell = worksheet.getCells().get(row, 4);

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
let subtotalCell = worksheet.getCells().get("E24");
subtotalCell.setFormula("SUM(E20:E22)");

worksheet.getCells().get("B25").putValue("Tax (10%):");
let taxCell = worksheet.getCells().get("E25");
taxCell.setFormula("E24*0.1");

worksheet.getCells().get("B26").putValue("Grand Total:");
let grandTotalCell = worksheet.getCells().get("E26");
grandTotalCell.setFormula("E24+E25");

// Style gras + devise pour les valeurs totales
let totalStyle = workbook.createStyle();
totalStyle.getFont().setIsBold(true);
totalStyle.setCustom("\"$\"#,##0.00");

subtotalCell.setStyle(totalStyle);
taxCell.setStyle(totalStyle);
grandTotalCell.setStyle(totalStyle);

// Style gras pour les étiquettes de totaux
let boldStyle = workbook.createStyle();
boldStyle.getFont().setIsBold(true);

worksheet.getCells().get("B24").setStyle(boldStyle);
worksheet.getCells().get("B25").setStyle(boldStyle);
worksheet.getCells().get("B26").setStyle(boldStyle);

// Enregistrer le classeur en tant que fichier OFD
workbook.save(dataDir + "Invoice.ofd", AsposeCells.SaveFormat.Ofd);
```
## **Conversion d'un fichier Excel existant au format OFD**
Aspose.Cells peut également charger un classeur Excel existant à partir du disque et l'exporter directement au format OFD. Cela est utile pour les pipelines de conversion par lots, les flux de travail d'archivage et les scénarios où le classeur source a été produit par un autre outil et doit simplement être réémis en tant qu'artefact à mise en page fixe. L'exemple suivant charge un classeur `.xlsx` existant, lit les données de ses cellules, applique des ajustements facultatifs de mise en page et enregistre le résultat sous forme de document OFD.

```javascript
let workbook = new AsposeCells.Workbook(dataDir + "SampleBook.xlsx");

// (1) Lire et afficher les valeurs des cellules sélectionnées pour confirmer que le fichier a été chargé
let firstSheet = workbook.getWorksheets().get(0);
console.log("First sheet name: " + firstSheet.getName());
console.log("Cell A1: " + firstSheet.getCells().get("A1").getStringValue());
console.log("Cell B1: " + firstSheet.getCells().get("B1").getStringValue());
console.log("Cell C1: " + firstSheet.getCells().get("C1").getStringValue());

// (2) Itérer sur la collection Worksheets pour énumérer les feuilles disponibles
console.log("\nAvailable worksheets:");
for (let i = 0; i < workbook.getWorksheets().getCount(); i++)
{
    let ws = workbook.getWorksheets().get(i);
    console.log("  [" + i + "] " + ws.getName());
}

// (3) Optionnellement, mettre à jour une cellule d'horodatage pour refléter la conversion
firstSheet.getCells().get("A1").putValue("Converted on: " + formatDate(new Date()));

// Insérer une ligne d'en-tête récapitulative en haut du bloc de données
firstSheet.getCells().insertRow(0);
firstSheet.getCells().get("A1").putValue("Conversion Summary");
firstSheet.getCells().get("A2").putValue("Generated: " + formatDate(new Date()));

// (4) Configurer les propriétés PageSetup sur la feuille de calcul
let pageSetup = firstSheet.getPageSetup();
pageSetup.setOrientation(AsposeCells.PageOrientationType.Landscape);
pageSetup.setPaperSize(AsposeCells.PaperSizeType.PaperA4);
pageSetup.setFitToPagesTall(1);
pageSetup.setFitToPagesWide(1);

// (5) Optionnellement, définir la zone d'impression pour la sortie OFD
let lastRow = firstSheet.getCells().getMaxDataRow();
let lastCol = firstSheet.getCells().getMaxDataColumn();
let lastColLetter = AsposeCells.CellsHelper.columnIndexToName(lastCol);
let printArea = "A1:" + lastColLetter + (lastRow + 1);
firstSheet.getPageSetup().setPrintArea(printArea);
console.log("\nPrint area set to: " + printArea);

// (6) Enregistrer le classeur en tant que fichier OFD
workbook.save(dataDir + "SampleBook.ofd", AsposeCells.SaveFormat.Ofd);
console.log("\nFile successfully converted to OFD format: " + dataDir + "SampleBook.ofd");
```

## **Articles connexes**
- [Fractionnement de fichiers Excel en plusieurs fichiers](/cells/fr/nodejs-cpp/splitting-excel-files-into-multiple-files/)
- [Insertion d'une image dans une cellule](/cells/fr/nodejs-cpp/inserting-an-image-into-a-cell/)
- [Lecture et écriture de fichiers DBF](/cells/fr/nodejs-cpp/dbf/)
- [Convertir un graphique sparkline en image et HTML dans Aspose.Cells for Node.js via C++](/cells/fr/nodejs-cpp/convert-sparkline-to-image-and-html/)
{{< app/cells/assistant language="javascript" >}}