---
title: 将 Excel 转换为 OFD 格式
linktitle: 将 Excel 转换为 OFD 格式
description: Aspose.Cells for JavaScript via C++ 是一个用于处理电子表格文件的 JavaScript 库，支持将 Excel 工作簿转换为 OFD（开放固定版式文档）格式。本文介绍如何创建 Excel 内容并将其导出为 OFD，以及如何使用 Aspose.Cells 将现有 Excel 文件转换为 OFD。
keywords: Aspose.Cells, Aspose.Cells for JavaScript via C++, JavaScript 库, 电子表格, Excel 转换为 OFD, OFD 转换, SaveFormat.Ofd, 固定版式文档, 工作簿导出
type: docs
weight: 195
url: /zh/javascript-cpp/converting-excel-to-ofd-format/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells 支持使用 `SaveFormat.Ofd` 枚举值将 Excel 工作簿直接转换为 OFD（开放固定版式文档）格式。生成的 OFD 文档会保留工作簿的可见布局、内容、合并单元格、列宽、行高、字体、颜色、边框和数字格式。因此，Aspose.Cells 适用于需要固定版式输出的归档、打印、监管申报和政府提交流程。
{{% /alert %}}

## **简介**
OFD（开放固定版式文档）是中国国家标准（GB/T 33190-2016），用于以基于页面的固定布局表示数字文档。在需要精确保留源文档原始视觉效果的场景中，其作用与 PDF 类似。OFD 已广泛应用于中华人民共和国境内的政府报送、监管申报、电子发票和长期归档。
在需要以只读、布局锁定的文档形式分发电子表格内容（而非提供可编辑的电子表格）的场景中，将 Excel 工作簿转换为 OFD 是一项常见需求。例如，向客户发送最终确认的发票、归档季度财务报告，或向监管机构提交预算电子表格。Aspose.Cells 通过 `SaveFormat.Ofd` 枚举值满足这一需求，无需中间转换步骤，即可将工作簿直接写入 OFD。OFD 输出会保留单元格值、合并区域、字体、颜色、边框、数字格式，以及工作簿中配置的页面设置选项。

{{% alert color="primary" %}}
Aspose.Cells 生成的 OFD 输出会保留源工作簿的可见布局，包括单元格内容、合并单元格、列宽和行高。字体、颜色、边框、对齐方式和数字格式等单元格格式也会呈现在固定版式输出中。在工作表上配置的页面设置选项（如纸张大小、页面方向和打印区域）也会影响最终 OFD 文档的布局。
{{% /alert %}}

## **创建 Excel 工作簿并保存为 OFD**
Aspose.Cells 允许您以编程方式构建工作簿、填充数据，然后使用 `SaveFormat.Ofd` 枚举值直接将其保存为 OFD 格式。以下示例从头创建一张发票。它添加公司徽标、标头信息、付款方信息、明细项目以及计算得出的总计金额，然后将工作簿导出为 OFD 文档。

### **创建带徽标的发票**
该示例通过将徽标图像插入左上角区域来构建发票工作表，填充公司名称和联系方式，在合并的单元格区域中设置“INVOICE”标题，记录发票编号和日期，列出付款方客户信息，构建包含说明、数量、单价和总计列的明细项目表，并使用单元格公式计算小计、税额和总计。粗体表头、价格的货币格式、边框和列宽等格式设置通过 `Style` 和 `Font` 对象应用。最后，使用 `SaveFormat.Ofd` 将工作簿保存为扩展名为 `.ofd` 的文件。

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
        const { Workbook, Color } = AsposeCells;
        const readyPromise = AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            try {
                // 创建一个新的工作簿
                const workbook = new Workbook();
                // 获取第一个工作表
                const worksheet = workbook.worksheets.get(0);
                const cells = worksheet.cells;
                // 设置列宽
                cells.setColumnWidth(0, 5);
                cells.setColumnWidth(1, 35);
                cells.setColumnWidth(2, 12);
                cells.setColumnWidth(3, 15);
                cells.setColumnWidth(4, 15);
                cells.setColumnWidth(5, 5);
                // 插入公司徽标
                // 由于浏览器没有文件系统路径，因此创建内存中的 PNG。
                const logoCanvas = document.createElement("canvas");
                logoCanvas.width = 100;
                logoCanvas.height = 30;
                const logoContext = logoCanvas.getContext("2d");
                logoContext.fillStyle = "#000080";
                logoContext.fillRect(0, 0, logoCanvas.width, logoCanvas.height);
                logoContext.fillStyle = "#FFFFFF";
                logoContext.font = "bold 18px Arial";
                logoContext.fillText("ACME", 16, 21);
                const logoBlob = await new Promise(resolve => logoCanvas.toBlob(resolve, "image/png"));
                if (!logoBlob) {
                    throw new Error("Unable to create the company logo.");
                }
                const logoData = new Uint8Array(await logoBlob.arrayBuffer());
                worksheet.pictures.add(1, 1, logoData);
                // 公司名称和联系方式
                cells.get("B3").value = "Acme Corporation";
                cells.get("B4").value = "123 Business Street";
                cells.get("B5").value = "City, State 12345";
                cells.get("B6").value = "Phone: (555) 123-4567";
                // INVOICE 标题 - 合并单元格
                cells.merge(7, 1, 2, 4);
                const titleCell = cells.get("B8");
                titleCell.value = "INVOICE";
                const titleStyle = workbook.createStyle();
                titleStyle.font.isBold = true;
                titleStyle.font.size = 20;
                titleStyle.horizontalAlignment = AsposeCells.TextAlignmentType.Center;
                titleCell.style = titleStyle;
                // 发票编号和日期
                cells.get("B11").value = "Invoice Number:";
                cells.get("C11").value = "INV-2024-001";
                cells.get("B12").value = "Date:";
                const now = new Date();
                const invoiceDate = [
                    now.getFullYear(),
                    String(now.getMonth() + 1).padStart(2, "0"),
                    String(now.getDate()).padStart(2, "0")
                ].join("-");
                cells.get("C12").value = invoiceDate;
                // 付款方信息
                cells.get("B14").value = "Bill To:";
                cells.get("B15").value = "Client Name";
                cells.get("B16").value = "Client Address";
                cells.get("B17").value = "Client City, State";
                // 明细项目表头
                const headerDesc = cells.get("B19");
                const headerQty = cells.get("C19");
                const headerPrice = cells.get("D19");
                const headerTotal = cells.get("E19");
                headerDesc.value = "Description";
                headerQty.value = "Quantity";
                headerPrice.value = "Unit Price";
                headerTotal.value = "Total";
                const headerStyle = workbook.createStyle();
                headerStyle.font.isBold = true;
                headerStyle.font.color = Color.fromArgb(255, 255, 255);
                headerStyle.foregroundColor = Color.fromArgb(0, 0, 128);
                headerStyle.pattern = AsposeCells.BackgroundType.Solid;
                headerStyle.horizontalAlignment = AsposeCells.TextAlignmentType.Center;
                headerStyle.borders.get(AsposeCells.BorderType.TopBorder).lineStyle = AsposeCells.CellBorderType.Thin;
                headerStyle.borders.get(AsposeCells.BorderType.BottomBorder).lineStyle = AsposeCells.CellBorderType.Thin;
                headerStyle.borders.get(AsposeCells.BorderType.LeftBorder).lineStyle = AsposeCells.CellBorderType.Thin;
                headerStyle.borders.get(AsposeCells.BorderType.RightBorder).lineStyle = AsposeCells.CellBorderType.Thin;
                headerDesc.style = headerStyle;
                headerQty.style = headerStyle;
                headerPrice.style = headerStyle;
                headerTotal.style = headerStyle;
                // 带边框的货币样式
                const currencyStyle = workbook.createStyle();
                currencyStyle.custom = '"$"#,##0.00';
                currencyStyle.borders.get(AsposeCells.BorderType.TopBorder).lineStyle = AsposeCells.CellBorderType.Thin;
                currencyStyle.borders.get(AsposeCells.BorderType.BottomBorder).lineStyle = AsposeCells.CellBorderType.Thin;
                currencyStyle.borders.get(AsposeCells.BorderType.LeftBorder).lineStyle = AsposeCells.CellBorderType.Thin;
                currencyStyle.borders.get(AsposeCells.BorderType.RightBorder).lineStyle = AsposeCells.CellBorderType.Thin;
                // 描述/数量单元格的普通边框样式
                const borderStyle = workbook.createStyle();
                borderStyle.borders.get(AsposeCells.BorderType.TopBorder).lineStyle = AsposeCells.CellBorderType.Thin;
                borderStyle.borders.get(AsposeCells.BorderType.BottomBorder).lineStyle = AsposeCells.CellBorderType.Thin;
                borderStyle.borders.get(AsposeCells.BorderType.LeftBorder).lineStyle = AsposeCells.CellBorderType.Thin;
                borderStyle.borders.get(AsposeCells.BorderType.RightBorder).lineStyle = AsposeCells.CellBorderType.Thin;
                // 明细项目行
                const lineItems = [
                    ["Product A - Widget", 2, 50.00],
                    ["Product B - Gadget", 3, 75.00],
                    ["Product C - Service", 1, 100.00]
                ];
                for (let i = 0; i < lineItems.length; i++) {
                    const row = 20 + i;
                    const descCell = cells.get(row, 1);
                    const qtyCell = cells.get(row, 2);
                    const priceCell = cells.get(row, 3);
                    const totalCell = cells.get(row, 4);
                    descCell.value = lineItems[i][0];
                    qtyCell.value = lineItems[i][1];
                    priceCell.value = lineItems[i][2];
                    totalCell.formula = "C" + (row + 1) + "*D" + (row + 1);
                    descCell.style = borderStyle;
                    qtyCell.style = borderStyle;
                    priceCell.style = currencyStyle;
                    totalCell.style = currencyStyle;
                }
                // 小计、税额、总计
                cells.get("B24").value = "Subtotal:";
                const subtotalCell = cells.get("E24");
                subtotalCell.formula = "SUM(E21:E23)";
                cells.get("B25").value = "Tax (10%):";
                const taxCell = cells.get("E25");
                taxCell.formula = "E24*0.1";
                cells.get("B26").value = "Grand Total:";
                const grandTotalCell = cells.get("E26");
                grandTotalCell.formula = "E24+E25";
                // 合计值的粗体 + 货币样式
                const totalStyle = workbook.createStyle();
                totalStyle.font.isBold = true;
                totalStyle.custom = '"$"#,##0.00';
                subtotalCell.style = totalStyle;
                taxCell.style = totalStyle;
                grandTotalCell.style = totalStyle;
                // 合计标签的粗体样式
                const boldStyle = workbook.createStyle();
                boldStyle.font.isBold = true;
                cells.get("B24").style = boldStyle;
                cells.get("B25").style = boldStyle;
                cells.get("B26").style = boldStyle;
                // 将工作簿保存为 OFD 文件
                const outputData = workbook.save(AsposeCells.SaveFormat.Ofd);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "Invoice.ofd";
                downloadLink.style.display = "block";
                document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            } catch (error) {
                console.error(error);
                document.getElementById('result').innerHTML = '<p style="color: red;">An error occurred: ' + error.message + '</p>';
            }
        });
        </script>
    </body>
</html>
```

## **将现有 Excel 文件转换为 OFD**
Aspose.Cells 还可以从磁盘中加载现有 Excel 工作簿，并将其直接导出为 OFD 格式。这适用于批量转换流水线、归档工作流，以及源工作簿由其他工具生成、只需重新导出为固定版式文档的场景。以下示例加载现有的 `.xlsx` 工作簿，从其单元格读取数据，根据需要调整页面设置，并将结果保存为 OFD 文档。

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8" />
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
        <script src="aspose.cells.js.min.js"></script>
        <script type="text/javascript">
            const { Workbook, CellsHelper } = AsposeCells;
            const fileInput = document.getElementById("fileInput");
            const runButton = document.getElementById("runExample");
            const downloadLink = document.getElementById("downloadLink");
            const result = document.getElementById("result");
            const readyPromise = AsposeCells.onReady({
                license: "/lic/aspose.cells.enc",
                fontPath: "/fonts/",
                fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
            }).then(() => {
                console.log("Aspose.Cells initialized");
            });
            function formatTimestamp(date) {
                const pad = value => String(value).padStart(2, "0");
                return date.getFullYear() + "-" +
                    pad(date.getMonth() + 1) + "-" +
                    pad(date.getDate()) + " " +
                    pad(date.getHours()) + ":" +
                    pad(date.getMinutes()) + ":" +
                    pad(date.getSeconds());
            }
            function escapeHtml(value) {
                const entities = {
                    "&": "&amp;",
                    "<": "&lt;",
                    ">": "&gt;",
                    '"': "&quot;",
                    "'": "&#39;"
                };
                return String(value).replace(/[&<>"']/g, character => entities[character]);
            }
            runButton.addEventListener("click", async () => {
                try {
                    const file = fileInput.files[0];
                    if (!file) {
                        result.innerHTML = '<p style="color: red;">Please select an Excel file first.</p>';
                        return;
                    }
                    runButton.disabled = true;
                    downloadLink.style.display = "none";
                    downloadLink.removeAttribute("href");
                    // 从磁盘打开现有的 Excel 工作簿
                    const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                    // (1) 读取并显示选定单元格的值，以确认文件已加载
                    const firstSheet = workbook.worksheets.get(0);
                    const cells = firstSheet.cells;
                    const output = [];
                    output.push("First sheet name: " + firstSheet.name);
                    output.push("Cell A1: " + cells.get("A1").stringValue);
                    output.push("Cell B1: " + cells.get("B1").stringValue);
                    output.push("Cell C1: " + cells.get("C1").stringValue);
                    // (2) 遍历 Worksheets 集合以枚举可用工作表
                    output.push("");
                    output.push("Available worksheets:");
                    for (let i = 0; i < workbook.worksheets.count; i++) {
                        const ws = workbook.worksheets.get(i);
                        output.push("  [" + i + "] " + ws.name);
                    }
                    // (3) 可选择更新一个时间戳单元格以反映转换情况
                    cells.get("A1").value = "Converted on: " + formatTimestamp(new Date());
                    // 在数据块顶部追加摘要标题行
                    cells.insertRow(0);
                    cells.get("A1").value = "Conversion Summary";
                    cells.get("A2").value = "Generated: " + formatTimestamp(new Date());
                    // (4) 配置工作表的 PageSetup 属性
                    const pageSetup = firstSheet.pageSetup;
                    pageSetup.orientation = AsposeCells.PageOrientationType.Landscape;
                    pageSetup.paperSize = AsposeCells.PaperSizeType.PaperA4;
                    pageSetup.fitToPagesTall = 1;
                    pageSetup.fitToPagesWide = 1;
                    // (5) 可选择为 OFD 输出设置打印区域
                    const lastRow = cells.maxDataRow;
                    const lastCol = cells.maxDataColumn;
                    const lastColLetter = CellsHelper.columnIndexToName(lastCol);
                    const printArea = "A1:" + lastColLetter + (lastRow + 1);
                    pageSetup.printArea = printArea;
                    output.push("");
                    output.push("Print area set to: " + printArea);
                    // (6) 将工作簿保存为 OFD 文件
                    const outputData = workbook.save(AsposeCells.SaveFormat.Ofd);
                    const blob = new Blob([outputData]);
                    downloadLink.href = URL.createObjectURL(blob);
                    downloadLink.download = "SampleBook.ofd";
                    downloadLink.textContent = "Download SampleBook.ofd";
                    downloadLink.style.display = "block";
                    output.push("");
                    output.push("File successfully converted to OFD format: SampleBook.ofd");
                    result.innerHTML =
                        '<pre style="white-space: pre-wrap;">' +
                        escapeHtml(output.join("\n")) +
                        "</pre>" +
                        '<p style="color: green;">Done! Click the download link to get the result file.</p>';
                } catch (error) {
                    console.error(error);
                    const message = error && error.message ? error.message : String(error);
                    result.innerHTML = '<p style="color: red;">Error: ' + escapeHtml(message) + "</p>";
                } finally {
                    runButton.disabled = false;
                }
            });
        </script>
    </body>
</html>
```

## **相关文章**

{{< app/cells/assistant language="javascript-cpp" >}}