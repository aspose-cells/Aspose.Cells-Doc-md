---
title: Excel Themen und Farben
linktitle: Excel Themen und Farben  
type: docs  
weight: 100  
url: /de/javascript-cpp/excel-themes-and-colors/  
description: Erfahren Sie, wie man benutzerdefinierte Farbschemata mit Aspose.Cells for JavaScript über C++ verwendet.  
keywords: JavaScript Farbschemata erstellen und anwenden, JavaScript Programmatisch ein benutzerdefiniertes Farbschema erstellen, Programmatisch anwenden, wie man ein Farbschema in Excel verwendet  
---

## **Wie man ein Farbschema in Excel erstellt und anwendet**  
Dokumentthemen erleichtern die Koordination von Farben, Schriftarten und grafischen Formatierungseffekten von Excel-Dokumenten und ermöglichen eine schnelle Aktualisierung.  
Themen bieten ein einheitliches Erscheinungsbild mit benannten Stilen, grafischen Effekten und anderen Objekten, die in einer Arbeitsmappe verwendet werden. Zum Beispiel sieht der Accent1-Stil in den Office- und den Apex-Themen unterschiedlich aus. Oft wenden Sie ein Dokumententhema an und ändern es dann nach Wunsch.  

### **Wie man ein Farbschema in Excel anwendet**  
1. Öffnen Sie Excel und wechseln Sie zum Register „Seitenlayout“ im Excel-Band.  
1. Klicken Sie auf die Schaltfläche „Farben“ im Abschnitt „Themen“.  
<br>  
<img src="color.png" width=70% />  
1. Wählen Sie eine Farbpalette aus, die Ihren Anforderungen entspricht, oder fahren Sie mit der Maus über ein Schema, um eine Live-Vorschau anzuzeigen.  

### **Wie man ein benutzerdefiniertes Farbschema in Excel erstellt**  
Sie können Ihre eigene Farbgebung erstellen, um Ihrem Dokument ein frisches, einzigartiges Aussehen zu verleihen oder den Markenstandards Ihrer Organisation zu entsprechen.  

1. Öffnen Sie Excel und wechseln Sie zum Register „Seitenlayout“ im Excel-Band.  
1. Klicken Sie auf die Schaltfläche „Farben“ im Abschnitt „Themen“.  
1. Klicken Sie auf die Schaltfläche „Farben anpassen...“.  
<br>  
<img src="color2.png" width=70% />  

1. In dem Dialogfeld „Neue Designfarben erstellen“ können Sie für jedes Element Farben auswählen, indem Sie auf die Farbauswahlfelder neben ihnen klicken. Sie können Farben aus der Palette auswählen oder benutzerdefinierte Farben über die Option „Mehr Farben“ definieren.  
<br>  
<img src="color3.png" width=70% />  
1. Nach Auswahl aller gewünschten Farben geben Sie einen Namen für Ihr benutzerdefiniertes Farbschema im Feld „Name“ an.  

1. Klicken Sie auf die Schaltfläche „Speichern“, um Ihr benutzerdefiniertes Farbschema zu speichern. Ihr benutzerdefiniertes Farbschema steht jetzt im Drop-Down-Menü „Farben“ für zukünftige Verwendungen zur Verfügung.  

## **Wie man ein Farbschema in Aspose.Cells erstellt und anwendet**  
Aspose.Cells bietet Funktionen zur Anpassung von Themen und Farben.  

### **Wie man ein benutzerdefiniertes Farbdesign in Aspose.Cells erstellt**  
Wenn im Dokument Themenfarben verwendet werden, müssen wir nicht jede Zelle einzeln ändern; wir müssen nur die Farben im Thema ändern.  

Das folgende Beispiel zeigt, wie benutzerdefinierte Designs mit den gewünschten Farben angewendet werden. Es wird eine Beispieldatei verwendet, die manuell in Microsoft Excel 2007 erstellt wurde.  

Das folgende Beispiel lädt eine Vorlage XLSX-Datei, definiert Farben für verschiedene Theme-Farbtypen, wendet die benutzerdefinierten Farben an und speichert die Excel-Datei.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Apply Custom Theme Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Color } = AsposeCells;

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Define Color array (of 12 colors) for Theme.
            const carr = [
                new Color("AntiqueWhite"), // Background1
                new Color("Brown"), // Text1
                new Color("AliceBlue"), // Background2
                new Color("Yellow"), // Text2
                new Color("YellowGreen"), // Accent1
                new Color("Red"), // Accent2
                new Color("Pink"), // Accent3
                new Color("Purple"), // Accent4
                new Color("PaleGreen"), // Accent5
                new Color("Orange"), // Accent6
                new Color("Green"), // Hyperlink
                new Color("Gray") // Followed Hyperlink
            ];

            // Set the custom theme with specified colors.
            workbook.customTheme("CustomeTheme1", carr);

            // Save as the excel file.
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Custom theme applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```



### **So wenden Sie Designs in Aspose.Cells an**  
Das folgende Beispiel wendet die Vordergrund- und Schriftfarben einer Zelle basierend auf den Standard-Theme-Farbtypen an. Es speichert auch die Excel-Datei auf der Festplatte.  


```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            // Instantiate a Workbook.
            const workbook = new Workbook();

            // Get cells collection in the first (default) worksheet.
            const cells = workbook.worksheets.get(0).cells;

            // Get the D3 cell.
            const c = cells.get("D3");

            // Get the style of the cell.
            const s = c.style;

            // Set foreground color for the cell from the default theme Accent2 color.
            s.foregroundThemeColor = new AsposeCells.ThemeColor(AsposeCells.ThemeColorType.Accent2, 0.5);

            // Set the pattern type.
            s.pattern = AsposeCells.BackgroundType.Solid;

            // Get the font for the style.
            const f = s.font;

            // Set the theme color.
            f.themeColor = new AsposeCells.ThemeColor(AsposeCells.ThemeColorType.Accent4, 0.1);

            // Apply style.
            c.style = s;

            // Put a value.
            c.value = "Testing1";

            // Save the excel file and provide download link.
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created. Click the download link to save the file.</p>';
        });
    </script>
</html>
```


### **So erhalten und setzen Sie Designs in Aspose.Cells**  
Nachfolgend finden Sie einige Methoden und Eigenschaften, die Designs implementieren.  

- [**Style.foregroundThemeColor**](https://reference.aspose.com/cells/javascript-cpp/style/#foregroundThemeColor-themecolor-): Wird verwendet, um die Vordergrundfarbe festzulegen.  
- [**Style.backgroundThemeColor**](https://reference.aspose.com/cells/javascript-cpp/style/#backgroundThemeColor-themecolor-): Wird verwendet, um die Hintergrundfarbe festzulegen.  
- [**Font.themeColor**](https://reference.aspose.com/cells/javascript-cpp/font/#themeColor-themecolor-): Wird verwendet, um die Schriftfarbe festzulegen.  
- [**Workbook.themeColor**](https://reference.aspose.com/cells/javascript-cpp/workbook/#themeColor-themecolortype-): Wird verwendet, um eine Thema-Farbe zu erhalten.  
- [**Workbook.themeColor**](https://reference.aspose.com/cells/javascript-cpp/workbook/#themeColor-themecolortype-color-): Wird verwendet, um eine Thema-Farbe festzulegen.  

Das folgende Beispiel zeigt, wie Designs erhalten und gesetzt werden.  

Das folgende Beispiel verwendet eine Vorlage XLSX-Datei, erhält die Farben für verschiedene Theme-Farbtypen, ändert die Farben und speichert die Microsoft Excel-Datei.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Theme Color Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Color, ThemeColorType } = AsposeCells;

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object and opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the Background1 theme color.
            let c = workbook.themeColor(ThemeColorType.Background1);
            console.log("theme color Background1: ", c);

            // Get the Accent2 theme color.
            c = workbook.themeColor(ThemeColorType.Accent2);
            console.log("theme color Accent2: ", c);

            // Change the Background1 theme color.
            workbook.themeColor(ThemeColorType.Background1, Color.Red);

            // Get the updated Background1 theme color.
            c = workbook.themeColor(ThemeColorType.Background1);
            console.log("theme color Background1 changed to: ", c);

            // Change the Accent2 theme color.
            workbook.themeColor(ThemeColorType.Accent2, Color.Blue);

            // Get the updated Accent2 theme color.
            c = workbook.themeColor(ThemeColorType.Accent2);
            console.log("theme color Accent2 changed to: ", c);

            // Saving the updated file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Updated Excel File';

            // Display results
            let resultHtml = '';
            resultHtml += `<p>theme color Background1: ${JSON.stringify(workbook.themeColor(ThemeColorType.Background1))}</p>`;
            resultHtml += `<p>theme color Accent2: ${JSON.stringify(workbook.themeColor(ThemeColorType.Accent2))}</p>`;
            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! See console for detailed logs.</p>' + resultHtml;
        });
    </script>
</html>
```


## **Erweiterte Themen**  
- [Extrahieren von Themen-Daten aus Excel-Datei](/cells/de/javascript-cpp/extract-theme-data-from-excel-file/)
