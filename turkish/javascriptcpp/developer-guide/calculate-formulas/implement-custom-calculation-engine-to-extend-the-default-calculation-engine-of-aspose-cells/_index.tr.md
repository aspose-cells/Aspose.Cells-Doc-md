---
title: Aspose.Cells in Varsayılan Hesaplama Motorunu geliştirmek için JavaScript ile C++ kullanarak Özel Hesaplama Motoru Uygula
linktitle: Aspose.Cells in Varsayılan Hesaplama Motorunu Genişletmek
description: Bu makale, js kullanarak Aspose.Cells kütüphanesini kullanarak özel hesaplama motoru uygulayarak varsayılan hesaplama motorunu genişletme adımlarını anlatmaktadır. Bir Excel dosyasını yükleyin veya yeni bir tane oluşturun, sağlanan yöntemleri kullanın ve değiştirilmiş Excel dosyasını kaydedin.
keywords: Aspose.Cells, Excel, Özel Hesaplama Motoru, JavaScript ile C++
type: docs
weight: 80
url: /tr/javascript-cpp/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/
---

## **Özel Hesaplama Motorunu Uygulama**

Aspose.Cells'in neredeyse tüm Microsoft Excel formüllerini hesaplayabilen güçlü bir hesaplama motoru bulunmaktadır. Bununla birlikte, varsayılan hesaplama motorunu genişletmenize olanak tanır ve size daha fazla güç ve esneklik sağlar.

Bu özellik uygulamada kullanılan özellik ve sınıflar.

- [**CalculationOptions.customEngine**](https://reference.aspose.com/cells/javascript-cpp/calculationoptions/#customEngine--)
- [**AbstractCalculationEngine**](https://reference.aspose.com/cells/javascript-cpp/abstractcalculationengine)
- [**CalculationData**](https://reference.aspose.com/cells/javascript-cpp/calculationdata)

Aşağıdaki kod, Özel Hesaplama Motorunu uygular. [**AbstractCalculationEngine**](https://reference.aspose.com/cells/javascript-cpp/abstractcalculationengine) arayüzünü uygular ve [**calculate(CalculationData data)**](https://reference.aspose.com/cells/javascript-cpp/abstractcalculationengine/#calculate-calculationdata-) yöntemine sahiptir. Bu yöntem, tüm formülleriniz üzerinde çağrılır. Bu yöntemde, **BUGÜN** fonksiyonunu yakalar ve sistem tarihine bir gün ekleriz. Eğer şu anki tarih 27/07/2023 ise, özel motor **BUGÜN()** fonksiyonunu 28/07/2023 olarak hesaplar.

### **Programlama Örneği**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Custom Calculation Engine Example</title>
    </head>
    <body>
        <h1>Custom Calculation Engine Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample" disabled>Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, CalculationOptions, CellsHelper } = AsposeCells;

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
            document.getElementById('runExample').disabled = false;
        });

        // Create a new class derived from AbstractCalculationEngine
        class CustomEngine extends AsposeCells.AbstractCalculationEngine {
            constructor() {
                super();
                // Indicate processing built-in functions
                this.processBuiltInFunctions = true;
            }

            // Override the Calculate method with custom logic
            calculate(data) {
                // Check the formula name and change the implementation
                if (data.functionName.toUpperCase() === "TODAY") {
                    // Assign the CalculationData.CalculatedValue: add one day offset for the date
                    data.calculatedValue = CellsHelper.getDoubleFromDateTime(new Date(), false) + 1.0;
                }
            }
        }

        class ImplementCustomCalculationEngine {
            static run() {
                // Create an instance of Workbook
                const workbook = new Workbook();

                // Access first Worksheet from the collection
                const sheet = workbook.worksheets.get(0);

                // Access Cell A1 and put a formula to sum values of B1 to B2
                const a1 = sheet.cells.get("A1");
                const style = a1.style;
                style.number = 14;
                a1.style = style;

                a1.formula = "=TODAY()";

                // Calculate all formulas in the Workbook 
                workbook.calculateFormula();

                // The result of A1 with default calculation engine
                console.log("The value of A1 with default calculation engine: " + a1.stringValue);

                // Create an instance of CustomEngine
                const engine = new CustomEngine();

                // Create an instance of CalculationOptions
                const opts = new CalculationOptions();

                // Assign the CalculationOptions.CustomEngine property to the instance of CustomEngine
                opts.customEngine = engine;

                // Recalculate all formulas in Workbook using the custom calculation engine
                workbook.calculateFormula(opts);

                // The result of A1 with custom calculation engine
                console.log("The value of A1 with custom calculation engine: " + a1.stringValue);

                console.log("Press any key to continue...");

                document.getElementById('result').innerHTML = '<p style="color: green;">Calculation completed. Check console for output.</p>';
            }
        }

        document.getElementById('runExample').addEventListener('click', () => {
            ImplementCustomCalculationEngine.run();
        });
    </script>
</html>
```

### **Sonuç**

Lütfen yukarıdaki örnek kodun konsol çıktısını kontrol edin; özel motor ile A1 hücresinin değeri (tarih ve saat), motor kullanılmadan sonucu ise en az bir gün farklı olmalıdır.

### **İlgili Makale**

{{% alert color="primary" %}}

[İşletmeye yazmadan özel fonksiyonların doğrudan hesaplanması](/cells/tr/javascript-cpp/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)

{{% /alert %}}
