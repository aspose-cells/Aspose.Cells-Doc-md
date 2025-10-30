---
title: Wie man Text in einer Zelle dreht
linktitle: Wie man Text in einer Zelle dreht  
type: docs  
weight: 80  
url: /de/javascript-cpp/how-to-rotate-text-of-cell/  
description: Erfahren Sie, wie Sie den Text einer Zelle programmatisch mit Aspose.Cells for JavaScript via C++ drehen.  
keywords: JavaScript via C++ Drehen des Texts einer Zelle, JavaScript Programmierung zum Drehen des Texts einer Zelle im Arbeitsbuch, Programmgesteuertes Einstellen des Zellrotationswinkels im Arbeitsbuch, JavaScript, wie man den Text einer Zelle in Excel dreht  
---

## **Drehen des Texts einer Zelle in Aspose.Cells for JavaScript via C++**

Aspose.Cells ist eine leistungsstarke JavaScript-Komponente, die Entwicklern ermöglicht, mit Excel-Tabellen programmatisch zu arbeiten. Eine der Funktionen von Aspose.Cells ist die Fähigkeit, Zellen zu drehen, was die Orientierung des Textes anpasst und die visuelle Präsentation Ihrer Daten verbessert. In diesem Dokument zeigen wir, wie man Zellen mit Aspose.Cells dreht.

## **Wie man den Text einer Zelle in Excel dreht**
Um eine Zelle in Excel zu drehen, können Sie die folgenden Schritte verwenden:
1. Öffnen Sie Excel und wählen Sie die Zelle oder den Zellenbereich aus, den Sie drehen möchten.
1. Klicken Sie mit der rechten Maustaste auf die ausgewählte Zelle(n) und wählen Sie "Zellen formatieren" aus dem Kontextmenü. Alternativ können Sie zum Register "Start" im Excel-Menüband gehen, auf die Dropdown-Schaltfläche "Format" in der Gruppe "Zellen" klicken und "Zellen formatieren" auswählen.
1. In dem Dialogfeld "Zellen formatieren" wechseln Sie zum Register "Ausrichtung".
1. Im Abschnitt "Ausrichtung" sehen Sie die Optionen zum Drehen des Textes. Sie können den gewünschten Drehwinkel in Grad direkt in das Feld "Grad" eingeben. Positive Werte drehen den Text gegen den Uhrzeigersinn, und negative Werte drehen ihn im Uhrzeigersinn.
<br>
![todo:image_alt_text](alignment.png)
1. Nachdem Sie die gewünschte Rotation ausgewählt haben, klicken Sie auf "OK", um die Änderungen anzuwenden. Die ausgewählte(n) Zelle(n) wird/werden nun je nach gewähltem Rotationswinkel oder -orientierung gedreht.

## **Wie man den Text einer Zelle mit Aspose.Cells API dreht**

Die [**Style.rotationAngle(number)**](https://reference.aspose.com/cells/javascript-cpp/style/#rotationAngle-number-)-Eigenschaft macht es bequem, Zellen zu drehen. Um Zellen in Aspose.Cells zu drehen, müssen Sie die folgenden Schritte befolgen:
1. Laden Sie die Excel-Arbeitsmappe  
<br>
Zunächst müssen Sie die Excel-Arbeitsmappe mit Aspose.Cells laden. Sie können die Workbook-Klasse verwenden, um eine vorhandene Excel-Datei zu öffnen oder eine neue zu erstellen. 

1. Zugriff auf das Arbeitsblatt  
<br>
Sobald die Arbeitsmappe geladen ist, müssen Sie auf das Arbeitsblatt zugreifen, auf dem Sie die Zellen drehen möchten. Sie können entweder auf das Arbeitsblatt nach Index oder Namen zugreifen. 

1. Text der Zelle drehen  
<br>
Nun, da Sie Zugriff auf das Arbeitsblatt haben, können Sie die Zellen drehen, indem Sie das Style-Objekt der gewünschten Zellen ändern. Das Style-Objekt ermöglicht es Ihnen, verschiedene Formatierungsoptionen festzulegen, einschließlich der Rotation. 

1. Arbeitsmappe speichern  
<br>
Nachdem die Zellen gedreht wurden, können Sie die modifizierte Arbeitsmappe mithilfe der Save-Methode wieder in eine Datei oder einen Stream speichern.

## **JavaScript-Beispielcode**

Bitte sehen Sie sich den folgenden Code an, er erstellt ein Arbeitsbuch-Objekt und setzt verschiedene Drehwinkel für mehrere Zellen. Der Screenshot zeigt das Ergebnis nach Ausführung des Beispielcodes.
<br>
<img src="rotation.png" width=80% />

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Rotate Text in Cells Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
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
            // Creating a new Workbook (blank)
            const workbook = new Workbook();

            // Obtaining the reference of the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Row index of the cell
            let row = 0;
            // Column index of the cell
            let column = 0; 

            let a1 = worksheet.cells.get(row, column);
            a1.putValue("a1 rotate text");
            let a1Style = a1.style;

            // Set the rotation angle in degrees
            a1Style.rotationAngle = 45; 
            a1.style = a1Style;

            // set Column index of the cell
            column = 1;
            let b1 = worksheet.cells.get(row, column);
            b1.putValue("b1 rotate text");
            let b1Style = b1.style;

            // Set the rotation angle in degrees
            b1Style.rotationAngle = 255;
            b1.style = b1Style;

            // set Column index of the cell
            column = 2;
            let c1 = worksheet.cells.get(row, column);
            c1.putValue("c1 rotate text");
            let c1Style = c1.style;

            // Set the rotation angle in degrees
            c1Style.rotationAngle = -90;
            c1.style = c1Style;

            // set Column index of the cell
            column = 3;
            let d1 = worksheet.cells.get(row, column);
            d1.putValue("d1 rotate text");
            let d1Style = d1.style;

            // Set the rotation angle in degrees
            d1Style.rotationAngle = -90;
            d1.style = d1Style;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
