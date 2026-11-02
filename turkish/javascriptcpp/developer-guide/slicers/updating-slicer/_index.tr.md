---
title: JavaScript via C++ ile Dilimleyici Güncelleme
linktitle: Dilimleyici Güncelleme
type: docs
weight: 50
url: /tr/javascript-cpp/updating-slicer/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
description: Bu makale, Aspose.Cells for JavaScript via C++ kullanılarak bağlantılı Pivot Tablosunun veya tablonun verilerini filtrelemek için dilimleyicinin nasıl güncelleneceğini gösterir.
keywords: Aspose.Cells JavaScript via C++, JavaScript dilimleyici güncelleme, JavaScript dilimleyici nasıl değiştirilir, JavaScript dilimleyici ile Pivot Tablosu nasıl filtrelenir, Slicer selectItems, Slicer clearFilter, Slicer unselectItems.
---

## **Olası Kullanım Senaryoları**
Dilimleyici güncellemek, dilimleyicinin bağlı olduğu Pivot Tablosunun veya tablonun verilerini filtrelemek anlamına gelir. Microsoft Excel'de dilimleyici öğelerini seçtiğinizde veya seçimini kaldırdığınızda, bağlantılı Pivot Tablosu veya tablo buna göre yeniden hesaplanır. Aspose.Cells for JavaScript via C++ ile dilimleyici önbelleği öğeleri arasında yineleme yapmanıza ve dilimleyiciyi elle yenilemenize gerek yoktur — [**Slicer.selectItems(labels, append)**](https://reference.aspose.com/cells/javascript-cpp/slicer/) yöntemi dilimleyiciyi günceller ve bağlantılı Pivot Tablosunu veya tabloyu doğrudan filtre öğelerinden yeniden hesaplar:
- `Slicer.selectItems(labels, append)` — belirtilen etiketleri seçer ve bağlantılı Pivot Tablosunu veya tabloyu yeniden hesaplar. `append` `true` olduğunda, başlangıçta seçili etiketler korunur ve belirtilen etiketler seçime eklenir; `append` `false` olduğunda, tüm başlangıç seçimleri temizlenir ve yalnızca belirtilen etiketler seçili kalır.
- `Slicer.unselectItems(labels)` — o anda seçili öğelerin bir kısmının seçimini kaldırır.
- `Slicer.clearFilter()` — filtreyi kaldırır ve tüm öğeleri seçer.

{{% alert color="primary" %}}
Aspose.Cells for JavaScript via C++ 26.10 sürümünden itibaren `SlicerCacheItem.selected` özelliği salt okunur hale gelir ve ayarlayıcısı artık desteklenmez. `SlicerCacheItem.selected` özelliğini öğe öğe ayarlamak yerine `Slicer.selectItems`, `Slicer.unselectItems` ve `Slicer.clearFilter` yöntemlerini kullanın.
{{% /alert %}}

## **Dilimleyici Nasıl Güncellenir**
Aşağıdaki örnek kod, bir Pivot Tablosuna bağlı mevcut bir dilimleyici içeren [örnek Excel dosyasını](67338475.xlsx) yükler. Dilimleyicinin yalnızca "Blue" ve "Pink" öğelerini `Slicer.selectItems(labels, false)` ile seçer — Pivot Tablosu, elle bir `Slicer.refresh()` çağrısı yapılmadan doğrudan filtre öğelerinden yeniden hesaplanır. Ardından çalışma kitabını [çıktı Excel dosyası](67338476.xlsx) olarak kaydeder. Aşağıdaki ekran görüntüsü, örnek kodun örnek Excel dosyası üzerindeki etkisini göstermektedir. Ekran görüntüsünde görebileceğiniz gibi Pivot Tablosu yalnızca filtrelenmiş öğeleri gösterir.
![todo:image_alt_text](updating-slicer_1.png)

## **Örnek Kod**
Mevcut seçimi değiştirin (yalnızca belirtilen etiketler seçili kalır) ve bağlantılı Pivot Tablosunu veya tabloyu yeniden hesaplayın:

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Update Slicer</title>
    </head>
    <body>
        <h1>Update Slicer Example</h1>
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

            // Instantiate Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const ws = workbook.worksheets.get(0);

            // Access the first slicer inside the slicer collection
            const slicer = ws.slicers.get(0);

            // Select only "Blue" and "Pink"; the linked pivot table or table
            // is recalculated directly from the filter items
            slicer.selectItems(["Blue", "Pink"], false);

            // Save modified workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Slicer updated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

Şu anda seçili etiketleri koruyun ve ek olarak daha fazla öğe seçin:

```javascript
// Keep the current selection and add "Red" to it.
slicer.selectItems(["Red"], true);
```

Seçili öğelerin bir kısmının seçimini kaldırın:

```javascript
// Remove "Pink" from the current selection.
slicer.unselectItems(["Pink"]);
```

Filtreyi kaldırın (tüm öğeleri seçin):

```javascript
// Clear the filter; all slicer items become selected again.
slicer.clearFilter();
```

{{< app/cells/assistant language="javascript-cpp" >}}