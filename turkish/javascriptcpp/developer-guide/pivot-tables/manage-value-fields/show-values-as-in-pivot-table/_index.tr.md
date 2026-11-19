---
title: Pivot Tablosunda Değerleri Göster
linktitle: Pivot Tablosunda Değerleri Göster
description: Pivot Tablosu veri alanı değerlerini toplamın yüzdesi, temel bir öğeden fark, yürüyen toplamlar, sıralamalar ve daha fazlası şeklinde gösterin, Aspose.Cells for JavaScript via C++ ile.
keywords: Aspose.Cells, JavaScript via C++, Pivot Tablosu, değerleri göster, PivotShowValuesAsType, PercentageOfTotal, PivotShowValuesSetting, showValuesAs, BaseFieldIndex, BaseItemIndex
type: docs
weight: 145
url: /tr/javascript-cpp/show-values-as-in-pivot-table/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Olası Kullanım Senaryoları**
Bir pivot tablosu, genellikle `Sum` veya `Count` gibi bir toplama işleviyle her veri alanını toplar. Excel’in **Değerleri Göster** özelliği, her görüntülenen sonucu bu birincil toplama sonucundan türetilen ikincil bir hesaplamayla (örneğin, toplamın yüzdesi, yürüyen toplam, seçilen bir temel öğeden fark veya sıralama) değiştirir; böylece yardımcı formüller veya hesaplanmış sütunlar olmadan karşılaştırmalı analiz yapabilirsiniz.  
Tipik kullanım alanları arasında satır, sütun veya tüm veri kümesinin yüzdesi gibi toplam payı analizleri; bir dönem alanındaki yürüyen toplamla kümülatif raporlama; bir temel öğeye göre fark veya yüzde fark kullanarak kıyaslama analizi; ve değerlerin en küçükten en büyüğe veya en büyükten en küçüğe sıralanması bulunur.  
Aspose.Cells for JavaScript via C++ içinde, `PivotShowValuesAsType` enum’u ikincil hesaplamayı seçer. Salt okuma özelliğine sahip `PivotField.showValuesSetting` özelliği bir `PivotShowValuesSetting` nesnesi döndürür; bu nesnenin yazılabilir `showValuesAs`, `baseFieldIndex` ve `baseItemIndex` özellikleri davranışı yapılandırır; aynı ayarları tek bir çağrıda uygulayan `PivotField.showValuesAs(...)` yardımcı yöntemi de mevcuttur. Bu ayarları `PivotTable.dataFields` aracılığıyla elde edilen bir veri veya değer alanına uygulayın.

## **PivotShowValuesAsType Enum Üyeleri**
Veri alanı toplama işlevini (Sum veya Count gibi) korurken, **Değerleri Göster** yalnızca birleştirilmiş değerin nasıl gösterileceğini değiştirir.  
`PivotShowValuesSetting` özelliklerini doğrudan yazmanın yanı sıra (bkz. son bölüm), aynı yapılandırmayı bir çağrıda uygulayan bir yardımcı yöntem de vardır. Bu yöntem iki biçimde sunulur — biri temel alan ve temel öğeyi indeksle, diğeri ise isimle adresler:

```html
function showValuesAs(pivotField, showValuesAsType, baseField, baseItem) {
    pivotField.showValuesAs(showValuesAsType, baseField, baseItem);
}
function showValuesAsByName(pivotField, showValuesAsType, baseField, baseItem) {
    pivotField.showValuesAs(showValuesAsType, baseField, baseItem);
}
// index form: AsposeCells.PivotShowValuesAsType.PercentageOfTotal, 0, 0
// name form:  AsposeCells.PivotShowValuesAsType.PercentageOf, "Fruit", "Apple"
```

| Parametre | Anlam | Gereklilik Durumu |
| --- | --- | --- |
| `showValuesAsType` | Uygulanacak `PivotShowValuesAsType` ikincil hesaplama. | Her zaman. |
| `baseField` | Pivot tablosunun temel alanları arasında (örneğin, temel öğenin ait olduğu satır alanının indeksi) sıfır‑tabanlı indeks veya — isim biçiminde — temel alanın adı. | Aşağıdaki sekiz temel‑ilişkili biçim (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`, `RunningTotalIn`, `PercentageOfParentTotal`, `PercentageOfRunningTotalIn`, `RankSmallestToLargest`, `RankLargestToSmallest`) için gereklidir; diğer tüm biçimler için `0` (veya isim biçiminde `null`) gönderin. |
| `baseItem` | Temel öğenin sıfır‑tabanlı indeksi; iki sentinel değeri vardır: `-1` önceki öğeyi, `-2` sonraki öğeyi seçer (JavaScript via C++ bağlayıcısı adlandırılmış sabitleri dışa aktarmaz — literal değerleri gönderin). İsim biçimi temel öğenin başlığını alır ve biçim temel öğe gerektirmiyorsa `null` gönderilir. | Yalnızca üç temel‑öğe biçimi (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`) temel öğeyi değerlendirir; beş alan‑ilişkili biçim (`RunningTotalIn`, `PercentageOfParentTotal`, `PercentageOfRunningTotalIn`, iki sıralama) bunu görmez — `0` ya da `null` gönderin. |

| Hesaplama Tipi | Davranış | Temel Öğe Parametreleri |
| --- | --- | --- |
| `Normal` | İkincil bir hesaplama yok; birleştirilmiş değer olduğu gibi gösterilir (varsayılan). | — |
| `DifferenceFrom` | Değeri, temel alandaki bir temel öğenin değerinden fark olarak gösterir. | `baseField` + `baseItem` (indeks, başlık veya önceki/sonraki sentinel) |
| `PercentageOf` | Değeri, temel alandaki bir temel öğenin değerinin yüzdesi olarak gösterir. | `baseField` + `baseItem` (indeks, başlık veya önceki/sonraki sentinel) |
| `PercentageDifferenceFrom` | Değeri, temel alandaki bir temel öğenin değerine göre yüzde fark olarak gösterir. | `baseField` + `baseItem` (indeks, başlık veya önceki/sonraki sentinel) |
| `RunningTotalIn` | Değeri, temel alanın art arda gelen öğeleri için bir yürüyen toplam olarak gösterir. | `baseField` (toplamı yönlendiren alan) |
| `PercentageOfRow` | Değeri, satır toplamının yüzdesi olarak gösterir. | — |
| `PercentageOfColumn` | Değeri, sütun toplamının yüzdesi olarak gösterir. | — |
| `PercentageOfTotal` | Değeri, genel toplamın yüzdesi olarak gösterir. | — |
| `Index` | Değeri, Excel indeks formülü ((value * grand total) / (row total * column total)) ile gösterir. | — |
| `PercentageOfParentRowTotal` | Değeri, üst satır toplamının yüzdesi olarak gösterir (iç içe satır alanları için). | — |
| `PercentageOfParentColumnTotal` | Değeri, üst sütun toplamının yüzdesi olarak gösterir (iç içe sütun alanları için). | — |
| `PercentageOfParentTotal` | Değeri, üst toplamın yüzdesi olarak gösterir. | `baseField` (referans alınan üst alan) |
| `PercentageOfRunningTotalIn` | Değeri, temel alandaki bir yürüyen toplamın yüzdesi olarak gösterir. | `baseField` (biriktirme alanı) |
| `RankSmallestToLargest` | Değeri en küçükten (1) en büyüğe sıralar. | `baseField` (sıralama kapsamını tanımlayan alan) |
| `RankLargestToSmallest` | Değeri en büyükten (1) en küçüğe sıralar. | `baseField` (sıralama kapsamını tanımlayan alan) |

{{% alert color="primary" %}}
`showValuesAs(...)` yöntemi `PivotShowValuesSetting` özelliklerini (`showValuesAs`, `baseFieldIndex` ve `baseItemIndex`) yazar — yöntem ve özellik nesnesi aynı durumu yapılandırmak için iki yoldur; Excel’in **Değerleri Göster** iletişim kutusundaki temel alan ve temel öğe seçicilerini yansıtır.
{{% /alert %}}

## **Değerleri Toplam Yüzdesi Olarak Göster**
`PivotField.showValuesAs` yöntemini `PivotShowValuesAsType.PercentageOfTotal` ile çağırarak, tüm veri alanı hücrelerini (genel toplam dahil) toplamın payı olarak dönüştürün. Böylece gösterilen sayılar, tam sonuç kümesinin oranı gibi okunur. Bu biçim yalnızca genel toplam karşısında ölçüm yapar, bu yüzden temel alan veya temel öğe gerektirmez — son parametreler (`0`, `0`) format tarafından göz ardı edilen yer tutuculardır, yukarıdaki parametre tablosunda da belirtildiği gibi.

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
        <script src="aspose.cells.js.min.js"></script>
        <script type="text/javascript">
            const { Workbook, SaveFormat } = AsposeCells;
            const readyPromise = AsposeCells.onReady({
                license: "/lic/aspose.cells.enc",
                fontPath: "/fonts/",
                fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
            }).then(() => {
                console.log("Aspose.Cells initialized");
            });
            document.getElementById("runExample").addEventListener("click", async () => {

                // Load or create a workbook with source data
                const workbook = new Workbook();
                const dataSheet = workbook.worksheets.get(0);
                const cells = dataSheet.cells;
                cells.get("A1").value = "Fruit";
                cells.get("B1").value = "Amount";
                const fruits = ["Apple", "Banana", "Apple", "Cherry", "Banana", "Apple"];
                const amounts = [10, 20, 30, 40, 50, 60];
                for (let i = 0; i < fruits.length; i++) {
                    cells.get(i + 1, 0).value = fruits[i];
                    cells.get(i + 1, 1).value = amounts[i];
                }
                // Add a pivot table on a new worksheet
                const pivotSheetIndex = workbook.worksheets.add();
                const pivotSheet = workbook.worksheets.get(pivotSheetIndex);
                const pivotTable = pivotSheet.pivotTables.add("=Sheet1!A1:B7", 2, 2);
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
                pivotTable.calculateData();
                // Show the Amount data field as a percentage of the grand total with the
                // one-call method; PercentageOfTotal takes no base item, so the trailing
                // base arguments (0, 0) are placeholders the format ignores
                const dataField = pivotTable.dataFields.get(0);
                dataField.showValuesAs(AsposeCells.PivotShowValuesAsType.PercentageOfTotal, 0, 0);
                pivotTable.calculateData();
                // Body now reads (underlying values are fractions, shown with the
                // percentage format): Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById("downloadLink");
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "ShowValuesAsPercentageOfTotal.xlsx";
                downloadLink.style.display = "block";
                document.getElementById("result").innerHTML =
                    '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            });
        </script>
    </body>
</html>
```

## **PivotField.showValuesSetting’ı Okuma ve Yapılandırma**
Mevcut yapılandırmayı `PivotField.showValuesSetting` üzerinden okuyun: salt‑okuma özellik, alanın `PivotShowValuesSetting` nesnesini döndürür; bu nesnenin özellikleri etkin **Değerleri Göster** hesabını açıklar. Yapılandırmayı değiştirmek için `PivotField.showValuesAs` yöntemini çağırın — bu yöntem tüm ayarları tek bir çağrıda yazar, böylece özellikleri tek tek atamanıza gerek kalmaz.  
`PivotShowValuesSetting` nesnesi şu durumu ortaya koyar:
- `showValuesAs` `PivotShowValuesAsType` ikincil hesabını seçer.  
- `baseFieldIndex` pivot alanları içinde temel alanın sıfır‑tabanlı indeksini belirtir; temel‑ilişkili biçimler tarafından kullanılır.  
- `baseItemIndex` temel öğeyi belirtir: belirli bir pivot öğesinin sıfır‑tabanlı indeksi veya iki sentinel değerinden biri — `-1` önceki öğe, `-2` sonraki öğe (bağlayıcı adlandırılmış sabitleri dışa aktarmaz). Bu, temel‑öğe biçimleri tarafından kullanılır.  
- `baseFieldName` ve `baseItemCaption` salt‑okuma görünümleridir; çözümlenen temel alan adını ve temel öğe başlığını rapor eder; örneğin önceki‑öğe sentinelı seçildiğinde `baseItemCaption` `(previous)` döndürür.  
`showValuesAs` çağrısından sonra `PivotTable.calculateData()` yöntemiyle pivot gövdesini yeniden hesaplayıp güncellenmiş yapılandırmayla yeniden çizdirin.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xlsx" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;
        const ready = AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            try {
                await ready;
                const file = document.getElementById('fileInput').files[0];
                if (!file) {
                    throw new Error("Please select ShowValuesAsPercentageOfTotal.xlsx.");
                }
                const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                const worksheet = workbook.worksheets.get(1);
                const pivotTable = worksheet.pivotTables.get(0);
                const dataField = pivotTable.dataFields.get(0);
                // Read the current show-values settings
                const settings = dataField.showValuesSetting;
                const messages = [
                    `ShowValuesAs: ${settings.showValuesAs}`,
                    `BaseFieldIndex: ${settings.baseFieldIndex}`,
                    `BaseItemIndex: ${settings.baseItemIndex}`,
                    `BaseFieldName: ${settings.baseFieldName}`,
                    `BaseItemCaption: ${settings.baseItemCaption}`
                ];
                document.getElementById('result').innerHTML = messages
                    .map(message => `<p>${message}</p>`)
                    .join("");
                // Switch to a base-item calculation with the one-call method: difference
                // from the value of the previous item in the row field
                // (-1 is the previous-item sentinel; the binding does not export the constant)
                dataField.showValuesAs(
                    AsposeCells.PivotShowValuesAsType.DifferenceFrom,
                    pivotTable.rowFields.get(0).baseIndex,
                    -1
                );
                pivotTable.calculateData();
                // Note: the percentage number format saved by the previous example still
                // clings to the data field cells; the underlying values are now differences
                // Re-read the applied configuration
                messages.push(`ShowValuesAs now: ${dataField.showValuesSetting.showValuesAs}`);
                document.getElementById('result').innerHTML = messages
                    .map(message => `<p>${message}</p>`)
                    .join("");
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "ShowValuesAsDifferenceFrom.xlsx";
                downloadLink.style.display = "block";
            } catch (error) {
                document.getElementById('result').innerHTML =
                    `<p style="color: red;">${error.message}</p>`;
            }
        });
    </script>
</html>
```

## **İlgili Makaleler**
- [Pivot Tablosunda Değer Alanlarını Yönetme](/cells/tr/javascript-cpp/manage-value-fields/)
- [Pivot Tablosunu Yenileme](/cells/tr/javascript-cpp/refresh-pivot-table/)
- [Pivot Tablosuna Stil Uygulama](/cells/tr/javascript-cpp/apply-style-to-pivot-table/)

{{< app/cells/assistant language="javascript-cpp" >}}