---
title: Kontrollera lösenord för att ändra med Aspose.Cells for JavaScript via C++
linktitle: Kontrollera lösenord för att ändra
type: docs
weight: 2400
url: /sv/javascript-cpp/check-password-to-modify-using-aspose-cells/
description: Lär dig hur du kontrollerar om ett lösenord för att ändra matchar med Aspose.Cells for JavaScript via C++.
---

{{% alert color="primary" %}}  
Ibland behöver du kontrollera om det givna lösenordet matchar med **Lösenord för att ändra** programatiskt. Aspose.Cells erbjuder metoden `WorkbookSettings.writeProtection.validatePassword()` som du kan använda för att kontrollera om det givna Lösenord för att ändra är korrekt eller inte.  
{{% /alert %}}  

## **Kontrollera lösenord för modifiering i Microsoft Excel**  

Du kan tilldela **Lösenord för att öppna** och **Lösenord för att modifiera** när du skapar dina arbetsböcker i Microsoft Excel. Se denna skärmbild som visar gränssnittet som Microsoft Excel tillhandahåller för att ange dessa lösenord.  

|![todo:image_alt_text](check-password-to-modify-using-aspose-cells_1.png)|  
| :- |  

## **Kontrollera lösenord för att ändra med Aspose.Cells for JavaScript via C++**  

Följande exempel laddar [källexemplet](5112232.xlsx). Filen har ett Lösenord för öppning 1234 och ett Lösenord för att ändra 5678. Koden kontrollerar först om 567 är det korrekta lösenordet för att ändra och ger `false`, och sedan kontrollerar den om 5678 är rätt lösenord för att ändra och ger `true`.  

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

### **Konsoloutput**  



{{< highlight java >}}  
Is 567 correct Password to modify: False  
Is 5678 correct Password to modify: True  
{{< /highlight >}}
