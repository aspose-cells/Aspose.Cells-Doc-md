---
title: Updating Slicer with JavaScript via C++
linktitle: Updating Slicer
type: docs
weight: 50
url: /javascript-cpp/updating-slicer/
description: This article shows how to update linked pivot tables by updating a slicer using Aspose.Cells for JavaScript via C++.
keywords: Aspose.Cells JavaScript via C++, Update slicer JavaScript, how to change the slicer JavaScript, how to adjust the slicer in JavaScript, how to select or deselect the slicer items JavaScript via C++.
---

## **Possible Usage Scenarios**

If you want to update a slicer in Microsoft Excel, select or deselect its items, and it will then update the slicer table or pivot table accordingly. Please use [**Slicer.slicerCacheItems**](https://reference.aspose.com/cells/javascript-cpp/slicercache/#slicerCacheItems--) to select or deselect slicer items with Aspose.Cells and then call the [**Slicer.refresh()**](https://reference.aspose.com/cells/javascript-cpp/slicer/#refresh--) method to update the slicer table or pivot table.

## **How to Update Slicer**

The following sample code loads the [sample Excel file](67338475.xlsx) that contains an existing slicer. It deselects the 2nd and 3rd items of the slicer and refreshes the slicer. It then saves the workbook as [output Excel file](67338476.xlsx). The following screenshot shows the effect of the sample code on the sample Excel file. As you can see in the screenshot, refreshing the slicer with selected items has also refreshed the pivot table accordingly.

![todo:image_alt_text](updating-slicer_1.png)

## **Sample Code**

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
            
            // Access the slicer items via slicer cache
            const items = slicer.slicerCache.slicerCacheItems;
            
            // Iterate items and deselect "Pink" and "Green"
            for (let i = 0; i < items.count; i++) {
                const item = items.get(i);
                if (item.value === "Pink" || item.value === "Green") {
                    item.selected = false;
                }
            }
            
            // Refresh slicer to apply changes
            slicer.refresh();
            
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