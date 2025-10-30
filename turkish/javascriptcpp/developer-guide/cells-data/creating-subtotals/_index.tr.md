---
title: Araltı Oluşturma
type: docs
weight: 800
url: /tr/javascript-cpp/creating-subtotals/
description: Bir elektronik tabloda tekrar eden değerler için alt toplamlar oluşturmayı nasıl yapacağınızı öğrenin, Aspose.Cells for JavaScript C++ API kullanarak.
keywords: Alt Toplamları Uygula, Alt Toplamları Ayarla, Alt toplamlar ekle, Alt Toplamlar Oluştur, Bir çalışma sayfasına alt toplamlar eklemek için nasıl 
---

{{% alert color="primary" %}}

Herhangi bir tekrar eden değerler için otomatik olarak alt toplamlar oluşturabilirsiniz. Aspose.Cells for JavaScript C++ API özellikleri size dosyalara programlı olarak alt toplamlar eklemenizde yardımcı olur.

{{% /alert %}}

## **Microsoft Excel Kullanımı**

Microsoft Excel'de aralık eklemek için:

1. İlk çalışma kitabının ilk çalışma sayfasında basit bir veri listesi oluşturun (aşağıdaki şekilde gösterildiği gibi) ve dosyayı Book1.xls olarak kaydedin.
1. Listenizdeki herhangi bir hücreyi seçin.
1. **Veri** menüsünden **Aralıklar**'ı seçin. Aralık iletişim kutusu görüntülenecektir. Kullanılacak işlevi ve aralıkların nereye yerleştirileceğini tanımlayın.

## **Aspose.Cells for JavaScript C++ API kullanımıyla**

Aspose.Cells for JavaScript C++ bir sınıf sağlar, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook), bu sınıf bir Microsoft Excel dosyasını temsil eder. [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) sınıfı, Excel dosyasındaki her çalışma sayfasına erişim sağlayan bir [**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--) koleksiyonu içerir.

Bir çalışma sayfası [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) sınıfı ile temsil edilir. Sınıf, çalışma sayfalarını ve diğer nesneleri yönetmek için çeşitli özellikler ve yöntemler sağlar. Her çalışma sayfası [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) koleksiyonundan oluşur. Bir çalışma sayfasına alt toplamlar eklemek için [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) sınıfının [**subtotal**](https://reference.aspose.com/cells/javascript-cpp/cells/#subtotal-cellarea-number-consolidationfunction-numberarray-) yöntemini kullanın. Yönteme parametre değerleri sağlayarak toplamların nasıl hesaplanacağı ve yerleştirileceğini belirtin.

Aşağıdaki örneklerde, [şablon dosyası](book1.xlsx) ilk çalışma sayfasına uygun olarak altyapı eklemek için Aspose.Cells for JavaScript C++ API kullanılmıştır. Kod çalıştırıldığında, toplamlar içeren bir çalışma sayfası oluşturulur.

Aşağıdaki kod parçacıkları, Aspose.Cells for JavaScript C++ kullanarak çalışma sayfasına alt toplamlar eklemeyi gösterir.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Apply Subtotal Example</h1>
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

            // Instantiate a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the Cells collection in the first worksheet
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;

            // Create a cellarea i.e., B3:C19
            const ca = new AsposeCells.CellArea();
            ca.startRow = 2;
            ca.startColumn = 1;
            ca.endRow = 18;
            ca.endColumn = 2;

            // Apply subtotal, the consolidation function is Sum and it will be applied to
            // Second column (C) in the list
            cells.subtotal(ca, 0, AsposeCells.ConsolidationFunction.Sum, [1]);

            // Save the excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Subtotal applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
