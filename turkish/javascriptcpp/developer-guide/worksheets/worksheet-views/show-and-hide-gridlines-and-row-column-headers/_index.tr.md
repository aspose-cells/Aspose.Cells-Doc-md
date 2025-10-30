---
title: JavaScript ile C++ kullanarak ızgara çizgilerini ve Satır Sütun başlıklarını gösterme ve gizleme
linktitle: Izgara Çizgileri ve Satır Sütun Başlıklarını Gösterme ve Gizleme
type: docs
weight: 30
url: /tr/javascript-cpp/show-and-hide-gridlines-and-row-column-headers/
description: Bu makale, JavaScript API veya JavaScript Kütüphanesi kullanarak Excel çalışma sayfasının ızgara çizgilerini ve satır sütun başlıklarını programatik olarak gizleme veya gösterme ile ilgili örnek kodlar sağlar.
---

{{% alert color="primary" %}}  
Aspose.Cells, varsayılan olarak görünür olan çalışma taşraflarının izgara çizgilerini gizleme ve göstermeyi destekler. Aynı zamanda çalışma taşraflarının Satır Sütun Başlıklarının görünürlüğünü kontrol etmeyi sağlar.  
{{% /alert %}}  

## **Izgara Çizgilerini Gösterme ve Gizleme**  

Tüm Excel çalışma taşraları varsayılan olarak izgara çizgilerine sahiptir. Onlar, belirli hücrelere veri girmeyi kolaylaştırdığı için hücreleri çevreler. Izgara çizgileri, bir çalışma taşrasını hücre koleksiyonu olarak görüntülememizi sağlar, burada her hücre kolayca tanımlanabilir.  

### **Izgaraların Görünürlüğünü Kontrol Etme**  

Aspose.Cells, Microsoft Excel dosyasını temsil eden [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) adlı bir sınıf sağlar. [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) sınıfı, geliştiricilerin Excel dosyasındaki her çalışma sayfasına erişmesine olanak tanıyan [**Workbook.worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--) koleksiyonunu içerir. Bir çalışma sayfası, [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) sınıfı ile temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) sınıfı, bir çalışma sayfasını yönetmek için geniş özellikler ve yöntemler sunar. Izgara çizgilerinin görünürlüğünü kontrol etmek için [**Worksheet.isGridlinesVisible()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#isGridlinesVisible--) özelliğini kullanın. [**Worksheet.isGridlinesVisible()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#isGridlinesVisible--) bir Boolean özelliğidir, bu da yalnızca **doğru** veya **yanlış** değerleri depolayabileceği anlamına gelir.  

#### **Izgaraları Görünür Yapma**  

Izgara çizgilerini görünür hale getirmek için [**Worksheet.isGridlinesVisible()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#isGridlinesVisible--) özelliğini **true** olarak ayarlayın.  

#### **Izgaraları Gizleme**  

Izgara çizgilerini gizlemek için [**Worksheet.isGridlinesVisible()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#isGridlinesVisible--) özelliğini **false** olarak ayarlayın.  

Aşağıda, bir excel dosyasını (book1.xls) açarak ilk çalışma sayfasındaki ızgara çizgilerini gizleyen ve değiştirilmiş dosyayı output.xls olarak kaydeden [**Worksheet.isGridlinesVisible()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#isGridlinesVisible--) özelliğinin kullanımı gösterilmektedir.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Hide Gridlines Example</title>
    </head>
    <body>
        <h1>Hide Gridlines Example</h1>
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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object
            // Opening the Excel file through the file data
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Hiding the grid lines of the first worksheet of the Excel file
            worksheet.isGridlinesVisible = false;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Gridlines hidden successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

## **Satır Sütun Başlıklarını Göster ve Gizle**  

Bir Excel dosyasındaki tüm çalışma sayfaları, satırlar ve sütunlarda düzenlenmiş hücrelerden oluşur. Tüm satırlar ve sütunlar benzersiz değerlere sahiptir ve bunları tanımlamak ve bireysel hücreleri tanımlamak için kullanılır. Örneğin, satırlar numaralandırılır - 1, 2, 3, 4, vb. - ve sütunlar alfabetik sıraya göre düzenlenir - A, B, C, D, vb. Satır ve sütun değerleri başlıklarda görüntülenir. Aspose.Cells kullanılarak, geliştiriciler bu satır ve sütun başlıklarının görünürlüğünü kontrol edebilir.  

### **Çalışma sayfalarının görünürlüğünü kontrol etmek**  

Aspose.Cells, Microsoft Excel dosyasını temsil eden [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) adlı bir sınıf sağlar. [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) sınıfı, geliştiricilerin Excel dosyasındaki her çalışma sayfasına erişmesine olanak tanıyan [**Workbook.worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--) koleksiyonunu içerir. Bir çalışma sayfası, [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) sınıfı ile temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) sınıfı, bir çalışma sayfasını yönetmek için geniş özellikler ve yöntemler sunar. Satır ve sütun başlıklarının görünürlüğünü kontrol etmek için [**Worksheet.isRowColumnHeadersVisible()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#isRowColumnHeadersVisible--) özelliğini kullanın. [**Worksheet.isRowColumnHeadersVisible()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#isRowColumnHeadersVisible--) bir Boolean özelliğidir, bu da yalnızca **doğru** veya **yanlış** değerleri depolayabileceği anlamına gelir.  

#### **Satır/Sütun Başlıklarını Görünür Yapma**  

Satır ve sütun başlıklarını görünür yapmak için [**Worksheet.isRowColumnHeadersVisible()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#isRowColumnHeadersVisible--) özelliğini **true** olarak ayarlayın.  

#### **Satır/Sütun Başlıklarını Gizleme**  

Satır ve sütun başlıklarını gizlemek için [**Worksheet.isRowColumnHeadersVisible()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#isRowColumnHeadersVisible--) özelliğini **false** olarak ayarlayın.  

Aşağıda, bir excel dosyasını (book1.xls) açarak ilk çalışma sayfasındaki satır ve sütun başlıklarını gizleyen ve değiştirilmiş dosyayı output.xls olarak kaydeden [**Worksheet.isRowColumnHeadersVisible()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#isRowColumnHeadersVisible--) özelliğinin kullanımı gösterilmektedir.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Hide Row/Column Headers</title>
    </head>
    <body>
        <h1>Hide Row and Column Headers Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
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

            // Instantiating a Workbook object with the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Hiding the headers of rows and columns
            worksheet.isRowColumnHeadersVisible = false;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Headers hidden successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

{{% alert color="primary" %}}  
Ayrıca, [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) sınıfının [**Cells.unhideRows(number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#unhideRows-number-number-number-) ve [**Cells.unhideColumns(number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#unhideColumns-number-number-number-) metodlarını kullanarak birden fazla satır ve sütunu görünür hale getirmek de mümkündür.  
{{% /alert %}}
