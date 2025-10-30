---
title: Tabellenblattzellen in einer Arbeitsmappe mit JavaScript über C++ formatieren
linktitle: 	Zellen in einem Arbeitsblatt in einer Arbeitsmappe formatieren
description: Lernen Sie, wie Sie Arbeitsblattzellen in einer Arbeitsmappe mithilfe von Aspose.Cells for JavaScript über C++ formatieren. Passen Sie das Erscheinungsbild und den Stil der Daten in Tabellen an.
keywords: Aspose.Cells, Arbeitsmappe, Arbeitsblatt, Zelle, Formatierung, Erscheinungsbild, Stil, JavaScript über C++
type: docs
weight: 2000
url: /de/javascript-cpp/format-worksheet-cells-in-a-workbook/
---

{{% alert color="primary" %}}  

Dieser Artikel zeigt, wie: 

1. Styles verwenden, um Daten schnell zu formatieren.
2. Zellen in Zeilen und Spalten formatieren.
3. Rändern und Farben verwenden, um Daten hervorzuheben.
4. Zahlenformate anwenden, um Daten hervorzuheben.
5. Schriftarten und Attribute verwenden, um Daten zu markieren.
6. Daten im benannten Bereich formatieren.
7. Daten-Ausrichtung und -Orientierung ändern.
8. Zeilenhöhe und Spaltenbreite einstellen.

Das Beispielprojekt führt alle diese Aufgaben aus und bietet Entwicklern eine detaillierte Beschreibung, wie man eine Arbeitsmappe erstellt, Daten hinzufügt und Formatierungen mithilfe von [Aspose.Cells](https://products.aspose.com/cells/javascript-cpp/) anwendet.

{{% /alert %}}  

## **Datenaufbereitung**

Formatierung wird verwendet, um zwischen verschiedenen Arten von Informationen zu unterscheiden und Daten klar anzuzeigen.

Ein Format stellt einen Stil dar und wird definiert als eine Reihe von Merkmalen, wie Schriftarten und Schriftgrößen, Zahlenformate, Zellrahmen, Zellenschattierung, Einzug, Ausrichtung und Textausrichtung. Rahmen bieten weitere Möglichkeiten, Informationen hervorzuheben. Ein Rahmen ist eine Linie um eine Zelle oder eine Gruppe von Zellen gezogen.

Zahlenformate machen Daten auch aussagekräftiger. Durch Anwendung verschiedener Zahlenformate können Sie das Erscheinungsbild von Zahlen ändern, ohne die zugrunde liegende Zahl zu ändern.

Aspose.Cells ermöglicht es Ihnen, leicht Rahmen um Zellen und Bereiche zu zeichnen. Es erlaubt auch, Schriftarten anzuwenden und Zellen zu schattieren. Die Komponente ist so effizient, dass Sie eine komplette Zeile oder Spalte formatieren, Ausrichtungen einstellen, Text umbrechen und rotieren können. Aspose.Cells unterstützt darüber hinaus alle Zahlformate, die von Microsoft Excel unterstützt werden.

Dieser Artikel zeigt, wie man eine Konsolenanwendung erstellt, die einen jährlichen Umsatzbericht generiert. Die Arbeitsmappe wird von Grund auf neu erstellt, anschließend werden Daten eingefügt und die Arbeitsmappe formatiert. Wir zeigen, wie man eine einfache Konsolenanwendung erstellt, die eine Excel-Arbeitsmappe (Sie können auch eine Vorlage verwenden) erstellt, Verkaufsdaten in das erste Arbeitsblatt einfügt, die Daten formatiert und eine Excel-Datei speichert.

### **Verfahren**

Im Folgenden sind die Schritte aufgeführt, wie man ein Tabellenblatt erstellt und verschiedene Zellen in verschiedenen Zeilen und Spalten eines Tabellenblatts formatiert.

1. Laden Sie Aspose.Cells herunter und installieren Sie es:
   1. [Herunterladen](https://downloads.aspose.com/cells/javascript-cpp) von Aspose.Cells for JavaScript über C++.
   1. Installieren Sie es auf Ihrem Entwicklungscomputer.
2. Erstellen Sie ein Projekt und fügen Sie Referenzen hinzu:
   1. Starten Sie Ihren Code-Editor/IDE.
   1. Erstellen Sie eine neue Konsolenanwendung.
   1. Fügen Sie einen Verweis auf Aspose.Cells in Ihr JavaScript-Projekt ein.
3. Fügen Sie den folgenden Code zum Projekt hinzu:

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Code Example (Fallback)</title>
    </head>
    <body>
        <h1>Code Example</h1>
        <p><strong>Note:</strong> This example shows the original JavaScript code. Please convert manually to browser JavaScript.</p>
        <pre><code>try
        {
            const AsposeCells = require(&quot;aspose.cells.node&quot;);
            const path = require(&quot;path&quot;);

            class FormatWorksheetCells 
            {
                static run() {
                    const dataDir = path.join(__dirname, &quot;data&quot;);
                    const filename = path.join(dataDir, &quot;FormatWorksheet.xls&quot;);
                    FormatWorksheetCells.createSalesReport(filename);
                }

                static createSalesReport(filename) {
                    const cellsLicense = new AsposeCells.License();
                    cellsLicense.setLicense(&quot;Aspose.Cells.lic&quot;);

                    const workbook = new AsposeCells.Workbook();
                    workbook.changePalette(new AsposeCells.Color(155, 204, 255), 55);
                    workbook.changePalette(new AsposeCells.Color(0, 51, 105), 54);
                    workbook.changePalette(new AsposeCells.Color(250, 250, 200), 53);
                    workbook.changePalette(new AsposeCells.Color(124, 199, 72), 52);

                    FormatWorksheetCells.createReportData(workbook);
                    FormatWorksheetCells.createCellsFormatting(workbook);

                    const worksheet = workbook.getWorksheets().get(0);
                    worksheet.setName(&quot;Sales Report&quot;);
                    workbook.save(filename);
                }

                static createReportData(workbook) {
                    const cells = workbook.getWorksheets().get(0).getCells();
                    cells.get(&quot;B1&quot;).putValue(&quot;Western Product Sales 2006&quot;);

                    const headers = [&quot;January&quot;, &quot;February&quot;, &quot;March&quot;, &quot;April&quot;, &quot;May&quot;, &quot;June&quot;, &quot;July&quot;, &quot;August&quot;, &quot;September&quot;, &quot;October&quot;, &quot;November&quot;, &quot;December&quot;, &quot;Total&quot;];
                    headers.forEach((header, index) =&gt; {
                        cells.get(1, index + 1).putValue(header);
                    });

                    const productNames = [&quot;Biscuits&quot;, &quot;Coffee&quot;, &quot;Tofu&quot;, &quot;Ikura&quot;, &quot;Choclade&quot;, &quot;Maxilaku&quot;, &quot;Scones&quot;, &quot;Sauce&quot;, &quot;Syrup&quot;, &quot;Spegesild&quot;, &quot;Filo Mix&quot;, &quot;Pears&quot;, &quot;Konbu&quot;, &quot;Kaviar&quot;, &quot;Zaanse&quot;, &quot;Cabrales&quot;, &quot;Gnocchi&quot;, &quot;Wimmers&quot;, &quot;Breads&quot;, &quot;Lager&quot;, &quot;Gravad&quot;, &quot;Telino&quot;, &quot;Pavlova&quot;, &quot;Total&quot;];
                    productNames.forEach((name, index) =&gt; {
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

                    salesData.forEach((rowData, rowIndex) =&gt; {
                        rowData.forEach((value, colIndex) =&gt; {
                            cells.get(rowIndex + 3, colIndex + 1).putValue(value);
                        });
                    });

                    for (let i = 2; i &lt; 27; i++) {
                        cells.get(i, 13).setFormula(`=SUM(B${i+1}:M${i+1})`);
                    }
                    for (let i = 3; i &lt;= 25; i++) {
                        cells.get(i, 13).setFormula(`=SUM(B${i + 1}:M${i + 1})`);
                    }

                    cells.get(26, 13).setFormula(&quot;=SUM(N3:N25)&quot;);
                }

                static createCellsFormatting(workbook)
                {
                    let stl0 = workbook.createStyle();
                    stl0.setForegroundColor(new AsposeCells.Color(155, 204, 255));
                    stl0.setPattern(AsposeCells.BackgroundType.Solid);
                    stl0.getFont().setName(&quot;Trebuchet MS&quot;);
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
                    stl1.getFont().setName(&quot;Times New Roman&quot;);
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
                    stl2.getFont().setName(&quot;Trebuchet MS&quot;);
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
                    cells.get(&quot;A2&quot;).setStyle(stl3);

                    let stl4 = workbook.createStyle();
                    stl4.getFont().setColor(new AsposeCells.Color(0, 51, 105));
                    stl4.getBorders().get(AsposeCells.BorderType.BottomBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
                    stl4.getBorders().get(AsposeCells.BorderType.BottomBorder).setColor(new AsposeCells.Color(124, 199, 72));
                    stl4.setForegroundColor(AsposeCells.Color.White);
                    stl4.setPattern(AsposeCells.BackgroundType.Solid);
                    stl4.setCustom(&quot;$#,##0.0&quot;);

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
                    stl5.setCustom(&quot;$#,##0.0&quot;);
                    stl5.getFont().setColor(AsposeCells.Color.Maroon);

                    const range = workbook.getWorksheets().get(0).getCells().createRange(&quot;B3&quot;, &quot;M25&quot;);
                    range.setName(&quot;MyRange&quot;);
                    range.applyStyle(stl4, flag);

                    for (let i = 0; i &lt; 23; i++) {
                        for (let j = 0; j &lt; 12; j++) {
                            if (i % 2 === 0) {
                                range.get(i, j).setStyle(stl5);
                            }
                        }
                    }

                    let stl6 = workbook.createStyle();
                    stl6.setForegroundColor(new AsposeCells.Color(0, 51, 105));
                    stl6.setPattern(AsposeCells.BackgroundType.Solid);
                    stl6.getFont().setName(&quot;Arial&quot;);
                    stl6.getFont().setSize(10);
                    stl6.getFont().setColor(AsposeCells.Color.White);
                    stl6.getFont().setIsBold(true);
                    stl6.setCustom(&quot;$#,##0.0&quot;);

                    flag = new AsposeCells.StyleFlag();
                    flag.setCellShading(true);
                    flag.setFontName(true);
                    flag.setFontSize(true);
                    flag.setFontColor(true);
                    flag.setFontBold(true);
                    flag.setNumberFormat(true);

                    row = workbook.getWorksheets().get(0).getCells().getRows().get(25);
                    row.applyStyle(stl6, flag);

                    for (let i = 2; i &lt; 25; i++) {
                        cells.get(i, 13).setStyle(stl6);
                    }

                    workbook.getWorksheets().get(0).getCells().setColumnWidth(13, 9.33);
                }
            }

            FormatWorksheetCells.run();
        } catch (error) {
            console.error(&quot;Error occurred:&quot;, error);
        }</code></pre>

        <script src="aspose.cells.js.min.js"></script>
        <script>
            AsposeCells.onReady({
                license: "/lic/aspose.cells.enc",
                fontPath: "/fonts/",
                fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
            }).then(() => {
                console.log("Aspose.Cells initialized - manual conversion required");
            });
        </script>
    </body>
</html>
```
