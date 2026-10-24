---
title: Conversion d’Excel au format OFD
linktitle: Conversion d’Excel au format OFD
description: Aspose.Cells for Python via Java est une bibliothèque qui permet de travailler avec des fichiers de feuille de calcul et prend en charge la conversion des classeurs Excel au format OFD (Open Fixed-layout Document). Cet article explique comment créer du contenu Excel et l’exporter au format OFD, ainsi que comment convertir des fichiers Excel existants au format OFD à l’aide d’Aspose.Cells for Python via Java.
keywords: Aspose.Cells, bibliothèque Python via Java, feuille de calcul, conversion d’Excel en OFD, conversion OFD, SaveFormat.OFD, document à mise en page fixe, export de classeurs
type: docs
weight: 195
url: /fr/python-java/converting-excel-to-ofd-format/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells for Python via Java prend en charge la conversion directe des classeurs Excel au format OFD (Open Fixed-layout Document) à l’aide de la valeur d’énumération `SaveFormat.OFD`. Le document OFD obtenu préserve la mise en page visible et le contenu du classeur, ainsi que les cellules fusionnées, les largeurs des colonnes, les hauteurs des lignes, les polices, les couleurs, les bordures et les formats numériques. Cette fonctionnalité fait d’Aspose.Cells for Python via Java une solution adaptée aux flux de travail d’archivage, d’impression, de dépôt réglementaire et de transmission aux administrations qui exigent une sortie à mise en page fixe.
{{% /alert %}}

## **Introduction**
Le format OFD (Open Fixed-layout Document) est une norme nationale chinoise (GB/T 33190-2016) qui permet de représenter des documents numériques dans une mise en page fixe et structurée en pages. Il a un rôle comparable à celui du format PDF lorsque l’apparence visuelle du document source doit être conservée à l’identique. Le format OFD est largement utilisé pour les transmissions aux administrations, les dépôts réglementaires, les factures électroniques et l’archivage à long terme en République populaire de Chine.
La conversion des classeurs Excel en OFD est une exigence fréquente lorsque le contenu d’une feuille de calcul doit être distribué sous la forme d’un document en lecture seule dont la mise en page est verrouillée, plutôt que sous la forme d’une feuille de calcul modifiable. Les cas d’utilisation comprennent l’envoi d’une facture finalisée à un client, l’archivage d’un rapport financier trimestriel ou la soumission d’une feuille de calcul budgétaire à une autorité réglementaire. Aspose.Cells for Python via Java répond à ce besoin grâce à la valeur d’énumération `SaveFormat.OFD`, qui écrit le classeur directement au format OFD sans étape de conversion intermédiaire. Le document OFD produit préserve les valeurs des cellules, les plages fusionnées, les polices, les couleurs, les bordures, les formats numériques et les options de mise en page configurées dans le classeur.

{{% alert color="primary" %}}
Le document OFD généré par Aspose.Cells for Python via Java préserve la mise en page visible du classeur source, notamment le contenu des cellules, les cellules fusionnées, les largeurs des colonnes et les hauteurs des lignes. La mise en forme des cellules, notamment les polices, les couleurs, les bordures, l’alignement et les formats numériques, est également reproduite dans le document OFD à mise en page fixe. Les options de mise en page configurées sur la feuille de calcul, telles que le format du papier, l’orientation et la zone d’impression, influencent la mise en page du document OFD obtenu.
{{% /alert %}}

## **Création d’un classeur Excel et enregistrement au format OFD**
Aspose.Cells for Python via Java vous permet de créer un classeur par programme, de le renseigner avec des données, puis de l’enregistrer directement au format OFD à l’aide de la valeur d’énumération `SaveFormat.OFD`. L’exemple suivant crée une facture complète. Il ajoute un logo d’entreprise, des informations d’en-tête, une section consacrée au destinataire de la facture, des lignes de facture, puis calcule les totaux avant d’exporter le classeur vers un document OFD.

### **Création d’une facture avec un logo**
L’exemple construit une feuille de calcul dédiée à la facture en insérant le logo dans la zone supérieure gauche, en renseignant le nom de l’entreprise et ses coordonnées, en ajoutant un titre « FACTURE » sur plusieurs cellules fusionnées, en indiquant le numéro et la date de la facture, en mentionnant le client destinataire, en créant un tableau des lignes de facture comportant les colonnes « Description », « Quantité », « Prix unitaire » et « Total », et en calculant le sous-total, la taxe et le total général à l’aide de formules. Des éléments de mise en forme, tels que les en-têtes en gras, un format monétaire pour les prix, les bordures et les largeurs des colonnes, sont appliqués à l’aide des objets `Style` et `Font`. Enfin, le classeur est enregistré sous l’extension `.ofd` à l’aide de `SaveFormat.OFD`.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, Style, Cell, TextAlignmentType, BorderType, CellBorderType, Color
dataDir = "/tmp/"
# Créer un nouveau classeur
workbook = Workbook()
# Obtenir la première feuille de calcul
worksheet = workbook.getWorksheets().get(0)
# Définir la largeur des colonnes
worksheet.getCells().setColumnWidth(0, 5)
worksheet.getCells().setColumnWidth(1, 35)
worksheet.getCells().setColumnWidth(2, 12)
worksheet.getCells().setColumnWidth(3, 15)
worksheet.getCells().setColumnWidth(4, 15)
worksheet.getCells().setColumnWidth(5, 5)
# Insérer le logo de l’entreprise
worksheet.getPictures().add(1, 1, dataDir + "logo.png")
# Nom de l’entreprise et coordonnées
worksheet.getCells().get("B3").putValue("Acme Corporation")
worksheet.getCells().get("B4").putValue("123 Business Street")
worksheet.getCells().get("B5").putValue("City, State 12345")
worksheet.getCells().get("B6").putValue("Phone: (555) 123-4567")
# Titre FACTURE - fusionner les cellules
worksheet.getCells().merge(7, 1, 2, 4)
titleCell = worksheet.getCells().get("B8")
titleCell.putValue("INVOICE")
titleStyle = workbook.createStyle()
titleStyle.getFont().setBold(True)
titleStyle.getFont().setSize(20)
titleStyle.setHorizontalAlignment(TextAlignmentType.CENTER)
titleCell.setStyle(titleStyle)
# Numéro de facture et date
worksheet.getCells().get("B11").putValue("Invoice Number:")
worksheet.getCells().get("C11").putValue("INV-2024-001")
worksheet.getCells().get("B12").putValue("Date:")
worksheet.getCells().get("C12").putValue(datetime.datetime.now().strftime("%Y-%m-%d"))
# Section du destinataire
worksheet.getCells().get("B14").putValue("Bill To:")
worksheet.getCells().get("B15").putValue("Client Name")
worksheet.getCells().get("B16").putValue("Client Address")
worksheet.getCells().get("B17").putValue("Client City, State")
# En-tête des articles
headerDesc = worksheet.getCells().get("B19")
headerQty = worksheet.getCells().get("C19")
headerPrice = worksheet.getCells().get("D19")
headerTotal = worksheet.getCells().get("E19")
headerDesc.putValue("Description")
headerQty.putValue("Quantity")
headerPrice.putValue("Unit Price")
headerTotal.putValue("Total")
headerStyle = workbook.createStyle()
headerStyle.getFont().setBold(True)
headerStyle.getFont().setColor(Color.getWhite())
headerStyle.setBackgroundColor(Color.getNavy())
headerStyle.setHorizontalAlignment(TextAlignmentType.CENTER)
headerStyle.getBorders().getByBorderType(BorderType.TOP_BORDER).setLineStyle(CellBorderType.THIN)
headerStyle.getBorders().getByBorderType(BorderType.BOTTOM_BORDER).setLineStyle(CellBorderType.THIN)
headerStyle.getBorders().getByBorderType(BorderType.LEFT_BORDER).setLineStyle(CellBorderType.THIN)
headerStyle.getBorders().getByBorderType(BorderType.RIGHT_BORDER).setLineStyle(CellBorderType.THIN)
headerDesc.setStyle(headerStyle)
headerQty.setStyle(headerStyle)
headerPrice.setStyle(headerStyle)
headerTotal.setStyle(headerStyle)
# Style monétaire avec bordures
currencyStyle = workbook.createStyle()
currencyStyle.setCustom("\"$\"#,##0.00")
currencyStyle.getBorders().getByBorderType(BorderType.TOP_BORDER).setLineStyle(CellBorderType.THIN)
currencyStyle.getBorders().getByBorderType(BorderType.BOTTOM_BORDER).setLineStyle(CellBorderType.THIN)
currencyStyle.getBorders().getByBorderType(BorderType.LEFT_BORDER).setLineStyle(CellBorderType.THIN)
currencyStyle.getBorders().getByBorderType(BorderType.RIGHT_BORDER).setLineStyle(CellBorderType.THIN)
# Style de bordure simple pour les cellules de description/quantité
borderStyle = workbook.createStyle()
borderStyle.getBorders().getByBorderType(BorderType.TOP_BORDER).setLineStyle(CellBorderType.THIN)
borderStyle.getBorders().getByBorderType(BorderType.BOTTOM_BORDER).setLineStyle(CellBorderType.THIN)
borderStyle.getBorders().getByBorderType(BorderType.LEFT_BORDER).setLineStyle(CellBorderType.THIN)
borderStyle.getBorders().getByBorderType(BorderType.RIGHT_BORDER).setLineStyle(CellBorderType.THIN)
# Lignes d’articles
lineItems = [
    ["Product A - Widget", 2, 50.00],
    ["Product B - Gadget", 3, 75.00],
    ["Product C - Service", 1, 100.00]
]
for i in range(len(lineItems)):
    row = 20 + i
    descCell = worksheet.getCells().get(row, 1)
    qtyCell = worksheet.getCells().get(row, 2)
    priceCell = worksheet.getCells().get(row, 3)
    totalCell = worksheet.getCells().get(row, 4)
    descCell.putValue(lineItems[i][0])
    qtyCell.putValue(lineItems[i][1])
    priceCell.putValue(lineItems[i][2])
    totalCell.setFormula("C" + str(row) + "*D" + str(row))
    descCell.setStyle(borderStyle)
    qtyCell.setStyle(borderStyle)
    priceCell.setStyle(currencyStyle)
    totalCell.setStyle(currencyStyle)
# Sous-total, taxe et total général
worksheet.getCells().get("B24").putValue("Subtotal:")
subtotalCell = worksheet.getCells().get("E24")
subtotalCell.setFormula("SUM(E20:E22)")
worksheet.getCells().get("B25").putValue("Tax (10%):")
taxCell = worksheet.getCells().get("E25")
taxCell.setFormula("E24*0.1")
worksheet.getCells().get("B26").putValue("Grand Total:")
grandTotalCell = worksheet.getCells().get("E26")
grandTotalCell.setFormula("E24+E25")
# Style gras et monétaire pour les valeurs totales
totalStyle = workbook.createStyle()
totalStyle.getFont().setBold(True)
totalStyle.setCustom("\"$\"#,##0.00")
subtotalCell.setStyle(totalStyle)
taxCell.setStyle(totalStyle)
grandTotalCell.setStyle(totalStyle)
# Style gras pour les libellés de total
boldStyle = workbook.createStyle()
boldStyle.getFont().setBold(True)
worksheet.getCells().get("B24").setStyle(boldStyle)
worksheet.getCells().get("B25").setStyle(boldStyle)
worksheet.getCells().get("B26").setStyle(boldStyle)
# Enregistrer le classeur dans un fichier OFD
workbook.save(dataDir + "Invoice.ofd", SaveFormat.OFD)
jpype.shutdownJVM()
```

## **Conversion d’un fichier Excel existant en OFD**
Aspose.Cells for Python via Java permet également de charger un classeur Excel existant depuis le disque et de l’exporter directement au format OFD. Cette opération est utile pour les flux de conversion par lots, les flux d’archivage et les situations où le classeur source a été produit par un autre outil et doit uniquement être régénéré sous la forme d’un document à mise en page fixe. L’exemple suivant charge un classeur `.xlsx` existant, lit les données de ses cellules, applique des réglages facultatifs de mise en page, puis enregistre le résultat sous forme de document OFD.

```python
from datetime import datetime
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PageOrientationType, PaperSizeType, CellsHelper
dataDir = "C:\\Examples\\"
# Ouvrir un classeur Excel existant depuis le disque
workbook = Workbook(dataDir + "SampleBook.xlsx")
# (1) Lire et afficher les valeurs de certaines cellules pour confirmer le chargement du fichier
firstSheet = workbook.getWorksheets().get(0)
print("First sheet name: " + firstSheet.getName())
print("Cell A1: " + firstSheet.getCells().get("A1").getStringValue())
print("Cell B1: " + firstSheet.getCells().get("B1").getStringValue())
print("Cell C1: " + firstSheet.getCells().get("C1").getStringValue())
# (2) Parcourir la collection Worksheets pour énumérer les feuilles disponibles
print("\nAvailable worksheets:")
for i in range(workbook.getWorksheets().getCount()):
    ws = workbook.getWorksheets().get(i)
    print("  [" + str(i) + "] " + ws.getName())
# (3) Facultativement, mettre à jour une cellule d'horodatage pour refléter la conversion
firstSheet.getCells().get("A1").putValue("Converted on: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
# Ajouter une ligne d'en-tête récapitulative en haut du bloc de données
firstSheet.getCells().insertRow(0)
firstSheet.getCells().get("A1").putValue("Conversion Summary")
firstSheet.getCells().get("A2").putValue("Generated: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
# (4) Configurer les propriétés PageSetup de la feuille de calcul
pageSetup = firstSheet.getPageSetup()
pageSetup.setOrientation(PageOrientationType.LANDSCAPE)
pageSetup.setPaperSize(PaperSizeType.PAPER_A_4)
pageSetup.setFitToPagesTall(1)
pageSetup.setFitToPagesWide(1)
# (5) Facultativement, définir la zone d'impression pour la sortie OFD
lastRow = firstSheet.getCells().getMaxDataRow()
lastCol = firstSheet.getCells().getMaxDataColumn()
lastColLetter = CellsHelper.columnIndexToName(lastCol)
printArea = "A1:" + lastColLetter + str(lastRow + 1)
firstSheet.getPageSetup().setPrintArea(printArea)
print("\nPrint area set to: " + printArea)
# (6) Enregistrer le classeur dans un fichier OFD
workbook.save(dataDir + "SampleBook.ofd", SaveFormat.OFD)
print("\nFile successfully converted to OFD format: " + dataDir + "SampleBook.ofd")
jpype.shutdownJVM()
```

{{< app/cells/assistant language="python" >}}