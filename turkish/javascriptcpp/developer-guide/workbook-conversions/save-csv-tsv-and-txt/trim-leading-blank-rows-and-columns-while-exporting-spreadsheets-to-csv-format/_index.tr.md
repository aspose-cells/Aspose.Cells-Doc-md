---
title: JavaScript aracılığıyla C++ kullanarak çalışma sayfalarını CSV formatına aktarırken İlk Boş Satır ve Sütunları Kısaltın
linktitle: CSV formatına yayılım tablolarını dışa aktarırken Önde Gelen Boş Satırları ve Sütunları Kırpmak
type: docs
weight: 100
url: /tr/javascript-cpp/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/
description: Çalışma sayfalarını CSV formatına aktarırken ilk boş satır ve sütunları kısaltmayı öğrenin, Aspose.Cells for JavaScript kullanarak C++.
---

## **Olası Kullanım Senaryoları**

Bazen, Excel veya CSV dosyanızın önde gelen boş sütunları veya satırları bulunur. Örneğin, şu satırı düşünün

{{< highlight javascript >}}

 ,,,data1,data2

{{< /highlight >}}

Burada ilk üç hücre veya sütun boştur. Bu tür bir CSV dosyasını Microsoft Excel'de açarsanız, Microsoft Excel bu önde gelen boş satırları ve sütunları atar.

Varsayılan olarak, Aspose.Cells for JavaScript kullanarak C++ kaydederken ilk boş sütun ve satırları kaldırmaz, ancak bunları Microsoft Excel gibi kaldırmak istiyorsanız, Aspose.Cells [**TxtSaveOptions.trimLeadingBlankRowAndColumn**](https://reference.aspose.com/cells/javascript-cpp/txtsaveoptions/#trimLeadingBlankRowAndColumn--) özelliği sağlar. Lütfen onu **true** olarak ayarlayın ve ardından kaydederken tüm ilk boş satır ve sütunlar atılır.

{{% alert color="primary" %}}

Aspose.Cells for JavaScript kullanmadan önce, C++ 20.4 sürümünden önce [**TxtSaveOptions.trimLeadingBlankRowAndColumn**](https://reference.aspose.com/cells/javascript-cpp/txtsaveoptions/#trimLeadingBlankRowAndColumn--) varsayılan değeri **false** idi. 20.4 sürümünden itibaren, [**TxtSaveOptions.trimLeadingBlankRowAndColumn**](https://reference.aspose.com/cells/javascript-cpp/txtsaveoptions/#trimLeadingBlankRowAndColumn--) varsayılan değeri **true** olarak ayarlandı.

{{% /alert %}}

## **CSV formatına elektronik tabloları dışa aktarırken Öneki Boş Satırları ve Sütunları Kırp**

Aşağıdaki örnek kod, iki başlangıç boş sütunu olan [kaynak excel dosyasını](sampleTrimBlankColumns.xlsx) yükler. İlk olarak, excel dosyasını değişiklik yapmadan CSV formatında kaydeder, ardından [**TxtSaveOptions.trimLeadingBlankRowAndColumn**](https://reference.aspose.com/cells/javascript-cpp/txtsaveoptions/#trimLeadingBlankRowAndColumn--) özelliğini **true** yapıp tekrar kaydeder. Ekran görüntüsü, [kaynak excel dosyasını](sampleTrimBlankColumns.xlsx), [düzenlenmemiş çıktı CSV dosyasını](outputWithoutTrimBlankColumns.csv) ve [düzenlenmiş çıktı CSV dosyasını](outputTrimBlankColumns.csv) gösterir.

![todo:image_alt_text](trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format_1.png)

## **Örnek Kod**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Trim Blank Columns</title>
    </head>
    <body>
        <h1>Trim Blank Columns Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink1" style="display: none;">Download Result 1</a>
        <a id="downloadLink2" style="display: none; margin-left: 10px;">Download Result 2</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, TxtSaveOptions, Utils } = AsposeCells;

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

            // Load source workbook
            const wb = new Workbook(new Uint8Array(arrayBuffer));

            // Save in csv format (without trimming)
            const outputData1 = wb.save(SaveFormat.Csv);
            const blob1 = new Blob([outputData1]);
            const downloadLink1 = document.getElementById('downloadLink1');
            downloadLink1.href = URL.createObjectURL(blob1);
            downloadLink1.download = 'outputWithoutTrimBlankColumns.csv';
            downloadLink1.style.display = 'inline-block';
            downloadLink1.textContent = 'Download CSV Without Trimming';

            // Now save again with TrimLeadingBlankRowAndColumn as true
            const opts = new TxtSaveOptions();
            opts.trimLeadingBlankRowAndColumn = true;

            // Save in csv format (with trimming)
            const outputData2 = wb.save(opts);
            const blob2 = new Blob([outputData2]);
            const downloadLink2 = document.getElementById('downloadLink2');
            downloadLink2.href = URL.createObjectURL(blob2);
            downloadLink2.download = 'outputTrimBlankColumns.csv';
            downloadLink2.style.display = 'inline-block';
            downloadLink2.textContent = 'Download CSV With Trimmed Blank Columns';

            resultDiv.innerHTML = '<p style="color: green;">Files generated. Use the links above to download the CSVs.</p>';
        });
    </script>
</html>
```
