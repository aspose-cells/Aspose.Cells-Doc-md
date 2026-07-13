---
title: Conversion d'Excel au format OFD
linktitle: Conversion d'Excel au format OFD
description: Aspose.Cells for Python via .NET est une bibliothèque de traitement de feuilles de calcul qui prend en charge la conversion des classeurs Excel au format OFD (Open Fixed-layout Document). Cet article montre comment créer du contenu Excel et l'exporter en OFD, ainsi que comment convertir des fichiers Excel existants en OFD à l'aide d'Aspose.Cells.
keywords: Aspose.Cells, bibliothèque Python via .NET, feuille de calcul, Excel vers OFD, conversion OFD, SaveFormat.Ofd, document à mise en page fixe, export de classeur
type: docs
weight: 195
url: /fr/python-net/converting-excel-to-ofd-format/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells prend en charge la conversion directe des classeurs Excel au format OFD (Open Fixed-layout Document) à l'aide de la valeur d'énumération `SaveFormat.Ofd`. Le document OFD résultant préserve la mise en page visible du classeur, le contenu, les cellules fusionnées, les largeurs de colonnes, les hauteurs de lignes, les polices, les couleurs, les bordures et les formats numériques. Cela rend Aspose.Cells adapté aux workflows d'archivage, d'impression, de dépôt réglementaire et de soumission gouvernementale qui nécessitent une sortie à mise en page fixe.

{{% /alert %}}
## **Introduction**
OFD (Open Fixed-layout Document) est une norme nationale chinoise (GB/T 33190-2016) pour représenter des documents numériques dans une mise en page fixe, basée sur des pages. Elle joue un rôle similaire à celui du PDF pour les cas d'utilisation où l'apparence visuelle du document source doit être conservée exactement telle qu'elle a été créée. L'OFD est largement adopté pour les soumissions gouvernementales, les dépôts réglementaires, les factures électroniques et l'archivage à long terme en République populaire de Chine.

La conversion de classeurs Excel en OFD est une exigence courante dans les scénarios où le contenu d'une feuille de calcul doit être distribué sous forme d'artefact en lecture seule, à mise en page verrouillée, plutôt qu'en tant que feuille de calcul modifiable. Parmi les exemples, citons l'envoi d'une facture finalisée à un client, l'archivage d'un rapport financier trimestriel ou la soumission d'une feuille de calcul budgétaire à une autorité réglementaire. Aspose.Cells répond à cette exigence grâce à la valeur d'énumération `SaveFormat.Ofd`, qui écrit le classeur directement au format OFD sans nécessiter d'étape de conversion intermédiaire. La sortie OFD préserve les valeurs des cellules, les plages fusionnées, les polices, les couleurs, les bordures, les formats numériques et les options de mise en page configurées sur le classeur.

{{% alert color="primary" %}}

La sortie OFD générée par Aspose.Cells préserve la mise en page visible du classeur source, y compris le contenu des cellules, les cellules fusionnées, les largeurs de colonnes et les hauteurs de lignes. La mise en forme des cellules, telle que les polices, les couleurs, les bordures, l'alignement et les formats numériques, est également rendue dans la sortie à mise en page fixe. Les options de mise en page configurées sur la feuille de calcul, telles que le format du papier, l'orientation et la zone d'impression, influencent la mise en page du document OFD résultant.

{{% /alert %}}
## **Création d'un classeur Excel et enregistrement en tant qu'OFD**
Aspose.Cells vous permet de créer un classeur par programmation, de le remplir avec des données, puis de l'enregistrer directement au format OFD à l'aide de l'énumération `SaveFormat.Ofd`. L'exemple suivant crée une facture à partir de zéro. Il ajoute un logo d'entreprise, les informations d'en-tête, une section de facturation, les lignes d'articles et les totaux calculés, puis exporte le classeur vers un document OFD.
### **Construction d'une facture avec un logo**
L'exemple construit une feuille de calcul de facture en insérant une image de logo dans la zone supérieure gauche, en remplissant le nom de l'entreprise et les coordonnées, en ajoutant un titre « FACTURE » sur des cellules fusionnées, en enregistrant le numéro et la date de la facture, en listant le client facturé, en construisant un tableau de lignes d'articles avec les colonnes de description, quantité, prix unitaire et total, et en calculant le sous-total, la taxe et le total général à l'aide de formules de cellules. La mise en forme, telle que les en-têtes en gras, le format monétaire pour les prix, les bordures et les largeurs de colonnes, est appliquée à l'aide des objets `Style` et `Font`. Enfin, le classeur est enregistré avec l'extension `.ofd` à l'aide de `SaveFormat.Ofd`.

```python
from datetime import datetime

data_dir = "C:\\Temp\\"

# Créer un nouveau classeur
workbook = ac.Workbook()

# Obtenir la première feuille de calcul
worksheet = workbook.worksheets[0]

# Définir les largeurs de colonnes
worksheet.cells.set_column_width(0, 5)
worksheet.cells.set_column_width(1, 35)
worksheet.cells.set_column_width(2, 12)
worksheet.cells.set_column_width(3, 15)
worksheet.cells.set_column_width(4, 15)
worksheet.cells.set_column_width(5, 5)

# Insérer le logo de l'entreprise
worksheet.pictures.add(1, 1, data_dir + "logo.png")

# Nom de l'entreprise et coordonnées
worksheet.cells["B3"].put_value("Acme Corporation")
worksheet.cells["B4"].put_value("123 Business Street")
worksheet.cells["B5"].put_value("City, State 12345")
worksheet.cells["B6"].put_value("Phone: (555) 123-4567")

# Titre FACTURE - fusionner les cellules
worksheet.cells.merge(7, 1, 2, 4)
title_cell = worksheet.cells["B8"]
title_cell.put_value("INVOICE")

title_style = workbook.create_style()
title_style.font.is_bold = True
title_style.font.size = 20
title_style.horizontal_alignment = ac.TextAlignmentType.CENTER
title_cell.set_style(title_style)

# Numéro de facture et date
worksheet.cells["B11"].put_value("Invoice Number:")
worksheet.cells["C11"].put_value("INV-2024-001")
worksheet.cells["B12"].put_value("Date:")
worksheet.cells["C12"].put_value(datetime.now().strftime("%Y-%m-%d"))

# Section Facturer à
worksheet.cells["B14"].put_value("Bill To:")
worksheet.cells["B15"].put_value("Client Name")
worksheet.cells["B16"].put_value("Client Address")
worksheet.cells["B17"].put_value("Client City, State")

# En-tête des articles de la ligne
header_desc = worksheet.cells["B19"]
header_qty = worksheet.cells["C19"]
header_price = worksheet.cells["D19"]
header_total = worksheet.cells["E19"]

header_desc.put_value("Description")
header_qty.put_value("Quantity")
header_price.put_value("Unit Price")
header_total.put_value("Total")

header_style = workbook.create_style()
header_style.font.is_bold = True
header_style.font.color = drawing.Color.white
header_style.background_color = drawing.Color.navy
header_style.horizontal_alignment = ac.TextAlignmentType.CENTER
header_style.borders[ac.BorderType.TOP_BORDER].line_style = ac.CellBorderType.THIN
header_style.borders[ac.BorderType.BOTTOM_BORDER].line_style = ac.CellBorderType.THIN
header_style.borders[ac.BorderType.LEFT_BORDER].line_style = ac.CellBorderType.THIN
header_style.borders[ac.BorderType.RIGHT_BORDER].line_style = ac.CellBorderType.THIN

header_desc.set_style(header_style)
header_qty.set_style(header_style)
header_price.set_style(header_style)
header_total.set_style(header_style)

# Style de devise avec bordures
currency_style = workbook.create_style()
currency_style.custom = "\"$\"#,##0.00"
currency_style.borders[ac.BorderType.TOP_BORDER].line_style = ac.CellBorderType.THIN
currency_style.borders[ac.BorderType.BOTTOM_BORDER].line_style = ac.CellBorderType.THIN
currency_style.borders[ac.BorderType.LEFT_BORDER].line_style = ac.CellBorderType.THIN
currency_style.borders[ac.BorderType.RIGHT_BORDER].line_style = ac.CellBorderType.THIN

# Style de bordure simple pour les cellules de description/quantité
border_style = workbook.create_style()
border_style.borders[ac.BorderType.TOP_BORDER].line_style = ac.CellBorderType.THIN
border_style.borders[ac.BorderType.BOTTOM_BORDER].line_style = ac.CellBorderType.THIN
border_style.borders[ac.BorderType.LEFT_BORDER].line_style = ac.CellBorderType.THIN
border_style.borders[ac.BorderType.RIGHT_BORDER].line_style = ac.CellBorderType.THIN

# Lignes des articles
line_items = [
    ["Product A - Widget", 2, 50.00],
    ["Product B - Gadget", 3, 75.00],
    ["Product C - Service", 1, 100.00]
]

for i in range(len(line_items)):
    row = 20 + i
    desc_cell = worksheet.cells[row, 1]
    qty_cell = worksheet.cells[row, 2]
    price_cell = worksheet.cells[row, 3]
    total_cell = worksheet.cells[row, 4]

    desc_cell.put_value(line_items[i][0])
    qty_cell.put_value(line_items[i][1])
    price_cell.put_value(line_items[i][2])
    total_cell.formula = "C" + str(row) + "*D" + str(row)

    desc_cell.set_style(border_style)
    qty_cell.set_style(border_style)
    price_cell.set_style(currency_style)
    total_cell.set_style(currency_style)

# Sous-total, taxe, total général
worksheet.cells["B24"].put_value("Subtotal:")
subtotal_cell = worksheet.cells["E24"]
subtotal_cell.formula = "SUM(E20:E22)"

worksheet.cells["B25"].put_value("Tax (10%):")
tax_cell = worksheet.cells["E25"]
tax_cell.formula = "E24*0.1"

worksheet.cells["B26"].put_value("Grand Total:")
grand_total_cell = worksheet.cells["E26"]
grand_total_cell.formula = "E24+E25"

# Style gras + devise pour les valeurs totales
total_style = workbook.create_style()
total_style.font.is_bold = True
total_style.custom = "\"$\"#,##0.00"

subtotal_cell.set_style(total_style)
tax_cell.set_style(total_style)
grand_total_cell.set_style(total_style)

# Style gras pour les étiquettes des totaux
bold_style = workbook.create_style()
bold_style.font.is_bold = True

worksheet.cells["B24"].set_style(bold_style)
worksheet.cells["B25"].set_style(bold_style)
worksheet.cells["B26"].set_style(bold_style)

# Enregistrer le classeur en tant que fichier OFD
workbook.save(data_dir + "Invoice.ofd", ac.SaveFormat.Ofd)
```
## **Conversion d'un fichier Excel existant en OFD**
Aspose.Cells peut également charger un classeur Excel existant à partir du disque et l'exporter directement au format OFD. Cela est utile pour les pipelines de conversion par lots, les workflows d'archivage et les scénarios où le classeur source a été produit par un autre outil et doit simplement être réémis en tant qu'artefact à mise en page fixe. L'exemple suivant charge un classeur `.xlsx` existant, lit les données de ses cellules, applique des ajustements optionnels de mise en page et enregistre le résultat en tant que document OFD.

```python
from datetime import datetime

dataDir = "C:\\Examples\\"

# Ouvrir un classeur Excel existant à partir du disque
workbook = ac.Workbook(dataDir + "SampleBook.xlsx")

# (1) Lire et afficher les valeurs des cellules sélectionnées pour confirmer le chargement du fichier
firstSheet = workbook.worksheets[0]
print("First sheet name: " + firstSheet.name)
print("Cell A1: " + firstSheet.cells["A1"].string_value)
print("Cell B1: " + firstSheet.cells["B1"].string_value)
print("Cell C1: " + firstSheet.cells["C1"].string_value)

# (2) Parcourir la collection Worksheets pour énumérer les feuilles disponibles
print("\nAvailable worksheets:")
for i in range(workbook.worksheets.count):
    ws = workbook.worksheets[i]
    print("  [" + str(i) + "] " + ws.name)

# (3) Optionnellement, mettre à jour une cellule d'horodatage pour refléter la conversion
firstSheet.cells["A1"].put_value("Converted on: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# Ajouter une ligne d'en-tête récapitulative en haut du bloc de données
firstSheet.cells.insert_row(0)
firstSheet.cells["A1"].put_value("Conversion Summary")
firstSheet.cells["A2"].put_value("Generated: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# (4) Configurer les propriétés PageSetup sur la feuille de calcul
pageSetup = firstSheet.page_setup
pageSetup.orientation = ac.PageOrientationType.LANDSCAPE
pageSetup.paper_size = ac.PaperSizeType.PAPER_A4
pageSetup.fit_to_pages_tall = 1
pageSetup.fit_to_pages_wide = 1

# (5) Optionnellement, définir la zone d'impression pour la sortie OFD
lastRow = firstSheet.cells.max_data_row
lastCol = firstSheet.cells.max_data_column
lastColLetter = ac.CellsHelper.column_index_to_name(lastCol)
printArea = "A1:" + lastColLetter + str(lastRow + 1)
firstSheet.page_setup.print_area = printArea
print("\nPrint area set to: " + printArea)

# (6) Enregistrer le classeur en tant que fichier OFD
workbook.save(dataDir + "SampleBook.ofd", ac.SaveFormat.Ofd)
print("\nFile successfully converted to OFD format: " + dataDir + "SampleBook.ofd")
```

## **Articles connexes**
- [Fractionnement de fichiers Excel en plusieurs fichiers](/cells/fr/python-net/splitting-excel-files-into-multiple-files/)
- [Insertion d'une image dans une cellule](/cells/fr/python-net/inserting-an-image-into-a-cell/)
- [Lecture et écriture de fichiers DBF](/cells/fr/python-net/dbf/)
- [Convertir une sparkline en image et HTML dans Aspose.Cells pour Aspose.Cells for Python via .NET](/cells/fr/python-net/convert-sparkline-to-image-and-html/)
{{< app/cells/assistant language="python" >}}