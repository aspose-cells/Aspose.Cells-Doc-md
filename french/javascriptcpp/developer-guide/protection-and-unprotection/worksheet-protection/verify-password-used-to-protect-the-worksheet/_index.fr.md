---
title: Vérifier le mot de passe utilisé pour protéger la feuille avec JavaScript via C++
linktitle: Vérifiez le mot de passe utilisé pour protéger la feuille de calcul
type: docs
weight: 370
url: /fr/javascript-cpp/verify-password-used-to-protect-the-worksheet/
description: Apprenez à vérifier le mot de passe utilisé pour protéger une feuille en utilisant Aspose.Cells for JavaScript via C++.
---

{{% alert color="primary" %}}

Les API Aspose.Cells ont amélioré la classe [**Protection**](https://reference.aspose.com/cells/javascript-cpp/protection) en introduisant certaines propriétés et méthodes utiles. L'une de ces méthodes est [**Protection.verifyPassword(string)**](https://reference.aspose.com/cells/javascript-cpp/protection/#verifyPassword-string-) qui permet de spécifier un mot de passe sous forme d'instance de *string* et de vérifier si le même mot de passe a été utilisé pour protéger le [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet).

{{% /alert %}}

La méthode [**Protection.verifyPassword(string)**](https://reference.aspose.com/cells/javascript-cpp/protection/#verifyPassword-string-) retourne **true** si le mot de passe spécifié correspond au mot de passe utilisé pour protéger la feuille de calcul donnée et **false** dans le cas contraire. Le code suivant utilise la méthode [**Protection.verifyPassword(string)**](https://reference.aspose.com/cells/javascript-cpp/protection/#verifyPassword-string-) en conjonction avec la propriété [**Protection.isProtectedWithPassword()**](https://reference.aspose.com/cells/javascript-cpp/protection/#isProtectedWithPassword--) pour détecter la protection par mot de passe et vérifier ce dernier.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Check Worksheet Password Protection</h1>
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

            // Instantiate Workbook with file bytes
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet in the Excel file
            const sheet = workbook.worksheets.get(0);

            // Check if Worksheet is password protected
            if (sheet.protection.isProtectedWithPassword()) {
                // Verify the password used to protect the Worksheet
                if (sheet.protection.verifyPassword("1234")) {
                    resultDiv.innerHTML = '<p style="color: green;">Specified password has matched</p>';
                } else {
                    resultDiv.innerHTML = '<p style="color: red;">Specified password has not matched</p>';
                }
            } else {
                resultDiv.innerHTML = '<p style="color: blue;">Worksheet is not password protected</p>';
            }
        });
    </script>
</html>
```
