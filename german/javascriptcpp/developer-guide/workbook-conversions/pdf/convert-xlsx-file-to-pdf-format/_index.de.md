---
title: Konvertiere XLSX Datei in PDF Format mit JavaScript via C++
linktitle: XLSX Datei in PDF Format konvertieren
type: docs
weight: 30
url: /de/javascript-cpp/convert-xlsx-file-to-pdf-format/
description: Diese Anleitung erklärt, wie man eine Excel Datei (XLSX) mit Aspose.Cells for JavaScript via C++ in das PDF Format konvertiert. 
---

{{% alert color="primary" %}}

PDF (Portable Document Format) repräsentiert Dokumente unabhängig von der Software, Hardware und dem Betriebssystem, die zur Erstellung dieser Dokumente verwendet werden. Eine PDF-Datei kann Dokumente mit einer beliebigen Kombination von Text, Grafiken und Bildern in einer geräteunabhängigen und auflösungsunabhängigen Weise darstellen. PDF-Dateien werden oft komprimiert, so dass sie weniger Speicherplatz als die Originaldatei benötigen.

Manchmal ist es notwendig, eine Microsoft Excel-Datei in PDF umzuwandeln. Für diesen Zweck benötigen Sie eine schnelle, sichere, genaue und zuverlässige Lösung, mit der Sie PDF-Dokumente weltweit verteilen können. Es gibt zahlreiche Konvertierungstools, die diese Aufgabe erledigen können. Aber Sie müssen sicherstellen, dass das Layout des Original-Excel-Dokuments im Ausgabepdf erhalten bleibt. Bilder, Diagramme, Formen, Datenformatierungen, Schriftarten, Attribute, Farben, Seiteneinrichtung, Textausrichtung, Rahmen, Diagramme usw. sollten genau und präzise dargestellt werden. [Aspose.Cells](https://products.aspose.com/cells/javascript-cpp/) gewährleistet eine hochpräzise Konvertierung.

Dieses Dokument soll ein umfassendes Verständnis dafür vermitteln, wie ein Microsoft Excel-Dokument (mit Bildern, Diagrammen, Formatierungen usw.) in PDF konvertiert werden kann. Dazu zeigt es, wie man eine einfache Konsolenanwendung in JavaScript via C++ erstellt, die eine Excel-Datei mit Aspose.Cells API in PDF umwandelt. Die Konvertierung erfolgt mit hoher Präzision und Genauigkeit.

{{% /alert %}}

## **Konvertierung von Excel nach PDF**

Dieses Beispiel verwendet eine Excel-Datei (SampleInput.xlsx) als Vorlage. Die Arbeitsmappe enthält Arbeitsblätter mit Diagrammen und Bildern. Jedes Arbeitsblatt enthält verschiedene Typen von Formaten unter Verwendung von Schriftarten, Attributen, Farben, Schattierungseffekten und Rahmen. Auf dem ersten Arbeitsblatt befindet sich ein Säulendiagramm und auf dem letzten ein Bild.

### **Die Vorlagen Excel-Datei**

Die Vorlage-Datei hat drei Arbeitsblätter, darunter Diagramme und Bilder als Medien. Das erste Arbeitsblatt enthält Diagramme und das letzte ein Bild, wie in den Screenshots gezeigt.

|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet1.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet2.png)|
| :- | :- |
|Das erste Arbeitsblatt **(Umsatzprognose)**|Das zweite Arbeitsblatt **(Verkaufsbericht)**|
|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet3.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet4.png)|
|Das dritte Arbeitsblatt **(Dateneingabe)**|Das letzte Arbeitsblatt **(Bild)**|

### **Konvertierungsprozess**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Excel to PDF</title>
    </head>
    <body>
        <h1>Excel to PDF Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to PDF</button>
        <a id="downloadLink" style="display: none;"></a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils } = AsposeCells;

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

            // Instantiating a Workbook object with the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Saving the PDF file
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Output.out.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF generated successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}

Wenn die Tabelle Formeln enthält, ist es am besten, die Methode [Workbook.calculateFormula()](https://reference.aspose.com/cells/javascript-cpp/workbook/#calculateFormula--) kurz vor der Ausgabe in PDF aufzurufen. Dadurch wird sichergestellt, dass formelabhängige Werte neu berechnet werden und die korrekten Werte im PDF angezeigt werden.

{{% /alert %}}

### **Ergebnis**

Wenn der obige Code ausgeführt wurde, wird eine PDF-Datei im Ordner Files im Anwendungsverzeichnis erstellt.
Die folgenden Screenshots zeigen die PDF-Seiten. Beachten Sie, dass Kopf- und Fußzeilen auch in der Ausgabe-PDF-Datei beibehalten werden.

|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted1.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted2.png)|
| :- | :- |
|Das erste Arbeitsblatt **(Umsatzprognose)**|Das zweite Arbeitsblatt **(Verkaufsbericht)**|
|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted3.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted4.png)|
|Das dritte Arbeitsblatt **(Dateneingabe)**|Das letzte Arbeitsblatt **(Bild)**|
