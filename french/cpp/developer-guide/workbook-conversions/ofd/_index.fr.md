---
title: Conversion d'Excel au format OFD
linktitle: Conversion d'Excel au format OFD
description: Aspose.Cells est une bibliothèque C++ pour travailler avec des fichiers tableur qui prend en charge la conversion de classeurs Excel au format OFD (Open Fixed-layout Document). Cet article montre comment créer du contenu Excel et l'exporter en OFD, ainsi que comment convertir des fichiers Excel existants en OFD à l'aide d'Aspose.Cells.
keywords: Aspose.Cells, bibliothèque C++, tableur, Excel vers OFD, conversion OFD, SaveFormat.Ofd, document à mise en page fixe, exportation de classeur
type: docs
weight: 195
url: /fr/cpp/converting-excel-to-ofd-format/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells prend en charge la conversion de classeurs Excel directement au format OFD (Open Fixed-layout Document) en utilisant la valeur d'énumération `SaveFormat.Ofd`. Le document OFD résultant préserve la disposition visible du classeur, le contenu, les cellules fusionnées, les largeurs de colonnes, les hauteurs de lignes, les polices, les couleurs, les bordures et les formats de nombres. Cela rend Aspose.Cells adapté aux flux d'archivage, d'impression, de dépôt réglementaire et de soumission gouvernementale qui nécessitent une sortie à mise en page fixe.

{{% /alert %}}
## **Introduction**
OFD (Open Fixed-layout Document) est une norme nationale chinoise (GB/T 33190-2016) pour représenter des documents numériques dans une mise en page fixe, basée sur des pages. Elle joue un rôle similaire à celui du PDF pour les cas d'utilisation où l'apparence visuelle du document source doit être préservée exactement telle qu'elle a été conçue. L'OFD est largement adopté pour les soumissions gouvernementales, les dépôts réglementaires, les factures électroniques et l'archivage à long terme en République populaire de Chine.

La conversion de classeurs Excel en OFD est une exigence courante dans les scénarios où le contenu d'un tableur doit être distribué sous forme d'artefact en lecture seule et à mise en page verrouillée plutôt qu'en tant que tableur modifiable. Parmi les exemples, on peut citer l'envoi d'une facture finalisée à un client, l'archivage d'un rapport financier trimestriel ou la soumission d'un tableur budgétaire à une autorité réglementaire. Aspose.Cells répond à ce besoin grâce à la valeur d'énumération `SaveFormat.Ofd`, qui écrit le classeur directement en OFD sans nécessiter d'étape de conversion intermédiaire. La sortie OFD préserve les valeurs des cellules, les plages fusionnées, les polices, les couleurs, les bordures, les formats de nombres et les options de mise en page configurées sur le classeur.

{{% alert color="primary" %}}

La sortie OFD générée par Aspose.Cells préserve la disposition visible du classeur source, y compris le contenu des cellules, les cellules fusionnées, les largeurs de colonnes et les hauteurs de lignes. La mise en forme des cellules, comme les polices, les couleurs, les bordures, l'alignement et les formats de nombres, est également rendue dans la sortie à mise en page fixe. Les options de mise en page configurées sur la feuille de calcul, telles que le format du papier, l'orientation et la zone d'impression, influencent la disposition du document OFD résultant.

{{% /alert %}}
## **Création d'un classeur Excel et enregistrement en OFD**
Aspose.Cells vous permet de créer un classeur par programmation, de le remplir avec des données, puis de l'enregistrer directement au format OFD en utilisant l'énumération `SaveFormat.Ofd`. L'exemple suivant crée une facture à partir de zéro. Il ajoute un logo d'entreprise, des informations d'en-tête, une section de facturation, des lignes d'articles et des totaux calculés, puis exporte le classeur vers un document OFD.
### **Création d'une facture avec un logo**
L'exemple construit une feuille de calcul de facture en insérant une image de logo dans la zone supérieure gauche, en remplissant le nom de l'entreprise et les coordonnées, en ajoutant un titre « INVOICE » dans des cellules fusionnées, en enregistrant le numéro et la date de la facture, en listant le client facturé, en construisant un tableau de lignes d'articles avec les colonnes description, quantité, prix unitaire et total, et en calculant le sous-total, la taxe et le total général à l'aide de formules de cellules. La mise en forme, comme les en-têtes en gras, le format monétaire pour les prix, les bordures et les largeurs de colonnes, est appliquée à l'aide des objets `Style` et `Font`. Enfin, le classeur est enregistré avec l'extension `.ofd` en utilisant `SaveFormat.Ofd`.

```cpp
// Aspose.Cells pour C++ exemple
// Compiler avec Aspose.Cells 26.6.0 (ou version ultérieure) et un compilateur C++17 (ou version ultérieure)

#include "Aspose.Cells.h"
#include <string>
#include <ctime>

using namespace Aspose::Cells;

int main()
{
    // Initialiser Aspose.Cells
    Aspose::Cells::Startup();

    // Répertoire pour les ressources et la sortie
    const char16_t* dataDir = u"C:\\Temp\\";

    // Créer un nouveau classeur
    Workbook workbook;

    // Obtenir la première feuille de calcul
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();

    // Définir les largeurs de colonnes
    cells.SetColumnWidth(0, 5.0);
    cells.SetColumnWidth(1, 35.0);
    cells.SetColumnWidth(2, 12.0);
    cells.SetColumnWidth(3, 15.0);
    cells.SetColumnWidth(4, 15.0);
    cells.SetColumnWidth(5, 5.0);

    // Insérer le logo de l'entreprise
    worksheet.GetPictures().Add(1, 1, U16String(dataDir) + u"logo.png");

    // Nom de l'entreprise et coordonnées
    cells.Get(u"B3").PutValue(u"Acme Corporation");
    cells.Get(u"B4").PutValue(u"123 Business Street");
    cells.Get(u"B5").PutValue(u"City, State 12345");
    cells.Get(u"B6").PutValue(u"Phone: (555) 123-4567");

    // Titre FACTURE - fusionner les cellules
    cells.Merge(7, 1, 2, 4);
    Cell titleCell = cells.Get(u"B8");
    titleCell.PutValue(u"INVOICE");

    Style titleStyle = workbook.CreateStyle();
    titleStyle.GetFont().SetIsBold(true);
    titleStyle.GetFont().SetSize(20);
    titleStyle.SetHorizontalAlignment(TextAlignmentType::Center);
    titleCell.SetStyle(titleStyle);

    // Numéro et date de la facture
    cells.Get(u"B11").PutValue(u"Invoice Number:");
    cells.Get(u"C11").PutValue(u"INV-2024-001");
    cells.Get(u"B12").PutValue(u"Date:");

    std::time_t t = std::time(nullptr);
    std::tm* now = std::localtime(&t);
    char dateBuffer[11];
    std::strftime(dateBuffer, sizeof(dateBuffer), "%Y-%m-%d", now);
    cells.Get(u"C12").PutValue(U16String(dateBuffer));

    // Section Facturation à
    cells.Get(u"B14").PutValue(u"Bill To:");
    cells.Get(u"B15").PutValue(u"Client Name");
    cells.Get(u"B16").PutValue(u"Client Address");
    cells.Get(u"B17").PutValue(u"Client City, State");

    // En-tête des lignes d'articles
    Cell headerDesc = cells.Get(u"B19");
    Cell headerQty = cells.Get(u"C19");
    Cell headerPrice = cells.Get(u"D19");
    Cell headerTotal = cells.Get(u"E19");

    headerDesc.PutValue(u"Description");
    headerQty.PutValue(u"Quantity");
    headerPrice.PutValue(u"Unit Price");
    headerTotal.PutValue(u"Total");

    Style headerStyle = workbook.CreateStyle();
    headerStyle.GetFont().SetIsBold(true);
    headerStyle.GetFont().SetColor(Color::White());
    headerStyle.SetForegroundColor(Color{0, 0, 128});
    headerStyle.SetPattern(BackgroundType::Solid);
    headerStyle.SetHorizontalAlignment(TextAlignmentType::Center);
    headerStyle.GetBorders().Get(BorderType::TopBorder).SetLineStyle(CellBorderType::Thin);
    headerStyle.GetBorders().Get(BorderType::BottomBorder).SetLineStyle(CellBorderType::Thin);
    headerStyle.GetBorders().Get(BorderType::LeftBorder).SetLineStyle(CellBorderType::Thin);
    headerStyle.GetBorders().Get(BorderType::RightBorder).SetLineStyle(CellBorderType::Thin);

    headerDesc.SetStyle(headerStyle);
    headerQty.SetStyle(headerStyle);
    headerPrice.SetStyle(headerStyle);
    headerTotal.SetStyle(headerStyle);

    // Style de devise avec bordures
    Style currencyStyle = workbook.CreateStyle();
    currencyStyle.SetCustom(u"\"$\"#,##0.00");
    currencyStyle.GetBorders().Get(BorderType::TopBorder).SetLineStyle(CellBorderType::Thin);
    currencyStyle.GetBorders().Get(BorderType::BottomBorder).SetLineStyle(CellBorderType::Thin);
    currencyStyle.GetBorders().Get(BorderType::LeftBorder).SetLineStyle(CellBorderType::Thin);
    currencyStyle.GetBorders().Get(BorderType::RightBorder).SetLineStyle(CellBorderType::Thin);

    // Style de bordure simple pour les cellules description/quantité
    Style borderStyle = workbook.CreateStyle();
    borderStyle.GetBorders().Get(BorderType::TopBorder).SetLineStyle(CellBorderType::Thin);
    borderStyle.GetBorders().Get(BorderType::BottomBorder).SetLineStyle(CellBorderType::Thin);
    borderStyle.GetBorders().Get(BorderType::LeftBorder).SetLineStyle(CellBorderType::Thin);
    borderStyle.GetBorders().Get(BorderType::RightBorder).SetLineStyle(CellBorderType::Thin);

    // Lignes d'articles
    struct LineItem { const char16_t* desc; int qty; double price; };
    LineItem lineItems[] = {
        {u"Product A - Widget", 2, 50.00},
        {u"Product B - Gadget", 3, 75.00},
        {u"Product C - Service", 1, 100.00}
    };

    for (int i = 0; i < 3; i++)
    {
        int row = 20 + i;
        Cell descCell = cells.Get(row, 1);
        Cell qtyCell = cells.Get(row, 2);
        Cell priceCell = cells.Get(row, 3);
        Cell totalCell = cells.Get(row, 4);

        descCell.PutValue(lineItems[i].desc);
        qtyCell.PutValue(lineItems[i].qty);
        priceCell.PutValue(lineItems[i].price);

        std::string formula = "C" + std::to_string(row) + "*D" + std::to_string(row);
        totalCell.SetFormula(U16String(formula.c_str()));

        descCell.SetStyle(borderStyle);
        qtyCell.SetStyle(borderStyle);
        priceCell.SetStyle(currencyStyle);
        totalCell.SetStyle(currencyStyle);
    }

    // Sous-total, taxe, total général
    cells.Get(u"B24").PutValue(u"Subtotal:");
    Cell subtotalCell = cells.Get(u"E24");
    subtotalCell.SetFormula(u"SUM(E20:E22)");

    cells.Get(u"B25").PutValue(u"Tax (10%):");
    Cell taxCell = cells.Get(u"E25");
    taxCell.SetFormula(u"E24*0.1");

    cells.Get(u"B26").PutValue(u"Grand Total:");
    Cell grandTotalCell = cells.Get(u"E26");
    grandTotalCell.SetFormula(u"E24+E25");

    // Style gras + devise pour les valeurs totales
    Style totalStyle = workbook.CreateStyle();
    totalStyle.GetFont().SetIsBold(true);
    totalStyle.SetCustom(u"\"$\"#,##0.00");

    subtotalCell.SetStyle(totalStyle);
    taxCell.SetStyle(totalStyle);
    grandTotalCell.SetStyle(totalStyle);

    // Style gras pour les étiquettes des totaux
    Style boldStyle = workbook.CreateStyle();
    boldStyle.GetFont().SetIsBold(true);

    cells.Get(u"B24").SetStyle(boldStyle);
    cells.Get(u"B25").SetStyle(boldStyle);
    cells.Get(u"B26").SetStyle(boldStyle);

    // Enregistrer le classeur en tant que fichier OFD
    workbook.Save(U16String(dataDir) + u"Invoice.ofd", SaveFormat::Ofd);

    // Nettoyer les ressources Aspose.Cells
    Aspose::Cells::Cleanup();

    return 0;
}
```
## **Conversion d'un fichier Excel existant en OFD**
Aspose.Cells peut également charger un classeur Excel existant à partir du disque et l'exporter directement au format OFD. Cela est utile pour les pipelines de conversion par lots, les flux d'archivage et les scénarios dans lesquels le classeur source a été produit par un autre outil et n'a besoin que d'être réémis en tant qu'artefact à mise en page fixe. L'exemple suivant charge un classeur `.xlsx` existant, lit les données de ses cellules, applique des ajustements facultatifs de mise en page et enregistre le résultat en tant que document OFD.

```cpp
#include "Aspose.Cells.h"
#include <string>
#include <iostream>
#include <ctime>

using namespace Aspose::Cells;

std::string GetCurrentTimestamp() {
    std::time_t t = std::time(nullptr);
    std::tm* now = std::localtime(&t);
    char buffer[20];
    std::strftime(buffer, sizeof(buffer), "%Y-%m-%d %H:%M:%S", now);
    return std::string(buffer);
}

int main() {
    Aspose::Cells::Startup();

    std::string dataDir = "C:\\Examples\\";

    // Ouvrir un classeur Excel existant à partir du disque
    Workbook workbook(U16String((dataDir + "SampleBook.xlsx").c_str()));

    // (1) Lire et afficher les valeurs des cellules sélectionnées pour confirmer que le fichier a été chargé
    Worksheet firstSheet = workbook.GetWorksheets().Get(0);
    U16String sheetName = firstSheet.GetName();
    Cell a1 = firstSheet.GetCells().Get(u"A1");
    Cell b1 = firstSheet.GetCells().Get(u"B1");
    Cell c1 = firstSheet.GetCells().Get(u"C1");

    std::cout << "First sheet name: " << sheetName.ToUtf8() << std::endl;
    std::cout << "Cell A1: " << a1.GetStringValue().ToUtf8() << std::endl;
    std::cout << "Cell B1: " << b1.GetStringValue().ToUtf8() << std::endl;
    std::cout << "Cell C1: " << c1.GetStringValue().ToUtf8() << std::endl;

    // (2) Parcourir la collection Worksheets pour énumérer les feuilles disponibles
    std::cout << "\nAvailable worksheets:" << std::endl;
    WorksheetCollection sheets = workbook.GetWorksheets();
    int sheetCount = sheets.GetCount();
    for (int i = 0; i < sheetCount; ++i) {
        Worksheet ws = sheets.Get(i);
        U16String wsName = ws.GetName();
        std::cout << "  [" << i << "] " << wsName.ToUtf8() << std::endl;
    }

    // (3) Optionnellement, mettre à jour une cellule d'horodatage pour refléter la conversion
    std::string timestamp1 = GetCurrentTimestamp();
    firstSheet.GetCells().Get(u"A1").PutValue(U16String(("Converted on: " + timestamp1).c_str()));

    // Ajouter une ligne d'en-tête récapitulative en haut du bloc de données
    firstSheet.GetCells().InsertRow(0);
    firstSheet.GetCells().Get(u"A1").PutValue(u"Conversion Summary");

    std::string timestamp2 = GetCurrentTimestamp();
    firstSheet.GetCells().Get(u"A2").PutValue(U16String(("Generated: " + timestamp2).c_str()));

    // (4) Configurer les propriétés de PageSetup sur la feuille de calcul
    PageSetup pageSetup = firstSheet.GetPageSetup();
    pageSetup.SetOrientation(PageOrientationType::Landscape);
    pageSetup.SetPaperSize(PaperSizeType::PaperA4);
    pageSetup.SetFitToPagesTall(1);
    pageSetup.SetFitToPagesWide(1);

    // (5) Optionnellement, définir la zone d'impression pour la sortie OFD
    int lastRow = firstSheet.GetCells().GetMaxDataRow();
    int lastCol = firstSheet.GetCells().GetMaxDataColumn();
    U16String lastColLetter = CellsHelper::ColumnIndexToName(lastCol);
    std::string printArea = "A1:" + lastColLetter.ToUtf8() + std::to_string(lastRow + 1);
    firstSheet.GetPageSetup().SetPrintArea(U16String(printArea.c_str()));
    std::cout << "\nPrint area set to: " << printArea << std::endl;

    // (6) Enregistrer le classeur en tant que fichier OFD
    workbook.Save(U16String((dataDir + "SampleBook.ofd").c_str()), SaveFormat::Ofd);
    std::cout << "\nFile successfully converted to OFD format: " << dataDir << "SampleBook.ofd" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Articles connexes**
- [Fractionnement de fichiers Excel en plusieurs fichiers](/cells/fr/cpp/splitting-excel-files-into-multiple-files/)
- [Insertion d'une image dans une cellule](/cells/fr/cpp/inserting-an-image-into-a-cell/)
- [Lecture et écriture de fichiers DBF](/cells/fr/cpp/dbf/)
- [Convertir un sparkline en image et HTML dans Aspose.Cells for C++](/cells/fr/cpp/convert-sparkline-to-image-and-html/)
{{< app/cells/assistant language="cpp" >}}