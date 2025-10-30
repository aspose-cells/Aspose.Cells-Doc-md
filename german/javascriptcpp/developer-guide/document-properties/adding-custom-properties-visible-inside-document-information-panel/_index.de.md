---
title: Hinzufügen benutzerdefinierter Eigenschaften, die im Dokumentinformationspanel sichtbar sind, mit JavaScript in C++
linktitle: Hinzufügen von benutzerdefinierten Eigenschaften, die im Dokumentinformationsfeld sichtbar sind
type: docs
weight: 300
url: /de/javascript-cpp/adding-custom-properties-visible-inside-document-information-panel/
description: Lernen Sie, wie man benutzerdefinierte Eigenschaften zu einem Workbook Objekt hinzufügt, indem Sie Aspose.Cells for JavaScript in C++ verwenden. Diese Eigenschaften sind im Dokumentinformationspanel sichtbar.
---

## **Hinzufügen von benutzerdefinierten Eigenschaften, die im Dokumentinformationsfeld sichtbar sind**

Aspose.Cells for JavaScript in C++ kann verwendet werden, um benutzerdefinierte Eigenschaften im Workbook-Objekt hinzuzufügen, die im Dokumentinformationspanel sichtbar sind. Sie können das Dokumentinformationspanel in Microsoft Excel öffnen, indem Sie die Befehle Datei > Info > Eigenschaften > Dokumentpanel anzeigen verwenden.

Bitte verwenden Sie die [**ContentTypePropertyCollection.add(string, string)**](https://reference.aspose.com/cells/javascript-cpp/contenttypepropertycollection/#add-string-string-)-Methode, um eine benutzerdefinierte Eigenschaft hinzuzufügen, die im Dokumentinformationsbereich sichtbar ist.

Der folgende Beispielcode fügt zwei benutzerdefinierte Eigenschaften hinzu. Die erste Eigenschaft hat keinen Typ, die zweite Eigenschaft hat den Typ DateTime. Sobald Sie die Ausgabedatei im Excel öffnen, die mit diesem Code generiert wurde, sehen Sie diese beiden Eigenschaften im Dokumentinformationsbereich.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Adding Custom Properties Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Create Workbook with Custom Properties</button>
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
            // Create workbook object
            const workbook = new Workbook();

            // Add simple property without any type
            workbook.contentTypeProperties.add("MK31", "Simple Data");

            // Add date time property with type
            workbook.contentTypeProperties.add("MK32", "04-Mar-2015", "DateTime");

            // Save the workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'AddingCustomPropertiesVisible_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and saved. Click the download link to get the file.</p>';
        });
    </script>
</html>
```

### **Verwandter Artikel**

{{% alert color="primary" %}}

- [Verwendung von benutzerdefinierten XML-Teilen in Aspose.Cells](/cells/de/net/use-custom-xml-parts-in-aspose-cells/)

{{% /alert %}}
