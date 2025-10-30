---
title: JavaScript ile C++ kullanarak çalışma sayfasına yazmadan özel fonksiyonların doğrudan hesaplanması
linktitle: Eğitim tablosuna yazmadan özel bir fonksiyonun doğrudan hesaplanması
description: Bu makale, Aspose.Cells kütüphanesini kullanarak, JavaScript ile C++ kullanarak, Microsoft Excel de özel fonksiyonları doğrudan çalışma sayfasına yazmadan nasıl hesaplayacağınızı anlatmaktadır. Var olan bir Excel dosyasını yükleyin veya yeni bir tane oluşturun, özel fonksiyonu hesaplayın ve değiştirilmiş dosyayı kaydedin.
keywords: Aspose.Cells, Excel, özel fonksiyonlar, doğrudan hesaplamalar, JavaScript ile C++, yazmaya gerek yok, çalışma sayfaları
type: docs
weight: 90
url: /tr/javascript-cpp/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/
---

## **Özel işlevin çalışma tablosuna yazılmadan doğrudan hesaplanması**

Bu konu, özel fonksiyonlarınızı öncelikle çalışma sayfasına yazmadan doğrudan nasıl hesaplayabileceğinizi açıklar. Lütfen bu amaçla [**Worksheet.calculateFormula(formula, opts)**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#calculateFormula-string-CalculationOptions-) metodunu kullanın.

Bu metodu kullanımını gösteren aşağıdaki örnek kodu inceleyin. MyCompany.CustomFunction() adında özel bir işlev kullandık ve bu işlevin değerini "Aspose.Cells." olarak kendimiz hesapladık ve bu değer otomatik olarak hesaplama motoru tarafından "Hoş geldiniz " olan A1 hücresinin değeri ile birleştirildi ve son hesaplanmış değer olarak "Hoş geldiniz Aspose.Cells." olarak döndü. Kodun içinde özel bir işlevimizi çalıştırmadığımızı ve bunun yerine, özel mantığımızla doğrudan hesaplandığını görebilirsiniz.

### **Programlama Örneği**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Custom Function Example</title>
    </head>
    <body>
        <h1>Implement Direct Calculation Of Custom Function</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, AbstractCalculationEngine, CalculationOptions } = AsposeCells;

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

        class CustomEngine extends AbstractCalculationEngine {
            // Override the calculate method with custom logic
            calculate(data) {
                // Check the formula name and calculate it yourself
                if (data.functionName === "MyCompany.CustomFunction") {
                    // This is our calculated value
                    data.calculatedValue = "Aspose.Cells.";
                }
            }
        }

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                // Create a new workbook if no file is provided
                workbook = new Workbook();
            }

            // Access first worksheet
            const ws = workbook.worksheets.get(0);

            // Add some text in cell A1
            ws.cells.get("A1").putValue("Welcome to ");

            // Create a calculation options with custom engine
            const opts = new CalculationOptions();
            opts.customEngine = new CustomEngine();

            // This line shows how you can call your own custom function without
            // a need to write it in any worksheet cell
            // After the execution of this line, it will return
            // Welcome to Aspose.Cells.
            const ret = ws.calculateFormula("=A1 & MyCompany.CustomFunction()", opts);

            // Write the returned value into B1 for demonstration
            ws.cells.get("B1").putValue(ret);

            // Prepare download of the modified workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Calculated Value: ' + ret + '</p>';
        });
    </script>
</html>
```

### **Konsol Çıktısı**

Yukarıdaki örnek kodun konsol çıktısı aşağıdaki gibidir.

{{< highlight javascript >}}

Calculated Value: Welcome to Aspose.Cells.

{{< /highlight >}}

### **İlgili Makale**

{{% alert color="primary" %}}

[Varsayılan Hesaplama Motorunu Geliştirmek için Özel Hesaplama Motoru Uygula](/cells/tr/javascript-cpp/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)

{{% /alert %}}
