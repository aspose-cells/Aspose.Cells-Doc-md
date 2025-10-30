---
title: Aspose.Cells for JavaScript kullanarak parola korumasını kontrol edin
linktitle: Düzenleme parolası kontrolü yapma
type: docs
weight: 2400
url: /tr/javascript-cpp/check-password-to-modify-using-aspose-cells/
description: Parolanın doğrulamasını nasıl yapacağınızı, C++ ile Aspose.Cells for JavaScript kullanarak öğrenin.
---

{{% alert color="primary" %}}  
Bazen, programlı olarak verilen şifrenin “Düzenleme Parolası” ile eşleşip eşleşmediğini kontrol etmeniz gerekebilir. Aspose.Cells, verilen Parola ile doğrulama yapmanızı sağlayan `WorkbookSettings.writeProtection.validatePassword()` metodunu sağlar.  
{{% /alert %}}  

## **Microsoft Excel'de Değiştirme Şifresini Kontrol Etme**  

Microsoft Excel'de çalışma kitapları oluştururken **Açma Şifresi** ve **Değiştirme Şifresi** atayabilirsiniz. Bu şifreleri belirlemek için Microsoft Excel'in sağladığı arayüzü gösteren bu ekran görüntüsüne bakınız.  

|![todo:image_alt_text](check-password-to-modify-using-aspose-cells_1.png)|  
| :- |  

## **Şifreyi korumayı Aspose.Cells for JavaScript kullanarak C++ ile kontrol edin**  

Aşağıdaki örneklerde, [kaynak Excel dosyası](5112232.xlsx) yüklenir. Dosyanın açma şifresi 1234 ve düzenleme şifresi 5678 olarak belirlenmiştir. Kod ilk olarak, 567'nin doğru düzenleme parolası olup olmadığını kontrol eder ve false döner; ardından 5678 olup olmadığını kontrol eder ve true döner.  

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

### **Konsol Çıktısı**  



{{< highlight java >}}  
Is 567 correct Password to modify: False  
Is 5678 correct Password to modify: True  
{{< /highlight >}}
