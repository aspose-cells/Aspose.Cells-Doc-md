---
title: Conversion d’Excel au format OFD
description: Aspose.Cells for JavaScript via C++ est une bibliothèque JavaScript permettant de travailler avec des fichiers de tableur qui prend en charge la conversion des classeurs Excel au format OFD (Open Fixed-layout Document). Cet article explique comment créer du contenu Excel et l’exporter au format OFD, ainsi que comment convertir des fichiers Excel existants au format OFD à l’aide d’Aspose.Cells.
linktitle: OFD
keywords: Aspose.Cells, Aspose.Cells for JavaScript via C++, bibliothèque JavaScript, tableur, conversion d’Excel en OFD, conversion OFD, SaveFormat.Ofd, document à mise en page fixe, export de classeur
type: docs
weight: 195
url: /fr/javascript-cpp/converting-excel-to-ofd-format/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells permet de convertir directement les classeurs Excel au format OFD (Open Fixed-layout Document) à l’aide de la valeur d’énumération `SaveFormat.Ofd`. Le document OFD obtenu conserve la mise en page visible du classeur, son contenu, les cellules fusionnées, les largeurs de colonne, les hauteurs de ligne, les polices, les couleurs, les bordures et les formats numériques. Aspose.Cells est ainsi adapté aux flux de travail d’archivage, d’impression, de dépôt réglementaire et de soumission aux autorités gouvernementales qui nécessitent une sortie à mise en page fixe.
{{% /alert %}}

## **Introduction**
OFD (Open Fixed-layout Document) est une norme nationale chinoise (GB/T 33190-2016) destinée à représenter des documents numériques dans une mise en page fixe fondée sur des pages. Il joue un rôle comparable à celui de PDF dans les cas où l’apparence visuelle du document source doit être conservée exactement telle qu’elle a été conçue. OFD est largement utilisé pour les transmissions aux autorités publiques, les dépôts réglementaires, les factures électroniques et l’archivage à long terme en République populaire de Chine.
La conversion des classeurs Excel au format OFD est une exigence courante lorsque le contenu d’un tableur doit être distribué sous la forme d’un artefact en lecture seule dont la mise en page est verrouillée, plutôt que sous celle d’un tableur modifiable. Il peut notamment s’agir d’envoyer une facture finalisée à un client, d’archiver un rapport financier trimestriel ou de soumettre un tableur budgétaire à une autorité de régulation. Aspose.Cells répond à ce besoin grâce à la valeur d’énumération `SaveFormat.Ofd`, qui écrit le classeur directement au format OFD sans étape de conversion intermédiaire. La sortie OFD conserve les valeurs des cellules, les plages fusionnées, les polices, les couleurs, les bordures, les formats numériques et les options de mise en page configurées dans le classeur.

{{% alert color="primary" %}}
La sortie OFD générée par Aspose.Cells conserve la mise en page visible du classeur source, notamment le contenu des cellules, les cellules fusionnées, les largeurs de colonne et les hauteurs de ligne. La mise en forme des cellules, telle que les polices, les couleurs, les bordures, l’alignement et les formats numériques, est également rendue dans la sortie à mise en page fixe. Les options de mise en page configurées sur la feuille de calcul, telles que le format du papier, l’orientation et la zone d’impression, influent sur la mise en page du document OFD obtenu.
{{% /alert %}}

## **Création d’un classeur Excel et enregistrement au format OFD**
Aspose.Cells vous permet de créer un classeur par programme, de le remplir avec des données, puis de l’enregistrer directement au format OFD à l’aide de l’énumération `SaveFormat.Ofd`. L’exemple suivant crée une facture de toutes pièces. Il ajoute un logo d’entreprise, des informations d’en-tête, une section « Facturé à », des lignes de facture et des totaux calculés, puis exporte le classeur vers un document OFD.

### **Création d’une facture avec un logo**
L’exemple construit une feuille de calcul de facture en insérant une image de logo dans la zone supérieure gauche, en renseignant le nom de l’entreprise et ses coordonnées, en ajoutant un titre de facture sur des cellules fusionnées, en mentionnant le numéro et la date de la facture, en indiquant le client à facturer, en construisant un tableau de lignes de facture avec les colonnes description, quantité, prix unitaire et total, et en calculant le sous-total, la TVA et le total général à l’aide de formules de cellule. La mise en forme, notamment les en-têtes en gras, le format monétaire des prix, les bordures et les largeurs de colonne, est appliquée à l’aide des objets `Style` et `Font`. Enfin, le classeur est enregistré avec l’extension `.ofd` à l’aide de `SaveFormat.Ofd`.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
        <script src="aspose.cells.js.min.js"></script>
        <script type="text/javascript">
        const { Workbook, Color } = AsposeCells;
        const readyPromise = AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            try {
                // Créer un nouveau classeur
                const workbook = new Workbook();
                // Obtenir la première feuille de calcul
                const worksheet = workbook.worksheets.get(0);
                const cells = worksheet.cells;
                // Définir les largeurs des colonnes
                cells.setColumnWidth(0, 5);
                cells.setColumnWidth(1, 35);
                cells.setColumnWidth(2, 12);
                cells.setColumnWidth(3, 15);
                cells.setColumnWidth(4, 15);
                cells.setColumnWidth(5, 5);
                // Insérer le logo de l’entreprise
                // Créer un PNG en mémoire, car le navigateur ne dispose d’aucun chemin de système de fichiers.
                const logoCanvas = document.createElement("canvas");
                logoCanvas.width = 100;
                logoCanvas.height = 30;
                const logoContext = logoCanvas.getContext("2d");
                logoContext.fillStyle = "#000080";
                logoContext.fillRect(0, 0, logoCanvas.width, logoCanvas.height);
                logoContext.fillStyle = "#FFFFFF";
                logoContext.font = "bold 18px Arial";
                logoContext.fillText("ACME", 16, 21);
                const logoBlob = await new Promise(resolve => logoCanvas.toBlob(resolve, "image/png"));
                if (!logoBlob) {
                    throw new Error("Unable to create the company logo.");
                }
                const logoData = new Uint8Array(await logoBlob.arrayBuffer());
                worksheet.pictures.add(1, 1, logoData);
                // Nom de l’entreprise et coordonnées
                cells.get("B3").value = "Acme Corporation";
                cells.get("B4").value = "123 Business Street";
                cells.get("B5").value = "City, State 12345";
                cells.get("B6").value = "Phone: (555) 123-4567";
                // Titre FACTURE - fusionner les cellules
                cells.merge(7, 1, 2, 4);
                const titleCell = cells.get("B8");
                titleCell.value = "INVOICE";
                const titleStyle = workbook.createStyle();
                titleStyle.font.isBold = true;
                titleStyle.font.size = 20;
                titleStyle.horizontalAlignment = AsposeCells.TextAlignmentType.Center;
                titleCell.style = titleStyle;
                // Numéro de facture et date
                cells.get("B11").value = "Invoice Number:";
                cells.get("C11").value = "INV-2024-001";
                cells.get("B12").value = "Date:";
                const now = new Date();
                const invoiceDate = [
                    now.getFullYear(),
                    String(now.getMonth() + 1).padStart(2, "0"),
                    String(now.getDate()).padStart(2, "0")
                ].join("-");
                cells.get("C12").value = invoiceDate;
                // Section du destinataire
                cells.get("B14").value = "Bill To:";
                cells.get("B15").value = "Client Name";
                cells.get("B16").value = "Client Address";
                cells.get("B17").value = "Client City, State";
                // En-tête des articles
                const headerDesc = cells.get("B19");
                const headerQty = cells.get("C19");
                const headerPrice = cells.get("D19");
                const headerTotal = cells.get("E19");
                headerDesc.value = "Description";
                headerQty.value = "Quantity";
                headerPrice.value = "Unit Price";
                headerTotal.value = "Total";
                const headerStyle = workbook.createStyle();
                headerStyle.font.isBold = true;
                headerStyle.font.color = Color.fromArgb(255, 255, 255);
                headerStyle.foregroundColor = Color.fromArgb(0, 0, 128);
                headerStyle.pattern = AsposeCells.BackgroundType.Solid;
                headerStyle.horizontalAlignment = AsposeCells.TextAlignmentType.Center;
                headerStyle.borders.get(AsposeCells.BorderType.TopBorder).lineStyle = AsposeCells.CellBorderType.Thin;
                headerStyle.borders.get(AsposeCells.BorderType.BottomBorder).lineStyle = AsposeCells.CellBorderType.Thin;
                headerStyle.borders.get(AsposeCells.BorderType.LeftBorder).lineStyle = AsposeCells.CellBorderType.Thin;
                headerStyle.borders.get(AsposeCells.BorderType.RightBorder).lineStyle = AsposeCells.CellBorderType.Thin;
                headerDesc.style = headerStyle;
                headerQty.style = headerStyle;
                headerPrice.style = headerStyle;
                headerTotal.style = headerStyle;
                // Style monétaire avec bordures
                const currencyStyle = workbook.createStyle();
                currencyStyle.custom = '"$"#,##0.00';
                currencyStyle.borders.get(AsposeCells.BorderType.TopBorder).lineStyle = AsposeCells.CellBorderType.Thin;
                currencyStyle.borders.get(AsposeCells.BorderType.BottomBorder).lineStyle = AsposeCells.CellBorderType.Thin;
                currencyStyle.borders.get(AsposeCells.BorderType.LeftBorder).lineStyle = AsposeCells.CellBorderType.Thin;
                currencyStyle.borders.get(AsposeCells.BorderType.RightBorder).lineStyle = AsposeCells.CellBorderType.Thin;
                // Style de bordure simple pour les cellules de description et de quantité
                const borderStyle = workbook.createStyle();
                borderStyle.borders.get(AsposeCells.BorderType.TopBorder).lineStyle = AsposeCells.CellBorderType.Thin;
                borderStyle.borders.get(AsposeCells.BorderType.BottomBorder).lineStyle = AsposeCells.CellBorderType.Thin;
                borderStyle.borders.get(AsposeCells.BorderType.LeftBorder).lineStyle = AsposeCells.CellBorderType.Thin;
                borderStyle.borders.get(AsposeCells.BorderType.RightBorder).lineStyle = AsposeCells.CellBorderType.Thin;
                // Lignes d’articles
                const lineItems = [
                    ["Product A - Widget", 2, 50.00],
                    ["Product B - Gadget", 3, 75.00],
                    ["Product C - Service", 1, 100.00]
                ];
                for (let i = 0; i < lineItems.length; i++) {
                    const row = 20 + i;
                    const descCell = cells.get(row, 1);
                    const qtyCell = cells.get(row, 2);
                    const priceCell = cells.get(row, 3);
                    const totalCell = cells.get(row, 4);
                    descCell.value = lineItems[i][0];
                    qtyCell.value = lineItems[i][1];
                    priceCell.value = lineItems[i][2];
                    totalCell.formula = "C" + (row + 1) + "*D" + (row + 1);
                    descCell.style = borderStyle;
                    qtyCell.style = borderStyle;
                    priceCell.style = currencyStyle;
                    totalCell.style = currencyStyle;
                }
                // Sous-total, taxe et total général
                cells.get("B24").value = "Subtotal:";
                const subtotalCell = cells.get("E24");
                subtotalCell.formula = "SUM(E21:E23)";
                cells.get("B25").value = "Tax (10%):";
                const taxCell = cells.get("E25");
                taxCell.formula = "E24*0.1";
                cells.get("B26").value = "Grand Total:";
                const grandTotalCell = cells.get("E26");
                grandTotalCell.formula = "E24+E25";
                // Style gras et monétaire pour les valeurs totales
                const totalStyle = workbook.createStyle();
                totalStyle.font.isBold = true;
                totalStyle.custom = '"$"#,##0.00';
                subtotalCell.style = totalStyle;
                taxCell.style = totalStyle;
                grandTotalCell.style = totalStyle;
                // Style gras pour les libellés des totaux
                const boldStyle = workbook.createStyle();
                boldStyle.font.isBold = true;
                cells.get("B24").style = boldStyle;
                cells.get("B25").style = boldStyle;
                cells.get("B26").style = boldStyle;
                // Enregistrer le classeur dans un fichier OFD
                const outputData = workbook.save(AsposeCells.SaveFormat.Ofd);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "Invoice.ofd";
                downloadLink.style.display = "block";
                document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            } catch (error) {
                console.error(error);
                document.getElementById('result').innerHTML = '<p style="color: red;">An error occurred: ' + error.message + '</p>';
            }
        });
        </script>
    </body>
</html>
```

## **Conversion d’un fichier Excel existant au format OFD**
Aspose.Cells peut également charger un classeur Excel existant depuis le disque et l’exporter directement au format OFD. Cette approche est utile pour les chaînes de conversion par lots, les flux de travail d’archivage et les scénarios où le classeur source a été produit par un autre outil et où seule sa réémission sous la forme d’un artefact à mise en page fixe est nécessaire. L’exemple suivant charge un classeur `.xlsx` existant, lit les données de ses cellules, applique des ajustements facultatifs de la mise en page, puis enregistre le résultat sous forme de document OFD.

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8" />
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
        <script src="aspose.cells.js.min.js"></script>
        <script type="text/javascript">
            const { Workbook, CellsHelper } = AsposeCells;
            const fileInput = document.getElementById("fileInput");
            const runButton = document.getElementById("runExample");
            const downloadLink = document.getElementById("downloadLink");
            const result = document.getElementById("result");
            const readyPromise = AsposeCells.onReady({
                license: "/lic/aspose.cells.enc",
                fontPath: "/fonts/",
                fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
            }).then(() => {
                console.log("Aspose.Cells initialized");
            });
            function formatTimestamp(date) {
                const pad = value => String(value).padStart(2, "0");
                return date.getFullYear() + "-" +
                    pad(date.getMonth() + 1) + "-" +
                    pad(date.getDate()) + " " +
                    pad(date.getHours()) + ":" +
                    pad(date.getMinutes()) + ":" +
                    pad(date.getSeconds());
            }
            function escapeHtml(value) {
                const entities = {
                    "&": "&amp;",
                    "<": "&lt;",
                    ">": "&gt;",
                    '"': "&quot;",
                    "'": "&#39;"
                };
                return String(value).replace(/[&<>"']/g, character => entities[character]);
            }
            runButton.addEventListener("click", async () => {
                try {
                    const file = fileInput.files[0];
                    if (!file) {
                        result.innerHTML = '<p style="color: red;">Please select an Excel file first.</p>';
                        return;
                    }
                    runButton.disabled = true;
                    downloadLink.style.display = "none";
                    downloadLink.removeAttribute("href");
                    // Ouvrir un classeur Excel existant depuis le disque
                    const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                    // (1) Lire et afficher les valeurs des cellules sélectionnées pour confirmer que le fichier a été chargé
                    const firstSheet = workbook.worksheets.get(0);
                    const cells = firstSheet.cells;
                    const output = [];
                    output.push("First sheet name: " + firstSheet.name);
                    output.push("Cell A1: " + cells.get("A1").stringValue);
                    output.push("Cell B1: " + cells.get("B1").stringValue);
                    output.push("Cell C1: " + cells.get("C1").stringValue);
                    // (2) Parcourir la collection Worksheets pour énumérer les feuilles disponibles
                    output.push("");
                    output.push("Available worksheets:");
                    for (let i = 0; i < workbook.worksheets.count; i++) {
                        const ws = workbook.worksheets.get(i);
                        output.push("  [" + i + "] " + ws.name);
                    }
                    // (3) Facultativement, mettre à jour une cellule d'horodatage pour refléter la conversion
                    cells.get("A1").value = "Converted on: " + formatTimestamp(new Date());
                    // Ajouter une ligne d'en-tête récapitulative en haut du bloc de données
                    cells.insertRow(0);
                    cells.get("A1").value = "Conversion Summary";
                    cells.get("A2").value = "Generated: " + formatTimestamp(new Date());
                    // (4) Configurer les propriétés PageSetup de la feuille de calcul
                    const pageSetup = firstSheet.pageSetup;
                    pageSetup.orientation = AsposeCells.PageOrientationType.Landscape;
                    pageSetup.paperSize = AsposeCells.PaperSizeType.PaperA4;
                    pageSetup.fitToPagesTall = 1;
                    pageSetup.fitToPagesWide = 1;
                    // (5) Facultativement, définir la zone d'impression pour la sortie OFD
                    const lastRow = cells.maxDataRow;
                    const lastCol = cells.maxDataColumn;
                    const lastColLetter = CellsHelper.columnIndexToName(lastCol);
                    const printArea = "A1:" + lastColLetter + (lastRow + 1);
                    pageSetup.printArea = printArea;
                    output.push("");
                    output.push("Print area set to: " + printArea);
                    // (6) Enregistrer le classeur sous forme de fichier OFD
                    const outputData = workbook.save(AsposeCells.SaveFormat.Ofd);
                    const blob = new Blob([outputData]);
                    downloadLink.href = URL.createObjectURL(blob);
                    downloadLink.download = "SampleBook.ofd";
                    downloadLink.textContent = "Download SampleBook.ofd";
                    downloadLink.style.display = "block";
                    output.push("");
                    output.push("File successfully converted to OFD format: SampleBook.ofd");
                    result.innerHTML =
                        '<pre style="white-space: pre-wrap;">' +
                        escapeHtml(output.join("\n")) +
                        "</pre>" +
                        '<p style="color: green;">Done! Click the download link to get the result file.</p>';
                } catch (error) {
                    console.error(error);
                    const message = error && error.message ? error.message : String(error);
                    result.innerHTML = '<p style="color: red;">Error: ' + escapeHtml(message) + "</p>";
                } finally {
                    runButton.disabled = false;
                }
            });
        </script>
    </body>
</html>
```

{{< app/cells/assistant language="javascript-cpp" >}}