---
title: Paylaşılan Formül Ayarlama JavaScript ile C++ kullanarak
linktitle: Paylaşılan Formülü Ayarlama
type: docs
weight: 10
url: /tr/javascript-cpp/setting-shared-formula/
---

{{% alert color="primary" %}}

Bir çalışma sayfasına bazı hesaplamalar yapacak fonksiyon eklemek istiyorsanız, bu makale bu görevi Aspose.Cells for JavaScript kullanarak C++ ile nasıl gerçekleştireceğinizi açıklar.

{{% /alert %}}

## Aspose.Cells for JavaScript kullanarak C++ ile Paylaşılan Formül Ayarlama

Aşağıdaki örnek elektronik tabloya benzer biçimde veriyle dolu bir çalışma sayfasını varsayalım.

|**Giriş dosyası ile tek sütun veri**|
| :- |
|![todo:image_alt_text](setting-shared-formula_1.png)|

Bir fonksiyon eklemek istiyorsunuz ve bu fonksiyon, verinin ilk satırı için satış vergisini hesaplayacak. Vergi **%9**. Satış vergisini hesaplayan formül şudur: **"=A2*0.09"**. Bu makale, bu formülü Aspose.Cells ile nasıl uygulayacağınızı açıklar.

Aspose.Cells, [**Cell.formula**](https://reference.aspose.com/cells/javascript-cpp/cell/#formula--) özelliğini kullanarak bir formül belirtmenizi sağlar. Sütunun diğer hücrelerine (B3, B4, B5 ve benzeri) formül eklemek için iki seçenek bulunmaktadır.

İlk hücrede yaptığınız gibi, formülü her hücreye etkin şekilde ayarlayın, hücre referansını uygun şekilde güncelleyerek (A3*0.09, A4*0.09, A5*0.09 vb.). Bu, her satırın hücre referanslarının güncellenmesini gerektirir. Ayrıca, Aspose.Cells'un her formülü ayrı ayrı çözümlemesi gerekir, bu büyük tablolar ve karmaşık formüller için zaman alıcı olabilir. Ayrıca, fazla kod satırı eklenir, ancak döngüler bunları biraz azaltabilir.

Başka bir yaklaşım, **paylaşılan bir formül** kullanmaktır. Paylaşılan formülle, formüller her satırın hücre referansları için otomatik olarak güncellenir, böylece vergi uygun şekilde hesaplanır. [**Cell.sharedFormula(string, number, number)**](https://reference.aspose.com/cells/javascript-cpp/cell/#sharedFormula-string-number-number-) yöntemi, birinci yöntemden daha verimlidir.

Aşağıdaki örnek, bunu nasıl kullanacağınızı göstermektedir.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Apply Shared Formula</title>
    </head>
    <body>
        <h1>Apply Shared Formula Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell } = AsposeCells;

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

            // Instantiate a Workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the cells collection in the first worksheet
            const cells = workbook.worksheets.get(0).cells;

            // Apply the shared formula in the range i.e., B2:B14
            const cell = cells.get("B2");
            // Converted setSharedFormula(...) to property assignment per universal rule.
            cell.sharedFormula = { formula: "=A2*0.09", rowCount: 13, columnCount: 1 };

            // Save the excel file and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Shared formula applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
