---
title: Conversion d'Excel au format OFD
description: Aspose.Cells est une bibliothèque .NET pour travailler avec des fichiers de feuilles de calcul qui prend en charge la conversion des classeurs Excel au format OFD (Open Fixed-layout Document). Cet article montre comment créer du contenu Excel et l'exporter en tant qu'OFD, ainsi que comment convertir des fichiers Excel existants en OFD à l'aide d'Aspose.Cells.
linktitle: Conversion d'Excel au format OFD
keywords: Aspose.Cells, bibliothèque NET, feuille de calcul, Excel vers OFD, conversion OFD, SaveFormat.Ofd, document à mise en page fixe, export de classeur
type: docs
weight: 195
url: /fr/net/converting-excel-to-ofd-format/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells prend en charge la conversion des classeurs Excel directement au format OFD (Open Fixed-layout Document) à l'aide de la valeur d'énumération `SaveFormat.Ofd`. Le document OFD résultant préserve la mise en page visible du classeur, le contenu, les cellules fusionnées, les largeurs de colonnes, les hauteurs de lignes, les polices, les couleurs, les bordures et les formats de nombres. Cela rend Aspose.Cells adapté aux flux de travail d'archivage, d'impression, de dépôt réglementaire et de soumission gouvernementale qui nécessitent une sortie à mise en page fixe.
{{% /alert %}}

## **Introduction**
OFD (Open Fixed-layout Document) est une norme nationale chinoise (GB/T 33190-2016) pour représenter des documents numériques dans une mise en page fixe, basée sur des pages. Elle joue un rôle similaire à celui du PDF pour les cas d'utilisation où l'apparence visuelle du document source doit être préservée exactement telle qu'elle a été conçue. L'OFD est largement adopté pour les soumissions gouvernementales, les dépôts réglementaires, les factures électroniques et l'archivage à long terme en République populaire de Chine.
La conversion des classeurs Excel en OFD est une exigence courante dans les scénarios où le contenu d'une feuille de calcul doit être distribué sous forme d'artefact en lecture seule et à mise en page verrouillée plutôt que sous forme de feuille de calcul modifiable. Parmi les exemples, citons l'envoi d'une facture finalisée à un client, l'archivage d'un rapport financier trimestriel ou la soumission d'une feuille de calcul budgétaire à une autorité réglementaire. Aspose.Cells répond à cette exigence grâce à la valeur d'énumération `SaveFormat.Ofd`, qui écrit le classeur directement en OFD sans nécessiter d'étape de conversion intermédiaire. La sortie OFD préserve les valeurs des cellules, les plages fusionnées, les polices, les couleurs, les bordures, les formats de nombres et les options de mise en page configurées sur le classeur.

{{% alert color="primary" %}}
La sortie OFD générée par Aspose.Cells préserve la mise en page visible du classeur source, y compris le contenu des cellules, les cellules fusionnées, les largeurs de colonnes et les hauteurs de lignes. La mise en forme des cellules telle que les polices, les couleurs, les bordures, l'alignement et les formats de nombres est également restituée dans la sortie à mise en page fixe. Les options de mise en page configurées sur la feuille de calcul, telles que le format du papier, l'orientation et la zone d'impression, influencent la mise en page du document OFD résultant.
{{% /alert %}}

## **Création d'un classeur Excel et enregistrement au format OFD**
Aspose.Cells vous permet de construire un classeur par programmation, de le remplir avec des données, puis de l'enregistrer directement au format OFD à l'aide de l'énumération `SaveFormat.Ofd`. L'exemple suivant crée une facture à partir de zéro. Il ajoute un logo d'entreprise, des informations d'en-tête, une section de facturation, des lignes d'articles et des totaux calculés, puis exporte le classeur vers un document OFD.

### **Construction d'une facture avec un logo**
L'exemple construit une feuille de calcul de facture en insérant une image de logo dans la zone supérieure gauche, en remplissant le nom de l'entreprise et les coordonnées, en ajoutant un titre « INVOICE » sur des cellules fusionnées, en enregistrant le numéro et la date de la facture, en listant le client facturé, en construisant un tableau de lignes d'articles avec les colonnes description, quantité, prix unitaire et total, et en calculant le sous-total, la taxe et le total général à l'aide de formules de cellules. La mise en forme telle que les en-têtes en gras, le format monétaire pour les prix, les bordures et les largeurs de colonnes est appliquée à l'aide des objets `Style` et `Font`. Enfin, le classeur est enregistré avec l'extension `.ofd` à l'aide de `SaveFormat.Ofd`.

```csharp
using System;
using Aspose.Cells;
using System.Drawing;
string dataDir = "C:\\Temp\\";
// Create a new Workbook
Workbook workbook = new Workbook();
// Obtain the first worksheet
Worksheet worksheet = workbook.Worksheets[0];
// Set column widths
worksheet.Cells.SetColumnWidth(0, 5);
worksheet.Cells.SetColumnWidth(1, 35);
worksheet.Cells.SetColumnWidth(2, 12);
worksheet.Cells.SetColumnWidth(3, 15);
worksheet.Cells.SetColumnWidth(4, 15);
worksheet.Cells.SetColumnWidth(5, 5);
// Insert company logo
worksheet.Pictures.Add(1, 1, dataDir + "logo.png");
// Company name and contact details
worksheet.Cells["B3"].PutValue("Acme Corporation");
worksheet.Cells["B4"].PutValue("123 Business Street");
worksheet.Cells["B5"].PutValue("City, State 12345");
worksheet.Cells["B6"].PutValue("Phone: (555) 123-4567");
// INVOICE title - merge cells
worksheet.Cells.Merge(7, 1, 2, 4);
Cell titleCell = worksheet.Cells["B8"];
titleCell.PutValue("INVOICE");
Style titleStyle = workbook.CreateStyle();
titleStyle.Font.IsBold = true;
titleStyle.Font.Size = 20;
titleStyle.HorizontalAlignment = TextAlignmentType.Center;
titleCell.SetStyle(titleStyle);
// Invoice number and date
worksheet.Cells["B11"].PutValue("Invoice Number:");
worksheet.Cells["C11"].PutValue("INV-2024-001");
worksheet.Cells["B12"].PutValue("Date:");
worksheet.Cells["C12"].PutValue(DateTime.Now.ToString("yyyy-MM-dd"));
// Bill-to section
worksheet.Cells["B14"].PutValue("Bill To:");
worksheet.Cells["B15"].PutValue("Client Name");
worksheet.Cells["B16"].PutValue("Client Address");
worksheet.Cells["B17"].PutValue("Client City, State");
// Line items header
Cell headerDesc = worksheet.Cells["B19"];
Cell headerQty = worksheet.Cells["C19"];
Cell headerPrice = worksheet.Cells["D19"];
Cell headerTotal = worksheet.Cells["E19"];
headerDesc.PutValue("Description");
headerQty.PutValue("Quantity");
headerPrice.PutValue("Unit Price");
headerTotal.PutValue("Total");
Style headerStyle = workbook.CreateStyle();
headerStyle.Font.IsBold = true;
headerStyle.Font.Color = Color.White;
headerStyle.ForegroundColor = Color.Navy;
headerStyle.Pattern = BackgroundType.Solid;
headerStyle.HorizontalAlignment = TextAlignmentType.Center;
headerStyle.Borders[BorderType.TopBorder].LineStyle = CellBorderType.Thin;
headerStyle.Borders[BorderType.BottomBorder].LineStyle = CellBorderType.Thin;
headerStyle.Borders[BorderType.LeftBorder].LineStyle = CellBorderType.Thin;
headerStyle.Borders[BorderType.RightBorder].LineStyle = CellBorderType.Thin;
headerDesc.SetStyle(headerStyle);
headerQty.SetStyle(headerStyle);
headerPrice.SetStyle(headerStyle);
headerTotal.SetStyle(headerStyle);
// Currency style with borders
Style currencyStyle = workbook.CreateStyle();
currencyStyle.Custom = "\"$\"#,##0.00";
currencyStyle.Borders[BorderType.TopBorder].LineStyle = CellBorderType.Thin;
currencyStyle.Borders[BorderType.BottomBorder].LineStyle = CellBorderType.Thin;
currencyStyle.Borders[BorderType.LeftBorder].LineStyle = CellBorderType.Thin;
currencyStyle.Borders[BorderType.RightBorder].LineStyle = CellBorderType.Thin;
// Plain border style for description/quantity cells
Style borderStyle = workbook.CreateStyle();
borderStyle.Borders[BorderType.TopBorder].LineStyle = CellBorderType.Thin;
borderStyle.Borders[BorderType.BottomBorder].LineStyle = CellBorderType.Thin;
borderStyle.Borders[BorderType.LeftBorder].LineStyle = CellBorderType.Thin;
borderStyle.Borders[BorderType.RightBorder].LineStyle = CellBorderType.Thin;
// Line items rows
object[,] lineItems = new object[,] {
    {"Product A - Widget", 2, 50.00},
    {"Product B - Gadget", 3, 75.00},
    {"Product C - Service", 1, 100.00}
};
for (int i = 0; i < lineItems.GetLength(0); i++)
{
    int row = 20 + i;
    Cell descCell = worksheet.Cells[row, 1];
    Cell qtyCell = worksheet.Cells[row, 2];
    Cell priceCell = worksheet.Cells[row, 3];
    Cell totalCell = worksheet.Cells[row, 4];
    descCell.PutValue(lineItems[i, 0]);
    qtyCell.PutValue(lineItems[i, 1]);
    priceCell.PutValue(lineItems[i, 2]);
    totalCell.Formula = "C" + (row + 1) + "*D" + (row + 1);
    descCell.SetStyle(borderStyle);
    qtyCell.SetStyle(borderStyle);
    priceCell.SetStyle(currencyStyle);
    totalCell.SetStyle(currencyStyle);
}
// Subtotal, tax, grand total
worksheet.Cells["B24"].PutValue("Subtotal:");
Cell subtotalCell = worksheet.Cells["E24"];
subtotalCell.Formula = "SUM(E21:E23)";
worksheet.Cells["B25"].PutValue("Tax (10%):");
Cell taxCell = worksheet.Cells["E25"];
taxCell.Formula = "E24*0.1";
worksheet.Cells["B26"].PutValue("Grand Total:");
Cell grandTotalCell = worksheet.Cells["E26"];
grandTotalCell.Formula = "E24+E25";
// Bold + currency style for total values
Style totalStyle = workbook.CreateStyle();
totalStyle.Font.IsBold = true;
totalStyle.Custom = "\"$\"#,##0.00";
subtotalCell.SetStyle(totalStyle);
taxCell.SetStyle(totalStyle);
grandTotalCell.SetStyle(totalStyle);
// Bold style for total labels
Style boldStyle = workbook.CreateStyle();
boldStyle.Font.IsBold = true;
worksheet.Cells["B24"].SetStyle(boldStyle);
worksheet.Cells["B25"].SetStyle(boldStyle);
worksheet.Cells["B26"].SetStyle(boldStyle);
// Save the workbook as an OFD file
workbook.Save(dataDir + "Invoice.ofd", SaveFormat.Ofd);
```

## **Conversion d'un fichier Excel existant en OFD**
Aspose.Cells peut également charger un classeur Excel existant à partir du disque et l'exporter directement au format OFD. Cela est utile pour les pipelines de conversion par lots, les flux de travail d'archivage et les scénarios où le classeur source a été produit par un autre outil et doit uniquement être réémis en tant qu'artefact à mise en page fixe. L'exemple suivant charge un classeur `.xlsx` existant, lit les données de ses cellules, applique des ajustements optionnels de mise en page et enregistre le résultat sous forme de document OFD.

```csharp
using System;
using Aspose.Cells;
string dataDir = "C:\\Examples\\";
// Open an existing Excel workbook from disk
Workbook workbook = new Workbook(dataDir + "SampleBook.xlsx");
// (1) Read and display values from selected cells to confirm the file was loaded
Worksheet firstSheet = workbook.Worksheets[0];
Console.WriteLine("First sheet name: " + firstSheet.Name);
Console.WriteLine("Cell A1: " + firstSheet.Cells["A1"].StringValue);
Console.WriteLine("Cell B1: " + firstSheet.Cells["B1"].StringValue);
Console.WriteLine("Cell C1: " + firstSheet.Cells["C1"].StringValue);
// (2) Iterate over the Worksheets collection to enumerate available sheets
Console.WriteLine("\nAvailable worksheets:");
for (int i = 0; i < workbook.Worksheets.Count; i++)
{
    Worksheet ws = workbook.Worksheets[i];
    Console.WriteLine("  [" + i + "] " + ws.Name);
}
// (3) Optionally update a timestamp cell to reflect the conversion
firstSheet.Cells["A1"].PutValue("Converted on: " + DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss"));
// Append a summary header row at the top of the data block
firstSheet.Cells.InsertRow(0);
firstSheet.Cells["A1"].PutValue("Conversion Summary");
firstSheet.Cells["A2"].PutValue("Generated: " + DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss"));
// (4) Configure PageSetup properties on the worksheet
PageSetup pageSetup = firstSheet.PageSetup;
pageSetup.Orientation = PageOrientationType.Landscape;
pageSetup.PaperSize = PaperSizeType.PaperA4;
pageSetup.FitToPagesTall = 1;
pageSetup.FitToPagesWide = 1;
// (5) Optionally set the print area for the OFD output
int lastRow = firstSheet.Cells.MaxDataRow;
int lastCol = firstSheet.Cells.MaxDataColumn;
string lastColLetter = CellsHelper.ColumnIndexToName(lastCol);
string printArea = "A1:" + lastColLetter + (lastRow + 1);
firstSheet.PageSetup.PrintArea = printArea;
Console.WriteLine("\nPrint area set to: " + printArea);
// (6) Save the workbook as an OFD file
workbook.Save(dataDir + "SampleBook.ofd", SaveFormat.Ofd);
Console.WriteLine("\nFile successfully converted to OFD format: " + dataDir + "SampleBook.ofd");
```

## **Articles connexes**
- [Fractionner des fichiers Excel en plusieurs fichiers](/cells/fr/net/splitting-excel-files-into-multiple-files/)
- [Insertion d'une image dans une cellule](/cells/fr/net/inserting-an-image-into-a-cell/)
- [Lecture et écriture de fichiers DBF](/cells/fr/net/dbf/)
- [Convertir une sparkline en image et HTML dans Aspose.Cells for .NET](/cells/fr/net/convert-sparkline-to-image-and-html/)

{{< app/cells/assistant language="csharp" >}}