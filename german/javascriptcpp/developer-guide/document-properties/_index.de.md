---
title: Dokumenteigenschaften mit JavaScript über C++ verwalten
linktitle: Dokumenteigenschaften
type: docs
weight: 80
url: /de/javascript-cpp/managing-document-properties/
description: Erfahren Sie, wie Sie Dokumenteigenschaften durch die Aspose.Cells for JavaScript APIs in C++ verwalten.
keywords: Wie man Dokumenteigenschaften in JavaScript über C++ verwaltet, Dokumenteigenschaften mit JavaScript über C++ abrufen oder setzen, Dokumenteigenschaften hinzufügen oder löschen mit via JavaScript über C++, Dokumenteigenschaften mit JavaScript über C++ einfügen oder entfernen, Zugriff auf Dokumenteigenschaften mit Aspose.Cells for JavaScript APIs in C++.
---

## **Einführung**

Microsoft Excel bietet die Möglichkeit, Eigenschaften zu Tabellendateien hinzuzufügen. Diese Dokumenteigenschaften liefern nützliche Informationen und sind in 2 Kategorien unterteilt, wie unten näher beschrieben.

- Systemdefinierte (eingebaute) Eigenschaften: Eingebaute Eigenschaften enthalten allgemeine Informationen zum Dokument wie Dokumententitel, Autorname, Dokumentenstatistiken und so weiter.
- Benutzerdefinierte (benutzerdefinierte) Eigenschaften: Benutzerdefinierte Eigenschaften, die vom Endbenutzer in Form von Schlüssel-Wert-Paar definiert werden.

{{% alert color="primary" %}}

Der wichtigste Punkt über eingebaute und benutzerdefinierte Eigenschaften ist, dass auf eingebaute Eigenschaften zugegriffen und geändert, aber nicht erstellt oder entfernt werden kann. Benutzerdefinierte Eigenschaften hingegen können erstellt und verwaltet werden.

{{% /alert %}}

## **So verwalten Sie Dokumenteigenschaften mit Microsoft Excel**

Microsoft Excel ermöglicht es, die Dokumenteigenschaften der Excel-Dateien WYSIWYG-mäßig zu verwalten. Bitte folgen Sie den unten stehenden Schritten, um den **Eigenschaften**-Dialog in Excel 2016 zu öffnen.

1. Wählen Sie im **Datei**-Menü **Info** aus.

|**Auswahl des Info-Menüs**|
| :- |
|![todo:image_alt_text](managing-document-properties_1.png)|
1. Klicken Sie auf die Überschrift **Eigenschaften** und wählen Sie "Erweiterte Eigenschaften" aus.

|**Klicken Sie auf die Auswahl der erweiterten Eigenschaften**|
| :- |
|![todo:image_alt_text](managing-document-properties_2.png)|
1. Verwalten Sie die Dokumenteigenschaften der Datei.

|**Eigenschaften Dialog**|
| :- |
|![todo:image_alt_text](managing-document-properties_3.png)|
Im Eigenschaften-Dialog gibt es verschiedene Registerkarten wie Allgemein, Zusammenfassung, Statistiken, Inhalt und Benutzerdefinierte. Jede Registerkarte dient dazu, verschiedene Arten von Informationen im Zusammenhang mit der Datei zu konfigurieren. Die Registerkarte Benutzerdefiniert wird verwendet, um benutzerdefinierte Eigenschaften zu verwalten.

## **So arbeiten Sie mit Dokumenteigenschaften mit Aspose.Cells**

Entwickler können die Dokumenteigenschaften dynamisch mit den Aspose.Cells APIs verwalten. Diese Funktion hilft den Entwicklern, nützliche Informationen zusammen mit der Datei zu speichern, z. B. wann die Datei empfangen, verarbeitet, zeitgestempelt wurde usw.

{{% alert color="primary" %}}

Aspose.Cells for JavaScript über C++ schreibt direkt die API- und Versionsnummer-Informationen in Ausgabedokumente. Zum Beispiel füllt Aspose.Cells for JavaScript in C++ beim Rendern eines Dokuments zu PDF das Feld **Application** mit 'Aspose.Cells' und das Feld **PDF Producer** mit z.B. 'Aspose.Cells v17.9'.

Bitte beachten Sie, dass Sie Aspose.Cells for JavaScript in C++ nicht anweisen können, diese Informationen aus den Ausgabedokumenten zu ändern oder zu entfernen.

{{% /alert %}}

### **Wie Sie auf Dokumenteigenschaften zugreifen**

Aspose.Cells APIs unterstützen beide Arten von Dokumenteigenschaften, eingebaut und benutzerdefiniert. Die Klasse [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) von Aspose.Cells repräsentiert eine Excel-Datei und, wie eine Excel-Datei, kann die Klasse [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) mehrere Arbeitsblätter enthalten, die jeweils durch die Klasse [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) dargestellt werden, während die Sammlung der Arbeitsblätter durch die Klasse [**WorksheetCollection**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection) repräsentiert wird.

Verwenden Sie den [**WorksheetCollection**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection), um auf die Dokumenteigenschaften der Datei wie unten beschrieben zuzugreifen.

- Um auf die integrierten Dokumenteigenschaften zuzugreifen, verwenden Sie [**WorksheetCollection.builtInDocumentProperties()**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection/#builtInDocumentProperties--).
- Um auf benutzerdefinierte Dokumenteigenschaften zuzugreifen, verwenden Sie [**WorksheetCollection.customDocumentProperties()**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection/#customDocumentProperties--).

Sowohl [**WorksheetCollection.builtInDocumentProperties()**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection/#builtInDocumentProperties--) als auch [**WorksheetCollection.customDocumentProperties()**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection/#customDocumentProperties--) geben die Instanz von [**Aspose.Cells.Properties.DocumentPropertyCollection**](https://reference.aspose.com/cells/javascript-cpp/documentpropertycollection/) zurück. Diese Sammlung enthält [**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/javascript-cpp/documentproperty/) Objekte, die jeweils eine einzelne eingebaut oder benutzerdefinierte Dokumenteigenschaft repräsentieren.

Es liegt an der Anwendungsanforderung, wie man auf eine Eigenschaft zugreift; d.h. entweder durch Verwendung des Index oder des Namens der Eigenschaft aus [**DocumentPropertyCollection**](https://reference.aspose.com/cells/javascript-cpp/documentpropertycollection/), wie im Beispiel unten demonstriert.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Document Properties</title>
    </head>
    <body>
        <h1>Document Properties Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Load Document Properties</button>
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
            const resultEl = document.getElementById('result');
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                resultEl.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object and opening the Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Retrieve a list of all custom document properties of the Excel file
            const customProperties = workbook.customDocumentProperties;

            // Accessing a custom document property by using the property name
            const customProperty1 = customProperties.get("ContentTypeId");
            // Accessing the same custom document property by using the property index
            const customProperty2 = customProperties.get(0);

            const outputs = [];
            if (customProperty1) {
                outputs.push(`<p>${customProperty1.name} ${customProperty1.value}</p>`);
            }
            if (customProperty2) {
                outputs.push(`<p>${customProperty2.name} ${customProperty2.value}</p>`);
            }
            if (!outputs.length) {
                resultEl.innerHTML = '<p style="color: orange;">No custom document properties found.</p>';
            } else {
                resultEl.innerHTML = outputs.join('');
            }
        });
    </script>
</html>
```

Die Klasse [**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/javascript-cpp/documentproperty/) erlaubt das Abrufen des Namens, Werts und Typs der Dokumenteigenschaft:

- Um den Eigenschaftsnamen zu erhalten, verwenden Sie [**DocumentProperty.name()**](https://reference.aspose.com/cells/javascript-cpp/documentproperty/#name--).
- Um den Eigenschaftswert zu erhalten, verwenden Sie [**DocumentProperty.value()**](https://reference.aspose.com/cells/javascript-cpp/documentproperty/#value--). [**DocumentProperty.value()**](https://reference.aspose.com/cells/javascript-cpp/documentproperty/#value--) gibt den Wert als Objekt zurück.
- Um den Eigenschaftstyp zu erhalten, verwenden Sie [**DocumentProperty.type()**](https://reference.aspose.com/cells/javascript-cpp/documentproperty/#type--). Dies gibt einen der [**PropertyType**](https://reference.aspose.com/cells/javascript-cpp/propertytype/) Aufzählungswerte zurück. Nachdem Sie den Eigenschaftstyp erhalten haben, nutzen Sie eine der Methoden **DocumentProperty.ToXXX**, um den Wert des entsprechenden Typs zu erhalten, anstatt [**DocumentProperty.value()**](https://reference.aspose.com/cells/javascript-cpp/documentproperty/#value--) zu verwenden. Die **DocumentProperty.ToXXX**-Methoden sind in der Tabelle unten beschrieben.

{{% alert color="primary" %}}

Die Klasse [**DocumentProperty**](https://reference.aspose.com/cells/javascript-cpp/documentproperty/) bietet auch eine Reihe von Methoden, die die Werte anderer Datentypen zurückgeben.

{{% /alert %}}

|**Member Name**|**Beschreibung**|**ToXXX Methode**|
| :- | :- | :- |
|Boolean|Der Eigenschaftsdatentyp ist Boolean|ToBool|
|Date|Der Eigenschaftsdatentyp ist DateTime. Beachten Sie, dass Microsoft Excel nur den Datumsanteil speichert, keine Zeit in einer benutzerdefinierten Eigenschaft dieses Typs gespeichert werden kann|ToDateTime|
|Float|Der Eigenschaftsdatentyp ist Double|ToDouble|
|Number|Der Eigenschaftsdatentyp ist Int32|ToInt|
|String|Der Datentyp der Eigenschaft ist string|ToString|

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Retrieve Custom Document Properties Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
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
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');
            resultDiv.innerHTML = '';

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate a Workbook object by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Retrieve a list of all custom document properties of the Excel file
            const customProperties = workbook.customDocumentProperties;

            let outputHtml = '<h2>Custom Document Properties</h2>';

            // Accessing a custom document property (first)
            const customProperty1 = customProperties.get(0);
            if (customProperty1) {
                // Storing the value of the document property as an object
                const objectValue = customProperty1.value;
                outputHtml += `<p><strong>${customProperty1.name}</strong> (type: ${customProperty1.type}) : ${objectValue}</p>`;
            } else {
                outputHtml += '<p>No first custom property found.</p>';
            }

            // Accessing a custom document property (second)
            const customProperty2 = customProperties.get(1);
            if (customProperty2) {
                // Checking the type of the document property and then storing the value according to that type
                if (customProperty2.type === AsposeCells.PropertyType.String) {
                    const value = customProperty2.value.toString();
                    outputHtml += `<p>${customProperty2.name} : ${value}</p>`;
                } else {
                    outputHtml += `<p>${customProperty2.name} (type: ${customProperty2.type}) : ${customProperty2.value}</p>`;
                }
            } else {
                outputHtml += '<p>No second custom property found.</p>';
            }

            resultDiv.innerHTML = outputHtml;
        });
    </script>
</html>
```

### **Hinzufügen oder Entfernen von benutzerdefinierten Dokumenteigenschaften**

Wie wir zu Beginn dieses Themas bereits beschrieben haben, können Entwickler integrierte Eigenschaften nicht hinzufügen oder entfernen, da diese Eigenschaften systemdefiniert sind, es ist jedoch möglich, benutzerdefinierte Eigenschaften hinzuzufügen oder zu entfernen, da diese benutzerdefiniert sind.

### **Hinzufügen von benutzerdefinierten Eigenschaften**

Aspose.Cells APIs haben die Methode [**add(string, string)**](https://reference.aspose.com/cells/javascript-cpp/customdocumentpropertycollection/#add-string-string-) für die Klasse [**CustomDocumentPropertyCollection**](https://reference.aspose.com/cells/javascript-cpp/customdocumentpropertycollection/) bereitgestellt, um benutzerdefinierte Eigenschaften zur Sammlung hinzuzufügen. Die Methode [**add(string, string)**](https://reference.aspose.com/cells/javascript-cpp/customdocumentpropertycollection/#add-string-string-) fügt die Eigenschaft in die Excel-Datei ein und gibt eine Referenz auf die neue Dokumenteigenschaft als [**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/javascript-cpp/documentproperty/) Objekt zurück.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Add Custom Document Property</h1>
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

            document.getElementById('runExample').addEventListener('click', async () => {
                const fileInput = document.getElementById('fileInput');
                if (!fileInput.files.length) {
                    document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                    return;
                }

                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();

                // Instantiating a Workbook object and opening the Excel file
                const workbook = new Workbook(new Uint8Array(arrayBuffer));

                // Retrieve a list of all custom document properties of the Excel file
                const customProperties = workbook.customDocumentProperties;

                // Adding a custom document property to the Excel file
                customProperties.add("Publisher", "Aspose");

                // Saving the modified Excel file
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = 'out_sample-document-properties.xlsx';
                downloadLink.style.display = 'block';
                downloadLink.textContent = 'Download Modified Excel File';

                document.getElementById('result').innerHTML = '<p style="color: green;">Custom property added successfully! Click the download link to get the modified file.</p>';
            });
        });
    </script>
</html>
```

### **Wie konfiguriert man die benutzerdefinierte Eigenschaft „Verknüpfung zum Inhalt“?**

Um eine benutzerdefinierte Eigenschaft zu erstellen, die mit dem Inhalt eines bestimmten Bereichs verknüpft ist, rufen Sie die Methode [**CustomDocumentPropertyCollection.addLinkToContent(string, string)**](https://reference.aspose.com/cells/javascript-cpp/customdocumentpropertycollection/#addLinkToContent-string-string-) auf und übergeben den Eigenschaftsnamen und die Quelle. Sie können überprüfen, ob eine Eigenschaft als mit Inhalt verknüpft konfiguriert ist, indem Sie die [**DocumentProperty.isLinkedToContent()**](https://reference.aspose.com/cells/javascript-cpp/documentproperty/#isLinkedToContent--) Eigenschaft verwenden. Außerdem ist es möglich, den Quellenbereich mit der [**source()**](https://reference.aspose.com/cells/javascript-cpp/documentproperty/#source--) Eigenschaft der [**DocumentProperty**](https://reference.aspose.com/cells/javascript-cpp/documentproperty/) Klasse abzurufen.

Im Beispiel verwenden wir eine einfache Vorlage einer Microsoft Excel-Datei. Die Arbeitsmappe hat einen definierten benannten Bereich namens **MeinBereich**, der sich auf einen Zellenwert bezieht.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Custom Document Properties</h1>
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
            const fileInput = document.getElementById('fileInput');
            const resultEl = document.getElementById('result');
            if (!fileInput.files.length) {
                resultEl.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate a Workbook by loading the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Retrieve a list of all custom document properties of the Excel file
            const customProperties = workbook.worksheets.customDocumentProperties;

            // Add link to content.
            customProperties.addLinkToContent("Owner", "MyRange");

            // Accessing the custom document property by using the property name
            const customProperty1 = customProperties.get("Owner");

            // Check whether the property is linked to content
            const isLinkedToContent = customProperty1.isLinkedToContent;

            // Get the source for the property
            const source = customProperty1.source;

            // Save the file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out_sample-document-properties.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultEl.innerHTML = `<p style="color: green;">Operation completed successfully! Property linked: ${isLinkedToContent}. Source: ${source}. Click the download link to get the modified file.</p>`;
        });
    </script>
</html>
```

### **Wie entfernt man benutzerdefinierte Eigenschaften**

Um benutzerdefinierte Eigenschaften mit Aspose.Cells zu entfernen, rufen Sie die Methode [**DocumentPropertyCollection.remove(string)**](https://reference.aspose.com/cells/javascript-cpp/documentpropertycollection/#remove-string-) auf und übergeben den Namen der zu entfernenden Dokumenteigenschaft.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Remove Custom Document Property Example</title>
    </head>
    <body>
        <h1>Remove Custom Document Property Example</h1>
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
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate a Workbook object by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Retrieve a list of all custom document properties of the Excel file
            const customProperties = workbook.customDocumentProperties;

            // Removing a custom document property named "Publisher"
            customProperties.remove("Publisher");

            // Save the file and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out_sample-document-properties.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Custom property removed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Erweiterte Themen**
- [Hinzufügen von benutzerdefinierten Eigenschaften, die im Dokumentinformationsfeld sichtbar sind](/cells/de/javascript-cpp/adding-custom-properties-visible-inside-document-information-panel/)
- [Festlegen der Eigenschaften ScaleCrop und LinksUpToDate der integrierten Dokumenteigenschaften](/cells/de/javascript-cpp/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/)
- [Festlegen der Dokumentversion der Excel-Datei unter Verwendung eingebauter Dokumenteigenschaften](/cells/de/javascript-cpp/specify-document-version-of-the-excel-file-using-builtin-document-properties/)
- [Festlegen der Sprache der Excel-Datei unter Verwendung eingebauter Dokumenteigenschaften](/cells/de/javascript-cpp/specify-the-language-of-the-excel-file-using-builtin-document-properties/)
