---
title: Hücre Değerinin Veri Doğrulama Kurallarına Uygun Olup Olmadığını Doğrulayın
type: docs
weight: 210
url: /tr/javascript-cpp/verify-that-cell-value-satisfies-data-validation-rules/
description: C++ API sayesinde Hücre Doğrulama Kurallarını Uygun olup olmadığını doğrulama konusunda nasıl kontrol edeceğinizi öğrenin.
keywords: Hücre Doğrulama Değerini JavaScript aracılığıyla C++, Hücre Doğrulama Değerini JavaScript aracılığıyla Edinin, Bir değerin hücreye uygulanan doğrulama kurallarını karşılayıp karşılamadığını doğrula JavaScript aracılığıyla C++
---

{{% alert color="primary" %}} 

Microsoft Excel, kullanıcılara hücrelere veri doğrulama kuralları ekleme imkanı tanır. Örneğin, ondalık doğrulama, yalnızca 10 ile 20 arasında sayıların girilmesine izin verir. Kullanıcı farklı bir sayı girerse, Microsoft Excel hata mesajı gösterir ve doğru aralıkta sayı girmesini ister. Bir sayıyı kopyalayıp yapıştırırsanız, diyelim ki 3, Excel doğrulama kontrolü yapmaz veya hata mesajı göstermez.

Bazen, bir değerin hücreye uygulanan veri doğrulama kurallarını programlı olarak karşılayıp karşılamadığını doğrulamak gereklidir. Yukarıdaki durumda, örneğin, giriş başarısız olmalıdır.

{{% /alert %}} 
## **Giriş**
Aspose.Cells for JavaScript aracılığıyla C++ kullanılarak [Hücre.validationValue](https://reference.aspose.com/cells/javascript-cpp/cell/#validationValue--) özelliği programlı olarak hücre değerlerini doğrulamak için sağlar. Bir hücredeki değer, bu hücreye uygulanan doğrulama kuralını karşılamıyorsa, **false** döner, aksi takdirde **true**.

Aşağıdaki örnek kod, [Hücre.validationValue](https://reference.aspose.com/cells/javascript-cpp/cell/#validationValue--) özelliğinin nasıl çalıştığını gösterir. Öncelikle, C1 hücresine 3 değeri girilir. Bu, veri doğrulama kuralını karşılamadığı için, [Cell.validationValue](https://reference.aspose.com/cells/javascript-cpp/cell/#validationValue--) özelliği **false** döner. Ardından, C1 hücresine 15 değeri girilir. Bu değer doğrulama kuralını karşıladığı için, [Cell.validationValue](https://reference.aspose.com/cells/javascript-cpp/cell/#validationValue--) özelliği **true** döner. Benzer şekilde, 30 değeri için de **false** döner.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Validation Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Validation Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils } = AsposeCells;

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

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access Cell C1
            // Cell C1 has the Decimal Validation applied on it.
            // It can take only the values Between 10 and 20
            const cell = worksheet.cells.get("C1");

            // Enter 3 inside this cell (not between 10 and 20)
            cell.value = 3;

            // Check if number 3 satisfies the Data Validation rule applied on this cell
            const valid3 = cell.validationValue;
            console.log("Is 3 a Valid Value for this Cell: " + valid3);
            resultDiv.innerHTML += `<p>Is 3 a Valid Value for this Cell: ${valid3}</p>`;

            // Enter 15 inside this cell (between 10 and 20)
            cell.value = 15;

            // Check if number 15 satisfies the Data Validation rule applied on this cell
            const valid15 = cell.validationValue;
            console.log("Is 15 a Valid Value for this Cell: " + valid15);
            resultDiv.innerHTML += `<p>Is 15 a Valid Value for this Cell: ${valid15}</p>`;

            // Enter 30 inside this cell (not between 10 and 20)
            cell.value = 30;

            // Check if number 30 satisfies the Data Validation rule applied on this cell
            const valid30 = cell.validationValue;
            console.log("Is 30 a Valid Value for this Cell: " + valid30);
            resultDiv.innerHTML += `<p>Is 30 a Valid Value for this Cell: ${valid30}</p>`;
        });
    </script>
</html>
```


### **Çıktı**
{{< highlight javascript >}}

 Is 3 a Valid Value for this Cell: false

Is 15 a Valid Value for this Cell: true

Is 30 a Valid Value for this Cell: false

{{< /highlight >}}
