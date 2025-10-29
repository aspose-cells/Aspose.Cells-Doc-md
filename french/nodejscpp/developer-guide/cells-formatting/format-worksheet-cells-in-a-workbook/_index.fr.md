---  
title: Formater les cellules de la feuille de calcul dans un classeur avec Node.js via C++  
linktitle: Formater les cellules de feuille de calcul dans un classeur  
description: Apprenez comment formater les cellules d une feuille de calcul dans un classeur en utilisant Aspose.Cells for Node.js via C++. Personnalisez l apparence et le style des données dans les feuilles de calcul.  
keywords: Aspose.Cells, Classeur, Feuille de calcul, Cellule, Mise en forme, Apparence, Style, Node.js via C++  
type: docs  
weight: 2000  
url: /fr/nodejs-cpp/format-worksheet-cells-in-a-workbook/  
---  

{{% alert color="primary" %}}  

Cet article montre comment :

1. Utiliser des styles pour formater rapidement les données.
2. Formatez les cellules dans les lignes et colonnes.
3. Utilisez des bordures et des couleurs pour mettre en valeur les données.
4. Appliquez des formats numériques pour souligner les données.
5. Utilisez des polices et des attributs pour mettre en évidence les données.
6. Formatez les données dans une plage nommée.
7. Modifiez l'alignement et l'orientation des données.
8. Réglez la hauteur des lignes et la largeur des colonnes.

Le projet exemple effectue toutes ces tâches et fournit aux développeurs une description détaillée de la façon de créer un classeur, d'ajouter des données et d'appliquer la mise en forme en utilisant [Aspose.Cells](https://products.aspose.com/cells/nodejs-cpp/).

{{% /alert %}}  

## **Formatage des données**

Le formatage est utilisé pour distinguer les différents types d'informations et afficher clairement les données.

Un format représente un style et est défini comme un ensemble de caractéristiques, telles que les polices et les tailles de police, les formats de nombre, les bordures de cellules, l'ombrage des cellules, l'indentation, l'alignement et l'orientation du texte. Les bordures fournissent d'autres moyens de mettre en évidence des informations. Une bordure est une ligne dessinée autour d'une cellule ou d'un groupe de cellules.

Les formats de nombre rendent également les données plus significatives. En appliquant différents formats de nombre, vous pouvez changer l'apparence des nombres sans changer la valeur sous-jacente.

Aspose.Cells vous permet de tracer facilement des bordures autour des cellules et des plages. Il permet également d'appliquer des polices et de colorier les cellules. Le composant est suffisamment efficace pour que vous puissiez formater une ligne ou une colonne entière, définir des alignements, plier et faire pivoter du texte dans les cellules. Aspose.Cells supporte en outre tous les formats numériques pris en charge par Microsoft Excel.

Cet article montre comment créer une application console qui génère un rapport annuel de ventes. Le classeur est créé de zéro, puis les données sont insérées et la feuille de calcul est formatée. Nous montrons comment créer une application console simple qui crée un classeur Excel (vous pouvez également utiliser un fichier modèle), insérer des données de vente dans la première feuille, formater les données et enregistrer un fichier Excel.

### **Processus**

Voici les étapes pour créer une feuille de calcul et formater différentes cellules dans différentes lignes et colonnes d'une feuille de calcul.

1. Téléchargez et installez Aspose.Cells :
   1. [Télécharger](https://downloads.aspose.com/cells/nodejs-cpp) Aspose.Cells for Node.js via C++.
   1. Installez-le sur votre ordinateur de développement.
2. Créer un projet et ajouter des références :
   1. Démarrez votre éditeur/IDE de code.
   1. Créez une nouvelle application console.
   1. Ajoutez une référence à Aspose.Cells dans votre projet Node.js.
3. Ajoutez le code suivant au projet :

```javascript
try
        {
            const AsposeCells = require("aspose.cells.node");
            const path = require("path");

            class FormatWorksheetCells 
            {
                static run() {
                    const dataDir = path.join(__dirname, "data");
                    const filename = path.join(dataDir, "FormatWorksheet.xls");
                    FormatWorksheetCells.createSalesReport(filename);
                }

                static createSalesReport(filename) {
                    const cellsLicense = new AsposeCells.License();
                    cellsLicense.setLicense("Aspose.Cells.lic");

                    const workbook = new AsposeCells.Workbook();
                    workbook.changePalette(new AsposeCells.Color(155, 204, 255), 55);
                    workbook.changePalette(new AsposeCells.Color(0, 51, 105), 54);
                    workbook.changePalette(new AsposeCells.Color(250, 250, 200), 53);
                    workbook.changePalette(new AsposeCells.Color(124, 199, 72), 52);

                    FormatWorksheetCells.createReportData(workbook);
                    FormatWorksheetCells.createCellsFormatting(workbook);

                    const worksheet = workbook.getWorksheets().get(0);
                    worksheet.setName("Sales Report");
                    workbook.save(filename);
                }

                static createReportData(workbook) {
                    const cells = workbook.getWorksheets().get(0).getCells();
                    cells.get("B1").putValue("Western Product Sales 2006");

                    const headers = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December", "Total"];
                    headers.forEach((header, index) => {
                        cells.get(1, index + 1).putValue(header);
                    });

                    const productNames = ["Biscuits", "Coffee", "Tofu", "Ikura", "Choclade", "Maxilaku", "Scones", "Sauce", "Syrup", "Spegesild", "Filo Mix", "Pears", "Konbu", "Kaviar", "Zaanse", "Cabrales", "Gnocchi", "Wimmers", "Breads", "Lager", "Gravad", "Telino", "Pavlova", "Total"];
                    productNames.forEach((name, index) => {
                        cells.get(index + 3, 0).putValue(name);
                    });

                    const salesData = [
                        [5000, 4500, 6010, 7230, 5400, 5030, 3000, 6000, 9000, 3300, 2500, 5510],
                        [4000, 2500, 6000, 5300, 7400, 7030, 4000, 4000, 5500, 4500, 2500, 2510],
                        [2000, 1500, 3000, 2500, 3400, 4030, 2000, 2000, 1500, 2200, 2100, 2310],
                        [1000, 1300, 2000, 2600, 5400, 2030, 2100, 4000, 6500, 5600, 3300, 5110],
                        [3000, 3500, 1000, 4500, 5400, 2030, 3000, 3000, 4500, 6000, 3000, 3000],
                        [5000, 5500, 5000, 5500, 5400, 5030, 5000, 2500, 5500, 5200, 5500, 2510],
                        [4100, 1500, 1000, 2300, 3300, 4030, 5000, 6000, 3500, 4300, 2300, 2110],
                        [2000, 2300, 3000, 3300, 3400, 3030, 3000, 3000, 3500, 3500, 3500, 3510],
                        [4400, 4500, 4000, 4300, 4400, 4030, 5000, 5000, 4500, 4400, 4400, 4510],
                        [2000, 1500, 3000, 2300, 3400, 3030, 3000, 3000, 2500, 2500, 1500, 5110],
                        [4000, 1400, 1400, 3300, 3300, 3730, 3800, 3600, 2600, 4600, 1400, 2660],
                        [3000, 3500, 3333, 2330, 3430, 3040, 3040, 3030, 1509, 4503, 1503, 3113],
                        [2010, 1520, 3030, 2320, 3410, 3000, 3000, 3020, 2520, 2520, 1520, 5120],
                        [2220, 1200, 3220, 1320, 1400, 1030, 3200, 3020, 2100, 2100, 1100, 5210],
                        [1444, 1540, 3040, 2340, 1440, 1030, 3000, 4000, 4500, 2500, 4500, 5550],
                        [4000, 5500, 3000, 3300, 3330, 5330, 3400, 3040, 2540, 4500, 4500, 2110],
                        [2000, 2500, 3200, 3200, 2330, 5230, 2400, 3240, 2240, 4300, 4100, 2310]
                    ];

                    salesData.forEach((rowData, rowIndex) => {
                        rowData.forEach((value, colIndex) => {
                            cells.get(rowIndex + 3, colIndex + 1).putValue(value);
                        });
                    });

                    for (let i = 2; i < 27; i++) {
                        cells.get(i, 13).setFormula(`=SUM(B${i+1}:M${i+1})`);
                    }
                    for (let i = 3; i <= 25; i++) {
                        cells.get(i, 13).setFormula(`=SUM(B${i + 1}:M${i + 1})`);
                    }

                    cells.get(26, 13).setFormula("=SUM(N3:N25)");
                }

                static createCellsFormatting(workbook)
                {
                    let stl0 = workbook.createStyle();
                    stl0.setForegroundColor(new AsposeCells.Color(155, 204, 255));
                    stl0.setPattern(AsposeCells.BackgroundType.Solid);
                    stl0.getFont().setName("Trebuchet MS");
                    stl0.getFont().setSize(18);
                    stl0.getFont().setColor(AsposeCells.Color.Maroon);
                    stl0.getFont().setIsBold(true);
                    stl0.getFont().setIsItalic(true);

                    let flag = new AsposeCells.StyleFlag();
                    flag.setCellShading(true);
                    flag.setFontName(true);
                    flag.setFontSize(true);
                    flag.setFontColor(true);
                    flag.setFontBold(true);
                    flag.setFontItalic(true);

                    var row = workbook.getWorksheets().get(0).getCells().getRows().get(0);
                    row.applyStyle(stl0, flag);
                    const cells = workbook.getWorksheets().get(0).getCells();
                    cells.setRowHeight(0, 30);

                    let stl1 = workbook.createStyle();
                    stl1.setRotationAngle(45);
                    stl1.setForegroundColor(new AsposeCells.Color(0, 51, 105));
                    stl1.setPattern(AsposeCells.BackgroundType.Solid);
                    stl1.getBorders().get(AsposeCells.BorderType.LeftBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
                    stl1.getBorders().get(AsposeCells.BorderType.LeftBorder).setColor(AsposeCells.Color.White);
                    stl1.setHorizontalAlignment(AsposeCells.TextAlignmentType.Center);
                    stl1.setVerticalAlignment(AsposeCells.TextAlignmentType.Center);
                    stl1.getFont().setName("Times New Roman");
                    stl1.getFont().setSize(10);
                    stl1.getFont().setColor(AsposeCells.Color.White);
                    stl1.getFont().setIsBold(true);

                    flag = new AsposeCells.StyleFlag();
                    flag.setLeftBorder(true);
                    flag.setRotation(true);
                    flag.setCellShading(true);
                    flag.setHorizontalAlignment(true);
                    flag.setVerticalAlignment(true);
                    flag.setFontName(true);
                    flag.setFontSize(true);
                    flag.setFontColor(true);
                    flag.setFontBold(true);
                    row = workbook.getWorksheets().get(0).getCells().getRows().get(1);
                    row.applyStyle(stl1, flag);
                    cells.setRowHeight(1, 48);

                    let stl2 = workbook.createStyle();
                    stl2.setForegroundColor(new AsposeCells.Color(155, 204, 255));
                    stl2.setPattern(AsposeCells.BackgroundType.Solid);
                    stl2.getFont().setName("Trebuchet MS");
                    stl2.getFont().setColor(AsposeCells.Color.Maroon);
                    stl2.getFont().setSize(10);
                    flag = new AsposeCells.StyleFlag();
                    flag.setCellShading(true);
                    flag.setFontName(true);
                    flag.setFontColor(true);
                    flag.setFontSize(true);

                    const col = workbook.getWorksheets().get(0).getCells().getColumns().get(0);
                    col.applyStyle(stl2, flag);

                    let stl3 = workbook.createStyle();
                    stl3.setForegroundColor(new AsposeCells.Color(124, 199, 72));
                    stl3.setPattern(AsposeCells.BackgroundType.Solid);
                    cells.get("A2").setStyle(stl3);

                    let stl4 = workbook.createStyle();
                    stl4.getFont().setColor(new AsposeCells.Color(0, 51, 105));
                    stl4.getBorders().get(AsposeCells.BorderType.BottomBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
                    stl4.getBorders().get(AsposeCells.BorderType.BottomBorder).setColor(new AsposeCells.Color(124, 199, 72));
                    stl4.setForegroundColor(AsposeCells.Color.White);
                    stl4.setPattern(AsposeCells.BackgroundType.Solid);
                    stl4.setCustom("$#,##0.0");

                    flag = new AsposeCells.StyleFlag();
                    flag.setFontColor(true);
                    flag.setCellShading(true);
                    flag.setNumberFormat(true);
                    flag.setBottomBorder(true);

                    let stl5 = workbook.createStyle();
                    stl5.getBorders().get(AsposeCells.BorderType.BottomBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
                    stl5.getBorders().get(AsposeCells.BorderType.BottomBorder).setColor(new AsposeCells.Color(124, 199, 72));
                    stl5.setForegroundColor(new AsposeCells.Color(250, 250, 200));
                    stl5.setPattern(AsposeCells.BackgroundType.Solid);
                    stl5.setCustom("$#,##0.0");
                    stl5.getFont().setColor(AsposeCells.Color.Maroon);

                    const range = workbook.getWorksheets().get(0).getCells().createRange("B3", "M25");
                    range.setName("MyRange");
                    range.applyStyle(stl4, flag);

                    for (let i = 0; i < 23; i++) {
                        for (let j = 0; j < 12; j++) {
                            if (i % 2 === 0) {
                                range.get(i, j).setStyle(stl5);
                            }
                        }
                    }

                    let stl6 = workbook.createStyle();
                    stl6.setForegroundColor(new AsposeCells.Color(0, 51, 105));
                    stl6.setPattern(AsposeCells.BackgroundType.Solid);
                    stl6.getFont().setName("Arial");
                    stl6.getFont().setSize(10);
                    stl6.getFont().setColor(AsposeCells.Color.White);
                    stl6.getFont().setIsBold(true);
                    stl6.setCustom("$#,##0.0");

                    flag = new AsposeCells.StyleFlag();
                    flag.setCellShading(true);
                    flag.setFontName(true);
                    flag.setFontSize(true);
                    flag.setFontColor(true);
                    flag.setFontBold(true);
                    flag.setNumberFormat(true);

                    row = workbook.getWorksheets().get(0).getCells().getRows().get(25);
                    row.applyStyle(stl6, flag);

                    for (let i = 2; i < 25; i++) {
                        cells.get(i, 13).setStyle(stl6);
                    }

                    workbook.getWorksheets().get(0).getCells().setColumnWidth(13, 9.33);
                }
            }

            FormatWorksheetCells.run();
        } catch (error) {
            console.error("Error occurred:", error);
        }
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
