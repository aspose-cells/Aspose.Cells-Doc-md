---
title: Passwort zum Ändern mit Aspose.Cells for JavaScript via C++ überprüfen
linktitle: Passwort zum Ändern prüfen
type: docs
weight: 2400
url: /de/javascript-cpp/check-password-to-modify-using-aspose-cells/
description: Erfahren Sie, wie Sie überprüfen, ob das Passwort zum Ändern passt, mit Aspose.Cells for JavaScript via C++.
---

{{% alert color="primary" %}}  
Manchmal müssen Sie programmgesteuert prüfen, ob das angegebene Passwort mit dem **Passwort zum Ändern** übereinstimmt. Aspose.Cells bietet die Methode `WorkbookSettings.writeProtection.validatePassword()`, die Sie verwenden können, um zu überprüfen, ob das angegebene Passwort korrekt ist.  
{{% /alert %}}  

## **Passwort zum Ändern in Microsoft Excel überprüfen**  

Sie können beim Erstellen Ihrer Arbeitsbücher in Microsoft Excel **Passwort zum Öffnen** und **Passwort zum Ändern** zuweisen. Bitte sehen Sie sich diesen Screenshot an, der die Benutzeroberfläche zeigt, die Microsoft Excel zum Angeben dieser Passwörter bereitstellt.  

|![todo:image_alt_text](check-password-to-modify-using-aspose-cells_1.png)|  
| :- |  

## **Passwordüberprüfung vor Änderungen mit Aspose.Cells for JavaScript via C++**  

Die folgenden Beispielcodes laden die [Quelldatei Excel](5112232.xlsx). Sie hat ein Passwort zum Öffnen als 1234 und zum Ändern als 5678. Der Code überprüft zuerst, ob 567 das richtige Passwort zum Ändern ist, und gibt false zurück, und überprüft anschließend, ob 5678 das Passwort zum Ändern ist, wobei true zurückgegeben wird.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Check Write Protection Passwords</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, LoadOptions, SaveFormat, Utils } = AsposeCells;

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

            // Specify password to open inside the load options
            const opts = new LoadOptions();
            opts.password = "1234";

            // Open the source Excel file with load options
            const workbook = new Workbook(new Uint8Array(arrayBuffer), opts);

            // Check if 567 is Password to modify
            let ret = workbook.settings.writeProtection.validatePassword("567");
            let outputHtml = `<p>Is 567 correct Password to modify: ${ret}</p>`;

            // Check if 5678 is Password to modify
            ret = workbook.settings.writeProtection.validatePassword("5678");
            outputHtml += `<p>Is 5678 correct Password to modify: ${ret}</p>`;

            document.getElementById('result').innerHTML = outputHtml;
        });
    </script>
</html>
```  

### **Konsolenausgabe**  



{{< highlight java >}}  
Is 567 correct Password to modify: False  
Is 5678 correct Password to modify: True  
{{< /highlight >}}
