---
title: Importieren Sie XML in das Excel Arbeitsbuch mit JavaScript über C++
linktitle: XML Maps
type: docs
weight: 210
url: /de/javascript-cpp/import-xml-map-inside-a-workbook-using-aspose-cells/
description: Daten aus XML Dateien in Excel importieren mit Aspose.Cells for JavaScript via C++.
---

{{% alert color="primary" %}}

Aspose.Cells erlaubt das Importieren der XML-Karte innerhalb des Arbeitsbuchs mit der [**Workbook.importXml(string, string, number, number)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#importXml-string-string-number-number-)-Methode. Sie können XML-Map mit Microsoft Excel mit den folgenden Schritten importieren:

- Wählen Sie den **Entwickler**-Tab
- Klicken Sie auf **Importieren** im XML-Bereich und befolgen Sie die erforderlichen Schritte.

Sie müssen Ihre XML-Daten bereitstellen, um den Import abzuschließen. Hier ist ein [Beispiel-XML-Daten](5115037.txt), das Sie für Tests verwenden können.

{{% /alert %}}

## **Importieren Sie eine XML-Map mit Microsoft Excel**

Der folgende Screenshot zeigt, wie man eine XML-Map mit Microsoft Excel importiert.

|![todo:image_alt_text](import-xml-map-inside-a-workbook-using-aspose-cells_1.png)|
| :- |

## **XML-Karte mit Aspose.Cells for JavaScript via C++ importieren**

Der folgende Beispielcode zeigt, wie Sie die [**Workbook.importXml(string, string, number, number)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#importXml-string-string-number-number-) nutzen können. Es generiert die [Ausgabedatei Excel](5115036.xlsx) wie in diesem Screenshot gezeigt.

|![todo:image_alt_text](import-xml-map-inside-a-workbook-using-aspose-cells_2.png)|
| :- |

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Import XML</title>
    </head>
    <body>
        <h1>Import XML into Workbook Example</h1>
        <input type="file" id="xmlInput" accept=".xml,.txt" />
        <button id="runExample">Import XML and Save</button>
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
            const fileInput = document.getElementById('xmlInput');
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an XML file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const xmlText = await file.text();

            // Create a workbook
            const workbook = new Workbook();

            // Import your XML Map data starting from cell A1 on Sheet1
            workbook.importXml(xmlText, "Sheet1", 0, 0);

            // Save workbook to XLSX and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            resultDiv.innerHTML = '<p style="color: green;">XML imported and workbook saved. Click the download link to get the file.</p>';
        });
    </script>
</html>
```

## **Erweiterte Themen**
- [XML-Map innerhalb der Arbeitsmappe mit der Methode XmlMapCollection.add() hinzufügen](/cells/de/javascript-cpp/add-xml-map-inside-the-workbook-using-xmlmapcollection-add-method/)
- [Exportieren Sie XML-Daten, die mit der XML-Map in der Arbeitsmappe verknüpft sind](/cells/de/javascript-cpp/export-xml-data-linked-to-xml-map-inside-the-workbook/)
- [Finden Sie den Namen des Stammelements der XML-Map](/cells/de/javascript-cpp/find-the-root-element-name-of-xml-map/)
- [Zellen mit XML-Map-Elementen verknüpfen](/cells/de/javascript-cpp/link-cells-to-xml-map-elements/)
