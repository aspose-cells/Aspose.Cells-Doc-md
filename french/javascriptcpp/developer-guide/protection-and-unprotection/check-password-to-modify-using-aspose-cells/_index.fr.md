---
title: Vérifier le mot de passe pour modifier en utilisant Aspose.Cells for JavaScript via C++
linktitle: Vérifier le mot de passe pour modifier
type: docs
weight: 2400
url: /fr/javascript-cpp/check-password-to-modify-using-aspose-cells/
description: Apprenez comment vérifier si un mot de passe pour modifier correspond en utilisant Aspose.Cells for JavaScript via C++.
---

{{% alert color="primary" %}}  
 Parfois, vous avez besoin de vérifier si le mot de passe donné correspond avec le **mot de passe pour modification** de manière programmatique. Aspose.Cells fournit la méthode `WorkbookSettings.writeProtection.validatePassword()` que vous pouvez utiliser pour vérifier si le mot de passe pour modification est correct ou non.  
{{% /alert %}}  

## **Vérifiez le mot de passe pour modifier dans Microsoft Excel**  

Vous pouvez attribuer **Mot de passe pour ouvrir** et **Mot de passe pour modifier** lors de la création de vos classeurs dans Microsoft Excel. Veuillez consulter cette capture d'écran qui montre l'interface fournie par Microsoft Excel pour spécifier ces mots de passe.  

|![todo:image_alt_text](check-password-to-modify-using-aspose-cells_1.png)|  
| :- |  

## **Vérifiez le mot de passe pour modifier en utilisant Aspose.Cells for JavaScript via C++**  

 Les codes d'exemple suivants chargent le fichier [source Excel](5112232.xlsx). Il a un mot de passe pour ouvrir de 1234 et un mot de passe pour modifier de 5678. Le code vérifie d'abord si 567 est le bon mot de passe pour modifier et retourne false, puis il vérifie si 5678 est le mot de passe pour modifier et retourne true.  

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

### **Sortie console**  



{{< highlight java >}}  
Is 567 correct Password to modify: False  
Is 5678 correct Password to modify: True  
{{< /highlight >}}
