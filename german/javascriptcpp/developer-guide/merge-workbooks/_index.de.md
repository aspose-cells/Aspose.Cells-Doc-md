---
title: Mehrere Arbeitsmappen mit JavaScript via C++ zu einer einzigen Arbeitsmappe zusammenfassen
linktitle: Arbeitsmappen Zusammenführung
type: docs
weight: 66
url: /de/javascript-cpp/combine-multiple-workbooks-into-a-single-workbook/
description: Erfahren Sie, wie Sie mit Aspose.Cells for JavaScript via C++ mehrere Arbeitsmappen zu einer einzigen Arbeitsmappe zusammenfassen. 
---

{{% alert color="primary" %}}

Manchmal müssen Sie Arbeitsmappen mit verschiedenen Inhalten wie Bildern, Diagrammen und Daten in eine einzelne Arbeitsmappe zusammenfassen. Aspose.Cells for JavaScript via C++ unterstützt diese Funktion. Dieser Artikel zeigt, wie man eine Konsolenanwendung erstellt und Arbeitsmappen mit wenigen, einfachen Zeilen Code mit Aspose.Cells zusammenführt.

{{% /alert %}}

## **Arbeitsbücher mit Bildern und Diagrammen kombinieren**

Der Beispielcode kombiniert zwei Arbeitsmappen zu einer einzigen Arbeitsmappe mit Aspose.Cells for JavaScript via C++. Der Code lädt die Quelldatensätze, verwendet die [**Workbook.combine(Workbook)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#combine-workbook-) Methode, um sie zusammenzuführen, und speichert die Ausgabearbeitsmappe.

### **Quell-Arbeitsbücher**

- [charts.xlsx](5473097.xlsx)
- [picture.xlsx](5473096.xlsx)

### **Ausgabearbeitsbücher**

- [combined.xlsx](5473095.xlsx)

### **Screenshots**

Nachfolgend finden Sie Screenshots der Quell- und Ausgabearbeitsbücher.

{{% alert color="primary" %}}

Sie können beliebige Quellarbeitsmappen verwenden. Diese Bilder dienen nur zur Veranschaulichung.

{{% /alert %}}

**Die erste Arbeitsblatt der Diagramme Arbeitsmappe - gestapelt** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_1.jpg)

**Zweites Arbeitsblatt der Diagramme Arbeitsmappe - Linie** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_2.jpg)

**Erstes Arbeitsblatt der Bild Arbeitsmappe - Bild** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_3.jpg)

**Alle drei Arbeitsblätter in der kombinierten Arbeitsmappe - gestapelt, Linie, Bild** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_4.jpg)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Combine Workbooks Example</title>
    </head>
    <body>
        <h1>Combine Workbooks Example</h1>
        <p>Select two Excel files to combine:</p>
        <input type="file" id="fileInput1" accept=".xls,.xlsx" />
        <input type="file" id="fileInput2" accept=".xls,.xlsx" />
        <button id="runExample">Combine Workbooks</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell } = AsposeCells;

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
            const fileInput1 = document.getElementById('fileInput1');
            const fileInput2 = document.getElementById('fileInput2');

            if (!fileInput1.files.length || !fileInput2.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select two Excel files.</p>';
                return;
            }

            const file1 = fileInput1.files[0];
            const file2 = fileInput2.files[0];

            const arrayBuffer1 = await file1.arrayBuffer();
            const arrayBuffer2 = await file2.arrayBuffer();

            // Open the first excel file.
            const sourceBook1 = new Workbook(new Uint8Array(arrayBuffer1));

            // Open the second excel file.
            const sourceBook2 = new Workbook(new Uint8Array(arrayBuffer2));

            // Combining the two workbooks
            sourceBook1.combine(sourceBook2);

            // Save the combined workbook and provide download link
            const outputData = sourceBook1.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Combined.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Combined Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbooks combined successfully! Click the download link to get the combined file.</p>';
        });
    </script>
</html>
```

## **Erweiterte Themen**
- [Mehrere Arbeitsblätter in ein einziges Arbeitsblatt kombinieren](/cells/de/javascript-cpp/combine-multiple-worksheets-into-a-single-worksheet/)
- [Dateien zusammenführen](/cells/de/javascript-cpp/merge-files/)
