---
title: JavaScript ve C++ kullanarak Sayfa Sekmesi Çubuğunu nasıl kontrol edeceğinizi öğrenin.
linktitle: Sayfa Sekmesi Çubuğunu Nasıl Kontrol Edilir
type: docs
weight: 600
url: /tr/javascript-cpp/how-to-control-sheet-tab-bar/
description: C++ ve Aspose.Cells for JavaScript kullanarak sayfa sekmesi çubuğunu nasıl kontrol edeceğinizi öğrenin.
keywords: C++ ve JavaScript kullanarak Sayfa Sekmesi Çubuğunu Kontrol Etme, Sayfa Sekmesi Çubuğu ile İşlem Yapma, Sayfa Sekmesi Çubuğunu Ayarlama, JavaScript ile Sayfa Sekmesi Çubuğunu Kontrol Etme.  
---

## **Olası Kullanım Senaryoları**  
Excel sayfa çubuğunun görüntüsünü ayarlamak istediğinizde, sayfa sekmesi çubuğunu nasıl kontrol edeceğinizi bilmeniz gerekir; örneğin, sayfa sekmesi çubuğunu gizleme veya gösterme, genişliğini değiştirme, ilk görünen sekmeyi belirleme vb. Aspose.Cells for JavaScript ve C++ bu özellikleri destekler. Aspose.Cells, hedeflerinizi gerçekleştirmenize yardımcı olacak aşağıdaki özellikler ve yöntemler sağlar.

- [**WorkbookSettings.showTabs**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#showTabs--)
- [**WorkbookSettings.sheetTabBarWidth**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#sheetTabBarWidth--)
- [**WorkbookSettings.firstVisibleTab**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#firstVisibleTab--)

## **C++ ve Aspose.Cells for JavaScript kullanarak Sayfa Sekmesi Çubuğunu Nasıl Kontrol Edebilirsiniz**  
Bu örnek aşağıdakileri göstermektedir:

1. Bir çalışma kitabı oluşturma.
1. İlk çalışma sayfasındaki hücrelere veri ekleme.
1. Sayfa sekmesini görüntüleyin ve sekme çubuğunun genişliğini ayarlayın.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Populate Worksheet and Save</h1>
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

            // If a file is provided, load it; otherwise create a new workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Obtaining the reference of the first worksheet
            const ws = workbook.worksheets.get(0);
            const cells = ws.cells;

            // Setting the value to the cells (converted putValue -> value assignment)
            let cell = cells.get("A1");
            cell.value = "Fruit";
            cell = cells.get("B1");
            cell.value = "Count";
            cell = cells.get("C1");
            cell.value = "Price";

            cell = cells.get("A2");
            cell.value = "Apple";
            cell = cells.get("A3");
            cell.value = "Mango";
            cell = cells.get("A4");
            cell.value = "Blackberry";
            cell = cells.get("A5");
            cell.value = "Cherry";

            // Display the sheet tab and set the width of the tab bar (converted getters/setters -> properties)
            workbook.settings.showTabs = true;
            workbook.settings.sheetTabBarWidth = 150;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

Sonuç dosyası önizlemesi:  
<br>  
<image src="result.png" width="70%" />
