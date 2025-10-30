---
title: JavaScript kullanarak ve C++ ile Çalışma Kitabını Sıkıştırma Düzeyinde Kaydet
linktitle: Sıkı Açık XML Elektronik Tablo Biçimine Çalışma Kitabını Kaydet
type: docs
weight: 150
url: /tr/javascript-cpp/save-workbook-to-strict-open-xml-spreadsheet-format/
description: Aspose.Cells for JavaScript kullanarak çalışma kitabını Sıkı Open XML Tablo formatında kaydetmeyi öğrenin.
---

## **Olası Kullanım Senaryoları**

Aspose.Cells for JavaScript ile C++ kullanarak çalışma kitabını *Strict Open XML Spreadsheet* formatında kaydedebilirsiniz. Bunun için [**WorkbookSettings.compliance**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#compliance--) özelliğini sağlar. Değerini [**OoxmlCompliance.iso29500_2008_strict**](https://reference.aspose.com/cells/javascript-cpp/ooxmlcompliance) olarak ayarlarsanız, çıktı Excel dosyası Strict Open XML Spreadsheet formatında kaydedilecektir.

## **Sıkı Açık XML Elektronik Tablo Biçimine Çalışma Kitabını Kaydet**

Aşağıdaki örnek kod, bir çalışma kitabı oluşturur ve [**WorkbookSettings.compliance**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#compliance--) özelliğinin değerini [**OoxmlCompliance.iso29500_2008_strict**](https://reference.aspose.com/cells/javascript-cpp/ooxmlcompliance) olarak ayarlar ve [çıktı Excel dosyası](67338272.xlsx) olarak kaydeder. Çıktı Excel dosyasını Microsoft Excel'de açıp "Farklı Kaydet..." iletişim kutusunu açarsanız, formatını *Sıkı Open XML Elektronik Tablo* olarak göreceksiniz, bu ekran görüntüsünde gösterildiği gibi.

![todo:image_alt_text](save-workbook-to-strict-open-xml-spreadsheet-format_1.png)

## **Örnek Kod**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Save Workbook to Strict Open XML Spreadsheet Format</title>
    </head>
    <body>
        <h1>Save Workbook to Strict Open XML Spreadsheet Format</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, OoxmlCompliance, Utils } = AsposeCells;

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
            // Create a new workbook
            const workbook = new Workbook();

            // Specify - Strict Open XML Spreadsheet - Format.
            workbook.settings.compliance = OoxmlCompliance.Iso29500_2008_Strict;

            // Access first worksheet and set value in B4
            const worksheet = workbook.worksheets.get(0);
            const b4 = worksheet.cells.get("B4");
            b4.value = "This Excel file has Strict Open XML Spreadsheet format.";

            // Save to output Excel file and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputSaveWorkbookToStrictOpenXMLSpreadsheetFormat.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and saved to Strict Open XML Spreadsheet format. Click the download link to get the file.</p>';
        });
    </script>
</html>
```
