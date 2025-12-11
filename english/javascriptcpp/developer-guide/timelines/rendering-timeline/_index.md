---  
title: Rendering Timeline  
type: docs  
weight: 40  
url: /javascript-cpp/rendering-timeline/  
description: Manage timelines of Excel files with Aspose.Cells for JavaScript via C++.  
keywords: Rendering timeline without Office 2013, Office 2016, Office 2019, and Office 365  
---  

## **Possible Usage Scenarios**  
Aspose.Cells for JavaScript via C++ supports rendering of timeline shapes without requiring Office 2013, Office 2016, Office 2019, or Office 365. If you convert your worksheet into an image or save your workbook to PDF or HTML formats, you will see that timelines are rendered properly.  

## **Rendering Timeline**  
The following sample code loads the [sample Excel file](input.xlsx) that contains an existing timeline. Get the shape object by the name of the timeline, and then render it into a picture through the `Shape.ToImage()` method. The following image is the [output image](out.png) that shows the rendered timeline. As you can see, the timeline has been rendered properly and it looks the same as in the sample Excel file.  

![todo:image_alt_text](out.png)  

### **Sample Code**  
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Export Timeline Shape as Image</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ImageOrPrintOptions, ImageType, Utils } = AsposeCells;
        
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
            const downloadLink = document.getElementById('downloadLink');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by loading the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access second worksheet (index 1)
            const sheet = workbook.worksheets.get(1);

            // Add timeline relating to pivot table (access the first timeline)
            const timeline = sheet.timelines.get(0);

            // Prepare image options
            const options = new ImageOrPrintOptions();
            options.imageType = ImageType.Png;

            // Get timeline shape object by timeline's name
            const timeLineShape = sheet.shapes.get(timeline.name);

            // Export shape to image (browser returns image bytes)
            const imageData = timeLineShape.toImage(options);

            // Create blob and provide download link
            const blob = new Blob([imageData], { type: 'image/png' });
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.png';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Timeline Image';

            resultDiv.innerHTML = '<p style="color: green;">Timeline image generated successfully. Click the download link to save the image.</p>';
        });
    </script>
</html>
```