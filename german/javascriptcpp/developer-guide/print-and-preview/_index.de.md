---
title: Arbeitsmappe mit JavaScript via C++ Vorschau anzeigen
linktitle: Arbeitsbuchvorschau 
type: docs
weight: 70
url: /de/javascript-cpp/workbook-and-worksheet-preview/
description: Aspose.Cells unterstützt das Drucken und die Vorschau von Excel Dateien ohne Microsoft Excel Installation mit JavaScript via C++.
---

## **Druckvorschau**  

In manchen Fällen müssen Excel-Dateien mit Millionen von Seiten in PDFs oder Bilder umgewandelt werden. Die Verarbeitung solcher Dateien kann viel Zeit und Ressourcen in Anspruch nehmen. In solchen Fällen kann die Funktion „Arbeitsbuch- und Arbeitsblatt-Druckvorschau“ nützlich sein. Vor der Konvertierung können Nutzer die Gesamtzahl der Seiten überprüfen und entscheiden, ob die Datei konvertiert werden soll oder nicht. Dieser Artikel konzentriert sich auf die Verwendung der Klassen [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/javascript-cpp/workbookprintingpreview/) und [**SheetPrintingPreview**](https://reference.aspose.com/cells/javascript-cpp/sheetprintingpreview/), um die Gesamtzahl der Seiten zu ermitteln.  

Aspose.Cells bietet die Funktion der Druckvorschau. Für diese Funktion stellt die API die Klassen [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/javascript-cpp/workbookprintingpreview/) und [**SheetPrintingPreview**](https://reference.aspose.com/cells/javascript-cpp/sheetprintingpreview/) bereit. Um die Druckvorschau des gesamten Arbeitsbuchs zu erstellen, erstellen Sie eine Instanz der [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/javascript-cpp/workbookprintingpreview/)-Klasse durch Übergabe der Objekte [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook/) und [**ImageOrPrintOptions**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/) an den Konstruktor. Die [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/javascript-cpp/workbookprintingpreview/)-Klasse bietet eine Methode [**evaluatedPageCount**](https://reference.aspose.com/cells/javascript-cpp/workbookprintingpreview/#evaluatedPageCount--), die die Anzahl der Seiten in der generierten Vorschau zurückgibt. Ähnlich wie die [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/javascript-cpp/workbookprintingpreview/)-Klasse wird die [**SheetPrintingPreview**](https://reference.aspose.com/cells/javascript-cpp/sheetprintingpreview/)-Klasse verwendet, um eine Druckvorschau für ein bestimmtes Arbeitsblatt zu erstellen. Um die Vorschau eines Arbeitsblatts zu erstellen, erstellen Sie eine Instanz der [**SheetPrintingPreview**](https://reference.aspose.com/cells/javascript-cpp/sheetprintingpreview/)-Klasse durch Übergabe der Objekte [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet/) und [**ImageOrPrintOptions**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/) an den Konstruktor. Die [**SheetPrintingPreview**](https://reference.aspose.com/cells/javascript-cpp/sheetprintingpreview/)-Klasse bietet ebenfalls eine [**evaluatedPageCount**](https://reference.aspose.com/cells/javascript-cpp/workbookprintingpreview/#evaluatedPageCount--)-Methode, die die Anzahl der Seiten in der generierten Vorschau zurückgibt.  

Das folgende Codebeispiel demonstriert die Verwendung der Klassen [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/javascript-cpp/workbookprintingpreview/) und [**SheetPrintingPreview**](https://reference.aspose.com/cells/javascript-cpp/sheetprintingpreview/) anhand einer [Beispieldatei](94896177.xlsx).  

### **Beispielcode**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Printing Preview</title>
    </head>
    <body>
        <h1>Printing Preview Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, ImageOrPrintOptions, WorkbookPrintingPreview, SheetPrintingPreview } = AsposeCells;

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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Creating image/print options
            const imgOptions = new ImageOrPrintOptions();

            // Workbook printing preview
            const preview = new WorkbookPrintingPreview(workbook, imgOptions);
            const workbookPageCount = preview.evaluatedPageCount;
            console.log("Workbook page count: " + workbookPageCount);

            // Worksheet printing preview for first worksheet
            const preview2 = new SheetPrintingPreview(workbook.worksheets.get(0), imgOptions);
            const worksheetPageCount = preview2.evaluatedPageCount;
            console.log("Worksheet page count: " + worksheetPageCount);

            document.getElementById('result').innerHTML = `<p>Workbook page count: ${workbookPageCount}</p><p>Worksheet page count: ${worksheetPageCount}</p>`;
        });
    </script>
</html>
```  

Das folgende ist die Ausgabe, die durch das Ausführen des obigen Codes generiert wird.  

### **Konsolenausgabe**  

{{< highlight javascript >}}  
Workbook page count: 1  
Worksheet page count: 1  
{{< /highlight >}}  

## **Erweiterte Themen**  
- [Konfiguration von Schriftarten für die Darstellung von Tabellenkalkulationen](/cells/de/javascript-cpp/configuring-fonts-for-rendering-spreadsheets/)  
- [Arbeitsblatt in Bild konvertieren - Leerraum um Daten entfernen](/cells/de/javascript-cpp/convert-worksheet-to-image-remove-whitespace-around-data/)  
- [Arbeitsblatt in Bild und Arbeitsblatt in Bild nach Seite konvertieren](/cells/de/javascript-cpp/converting-worksheet-to-image-and-worksheet-to-image-by-page/)  
- [Arbeitsblatt in Bild mit den Optionen Bild oder Druck konvertieren](/cells/de/javascript-cpp/converting-worksheet-to-image-using-imageorprint-options/)  
- [Bereich von Zellen in einem Arbeitsblatt in ein Bild exportieren](/cells/de/javascript-cpp/export-range-of-cells-in-a-worksheet-to-image/)  
- [Arbeitsblatt oder Diagramm in Bild mit gewünschter Breite und Höhe exportieren](/cells/de/javascript-cpp/export-worksheet-or-chart-into-image-with-desired-width-and-height/)  
- [Extrahieren von Bildern aus Arbeitsblättern mit ImageOrPrintOptions](/cells/de/javascript-cpp/extract-images-from-worksheets-using-imageorprintoptions/)  
- [Generieren einer Miniaturansicht des Arbeitsblatts](/cells/de/javascript-cpp/generate-thumbnail-of-the-worksheet/)  
- [Leeres Blatt ausgeben, wenn nichts gedruckt werden muss](/cells/de/javascript-cpp/output-blank-page-when-there-is-nothing-to-print/)  
- [Seiteneinrichtungs- und Druckoptionen](/cells/de/javascript-cpp/page-setup-and-printing-options/)  
- [Sequenz von Seiten rendern mithilfe der Eigenschaften PageIndex und PageCount von ImageOrPrintOptions](/cells/de/javascript-cpp/render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions/)  
- [Arbeitsblatt in Grafikkontext rendern](/cells/de/javascript-cpp/render-worksheet-to-graphic-context/)  
- [Individuelle oder private Schriftsätze für das Rendern von Arbeitsbüchern angeben](/cells/de/javascript-cpp/specify-individual-or-private-set-of-fonts-for-workbook-rendering/)
