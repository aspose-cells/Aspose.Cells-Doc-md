---
title: Warnungen bei Font Substitution beim Rendern einer Excel Datei mit JavaScript via C++ erhalten
linktitle: Warnungen für Schriftarten ersetzen beim Rendern von Excel Dateien erhalten
type: docs
weight: 230
url: /de/javascript-cpp/get-warnings-for-font-substitution-while-rendering-excel-file/
description: Erfahren Sie, wie Sie Warnungen bei Schriftartersetzungen beim Rendern von Excel Dateien in PDF mit Aspose.Cells for JavaScript über C++ erhalten.
---

{{% alert color="primary" %}}  

Manchmal ersetzt Aspose.Cells beim Rendern einer Microsoft Excel-Datei in PDF Schriftarten. Aspose.Cells bietet eine Funktion, die Entwickler darüber informiert, welche bestimmte Schriftart durch eine Warnung ersetzt wurde. Dies ist eine nützliche Funktion, die Ihnen helfen kann zu erkennen, warum ein von Aspose.Cells gerendertes PDF anders aussieht als die ursprüngliche Microsoft Excel-Datei, damit Sie geeignete Maßnahmen ergreifen können. Zum Beispiel, das Installieren der fehlenden Schriftarten, damit die Rendierungsergebnisse gleich aussehen.

{{% /alert %}}  

Um Warnungen für Schriftartensubstitution beim Rendern von Excel-Dateien zu PDF zu erhalten, implementieren Sie die IWarningCallback Schnittstelle und setzen Sie die PdfSaveOptions.warningCallback Eigenschaft mit Ihrer implementierten Schnittstelle.

Der folgende Screenshot zeigt eine Quell-Excel-Datei, die wir im folgenden Code verwenden werden. Sie enthält einige Texte in den Zellen A6 und A7 in Schriftarten, die von Microsoft Excel nicht korrekt gerendert werden.

|**Nicht alle Schriftarten werden korrekt gerendert**|  
| :- |  
|![todo:image_alt_text](get-warnings-for-font-substitution-while-rendering-excel-file_1.png)|  
Aspose.Cells wird die Schriftarten in den Zellen A6 und A7 durch geeignete Schriftarten ersetzen, wie unten gezeigt.

|**Ersetzte Schriftarten**|  
| :- |  
|![todo:image_alt_text](get-warnings-for-font-substitution-while-rendering-excel-file_2.png)|  
## **Quelldatei herunterladen und PDF ausgeben**  
Sie können die Quelldatei und das PDF-Output von den folgenden Links herunterladen

- [source.xlsx](5112611.xlsx)  
- [output.pdf](5112616.pdf)  
## **Code**  
Der folgende Code implementiert IWarningCallback und setzt die PdfSaveOptions.warningCallback Eigenschaft auf die implementierte Schnittstelle. Jetzt wird bei jeder SchriftartSubstitution in einer Zelle eine Warnung von Aspose.Cells ausgelöst, innerhalb der WarningCallback.Warning() Methode.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - GetWarningsForFontSubstitution</title>
    </head>
    <body>
        <h1>GetWarningsForFontSubstitution Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PdfSaveOptions } = AsposeCells;

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

        class GetWarningsForFontSubstitution {
            static warning(info) {
                if (info.type === AsposeCells.WarningType.FontSubstitution) {
                    console.log("WARNING INFO: " + info.description);
                }
            }
        }

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();
            // Instantiate workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Prepare PDF save options and assign warning callback
            const options = new PdfSaveOptions();
            options.warningCallback = GetWarningsForFontSubstitution;

            // Save workbook as PDF
            const outputData = workbook.save(SaveFormat.Pdf, options);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            resultDiv.innerHTML = '<p style="color: green;">PDF generated successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```  
## **Ergebnis**  
Nachdem die Quell-Excel-Datei in PDF konvertiert wurde, werden die Warnungen wie folgt in die Debug-Konsole ausgegeben:

{{< highlight java >}}  

 WARNING INFO: Font substitution: Font [ Athene Logos; Regular ] has been substituted in Cell [ A6 ] in Sheet [ Sheet1 ].  

WARNING INFO: Font substitution: Font [ B Traffic; Regular ] has been substituted in Cell [ A7 ] in Sheet [ Sheet1 ].  

{{< /highlight >}}  

{{% alert color="primary" %}}  

Wenn Ihre Tabelle Formeln enthält, ist es am besten, die Methode Workbook.calculateFormula kurz vor dem Rendern der Tabelle im PDF-Format aufzurufen. Dadurch wird sichergestellt, dass die formelabhängigen Werte neu berechnet werden und die richtigen Werte im PDF gerendert werden.

{{% /alert %}}
