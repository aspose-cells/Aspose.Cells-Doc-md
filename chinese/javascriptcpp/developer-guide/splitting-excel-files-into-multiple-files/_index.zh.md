---
title: 将 Excel 文件拆分为多个文件
linktitle: 将 Excel 文件拆分为多个文件
description: Aspose.Cells for JavaScript via C++ 是一个用于处理电子表格文件的 JavaScript via C++ 库，支持将单个 Excel 文件拆分为多个文件。本篇文章将介绍如何通过将每个工作表复制到单独的工作簿以及将特定单元格区域复制到其他工作簿来拆分 Excel 文件。
keywords: Aspose.Cells, Aspose.Cells for JavaScript via C++ 库, 电子表格, 拆分 Excel 文件, 复制工作表, 复制区域, 多个工作簿, 另存为独立文件
type: docs
weight: 195
url: /zh/javascript-cpp/splitting-excel-files-into-multiple-files/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells for JavaScript via C++ 支持将单个 Excel 文件拆分为多个文件。有两种主要方式： (1) 将源工作簿的每个工作表复制到新工作簿并分别保存为独立文件；以及 (2) 将工作表中的特定单元格区域复制到新工作簿。两种方法都适用于需要分发数据子集、为不同收件人生成更小报告或将数据隔离以便单独处理的场景。
{{% /alert %}}

## **介绍**
在实际开发中，常常需要将一个 Excel 文件拆分成若干更小的文件。例如，工作簿中可能为每个部门提供一个工作表，而每位部门负责人只需接收自己的工作表。又或者希望从工作表中提取特定表格或数据块，作为独立文件通过邮件发送，而不暴露工作簿的其余内容。大型合并工作簿有时也需要拆分为更小的片段，以便更容易处理、加快加载速度，或供下游系统进一步处理。  
Aspose.Cells for JavaScript via C++ 提供了两种灵活的实现方式。第一种方式遍历源工作簿的所有工作表，将每个工作表的内容复制到全新的 `Workbook` 实例，并分别保存为独立文件。第二种方式聚焦于工作表中的特定单元格区域，仅将该区域复制到新工作簿。两种方式的通用流程相同：使用 `Workbook` 类加载源工作簿，通过 `Worksheet` 和 `Cells` 对象获取相关数据，将内容转移到目标 `Workbook`，最后将目标工作簿保存到磁盘。

## **通过复制每个工作表到新工作簿来拆分 Excel 文件**

### **方法概述**
在此方法中，先打开一次源工作簿，然后对其 `Worksheets` 集合中的每个 `Worksheet`，创建一个新的目标 `Workbook`。将源工作表的内容复制到目标工作簿的第一个工作表中，并使用源工作表的名称生成输出文件名。最终得到的结果是每个工作表对应一个输出文件，每个文件仅包含该源工作表的数据。  
当源工作簿中的每个工作表代表一个逻辑上独立的信息单元（如部门、地区、月份或产品线），且希望对每个单元单独交付或处理时，此方法是最佳选择。

### **步骤**
以下步骤说明如何通过复制每个工作表到新工作簿来拆分 Excel 文件：
1. 实例化 `Workbook` 对象并传入文件路径，以打开源 Excel 文件。  
2. 使用 `for` 或 `for...of` 循环遍历 `Workbook.Worksheets` 集合，处理源文件中的每个 `Worksheet`。  
3. 在循环内部，为当前工作表创建一个新的目标 `Workbook` 实例（空工作簿）。  
4. 将源工作表的内容复制到目标工作表。可以遍历源工作表的 `Cells` 集合并将值写入目标工作表对应的单元格，或使用 `Cells.Copy` 方法一次性复制整个区域。  
5. 构建输出文件路径，将源工作表的名称拼接进去（例如 `dataDir + worksheet.Name + ".xls"`），确保每个生成的文件名称唯一。  
6. 调用目标 `Workbook.Save` 方法将文件写入磁盘。  
7. 对下一个工作表重复步骤 3 到 6，直至处理完所有工作表。

### **代码示例**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xls" />
        <button id="runExample">Run Example</button>
        <div id="result"></div>
        <script src="aspose.cells.js.min.js"></script>
        <script type="text/javascript">
            const { Workbook } = AsposeCells;
            const readyPromise = AsposeCells.onReady({
                license: "/lic/aspose.cells.enc",
                fontPath: "/fonts/",
                fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
            });
            document.getElementById('runExample').addEventListener('click', async () => {
                const result = document.getElementById('result');
                try {
                    const fileInput = document.getElementById('fileInput');
                    const file = fileInput.files[0];
                    if (!file) {
                        result.innerHTML = '<p style="color: red;">Please select an .xls file.</p>';
                        return;
                    }
                    result.innerHTML = '<p>Processing...</p>';
                    const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                    const downloadLinks = document.createElement('div');
                    for (let i = 0; i < workbook.worksheets.count; i++) {
                        const sourceSheet = workbook.worksheets.get(i);
                        const sheetName = sourceSheet.name;
                        const destWorkbook = new Workbook();
                        const destIndex = destWorkbook.worksheets.add();
                        const destSheet = destWorkbook.worksheets.get(destIndex);
                        destSheet.name = sheetName;
                        destSheet.copy(sourceSheet);
                        const outputData = destWorkbook.save(AsposeCells.SaveFormat.Excel97To2003);
                        const blob = new Blob([outputData], { type: "application/vnd.ms-excel" });
                        const downloadLink = document.createElement('a');
                        downloadLink.href = URL.createObjectURL(blob);
                        downloadLink.download = `${sheetName}.xls`;
                        downloadLink.textContent = `Download ${sheetName}.xls`;
                        downloadLink.style.display = 'block';
                        downloadLink.style.marginTop = '8px';
                        downloadLinks.appendChild(downloadLink);
                    }
                    result.innerHTML = '<p style="color: green;">Done! Click a download link to get the result file.</p>';
                    result.appendChild(downloadLinks);
                } catch (error) {
                    console.error(error);
                    const errorMessage = document.createElement('p');
                    errorMessage.style.color = 'red';
                    errorMessage.textContent = `Error: ${error instanceof Error ? error.message : error}`;
                    result.replaceChildren(errorMessage);
                }
            });
        </script>
    </body>
</html>
```

预期的输出是一组位于 data 目录的新文件，每个文件对应源工作簿中的一个工作表。每个文件的名称来源于相应的源工作表，并且文件中包含该工作表的数据（以及可选的格式）。

## **通过复制区域到新工作簿来拆分 Excel 文件**

### **方法概述**
有时需要拆分的数据并非整张工作表，而是工作表中的特定矩形区域，例如 `A1:D10` 或表示某个表格的命名区域。在这种情况下，复制整个工作表会造成资源浪费，需要采用更精确的方式：定位源区域，仅将该区域复制到新工作簿，并保存为新文件。  
当您只想从大型工作表中提取单个表格、报告块或数据区域，同时舍弃所有不相关内容时，此方法非常适用。它也可用于将用户选定的工作表区域导出为独立文件。

### **步骤**
以下步骤说明如何通过复制特定区域到新工作簿来拆分 Excel 文件：
1. 实例化 `Workbook` 对象并提供文件路径，以打开源 Excel 文件。  
2. 从 `Worksheets` 集合中获取包含目标区域的 `Worksheet`，可按索引（例如第一张工作表）或按名称获取。  
3. 确定要复制的区域。可以是硬编码的单元格区域如 `A1:C10`，也可以是通过 `Worksheet.Cells` 集合获取的命名区域，或使用 `Worksheet.Cells.CreateRange` 创建的区域。  
4. 创建一个新的目标 `Workbook` 实例。  
5. 访问目标工作簿的第一个 `Worksheet`（默认工作表）。  
6. 将源区域复制到目标工作表，通常从单元格 `A1` 开始。可以使用目标 `Cells` 集合的 `Cells.Copy` 方法一次性复制整个区域，或遍历源区域的单元格并使用 `PutValue` 将值写入目标单元格。可选地提供 `CopyOptions` 以控制复制内容（仅值、值加样式、公式等）。  
7. 使用 `Workbook.Save` 方法将目标工作簿保存到磁盘上的新文件路径。

### **代码示例**
预期的输出是 data 目录中的一个新文件，该文件仅包含从源工作簿中提取的指定区域的值（以及可选的格式），文件的第一工作表从单元格 `A1` 开始，且与源文件的其他数据无任何关联。

## Related Articles
- [在 Aspose.Cells for JavaScript via C++ 中向数据透视表添加筛选字段](/cells/zh/javascript-cpp/add-page-field-in-pivot-table/)
- [在 Aspose.Cells for JavaScript via C++ 中为数据透视表应用样式](/cells/zh/javascript-cpp/apply-style-to-pivot-table/)
- [修改数据透视表的页面字段布局](/cells/zh/javascript-cpp/change-page-field-layout/)
- [在 Aspose.Cells for JavaScript via C++ 中将 Sparkline 转换为图像和 HTML](/cells/zh/javascript-cpp/convert-sparkline-to-image-and-html/)
- [将 Excel 转换为 OFD 格式](/cells/zh/javascript-cpp/converting-excel-to-ofd-format/)

{{< app/cells/assistant language="javascript-cpp" >}}