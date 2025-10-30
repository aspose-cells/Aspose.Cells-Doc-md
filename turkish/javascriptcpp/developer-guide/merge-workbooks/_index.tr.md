---
title: Birden fazla çalışma kitabını JavaScript ve C++ kullanarak tek bir çalışma kitabına birleştirin
linktitle: Çalışma Kitabı Birleştirme
type: docs
weight: 66
url: /tr/javascript-cpp/combine-multiple-workbooks-into-a-single-workbook/
description: C++ aracılığıyla Aspose.Cells for JavaScript kullanarak birden fazla çalışma kitabını nasıl birleştireceğinizi öğrenin. 
---

{{% alert color="primary" %}}

Bazen, resimler, grafikler ve veriler gibi çeşitli içeriklere sahip çalışma kitaplarını tek bir çalışma kitabında birleştirmeniz gerekir. Bu özellik C++ aracılığıyla Aspose.Cells for JavaScript tarafından desteklenir. Bu makale, Aspose.Cells kullanarak birkaç basit satır kodla çalışma kitaplarını nasıl oluşturacağınızı ve birleştireceğinizi gösterir.

{{% /alert %}}

## **Resimler ve Grafiklerle Çalışma Kitaplarını Birleştirme**

Örnek kod, C++ aracılığıyla Aspose.Cells for JavaScript kullanarak iki çalışma kitabını tek bir çalışma kitabına birleştirir. Kod, kaynak çalışma kitaplarını yükler, onları birleştirmek için [**Workbook.combine(Workbook)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#combine-workbook-) yöntemini kullanır ve çıktı çalışma kitabını kaydeder.

### **Kaynak Çalışma Kitapları**

- [charts.xlsx](5473097.xlsx)
- [picture.xlsx](5473096.xlsx)

### **Çıktı Çalışma Kitapları**

- [combined.xlsx](5473095.xlsx)

### **Ekran Görüntüleri**

Aşağıda, kaynak ve çıktı çalışma kitaplarının ekran görüntüleri bulunmaktadır.

{{% alert color="primary" %}}

Herhangi bir kaynak çalışma kitabını kullanabilirsiniz. Bu resimler sadece görsel amaçlar içindir.

{{% /alert %}}

**Grafik çalışma kitabının ilk çalışsayfası - yığılmış** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_1.jpg)

**Grafik çalışma kitabının ikinci çalışsayfası - çizgi** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_2.jpg)

**Resim çalışma kitabının ilk çalışma sayfası - resim** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_3.jpg)

**Birleşik çalışma kitabındaki tüm üç çalışma sayfası - yığılmış, çizgi, resim** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_4.jpg)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Combine Workbooks Example</title>
    </head>
    <body>
        <h1>Combine Workbooks Example</h1>
        <p>Select two Excel files to combine:</p>
        <input type="file" id="fileInput1" accept=".xls,.xlsx" />
        <input type="file" id="fileInput2" accept=".xls,.xlsx" />
        <button id="runExample">Combine Workbooks</button>
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
            const fileInput1 = document.getElementById('fileInput1');
            const fileInput2 = document.getElementById('fileInput2');

            if (!fileInput1.files.length || !fileInput2.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select two Excel files.</p>';
                return;
            }

            const file1 = fileInput1.files[0];
            const file2 = fileInput2.files[0];

            const arrayBuffer1 = await file1.arrayBuffer();
            const arrayBuffer2 = await file2.arrayBuffer();

            // Open the first excel file.
            const sourceBook1 = new Workbook(new Uint8Array(arrayBuffer1));

            // Open the second excel file.
            const sourceBook2 = new Workbook(new Uint8Array(arrayBuffer2));

            // Combining the two workbooks
            sourceBook1.combine(sourceBook2);

            // Save the combined workbook and provide download link
            const outputData = sourceBook1.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Combined.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Combined Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbooks combined successfully! Click the download link to get the combined file.</p>';
        });
    </script>
</html>
```

## **Gelişmiş Konular**
- [Birden Fazla Çalışma Sayfasını Tek Bir Çalışma Sayfasına Birleştirme](/cells/tr/javascript-cpp/combine-multiple-worksheets-into-a-single-worksheet/)
- [Dosyaları Birleştirme](/cells/tr/javascript-cpp/merge-files/)
