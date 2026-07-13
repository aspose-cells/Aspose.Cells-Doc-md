---
title: Conversion d'Excel au format OFD
linktitle: Conversion d'Excel au format OFD
description: Aspose.Cells for Python via Java est une bibliothèque permettant de travailler avec des fichiers de feuilles de calcul qui prend en charge la conversion de classeurs Excel au format OFD (Open Fixed-layout Document). Cet article montre comment créer du contenu Excel et l'exporter au format OFD, ainsi que comment convertir des fichiers Excel existants au format OFD à l'aide d'Aspose.Cells for Python via Java.
keywords: Aspose.Cells, Python via Java library, spreadsheet, Excel to OFD, OFD conversion, SaveFormat.Ofd, fixed-layout document, workbook export
type: docs
weight: 195
url: /fr/python-java/converting-excel-to-ofd-format/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells for Python via Java prend en charge la conversion directe des classeurs Excel au format OFD (Open Fixed-layout Document) en utilisant la valeur d'énumération `SaveFormat.Ofd`. Le document OFD résultant préserve la disposition visible du classeur, le contenu, les cellules fusionnées, les largeurs de colonnes, les hauteurs de lignes, les polices, les couleurs, les bordures et les formats de nombres. Cela rend Aspose.Cells for Python via Java adapté aux flux de travail d'archivage, d'impression, de dépôt réglementaire et de soumission gouvernementale qui nécessitent une sortie à mise en page fixe.

{{% /alert %}}
## **Introduction**
OFD (Open Fixed-layout Document) est une norme nationale chinoise (GB/T 33190-2016) pour la représentation de documents numériques dans une mise en page fixe, basée sur des pages. Il joue un rôle similaire au PDF pour les cas d'utilisation où l'apparence visuelle du document source doit être préservée exactement telle qu'elle a été conçue. OFD est largement adopté pour les soumissions gouvernementales, les dépôts réglementaires, les factures électroniques et l'archivage à long terme en République populaire de Chine.

La conversion des classeurs Excel au format OFD est une exigence courante dans les scénarios où le contenu des feuilles de calcul doit être distribué sous forme d'artefact en lecture seule, à mise en page verrouillée, plutôt que comme une feuille de calcul modifiable. Les exemples incluent l'envoi d'une facture finalisée à un client, l'archivage d'un rapport financier trimestriel ou la soumission d'une feuille de calcul budgétaire à une autorité réglementaire. Aspose.Cells for Python via Java répond à cette exigence grâce à la valeur d'énumération `SaveFormat.Ofd`, qui écrit le classeur directement au format OFD sans nécessiter d'étape de conversion intermédiaire. La sortie OFD préserve les valeurs des cellules, les plages fusionnées, les polices, les couleurs, les bordures, les formats de nombres et les options de mise en page configurées sur le classeur.

{{% alert color="primary" %}}

La sortie OFD générée par Aspose.Cells for Python via Java préserve la disposition visible du classeur source, y compris le contenu des cellules, les cellules fusionnées, les largeurs de colonnes et les hauteurs de lignes. La mise en forme des cellules, telle que les polices, les couleurs, les bordures, l'alignement et les formats de nombres, est également rendue dans la sortie à mise en page fixe. Les options de mise en page configurées sur la feuille de calcul, telles que le format du papier, l'orientation et la zone d'impression, influencent la mise en page du document OFD résultant.

{{% /alert %}}
## **Création d'un classeur Excel et enregistrement au format OFD**
Aspose.Cells for Python via Java vous permet de construire un classeur par programmation, de le remplir avec des données, puis de l'enregistrer directement au format OFD en utilisant l'énumération `SaveFormat.Ofd`. L'exemple suivant crée une facture à partir de zéro. Il ajoute un logo d'entreprise, des informations d'en-tête, une section de facturation, des articles de ligne et des totaux calculés, puis exporte le classeur vers un document OFD.
### **Construction d'une facture avec un logo**
L'exemple construit une feuille de calcul de facture en insérant une image de logo dans la zone supérieure gauche, en remplissant le nom de l'entreprise et les coordonnées, en ajoutant un titre « INVOICE » dans des cellules fusionnées, en enregistrant le numéro et la date de la facture, en listant le client facturé, en construisant un tableau d'articles avec les colonnes description, quantité, prix unitaire et total, et en calculant le sous-total, la taxe et le total général à l'aide de formules de cellules. La mise en forme, telle que les en-têtes en gras, le format monétaire pour les prix, les bordures et les largeurs de colonnes, est appliquée à l'aide des objets `Style` et `Font`. Enfin, le classeur est enregistré avec l'extension `.ofd` en utilisant `SaveFormat.Ofd`.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, Style, Cell, TextAlignmentType, BorderType, CellBorderType, Color

dataDir = "/tmp/"

# Créer un nouveau classeur
workbook = Workbook()

# Obtenir la première feuille de calcul
worksheet = workbook.getWorksheets().get(0)

# Définir les largeurs de colonnes
worksheet.getCells().setColumnWidth(0, 5)
worksheet.getCells().setColumnWidth(1, 35)
worksheet.getCells().setColumnWidth(2, 12)
worksheet.getCells().setColumnWidth(3, 15)
worksheet.getCells().setColumnWidth(4, 15)
worksheet.getCells().setColumnWidth(5, 5)

# Insérer le logo de l'entreprise
worksheet.getPictures().add(1, 1, dataDir + "logo.png")

# Nom de l'entreprise et coordonnées
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

# Section Facturer à
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
headerStyle.getBorders().get(BorderType.TOP_BORDER).setLineStyle(CellBorderType.THIN)
headerStyle.getBorders().get(BorderType.BOTTOM_BORDER).setLineStyle(CellBorderType.THIN)
headerStyle.getBorders().get(BorderType.LEFT_BORDER).setLineStyle(CellBorderType.THIN)
headerStyle.getBorders().get(BorderType.RIGHT_BORDER).setLineStyle(CellBorderType.THIN)

headerDesc.setStyle(headerStyle)
headerQty.setStyle(headerStyle)
headerPrice.setStyle(headerStyle)
headerTotal.setStyle(headerStyle)

# Style monétaire avec bordures
currencyStyle = workbook.createStyle()
currencyStyle.setCustom("\"$\"#,##0.00")
currencyStyle.getBorders().get(BorderType.TOP_BORDER).setLineStyle(CellBorderType.THIN)
currencyStyle.getBorders().get(BorderType.BOTTOM_BORDER).setLineStyle(CellBorderType.THIN)
currencyStyle.getBorders().get(BorderType.LEFT_BORDER).setLineStyle(CellBorderType.THIN)
currencyStyle.getBorders().get(BorderType.RIGHT_BORDER).setLineStyle(CellBorderType.THIN)

# Style de bordure simple pour les cellules description/quantité
borderStyle = workbook.createStyle()
borderStyle.getBorders().get(BorderType.TOP_BORDER).setLineStyle(CellBorderType.THIN)
borderStyle.getBorders().get(BorderType.BOTTOM_BORDER).setLineStyle(CellBorderType.THIN)
borderStyle.getBorders().get(BorderType.LEFT_BORDER).setLineStyle(CellBorderType.THIN)
borderStyle.getBorders().get(BorderType.RIGHT_BORDER).setLineStyle(CellBorderType.THIN)

# Lignes des articles
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

# Sous-total, taxe, total général
worksheet.getCells().get("B24").putValue("Subtotal:")
subtotalCell = worksheet.getCells().get("E24")
subtotalCell.setFormula("SUM(E20:E22)")

worksheet.getCells().get("B25").putValue("Tax (10%):")
taxCell = worksheet.getCells().get("E25")
taxCell.setFormula("E24*0.1")

worksheet.getCells().get("B26").putValue("Grand Total:")
grandTotalCell = worksheet.getCells().get("E26")
grandTotalCell.setFormula("E24+E25")

# Style gras + monétaire pour les valeurs totales
totalStyle = workbook.createStyle()
totalStyle.getFont().setBold(True)
totalStyle.setCustom("\"$\"#,##0.00")

subtotalCell.setStyle(totalStyle)
taxCell.setStyle(totalStyle)
grandTotalCell.setStyle(totalStyle)

# Style gras pour les étiquettes de totaux
boldStyle = workbook.createStyle()
boldStyle.getFont().setBold(True)

worksheet.getCells().get("B24").setStyle(boldStyle)
worksheet.getCells().get("B25").setStyle(boldStyle)
worksheet.getCells().get("B26").setStyle(boldStyle)

# Enregistrer le classeur en tant que fichier OFD
workbook.save(dataDir + "Invoice.ofd", SaveFormat.Ofd)

jpype.shutdownJVM()
```
## **Conversion d'un fichier Excel existant au format OFD**
Aspose.Cells for Python via Java peut également charger un classeur Excel existant à partir du disque et l'exporter directement au format OFD. Cela est utile pour les pipelines de conversion par lots, les flux de travail d'archivage et les scénarios où le classeur source a été produit par un autre outil et doit simplement être réémis sous forme d'artefact à mise en page fixe. L'exemple suivant charge un classeur `.xlsx` existant, lit les données de ses cellules, applique des ajustements facultatifs de mise en page et enregistre le résultat sous forme de document OFD.

```python
from datetime import datetime
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PageOrientationType, PaperSizeType, CellsHelper

dataDir = "C:\\Examples\\"

# Ouvrir un classeur Excel existant à partir du disque
workbook = Workbook(dataDir + "SampleBook.xlsx")

# (1) Lire et afficher les valeurs des cellules sélectionnées pour confirmer que le fichier a été chargé
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

# (3) Optionnellement, mettre à jour une cellule d'horodatage pour refléter la conversion
firstSheet.getCells().get("A1").putValue("Converted on: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# Ajouter une ligne d'en-tête récapitulative en haut du bloc de données
firstSheet.getCells().insertRow(0)
firstSheet.getCells().get("A1").putValue("Conversion Summary")
firstSheet.getCells().get("A2").putValue("Generated: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# (4) Configurer les propriétés de PageSetup sur la feuille de calcul
pageSetup = firstSheet.getPageSetup()
pageSetup.setOrientation(PageOrientationType.LANDSCAPE)
pageSetup.setPaperSize(PaperSizeType.PAPER_A_4)
pageSetup.setFitToPagesTall(1)
pageSetup.setFitToPagesWide(1)

# (5) Optionnellement, définir la zone d'impression pour la sortie OFD
lastRow = firstSheet.getCells().getMaxDataRow()
lastCol = firstSheet.getCells().getMaxDataColumn()
lastColLetter = CellsHelper.columnIndexToName(lastCol)
printArea = "A1:" + lastColLetter + str(lastRow + 1)
firstSheet.getPageSetup().setPrintArea(printArea)
print("\nPrint area set to: " + printArea)

# (6) Enregistrer le classeur en tant que fichier OFD
workbook.save(dataDir + "SampleBook.ofd", SaveFormat.Ofd)
print("\nFile successfully converted to OFD format: " + dataDir + "SampleBook.ofd")

jpype.shutdownJVM()
```

## **Articles connexes**
- [Fractionnement de fichiers Excel en plusieurs fichiers](/cells/fr/python-java/splitting-excel-files-into-multiple-files/)
- [Insertion d'une image dans une cellule](/cells/fr/python-java/inserting-an-image-into-a-cell/)
- [Lecture et écriture de fichiers DBF](/cells/fr/python-java/dbf/)
- [Convertir un sparkline en image et HTML dans Aspose.Cells for Python via Java](/cells/fr/python-java/convert-sparkline-to-image-and-html/)
{{< app/cells/assistant language="python" >}}