---
title: Fügen Sie eine Bibliotheksreferenz in das VBA Projekt der Arbeitsmappe mit JavaScript via C++ hinzu
linktitle: Fügen Sie eine Bibliotheksreferenz zum VBA Projekt in der Arbeitsmappe hinzu
type: docs
weight: 80
url: /de/javascript-cpp/add-a-library-reference-to-vba-project-in-workbook/
---

{{% alert color="primary" %}}

Manchmal müssen Sie den Bibliotheksverweis in das VBA-Projekt durch Code hinzufügen oder registrieren. Sie können dies mit der Methode [**VbaProjectReferenceCollection.addRegisteredReference(string, string)**](https://reference.aspose.com/cells/javascript-cpp/vbaprojectreferencecollection/#addRegisteredReference-string-string-) von Aspose.Cells tun.

{{% /alert %}}

## **Fügen Sie einem VBA-Projekt in Microsoft Excel einen Bibliotheksverweis hinzu.**

In Microsoft Excel können Sie manuell durch Klicken auf **Extras > Verweise...** einen Bibliotheksverweis auf das VBA-Projekt hinzufügen.

## **Fügen Sie eine Bibliotheksreferenz zum VBA-Projekt in einer Arbeitsmappe mit Aspose.Cells for JavaScript via C++ hinzu**

Das folgende Beispielcode fügt zwei Bibliotheksreferenzen zum VBA-Projekt der Arbeitsmappe mit der [**VbaProjectReferenceCollection.addRegisteredReference(string, string)**](https://reference.aspose.com/cells/javascript-cpp/vbaprojectreferencecollection/#addRegisteredReference-string-string-)-Methode hinzu oder registriert sie.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells - Add VBA References Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.xlsm,.csv" />
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
            // Creating a new Workbook
            const workbook = new Workbook();

            // Accessing the VBA project (converted from getVbaProject())
            const vbaProj = workbook.vbaProject;

            // Accessing References collection (converted from getReferences())
            vbaProj.references.addRegisteredReference("stdole", "*\\G{00020430-0000-0000-C000-000000000046}#2.0#0#C:\\Windows\\system32\\stdole2.tlb#OLE Automation");
            vbaProj.references.addRegisteredReference("Office", "*\\G{2DF8D04C-5BFA-101B-BDE5-00AA0044DE52}#2.0#0#C:\\Program Files\\Common Files\\Microsoft Shared\\OFFICE14\\MSO.DLL#Microsoft Office 14.0 Object Library");

            // Saving the workbook as XLSM and providing a download link
            const outputData = workbook.save(SaveFormat.Xlsm);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Output_out.xlsm';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Generated XLSM File';

            document.getElementById('result').innerHTML = '<p style="color: green;">VBA references added and file generated. Click the download link to save the file.</p>';
        });
    </script>
</html>
```
