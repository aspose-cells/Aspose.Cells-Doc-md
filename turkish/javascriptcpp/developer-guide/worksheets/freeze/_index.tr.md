---
title: C++ kullanarak JavaScript ile Excel Çalışma Sayfasının Panesini Dondur
linktitle: Pano Dondur
type: docs
weight: 190
url: /tr/javascript-cpp/how-to-freeze-panes-of-excel-worksheet
description: Bu makalede, C++ kullanarak Aspose.Cells for JavaScript ile Excel Çalışma Sayfalarının panelerini programlama yoluyla nasıl donduracağınızı öğreneceksiniz.
keywords: Panelleri dondur, Pencereyi dondur.
---

## **Giriş**  

Bu makalede, Panelleri Dondurmayı Öğreneceğiz. Bir anlamlı başlık altındaki büyük veri kümesine sahipseniz ve kaydırırken başlığı göremiyorsanız, veya her kayıtta birçok veri varsa, panelleri dondurabilir ve kaydırılan diğer verilerle birlikte donmuş bölümü görebilirsiniz. Üst satırlarda veya ilk sütunlarda başlıkları kolayca görebilirsiniz. Panelleri dondurma veya çözme, verilerin görünümünü değiştirir, veriyi değil.  

## **Excel'de**  

**![Excel'de Panoları Dondur](Freeze-panes.png)**  

1. Panelleri dondurmak, satır ve sütunları dondurmak istiyorsanız, önce bir hücre seçin (örneğin B2).  
2. Görünüm > Panoları Dondur'a tıklayın.  
3. Açılır menüden Panoları Dondur'a tıklayın.  
4. Kaydırdığınızda veya sağa kaydırdığınızda, ilk satır ve sütun donmuş kalır.  

**![Donmuş Paneller](Frozen-Panes.png)**  

Gördüğünüz gibi, 1. Satır ve sütun A dondurulmuştur, ikinci satır 32 ve ikinci görünür sütun D'dir.  

Panelleri dondurmak ile büyük verilerinizi satır veya sütun etiketlerini takip etmeye gerek kalmadan görüntüleyebilirsiniz.  

## **Aspose.Cells for JavaScript ile C++ kullanarak Pane Dondurma**  
C++ kullanarak Aspose.Cells for JavaScript ile paneleri dondurmak basittir. Seçilen Hücrede paneyi dondurmak için [**Worksheet.freezePanes(number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#freezePanes-number-number-number-number-) yöntemini kullanın.  
1. Dosyayı açmak veya boş bir dosya oluşturmak için Workbook'u oluşturun.  
2. Worksheet.freezePanes() yöntemi ile Pencereleri Dondur.  
3. Dosyayı kaydedin.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Freeze Panes Example</title>
    </head>
    <body>
        <h1>Freeze Panes Example</h1>
        <p>Select an Excel file (Freeze.xlsx) and click "Run Example" to freeze panes at B2.</p>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>

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
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Freezing panes at the cell B2
            worksheet.freezePanes("B2", 1, 1);

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'frozen.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Frozen Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Panes frozen successfully! Click the download link to get the modified file.</p>';
        });
    </script>
    </body>
</html>
```  

Ekli [örnek kaynak Excel dosyası](Freeze.xlsx).
