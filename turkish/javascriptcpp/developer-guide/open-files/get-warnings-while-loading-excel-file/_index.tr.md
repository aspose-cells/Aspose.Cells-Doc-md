---
title: Excel Dosyasını Yüklerken Uyarıları Alın (JavaScript ve C++ ile)
linktitle: Excel Dosyası Yüklenirken Uyarıları Al
type: docs
weight: 110
url: /tr/javascript-cpp/get-warnings-while-loading-excel-file/
description: C++ aracılığıyla Aspose.Cells for JavaScript kullanarak Excel dosyasını yüklerken uyarıları nasıl yakalayacağınızı öğrenin. Bozuk fakat yüklenebilir çalışma kitaplarını etkin şekilde yönetin.
---

## **Olası Kullanım Senaryoları**

Bazen kullanıcı, biraz bozuk fakat yüklenebilir olan bir çalışma kitabını yüklemeye çalışır. Bu durumlarda, Aspose.Cells yükleme sırasında uyarılar fırlatır. Bu uyarıları, [**IWarningCallback**](https://reference.aspose.com/cells/javascript-cpp/iwarningcallback) arayüzünü uygulayarak ve [**LoadOptions.warningCallback**](https://reference.aspose.com/cells/javascript-cpp/loadoptions/#warningCallback--) özelliğini ayarlayarak yakalayabilirsiniz.

## **Excel Dosyası Yüklenirken Uyarıları Al**

Aşağıdaki örnek kod, Excel dosyasını yüklerken uyarıları nasıl alacağınızı gösterir. Kod, [**DuplicateDefinedName**](https://reference.aspose.com/cells/javascript-cpp/warningtype) uyarısı veren [örnek Excel dosyasını](sampleDuplicateDefinedName.xlsx) yükler. Bu uyarı, [**IWarningCallback.warning(WarningInfo)**](https://reference.aspose.com/cells/javascript-cpp/iwarningcallback/#warning-warninginfo-) yöntemiyle yakalanır ve uyarı mesajlarını konsolda yazdırır. Daha sonra çalışma kitabı [çıktı excel dosyasına](outputDuplicateDefinedName.xlsx) kaydedilir. Eğer örnek Excel dosyasını Microsoft Excel'de açarsanız, bu uyarıyı görürsünüz; ekran görüntüsünde gösterildiği gibi. Lütfen aşağıdaki kodun konsol çıktısını da kontrol edin, daha iyi anlamak için.

![todo:image_alt_text](get-warnings-while-loading-excel-file_1.png)

## **Örnek Kod**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Warning Callback Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Warning Callback Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, LoadOptions, WarningType } = AsposeCells;

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

        // Implement IWarningCallback interface to catch warnings while loading workbook
        class WarningCallback extends AsposeCells.IWarningCallback {
            warning(warningInfo) {
                if (warningInfo.type === AsposeCells.WarningType.DuplicateDefinedName) {
                    console.log("Duplicate Defined Name Warning: " + warningInfo.description);
                }
            }
        }

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Create load options and set the WarningCallback property 
            // to catch warnings while loading workbook
            const options = new LoadOptions();
            options.warningCallback = new WarningCallback();

            // Load the source excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer), options);

            // Save the workbook and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputDuplicateDefinedName.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Resulting Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Workbook processed successfully. Check console for warnings.</p>';
        });
    </script>
</html>
```

## **Konsol Çıktısı**



{{< highlight java >}}

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:Introduction!$D$16:$D$17

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:Panel!$B$228

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:'Queries '!$D$14:$D$16

{{< /highlight >}}
