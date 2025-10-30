---
title: JavaScript ile C++ kullanarak Boş Çalışma Sayfalarını Tespit Etme
linktitle: Boş Çalışsayfası Bulma
type: docs
weight: 410
url: /tr/javascript-cpp/detecting-empty-worksheets/
description: Bu makale, C++ kütüphanesi ile JavaScript API kullanarak Excel çalışma kitaplarındaki boş çalışma sayfalarını programlı olarak nasıl tespit edeceğinizi anlatan kodlar sağlar.
keywords: JavaScript ile C++ kullanarak boş çalışma sayfası tespiti, boş excel çalışma sayfası JavaScript ile C++
---

## **Doldurulmuş Hücreleri Kontrol Etme**

İş sayfaları, içinde değerler bulunan bir veya daha fazla hücreye sahip olabilir, burada değer basit olabilir (metin, sayısal, tarih/zaman) veya bir formül ya da formül tabanlı bir değer olabilir. Bu durumda, verilen bir iş sayfasının boş olup olmadığını kolayca tespit edebilirsiniz. Kontrol etmemiz gereken tek şey [**Cells.maxDataRow**](https://reference.aspose.com/cells/javascript-cpp/cells/#maxDataRow--) veya [**Cells.maxDataColumn**](https://reference.aspose.com/cells/javascript-cpp/cells/#maxDataColumn--) özellikleridir. Yukarıda belirtilen özellikler sıfır veya pozitif değer döndürüyorsa, bu bir veya daha fazla hücreye değer atanmış anlamına gelir; ancak bu özelliklerden herhangi biri -1 ise, bu, ilgili iş sayfasında hiçbir hücrenin doldurulmadığını gösterir.

{{% alert color="primary" %}}

Satır ve sütun koleksiyonlarının sıfır tabanlı indeksleri vardır; bu nedenle, satır 0 ve sütun 0'daki bir hücre, iş sayfasındaki ilk hücre anlamına gelir, bu da A1.

{{% /alert %}}

## **Değerleri olan tüm hücreler otomatik olarak başlatılır, ancak bir çalışsayfada yalnızca biçimlendirmesi olan hücrelerin olma olasılığı vardır. Bu durumda, [Cells.MaxDataRow](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MaxDataRow) veya [Cells.MaxDataColumn](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MaxDataColumn) özellikleri, hücre biçimlendirmesi nedeniyle başlatılmış ancak doldurulmuş değerlerin yokluğunu gösteren -1 değerini döndürecektir. Bir çalışsayfanın boş başlatılmış hücreler içerip içermediğini kontrol etmek için, Cells koleksiyonundan alınan bir yineç üzerinde *Iterator.hasNext* metodu kullanılması önerilir. *iterator.hasNext* metodu true döndürürse, bu durum verilen çalışsayfada bir veya daha fazla başlatılmış hücre bulunduğunu gösterir.**

Değerleri olan tüm hücreler otomatik olarak başlatılır; ancak, bir iş sayfasında sadece biçimlendirme uygulanan hücrelerin olma ihtimali de vardır. Bu durumda, [**Cells.maxDataRow**](https://reference.aspose.com/cells/javascript-cpp/cells/#maxDataRow--) veya [**Cells.maxDataColumn**](https://reference.aspose.com/cells/javascript-cpp/cells/#maxDataColumn--) özellikleri -1 döndürür ve bu, doldurulmuş değerlerin olmadığı anlamına gelir, ancak biçimlendirme nedeniyle başlatılmış hücreler bu yöntemle tespit edilemez. Bir iş sayfasında boş başlatılmış hücrelerin olup olmadığını kontrol etmek için, [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) koleksiyonundan alınan sayıcıda `Enumerator.MoveNext` metodunu kullanmanız önerilir. Eğer `Enumerator.MoveNext` metodu **true** dönerse, bu, ilgili iş sayfasında bir veya daha fazla başlatılmış hücre olduğunu gösterir.

## **Şekilleri Kontrol Etme**

Bir iş sayfasının herhangi bir hücre içermemesi mümkündür; ancak, şekiller ve nesneler (kontroller, grafikler, resimler vb.) içerebilir. Bir iş sayfasında şekil olup olmadığını kontrol etmek istiyorsak, [**ShapeCollection.count**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#count--) özelliğini inceleyebiliriz. Pozitif herhangi bir değer, iş sayfasında şekil(s) olduğunu gösterir.

## **Programlama Örneği**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Check Non-Empty Worksheets Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

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
            const book = new Workbook(new Uint8Array(arrayBuffer));

            const messages = [];

            // Loop over all worksheets in the workbook
            for (let i = 0; i < book.worksheets.count; i++) {
                const sheet = book.worksheets.get(i);
                // Check if worksheet has populated cells
                if (sheet.cells.maxDataRow !== -1) {
                    messages.push(`${sheet.name} is not empty because one or more cells are populated`);
                }
                // Check if worksheet has shapes
                else if (sheet.shapes.count > 0) {
                    messages.push(`${sheet.name} is not empty because there are one or more shapes`);
                }
                // Check if worksheet has empty initialized cells
                else {
                    const range = sheet.cells.maxDisplayRange;
                    const rangeIterator = range.getEnumerator();
                    if (rangeIterator.moveNext()) {
                        messages.push(`${sheet.name} is not empty because one or more cells are initialized`);
                    }
                }
            }

            if (messages.length) {
                resultDiv.innerHTML = '<ul>' + messages.map(m => `<li>${m}</li>`).join('') + '</ul>';
            } else {
                resultDiv.innerHTML = '<p style="color: green;">No non-empty worksheets found.</p>';
            }
        });
    </script>
</html>
```
