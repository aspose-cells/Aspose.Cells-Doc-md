---
title: Leeres Arbeitsblatt mit JavaScript über C++ erkennen
linktitle: Erkennen leerer Arbeitsblätter
type: docs
weight: 410
url: /de/javascript-cpp/detecting-empty-worksheets/
description: Dieser Artikel zeigt Code, der erklärt, wie man leere Arbeitsblätter von Excel Arbeitsbüchern programmatisch mit der JavaScript API unter Verwendung der C++ Bibliothek erkennt.
keywords: Leeres Arbeitsblatt JavaScript über C++ erkennen, leeres Excel Arbeitsblatt JavaScript über C++ finden
---

## **Überprüfung auf belegte Zellen**

Arbeitsblätter können mit Werten gefüllt sein, wobei es sich um einfache Werte (Text, numerisch, Datum/Uhrzeit) oder Formeln oder formelbasierte Werte handelt. In einem solchen Fall ist es einfach zu erkennen, ob ein Arbeitsblatt leer ist oder nicht. Alles, was wir prüfen müssen, sind die Eigenschaften [**Cells.maxDataRow**](https://reference.aspose.com/cells/javascript-cpp/cells/#maxDataRow--) oder [**Cells.maxDataColumn**](https://reference.aspose.com/cells/javascript-cpp/cells/#maxDataColumn--). Wenn die oben genannten Eigenschaften Null oder positive Werte zurückgeben, bedeutet dies, dass ein oder mehrere Zellen gefüllt wurden; wenn jedoch eine dieser Eigenschaften -1 zurückgibt, weist dies darauf hin, dass keine Zellen im angegebenen Arbeitsblatt gefüllt sind.

{{% alert color="primary" %}}

Die Sammlungen Zeilen & Spalten haben nullbasierte Indizes; daher bedeutet eine Zelle in Zeile 0 & Spalte 0 die erste Zelle im Arbeitsblatt, nämlich A1.

{{% /alert %}}

## **Überprüfung auf leere initialisierte Zellen**

Alle Zellen mit Werten werden automatisch initialisiert; es besteht jedoch die Möglichkeit, dass ein Arbeitsblatt nur Zellen mit Formatierungen enthält. In einem solchen Szenario geben die Eigenschaften [**Cells.maxDataRow**](https://reference.aspose.com/cells/javascript-cpp/cells/#maxDataRow--) oder [**Cells.maxDataColumn**](https://reference.aspose.com/cells/javascript-cpp/cells/#maxDataColumn--) -1 zurück, was auf das Fehlen gefüllter Werte hinweist, aber initialisierte Zellen aufgrund von Zellformatierungen können mit diesem Ansatz nicht erkannt werden. Um zu prüfen, ob ein Arbeitsblatt leere initialisierte Zellen hat, wird empfohlen, die Methode `Enumerator.MoveNext` auf den von [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) gesammelten Enumerator anzuwenden. Wenn die Methode `Enumerator.MoveNext` **true** zurückgibt, bedeutet dies, dass es eine oder mehrere initialisierte Zellen im Arbeitsblatt gibt.

## **Überprüfung auf Formen**

Es ist möglich, dass ein Arbeitsblatt keine gefüllten Zellen hat; es könnte jedoch Formen & Objekte wie Steuerelemente, Diagramme, Bilder usw. enthalten. Wenn wir überprüfen möchten, ob ein Arbeitsblatt Formen enthält, können wir dies durch Inspektion der [**ShapeCollection.count**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#count--) Eigenschaft tun. Ein positiver Wert zeigt die Anwesenheit von Formen im Arbeitsblatt an.

## **Programmierbeispiel**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Check Non-Empty Worksheets Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

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
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const book = new Workbook(new Uint8Array(arrayBuffer));

            const messages = [];

            // Loop over all worksheets in the workbook
            for (let i = 0; i < book.worksheets.count; i++) {
                const sheet = book.worksheets.get(i);
                // Check if worksheet has populated cells
                if (sheet.cells.maxDataRow !== -1) {
                    messages.push(`${sheet.name} is not empty because one or more cells are populated`);
                }
                // Check if worksheet has shapes
                else if (sheet.shapes.count > 0) {
                    messages.push(`${sheet.name} is not empty because there are one or more shapes`);
                }
                // Check if worksheet has empty initialized cells
                else {
                    const range = sheet.cells.maxDisplayRange;
                    const rangeIterator = range.getEnumerator();
                    if (rangeIterator.moveNext()) {
                        messages.push(`${sheet.name} is not empty because one or more cells are initialized`);
                    }
                }
            }

            if (messages.length) {
                resultDiv.innerHTML = '<ul>' + messages.map(m => `<li>${m}</li>`).join('') + '</ul>';
            } else {
                resultDiv.innerHTML = '<p style="color: green;">No non-empty worksheets found.</p>';
            }
        });
    </script>
</html>
```
