---
title: Pivot Tablosunun Bölümünü Biçimlendirme
linktitle: Pivot Tablosunun Bölümünü Biçimlendirme
description: Aspose.Cells for JavaScript via C++ aracılığıyla bir pivot tablosunun bölümünü, PivotTable.Format üzerinden anlamsal PivotArea bölgelerine veya CellArea dikdörtgenlerine stiller uygulayarak biçimlendirin; biçimler PivotTable.PivotFormats içinde saklanır ve pivot tablo yenilendiğinde korunur.
keywords: Aspose.Cells for JavaScript via C++, pivot tablosu, biçim, PivotArea, CellArea, PivotTable.Format, PivotFormats, PivotTableSelectionType, LabelOnly, DataOnly, SelectField, FormatAll, C++
type: docs
weight: 20
url: /tr/javascript-cpp/format-part-of-pivot-table/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Olası Kullanım Senaryoları**
`PivotTable.FormatAll` tüm pivot tablosuna tek bir stil uygular ve ebeveyn sayfada ele alınmıştır. Etiketler, değerler, toplamlar veya raporun belirli bölgeleri arasında ayrım yapmaz.  
Uygulamada, bir pivot tablosunun yalnızca bir kısmının öne çıkması gerekir. Yaygın hedefler, bir satır alanına ait etiketler, bir alan tarafından üretilen değer hücreleri, toplam satırı veya ilk iki öğe satırı gibi isteğe bağlı bir dikdörtgen olabilir.  
Pivot tablosunun çalışma sayfası hücrelerine doğrudan bir stil uygulamak aynı şey değildir. Excel, pivot tablo biçimlendirmesini anlamsal `PivotArea` bölgeleri olarak saklar, normal hücre‑stil kayıtları olarak değil. Bir pivot‑alan formatı, bir alanın etiketleri veya veri değerleri gibi bir bölgeye bağlı kalır ve pivot tablo yeniden hesaplandığında, yenilendiğinde veya genişletildiğinde yeniden çözülür. Öte yandan doğrudan bir hücreye yazılan stil, o hücre konumuna aittir ve pivot modeli tarafından izlenmez.  
Aspose.Cells, her iki biçimlendirme türünün de kullanılabilmesi için tam `PivotTable.Format` aşırı yükleme ailesini sunar:
- `Format(PivotArea, Style)` bir stili, `PivotArea.Select` veya `PivotArea.SelectField` ile oluşturulan anlamsal bir bölgeye bağlar.
- `Format(CellArea, Style)` bir stili, pivot tablosu içindeki bir çalışma sayfası dikdörtgenine bağlar.
- `Format(int row, int column, Style)` tek bir hücreyi hedef alır.
- `FormatAll(Style)` tüm pivot tabloyu biçimlendirir.

## **Pivot Alanını Biçimlendirme**
Anlamsal alan iş akışı, bir vurgunun bir alanı veya raporun bir bölgesini takip etmesi gerektiğinde önerilen yaklaşımdır.
1. `new PivotArea(pivotTable)` ifadesiyle bir `PivotArea` oluşturun. Nesne, belirli pivot tabloya ait anlamsal bir bölgeyi tanımlar.
2. Belirli bir eksende, sıfır‑tabanlı konumuna göre bir alanı `PivotArea.Select(PivotFieldType axisType, int fieldPosition, PivotTableSelectionType selectionType)` ile seçin.
   - `PivotTableSelectionType.DataAndLabel` alanın hem etiketlerini hem de verilerini seçer.
   - `PivotTableSelectionType.LabelOnly` yalnızca alanın etiketlerini seçer.
   - `PivotTableSelectionType.DataOnly` yalnızca alanın veri hücrelerini seçer.
3. `PivotArea.SelectField(PivotFieldType axisType, string fieldName)` ile bir alanı adından seçin. Bir satır alanı adıyla seçildiğinde, bölge o alanın öğeleri tarafından üretilen değer hücrelerine çözülür.
4. `Workbook.CreateStyle()` ile bir `Style` oluşturun, yazı tipini, ön plan rengini ve katı arka plan desenini yapılandırın ve stili `PivotTable.Format(area, style)` metoduna geçirin.
5. `PivotArea` aşırı yüklemesine yapılan her çağrı, `PivotTable.PivotFormats` üzerine bir `PivotTableFormat` kaydı ekler.
6. Alan‑bağlı formatlar, pivot verileri hesaplandığında uygulanır. Bu nedenle, stillerin görünür olması için formatları uyguladıktan sonra `PivotTable.CalculateData()` metodunu çağırın.
Aşağıdaki örnek, küçük bir meyve‑satışları pivot tablosu oluşturur, `Fruit` satır etiketlerini `PivotArea.Select` ve `PivotTableSelectionType.LabelOnly` ile biçimlendirir, aynı satır alanı tarafından üretilen değer hücrelerini `PivotArea.SelectField` ile biçimlendirir ve ardından pivot tabloyu yeniden hesaplayarak her iki stilin de uygulanmasını sağlar.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
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
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const workbook = new Workbook();
            const sheet = workbook.worksheets.get(0);
            const cells = sheet.cells;
            // Fruit sales data
            const fruits = ["Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"];
            const years = [2024, 2024, 2025, 2025, 2024, 2025];
            const amounts = [100, 150, 120, 180, 90, 110];
            cells.get("A1").value = "Fruit";
            cells.get("B1").value = "Year";
            cells.get("C1").value = "Amount";
            for (let i = 0; i < fruits.length; i++) {
                cells.get(i + 1, 0).value = fruits[i];
                cells.get(i + 1, 1).value = years[i];
                cells.get(i + 1, 2).value = amounts[i];
            }
            // Pivot table with its top-left corner at E3 (row 2, column 4)
            const pivotTable = sheet.pivotTables.add("=A1:C7", 2, 4);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            pivotTable.calculateData();
            // Bold yellow fill on the row field's label cells
            const labelStyle = workbook.createStyle();
            labelStyle.font.isBold = true;
            labelStyle.foregroundColor = AsposeCells.Color.Yellow;
            labelStyle.pattern = AsposeCells.BackgroundType.Solid;
            const labelArea = new AsposeCells.PivotArea(pivotTable);
            labelArea.select(
                AsposeCells.PivotFieldType.Row,
                0,
                AsposeCells.PivotTableSelectionType.LabelOnly
            );
            pivotTable.format(labelArea, labelStyle);
            // Light green fill on the value cells the row field produces
            const valueStyle = workbook.createStyle();
            valueStyle.foregroundColor = AsposeCells.Color.LightGreen;
            valueStyle.pattern = AsposeCells.BackgroundType.Solid;
            const valueArea = new AsposeCells.PivotArea(pivotTable);
            valueArea.selectField(AsposeCells.PivotFieldType.Row, "Fruit");
            pivotTable.format(valueArea, valueStyle);
            // Field-anchored formats are painted when the data is calculated
            pivotTable.calculateData();
            // Label cells E4:E6 are now bold on yellow, value cells F4:F6 are light green
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "FormatPivotArea.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML =
                '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **Pivot Tablosunun Hücre Alanını Biçimlendirme**
İlgili bölge anlamsal bir pivot bölgesi yerine düz bir çalışma sayfası dikdörtgeni olduğunda `PivotTable.Format(CellArea, Style)` kullanın.
`CellArea`, `startRow`, `startColumn`, `endRow` ve `endColumn` alanlarıyla tanımlanır. Değerler sıfır‑tabanlı çalışma sayfası koordinatlarıdır ve bitiş koordinatları dikdörtgende dahil edilen son satır ve sütunu belirler; böylece alan, başlangıç konumundan bitiş konumuna kadar tüm hücreleri kapsar.
Alan‑bağlı bir formatın aksine, `CellArea` formatı hücrelere anında uygulanır. Stil görünmesi için ek bir `CalculateData()` çağrısına gerek yoktur.
`CellArea` dikdörtgeni etiket hücrelerini ve değer hücrelerini birlikte içerebilir. Sonraki bölüm, Aspose.Cells ve Excel'in bu dikdörtgeni dahili olarak nasıl temsil ettiğini açıklar.
Aşağıdaki örnek, pivot tablosunun `E4:F5` dikdörtgenini italic, açık‑mavi bir stil ile biçimlendirir ve çalışma kitabını başka bir yeniden hesaplamaya gerek kalmadan kaydeder.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
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
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const workbook = new Workbook();
            const sheet = workbook.worksheets.get(0);
            const cells = sheet.cells;
            const fruits = ["Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"];
            const years = [2024, 2024, 2025, 2025, 2024, 2025];
            const amounts = [100, 150, 120, 180, 90, 110];
            cells.get("A1").value = "Fruit";
            cells.get("B1").value = "Year";
            cells.get("C1").value = "Amount";
            for (let i = 0; i < fruits.length; i++) {
                cells.get(i + 1, 0).value = fruits[i];
                cells.get(i + 1, 1).value = years[i];
                cells.get(i + 1, 2).value = amounts[i];
            }
            const pivotTable = sheet.pivotTables.add("=A1:C7", 2, 4);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            pivotTable.calculateData();
            // Highlight the first two fruit rows (the rectangle E4:F5)
            const highlightStyle = workbook.createStyle();
            highlightStyle.font.isItalic = true;
            highlightStyle.foregroundColor = AsposeCells.Color.LightBlue;
            highlightStyle.pattern = AsposeCells.BackgroundType.Solid;
            const rectangle = new AsposeCells.CellArea();
            rectangle.startRow = 3;
            rectangle.startColumn = 4;
            rectangle.endRow = 4;
            rectangle.endColumn = 5;
            pivotTable.format(rectangle, highlightStyle);
            // E4:F5 is italic on light blue immediately, no recalculation needed
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "FormatPivotCellArea.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **Pivot Alanları ve Hücre Alanları Nasıl Haritalanır**
Excel, pivot tablo biçimlendirmesini normal çalışma sayfası hücre‑stil kayıtları yerine `pivotArea` kayıtları olarak saklar. Aynı model Aspose.Cells tarafından da kullanılır; bu nedenle bir biçimlendirme isteği kaydedildiğinde pivot alanlarına dönüştürülür.  
Kullanıcı tarafından sağlanan `CellArea` ile dahili olarak saklanan pivot alanları arasındaki ilişki her iki yönde de çok‑çok’tür.  
- Tek bir `CellArea` birden fazla pivot alanı üretebilir. Dikdörtgen hem etiket hem de değer hücrelerini kapsıyorsa, pivot modeli etiket biçimlendirmesini ve veri biçimlendirmesini bağımsız olarak ele aldığı için, bu alan ayrı etiket ve veri kurallarına bölünür.  
- Tek bir pivot alanı, birbirinden bağımsız birden fazla `CellArea` nesnesine çözülebilir. Toplam satırı gibi anlamsal bir bölge veya öğeleri kesintili bir alan, birden fazla dikdörtgeni kapsayabilir. Bu nedenle `PivotArea.GetCellAreas()` tek bir dikdörtgen yerine bir koleksiyon döndürür.  
`PivotTable.Format` aracılığıyla gerçekleştirilen her biçim işlemi `PivotTable.PivotFormats` içinde kaydedilir. Her `PivotTableFormat` kaydı, ilişkili `PivotArea` ve ona uygulanan `Style`ı gösterir. `PivotArea` aşırı yüklemesi, her çağrı için tam bir kayıt ekler; farklı anlamsal bölgeler içeren bir `CellArea` ise birden fazla kayıt ekleyebilir.  
Saklanan bölgeleri ayırt etmek için, her `PivotArea` `OnlyLabel` ve `OnlyData` bayraklarını gösterir. Aşağıdaki örnek, hem etiket hem de değerleri kapsayan tek bir dikdörtgeni biçimlendirir, `PivotTable.PivotFormats` inceler ve her saklanan pivot alanının çözüldüğü `CellArea` koordinatlarını yazdırır.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
        <script src="aspose.cells.js.min.js"></script>
        <script type="text/javascript">
            const { Workbook, SaveFormat, CellArea, Color } = AsposeCells;
            AsposeCells.onReady({
                license: "/lic/aspose.cells.enc",
                fontPath: "/fonts/",
                fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
            }).then(() => {
                console.log("Aspose.Cells initialized");
            });
            document.getElementById("runExample").addEventListener("click", async () => {
                const result = document.getElementById("result");
                const downloadLink = document.getElementById("downloadLink");
                const workbook = new Workbook();
                const sheet = workbook.worksheets.get(0);
                const cells = sheet.cells;
                const fruits = ["Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"];
                const years = [2024, 2024, 2025, 2025, 2024, 2025];
                const amounts = [100, 150, 120, 180, 90, 110];
                cells.get("A1").value = "Fruit";
                cells.get("B1").value = "Year";
                cells.get("C1").value = "Amount";
                for (let i = 0; i < fruits.length; i++) {
                    cells.get(i + 1, 0).value = fruits[i];
                    cells.get(i + 1, 1).value = years[i];
                    cells.get(i + 1, 2).value = amounts[i];
                }
                const pivotTable = sheet.pivotTables.add("=A1:C7", 2, 4);
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
                pivotTable.calculateData();
                const highlightStyle = workbook.createStyle();
                highlightStyle.font.isItalic = true;
                highlightStyle.foregroundColor = Color.LightBlue;
                highlightStyle.pattern = AsposeCells.BackgroundType.Solid;
                // ONE rectangle in...
                const rectangle = new CellArea();
                rectangle.startRow = 3;
                rectangle.startColumn = 4;
                rectangle.endRow = 4;
                rectangle.endColumn = 5;
                // ...TWO semantic pivot areas out: the label part and the data part are stored separately
                pivotTable.format(rectangle, highlightStyle);
                const pivotFormats = pivotTable.pivotFormats;
                const outputLines = [`Stored formats: ${pivotFormats.count}`];
                for (let i = 0; i < pivotFormats.count; i++) {
                    const pivotFormat = pivotFormats.get(i);
                    const storedArea = pivotFormat.pivotArea;
                    const onlyLabel = storedArea.onlyLabel ? "True" : "False";
                    const onlyData = storedArea.onlyData ? "True" : "False";
                    outputLines.push(`Format ${i}: OnlyLabel=${onlyLabel}, OnlyData=${onlyData}`);
                    const resolvedAreas = storedArea.cellAreas;
                    for (let j = 0; j < resolvedAreas.count; j++) {
                        const resolved = resolvedAreas.get(j);
                        outputLines.push(
                            `    rows ${resolved.startRow + 1}-${resolved.endRow + 1}, columns ${resolved.startColumn + 1}-${resolved.endColumn + 1}`
                        );
                    }
                }
                // This prints:
                // Stored formats: 2
                // Format 0: OnlyLabel=True, OnlyData=False
                //     rows 4-5, columns 5-5        (E4:E5, the label part)
                // Format 1: OnlyLabel=False, OnlyData=True
                //     rows 4-5, columns 6-6        (F4:F5, the data part)
                result.innerHTML =
                    `<pre>${outputLines.join("\n")}</pre>` +
                    `<p style="color: green;">Done! Click the download link to get the result file.</p>`;
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "FormatPivotAreasMap.xlsx";
                downloadLink.style.display = "block";
            });
        </script>
    </body>
</html>
```

{{% alert color="primary" %}}
Biçimler, normal hücre stilleri yerine pivot alanları olarak saklandığı için yeniden hesaplamalar ve yenilemeler sırasında korunur. Pivot tablo `PivotTable.RefreshData` ile yenilendiğinde, `CalculateData` ile yeniden hesaplandığında veya kaydedilip yeniden yüklendiğinde, her saklanan pivot alanı bölgesinin mevcut konumuna yeniden çözülür ve stili yeniden uygulanır.
{{% /alert %}}

Vurgunun yenilemeler sırasında bir alana veya anlamsal bir bölgeye bağlı kalması gerektiğinde `Select` veya `SelectField` ile oluşturulmuş bir `PivotArea` kullanın; mevcut pivot tablo düzeninde sabit bir dikdörtgeni biçimlendirmek yeterli olduğunda bir `CellArea` kullanın. Tek hücre `Format(int row, int column, Style)` aşırı yüklemesi bireysel bir hücreyi hedef alır. Tüm pivot tablonun bir kerede yeniden biçimlendirilmesi gerektiğinde ebeveyn sayfada anlatıldığı gibi `FormatAll` kullanın.

## **İlgili Makaleler**
- [Pivot Tablosuna Stil Uygulama](/cells/tr/javascript-cpp/apply-style-to-pivot-table/)
- [Pivot Tablosuna Satır ve Sütun Alanları Ekleme](/cells/tr/javascript-cpp/pivot-table-add-row-and-column-fields/)
- [Pivot Tablosunda Değer Alanlarını Yönetme](/cells/tr/javascript-cpp/manage-value-fields/)
- [Pivot Tablosunu Yenileme](/cells/tr/javascript-cpp/refresh-pivot-table/)

{{< app/cells/assistant language="javascript-cpp" >}}