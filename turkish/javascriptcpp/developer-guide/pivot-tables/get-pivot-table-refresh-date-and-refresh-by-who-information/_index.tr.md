---
title: Pivot Tablosu yenileme tarihini ve son yenileyeni alın
type: docs
weight: 100
url: /tr/javascript-cpp/get-pivot-table-refresh-date-and-refresh-by-who-information/
description: Aspose.Cells for JavaScript ile C++ kullanarak Pivot Tablo yenileme tarihini ve kimin tarafından yenilendiği bilgisini nasıl elde ederim
keywords: Aspose.Cells for JavaScript ile C++ Excel, Excel JavaScript kütüphanesi kullanarak, Pivot Tablo yenileme tarihini ve yenileyenin kim olduğunu nasıl alırım
---

{{% alert color="primary" %}}

Aspose.Cells for JavaScript ile C++ şu anda çalışma kitabından yenileme tarihini ve yenileyen bilgilerini alma desteği sağlar.

{{% /alert %}}

## **Pivot Tablosunun Yenileme Tarihini ve Kim Tarafından Yenilendiği Bilgisi Alma Yöntemi**
[**PivotTable.refreshDate**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#refreshDate--), PivotTablo raporunun son yenilendiği tarihi döndürür. Benzer şekilde, [**PivotTable.refreshedByWho**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#refreshedByWho--) özelliği raporun en son kimin tarafından yenilendiğini döndürür. Aşağıdaki örnek bu özelliği ve örnek dosyayı aşağıdaki bağlantıdan indirebilirsiniz.

[SourcePivotTable.xlsx](77496335.xlsx)

**Örnek Kod**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Pivot Table Info</title>
    </head>
    <body>
        <h1>Pivot Table Information</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

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

            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            const worksheet = workbook.worksheets.get(0);
            const pivotTable = worksheet.pivotTables.get(0);

            const refreshedByWho = pivotTable.refreshedByWho;
            const refreshDate = pivotTable.refreshDate;

            console.log("Pivot table refresh by who = " + refreshedByWho);
            console.log("Pivot table refresh date = " + refreshDate);

            document.getElementById('result').innerHTML = `
                <p>Pivot table refresh by who = ${refreshedByWho}</p>
                <p>Pivot table refresh date = ${refreshDate}</p>
            `;
        });
    </script>
</html>
```
