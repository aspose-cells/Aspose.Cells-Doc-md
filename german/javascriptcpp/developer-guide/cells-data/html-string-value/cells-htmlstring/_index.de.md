---
title: Zellen HTML String verwalten
type: docs
weight: 600
url: /de/javascript-cpp/manage-cells-html-string/
description: Erfahren Sie, wie man Zellen HTML String über die Aspose.Cells for JavaScript via C++ API verwaltet.
keywords: HTML String in die Zelle einfügen mit JavaScript via C++, HTML String in die Zelle setzen mit JavaScript via C++, HTML String hinzufügen mit JavaScript, HTML String aus der Zelle abrufen mit JavaScript via C++, Zellen HTML String verwalten mit JavaScript via C++
---

## **Mögliche Verwendungsszenarien**
Wenn Sie gestylte Daten für eine bestimmte Zelle festlegen müssen, können Sie einen HTML-String der Zelle zuweisen. Natürlich können Sie auch den HTML-String der Zelle abrufen. Aspose.Cells for JavaScript via C++ bietet diese Funktion. Aspose.Cells stellt die folgenden Eigenschaften und Methoden bereit, um Ihnen bei der Zielerreichung zu helfen.
- [**Cell.htmlString(string)**](https://reference.aspose.com/cells/javascript-cpp/cell/#htmlString-string-)

## **HTML-String mit Aspose.Cells for JavaScript via C++ abrufen und setzen**
Dieses Beispiel zeigt, wie Sie:

1. Erstellen Sie ein Arbeitsbuch und fügen Sie einige Daten hinzu.
1. Holen Sie sich die spezifische Zelle im ersten Arbeitsblatt.
1. Setzen Sie den HTML-String in die Zelle.
1. Holen Sie sich den HTML-String der Zelle.

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

            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Obtaining the reference of the newly added worksheet
            let ws = workbook.worksheets.get(0);
            let cells = ws.cells;

            // Setting the value to the cells
            let cell = cells.get("A1");
            cell.value = "Fruit";
            cell = cells.get("B1");
            cell.value = "Count";
            cell = cells.get("C1");
            cell.value = "Price";

            cell = cells.get("A2");
            cell.value = "Apple";
            cell = cells.get("A3");
            cell.value = "Mango";
            cell = cells.get("A4");
            cell.value = "Blackberry";
            cell = cells.get("A5");
            cell.value = "Cherry";

            let c3 = cells.get("C3");
            // set html string for C3 cell.
            c3.htmlString = "<b>test bold</b>";

            let c4 = cells.get("C4");
            // set html string for C4 cell.
            c4.htmlString = "<i>test italic</i>";

            // get the html string of specific cell.
            console.log(c3.htmlString);
            console.log(c4.htmlString);

            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


## Ausgabe, die vom Beispielcode generiert wurde

Der folgende Screenshot zeigt die Ausgabe des obigen Beispielcodes.

![todo:image_alt_text](htmlstring.png)
