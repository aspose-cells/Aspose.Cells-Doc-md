---
title: 如何在单元格中插入图片
type: docs
weight: 130
url: /zh/javascript-cpp/how-to-insert-picture-in-cell/
description: 学习如何通过 Aspose.Cells for JavaScript 通过 C++ 插入图片到单元格。
keywords: 如何在单元格中插入图片，在单元格上插入图片，在单元格中放置图片，在单元格上放置图片，如何在单元格中放置图像，如何在单元格上放置图像，在图片在单元格和在单元格上放置之间切换，从单元格中切换到单元格上放置、从单元格中切换到单元格上放置。
---

## **可能的使用场景**
图片为您的工作表增添了一丝明亮度，并提供了内容的视觉表示。它们还使您更容易理解数据并得出见解。尽管多年来您一直可以在Excel中使用图像，但是Excel最近才启用了图像成为实际单元格值的功能。即使图纸的布局被修改，它仍将附加到数据上。您可以在表格中使用它，在排序、筛选、包括在公式中等！

## **如何使用Excel在单元格中插入图片**
关于如何在Excel中在单元格中插入图片，请按照以下步骤操作：

1. 转到“插入”选项卡，单击“图片”选项。
2. 选择**放入单元格**。 从“从下拉菜单中插入图片”中选择以下来源之一（**此设备**，**库存图片** 和 **在线图片**）。 此设备用于从设备中插入图片。 库存图片用于从库存图片中插入图片。 在线图片用于从网络中插入图片。
<br>
<img src="1.png" width=60% />
3. 选择图片并将其插入到单元格中。
<br>
<img src="8.png" width=60% />

## **如何在Excel中在单元格上放置图片**
关于如何在Excel中在单元格上放置图片，请按照以下步骤操作：

1. 转到“插入”选项卡，单击“图片”选项。
2. 选择**放在单元格上**。 从“从下拉菜单中插入图片”中选择以下来源之一（**此设备**，**库存图片** 和 **在线图片**）。 此设备用于从设备中插入图片。 库存图片用于从库存图片中插入图片。 在线图片用于从网络中插入图片。
<br>
<img src="2.png" width=60% />
3. 选择图片并在单元格上插入图片。
<br>
<img src="3.png" width=60% />

## **如何在Excel中从单元格中的图片切换到单元格上的图片**
您可以轻松地从**单元格中**切换到**单元格上**。 请按照以下步骤操作：
1. 右键单元格，选择**单元格中** > **放在单元格上**。 
<br>
<img src="4.png" width=60% />
2. 切换后的结果如下：
<br>
<img src="5.png" width=60% />

## **如何在Excel中从单元格上方的图片切换到单元格内的图片**
您可以轻松地从 **单元格上方的图片** 切换到 **单元格内的图片**。请按照以下步骤操作：
1. 右键单击图片，然后选择 **放置在单元格中**。 
<br>
<img src="6.png" width=60% />
2. 切换后的结果如下：
<br>
<img src="7.png" width=60% />

## **如何使用 Aspose.Cells for JavaScript 通过 C++ 在单元格中插入图片**
使用 Aspose.Cells 在单元格中插入图片。请参阅以下示例代码。执行示例代码后，将在单元格中插入一张图片。
1. 实例化一个工作簿对象。 
2. 获取要插入图片的单元格。
3. 设置Cell.EmbeddedImage属性。 
4. 最后，以[out.xlsx]格式保存工作簿。 

## **示例代码**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Embed Image into New Workbook</h1>
        <p>Select an image file to embed into cell D8. A new workbook will be created with "Apple" in A2.</p>
        <input type="file" id="imageInput" accept="image/*" />
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
            const imageInput = document.getElementById('imageInput');
            const resultDiv = document.getElementById('result');

            // Create a new workbook
            const workbook = new Workbook();
            const cells = workbook.worksheets.get(0).cells;

            // Set A2 value to "Apple"
            const a2 = cells.get("A2");
            a2.value = "Apple";

            // Get D8 cell
            const d8 = cells.get("D8");

            // If an image file is selected, read it and embed into D8
            if (imageInput.files.length) {
                const file = imageInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                const imgBuf = new Uint8Array(arrayBuffer);
                d8.embeddedImage = imgBuf;
            }

            // Save workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Workbook created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
