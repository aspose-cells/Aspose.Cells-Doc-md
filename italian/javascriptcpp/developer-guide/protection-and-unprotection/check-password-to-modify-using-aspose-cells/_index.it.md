---
title: Controlla la password per modificare usando Aspose.Cells for JavaScript tramite C++
linktitle: Verifica password per modificare
type: docs
weight: 2400
url: /it/javascript-cpp/check-password-to-modify-using-aspose-cells/
description: Impara come verificare se la password per modificare corrisponde usando Aspose.Cells for JavaScript tramite C++. 
---

{{% alert color="primary" %}}  
A volte, è necessario verificare se la password fornita corrisponde alla **Password per modificare** programmaticamente. Aspose.Cells offre il metodo `WorkbookSettings.writeProtection.validatePassword()` che puoi usare per verificare se la Password per modificare è corretta o meno.  
{{% /alert %}}  

## **Verificare la password per modificare in Microsoft Excel**  

È possibile assegnare **Password per aprire** e **Password per modificare** durante la creazione dei propri workbook in Microsoft Excel. Si prega di vedere questa schermata che mostra l'interfaccia fornita da Microsoft Excel per specificare queste password.  

|![todo:image_alt_text](check-password-to-modify-using-aspose-cells_1.png)|  
| :- |  

## **Verifica password prima di modificare usando Aspose.Cells for JavaScript via C++**  

Gli esempi di codice caricanno il [file Excel di origine](5112232.xlsx). Ha una Password di apertura 1234 e una Password di modifica 5678. Il codice verifica prima se 567 è la password corretta per modificare, restituendo false, e poi verifica se 5678 è corretta, restituendo true.  

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

### **Output della console**  



{{< highlight java >}}  
Is 567 correct Password to modify: False  
Is 5678 correct Password to modify: True  
{{< /highlight >}}
