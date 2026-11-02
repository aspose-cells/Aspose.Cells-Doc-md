---
title: Pivot Tablosunda Değerleri Göster
linktitle: Pivot Tablosunda Değerleri Göster
description: Pivot tablo veri alanı değerlerini toplamın yüzde olarak, bir temel öğeden fark olarak, çalışan toplamlar, sıralamalar ve daha fazlası biçiminde Aspose.Cells for JavaScript via C++ ile görüntüleyin.
keywords: Aspose.Cells, JavaScript via C++, pivot tablosu, değerleri göster, veri gösterim biçimi, PivotFieldDataDisplayFormat, PercentageOfTotal, PivotShowValuesSetting, CalculationType, BaseFieldIndex
type: docs
weight: 145
url: /tr/javascript-cpp/show-values-as-in-pivot-table/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Olası Kullanım Senaryoları**
Bir pivot tablo genellikle her veri alanını `Sum` veya `Count` gibi bir toplama işleviyle toplar. Excel'in **Show Values As** özelliği, her görüntülenen sonucu bu toplamdan türetilen ikincil bir hesaplamayla değiştirir—örneğin, genel toplamın yüzde olarak, çalışan toplam, seçilen bir temel öğeden fark veya bir sıralama—böylece yardımcı formüller veya hesaplanmış sütunlar olmadan karşılaştırmalı analiz yapabilirsiniz.
Tipik kullanım senaryoları, bir satır, sütun veya genel toplamın yüzde olarak dahil olmak üzere toplam payı analizini; bir dönem alanında çalışan toplam kullanarak kümülatif raporlamayı; bir temel öğeden fark veya yüzde fark ile bir karşılaştırma öğesine karşı varyans analizini; ve en küçükten en büyüğe ya da en büyükten en küçüğe değerleri sıralamayı içerir.
Aspose.Cells for JavaScript via C++'de `PivotFieldDataDisplayFormat` ikincil hesaplamayı seçer. Salt okunur `PivotField.showValuesSetting` özelliği bir `PivotShowValuesSetting` nesnesi döndürür; bu nesnenin yazılabilir `calculationType`, `baseFieldIndex`, `baseItemPositionType` ve `baseItemIndex` özellikleri davranışı yapılandırır; kullanıcı dostu `PivotField.showValuesAs(...)` yöntemi aynı dört ayarı tek bir çağrıda uygular. Bu ayarları `PivotTable.dataFields` aracılığıyla elde edilen bir veri veya değer alanına uygulayın.

## **PivotFieldDataDisplayFormat Enum Üyeleri**
Veri alanı, Sum veya Count gibi toplama işlevini korurken, Show Values As yalnızca toplanan değerin nasıl görüntüleneceğini dönüştürür.
`PivotShowValuesSetting` özelliklerini doğrudan yazmanın (bkz. son bölüm) yanı sıra, tek çağrılı bir kullanıcı dostu yöntem aynı yapılandırmayı uygular:

```html
dataField.showValuesAs(displayFormat, baseField, baseItemPositionType, baseItem);
```

| Parametre | Anlam | Ne Zaman Gerekli |
| --- | --- | --- |
| `displayFormat` | Uygulanacak `PivotFieldDataDisplayFormat` ikincil hesaplama. | Her zaman. |
| `baseField` | Pivot tablosunun temel alanları arasındaki temel alanın sıfır tabanlı indeksi (örneğin, temel öğenin ait olduğu satır alanının indeksi). | Yalnızca aşağıdaki altı taban ilgili biçimi (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`, `RunningTotalIn`, `PercentageOfRunningTotalIn`, `PercentageOfParentTotal`); diğer tüm biçimler tarafından yok sayılır. |
| `baseItemPositionType` | Temel öğenin mevcut öğeye göre nasıl seçildiği: `PivotItemPositionType.Previous`, `.Next` veya `.Custom`. | Yalnızca üç taban öğesi biçimi (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`); diğer tüm biçimler tarafından yok sayılır. |
| `baseItem` | Temel öğenin sıfır tabanlı indeksi. | Yalnızca `baseItemPositionType` `Custom` ise (öğe indeksi tam temel öğeyi seçer); `Previous` / `Next` için ve temel olmayan biçimlerde yoksayılır — `0` gönderin. |

| Hesaplama Türü | Davranış | Temel Öğesi Parametreleri |
| --- | --- | --- |
| `Normal` | İkincil hesaplama yok; toplama değeri olduğu gibi görüntülenir (varsayılan). | — |
| `DifferenceFrom` | Değeri, bir temel alandaki temel öğenin değerinden fark olarak gösterir. | `baseField` + `Previous`/`Next`/`Custom` (`baseItem` sadece `Custom` ile) |
| `PercentageOf` | Değeri, bir temel alandaki temel öğenin değerinin yüzde olarak gösterir. | `baseField` + `Previous`/`Next`/`Custom` (`baseItem` sadece `Custom` ile) |
| `PercentageDifferenceFrom` | Değeri, bir temel alandaki temel öğenin değerinin yüzde farkı olarak gösterir. | `baseField` + `Previous`/`Next`/`Custom` (`baseItem` sadece `Custom` ile) |
| `RunningTotalIn` | Değeri, bir temel alanın ardışık öğeleri için çalışan toplam olarak gösterir. | `baseField` (birikimi yönlendiren alan) |
| `PercentageOfRow` | Değeri satır toplamının yüzde olarak gösterir. | — |
| `PercentageOfColumn` | Değeri sütun toplamının yüzde olarak gösterir. | — |
| `PercentageOfTotal` | Değeri genel toplamın yüzde olarak gösterir. | — |
| `Index` | Değeri Excel indeks formülü ((değer * genel toplam) / (satır toplamı * sütun toplamı)) kullanarak gösterir. | — |
| `PercentageOfParentRowTotal` | Değeri, üst satır toplamının yüzde olarak gösterir (iç içe satır alanları için). | — |
| `PercentageOfParentColumnTotal` | Değeri, üst sütun toplamının yüzde olarak gösterir (iç içe sütun alanları için). | — |
| `PercentageOfParentTotal` | Değeri, üst toplamın yüzde olarak gösterir. | `baseField` (referans üst alan) |
| `PercentageOfRunningTotalIn` | Değeri, bir temel alandaki çalışan toplamın yüzde olarak gösterir. | `baseField` (birikim alanı) |
| `RankSmallestToLargest` | Değeri en küçükten en büyüğe sıralar. | — |
| `RankLargestToSmallest` | Değeri en büyükten en küçüğe sıralar. | — |

{{% alert color="primary" %}}
`showValuesAs(...)` `PivotShowValuesSetting` özelliğini (`calculationType`, `baseFieldIndex`, `baseItemPositionType`, `baseItemIndex`) yazar — yöntem ve özellik nesnesi aynı durumu yapılandırmanın iki yoludur, Excel'in Show Values As iletişim kutusundaki temel alan ve temel öğe seçicilerini yansıtır.
{{% /alert %}}

## **Değerleri Toplamın Yüzdesi Olarak Göster**
`PivotField.showValuesAs` yöntemini `PivotFieldDataDisplayFormat.PercentageOfTotal` ile çağırarak, genel toplam dahil her veri alanı hücresini genel toplamın payına dönüştürün. Görüntülenen sayılar böylece tam sonuç kümesinin oranı olarak okunur. Bu biçim yalnızca her değeri genel toplamla ölçer, bu yüzden temel alan veya temel öğe gerekmez — son parametreler (`0`, `PivotItemPositionType.Previous`, `0`) bu biçimin görmezden geldiği yer tutuculardır, yukarıdaki parametre tablosunda belirtildiği gibi.

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
                // base arguments (0, Previous, 0) are placeholders the format ignores
                const dataField = pivotTable.dataFields.get(0);
                dataField.showValuesAs(
                    AsposeCells.PivotFieldDataDisplayFormat.PercentageOfTotal,
                    0,
                    AsposeCells.PivotItemPositionType.Previous,
                    0
                );
                pivotTable.calculateData();
                // Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
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

## **PivotField.showValuesSetting'ı Al ve Yapılandır**
`PivotField.showValuesSetting` aracılığıyla mevcut yapılandırmayı okuyun: salt okunur özellik, alanın `PivotShowValuesSetting` nesnesini döndürür; bu nesnenin dört özelliği aktif Show Values As hesaplamasını tanımlar. Yapılandırmayı değiştirmek için `PivotField.showValuesAs` yöntemini çağırın — bu yöntem tüm dört ayarı tek bir çağrıda yazar, böylece özellikleri tek tek atamanıza gerek kalmaz.
`PivotShowValuesSetting` nesnesi `showValuesAs` tarafından yazılan dört özelliği ortaya koyar:
- `calculationType` `PivotFieldDataDisplayFormat` ikincil hesaplamasını seçer.
- `baseFieldIndex` pivot alanları içinde temel alanın sıfır tabanlı indeksini belirtir. Taban ilgili biçimler tarafından kullanılır.
- `baseItemPositionType` temel öğenin mevcut öğeye göre nasıl konumlandırıldığını belirler ve `PivotItemPositionType.Next`, `PivotItemPositionType.Previous` veya `PivotItemPositionType.Custom` değerlerini kabul eder.
- `baseItemIndex` sıfır tabanlı temel öğe indeksini belirtir ve `baseItemPositionType` `Custom` olduğunda kullanılır.
`showValuesAs` çağrısından sonra `PivotTable.calculateData()` tekrar çağırın, böylece pivot gövdesi güncellenen yapılandırmayla yeniden hesaplanır ve yeniden renderlanır.

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
                    `CalculationType: ${settings.calculationType}`,
                    `BaseFieldIndex: ${settings.baseFieldIndex}`,
                    `BaseItemPositionType: ${settings.baseItemPositionType}`,
                    `BaseItemIndex: ${settings.baseItemIndex}`
                ];
                document.getElementById('result').innerHTML = messages
                    .map(message => `<p>${message}</p>`)
                    .join("");
                // Switch to a base-item calculation with the one-call method: difference
                // from the value of the previous item in the row field
                dataField.showValuesAs(
                    AsposeCells.PivotFieldDataDisplayFormat.DifferenceFrom,
                    pivotTable.rowFields.get(0).baseIndex,
                    AsposeCells.PivotItemPositionType.Previous,
                    0
                );
                pivotTable.calculateData();
                // Note: the percentage number format saved by the previous example still
                // clings to the data field cells; the underlying values are now differences
                // Re-read the applied configuration
                messages.push(`CalculationType now: ${dataField.showValuesSetting.calculationType}`);
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
- [Pivot Tablosundaki Değer Alanlarını Yönetme](/cells/tr/javascript-cpp/manage-value-fields/)
- [Pivot Tablosunu Yenileme](/cells/tr/javascript-cpp/refresh-pivot-table/)
- [Pivot Tablosuna Stil Uygulama](/cells/tr/javascript-cpp/apply-style-to-pivot-table/)

{{< app/cells/assistant language="javascript-cpp" >}}