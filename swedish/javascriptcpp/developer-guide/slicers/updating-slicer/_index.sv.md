---
title: Uppdatera en slicer med JavaScript via C++
linktitle: Uppdatera en slicer
type: docs
weight: 50
url: /sv/javascript-cpp/updating-slicer/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
description: Den här artikeln visar hur man uppdaterar en slicer för att filtrera data i den länkade pivottabellen eller tabellen med Aspose.Cells for JavaScript via C++.
keywords: Aspose.Cells JavaScript via C++, Uppdatera slicer JavaScript, hur man ändrar slicern i JavaScript, hur man filtrerar en pivottabell med slicer i JavaScript, Slicer selectItems, Slicer clearFilter, Slicer unselectItems.
---

## **Möjliga användningsscenarier**
Att uppdatera en slicer innebär att filtrera data i pivottabellen eller tabellen som slicern är kopplad till. När du markerar eller avmarkerar slicerobjekt i Microsoft Excel beräknas den länkade pivottabellen eller tabellen om därefter. Med Aspose.Cells for JavaScript via C++ behöver du inte iterera över slicer-cacheobjekten och uppdatera slicern manuellt — metoden [**Slicer.selectItems(labels, append)**](https://reference.aspose.com/cells/javascript-cpp/slicer/) uppdaterar slicern och beräknar om den länkade pivottabellen eller tabellen direkt från filterobjekten:
- `Slicer.selectItems(labels, append)` — markerar de angivna etiketterna och beräknar om den länkade pivottabellen eller tabellen. När `append` är `true` behålls de ursprungligen markerade etiketterna och de angivna etiketterna läggs till i urvalet; när `append` är `false` rensas alla ursprungliga markeringar och endast de angivna etiketterna förblir markerade.
- `Slicer.unselectItems(labels)` — avmarkerar en del av de för närvarande markerade objekten.
- `Slicer.clearFilter()` — tar bort filtret och markerar alla objekt.

{{% alert color="primary" %}}
Från och med Aspose.Cells for JavaScript via C++ 26.10 blir egenskapen `SlicerCacheItem.selected` skrivskyddad och dess setter stöds inte längre. Använd metoderna `Slicer.selectItems`, `Slicer.unselectItems` och `Slicer.clearFilter` istället för att sätta `SlicerCacheItem.selected` objekt för objekt.
{{% /alert %}}

## **Hur man uppdaterar en slicer**
Följande exempelkod laddar [exempel-Excel-filen](67338475.xlsx) som innehåller en befintlig slicer som är kopplad till en pivottabell. Den markerar endast objekten "Blue" och "Pink" i slicern med `Slicer.selectItems(labels, false)` — pivottabellen beräknas om direkt från filterobjekten, utan ett manuellt anrop av `Slicer.refresh()`. Därefter sparas arbetsboken som [utdata-Excel-filen](67338476.xlsx). Skärmbilden nedan visar effekten av exempelkoden på exempel-Excel-filen. Som du kan se på skärmbilden visar pivottabellen endast de filtrerade objekten.
![todo:image_alt_text](updating-slicer_1.png)

## **Exempelkod**

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

Behåll de för närvarande markerade etiketterna och markera ytterligare objekt:

```javascript
// Keep the current selection and add "Red" to it.
slicer.selectItems(["Red"], true);
```

Avmarkera en del av de markerade objekten:

```javascript
// Remove "Pink" from the current selection.
slicer.unselectItems(["Pink"]);
```

Ta bort filtret (markera alla objekt):

```javascript
// Clear the filter; all slicer items become selected again.
slicer.clearFilter();
```

{{< app/cells/assistant language="javascript-cpp" >}}