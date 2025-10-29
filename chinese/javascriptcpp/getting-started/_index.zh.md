---
title: 入门
type: docs
weight: 5
url: /zh/javascript-cpp/getting-started/
keywords: "Excel,浏览器,无服务器,XLS,XLSX,XLSB,CSV,PDF,JPG,PNG,HTML,ODS,XLSM,电子表格, Markdown,XPS,DOCX,PPTX,MHTML,SVG,JSON,SQL,XML"
description: "通过 C++ 设置 Aspose.Cells for JavaScript 的安装指南和配置."
---

## **产品描述**
Aspose.Cells for JavaScript 通过 C++ 是一款高性能、功能丰富的电子表格操作和转换库，支持 Excel（XLS, XLSX, XLSB, XLSM）、ODS、CSV 和 HTML 格式。它提供了一套全面的功能，用于在浏览器和 Node.js 环境中创建、编辑、转换和渲染电子表格。完全支持所有主要的 Excel 格式，确保在不同场景中的最大兼容性和灵活性。
采用 WebAssembly 构建，实现近原生性能，直接在浏览器中运行，Aspose.Cells for JavaScript via C++ 能实现快速高效的电子表格处理，无需服务器。其轻量级的运行时使其非常适合需要高级 Excel 功能的无服务器 Web 应用。无论你是在构建仪表盘、数据处理流程还是文档生成工具，Aspose.Cells for JavaScript via C++ 都提供了完整、可靠且高性能的解决方案。其支持浏览器和 Node.js，主要用于浏览器。

## **主要特性**
1. **文件创建与编辑：** 从零创建新电子表格或轻松编辑现有电子表格。这包括添加或修改数据、单元格格式、管理工作表等。
1. **数据处理：** 执行复杂的数据操作，如排序、筛选和验证。库还支持高级公式和函数，以便数据分析和计算。
1. **文件转换：** 将Excel文件转换为PDF、HTML、ODS及图片格式（如PNG和JPEG），方便分享和分发数据。
1. **图表与图形：** 创建和定制各种图表和图形以直观显示数据，支持条形图、折线图、饼图等以及设计和布局的定制选项。
1. **渲染与打印：** 将Excel工作表渲染为高品质图像和PDF，确保显示效果准确，支持打印布局和格式控制。
1. **高级保护与安全：** 用密码保护电子表格、加密文件、管理访问权限，确保数据安全和完整性。
1. **性能与扩展性：** 设计用于高效处理大型数据集和复杂电子表格，确保高性能和企业级应用的扩展能力。


## **先决条件**

开始使用前，请确保你已具备：
- 在你的系统上安装了 Node.js（可以从 https://nodejs.org/ 下载）
- 拥有有效的 Aspose 许可文件（例如 Aspose.Total.lic、Aspose.Cells.lic 或 aspose.cells.js.lic）以获得完整功能
- HTML 和 JavaScript 的基础知识

## **第 1 步：安装**

### 安装 Aspose.Cells for JavaScript

创建一个新的项目目录并安装包：

{{< highlight bash >}}
# Create a new project directory
mkdir my-excel-project
cd my-excel-project

# Install Aspose.Cells for JavaScript
npm install aspose.cells.js
{{< /highlight >}}

### 安装 HTTP 服务器（许可证设置必需）

全局安装一个简单的 HTTP 服务器：

{{< highlight bash >}}
npm install -g http-server
{{< /highlight >}}

或者使用 Python 内置服务器（如果已安装 Python）：
{{< highlight bash >}}
# Python 3
python -m http.server

# Python 2
python -m SimpleHTTPServer
{{< /highlight >}}

## **第 2 步：许可证设置（完整功能所需）**

### 加密您的许可证文件

1. **在您的项目目录中启动 HTTP 服务器**：
   {{< highlight bash >}}
   http-server -p 8080
   {{< /highlight >}}

2. **在浏览器中打开许可证加密工具**：
   ```
   http://localhost:8080/node_modules/aspose.cells.js/encrypt_lic.html
   ```

3. **上传您的许可证文件**：
   - 点击 “选择文件” 并选择您的许可证文件（如 `Aspose.Total.lic`、`Aspose.Cells.lic` 或 `aspose.cells.js.lic`）
   - 加密过程会自动完成（非常快）

4. **下载加密后的许可证**：
   - 点击 “下载已处理文件” 下载 `aspose.cells.enc`
   - 将此文件保存到您的项目目录

### 放置加密许可证

将 `aspose.cells.enc` 文件移动到您的项目根目录或应用可以访问的特定文件夹中。

## **第 3 步：使用示例**

### 浏览器使用方法

在你的项目目录中创建一个 `index.html` 文件：

{{< highlight html >}}
<!DOCTYPE html>
<html>
<head>
    <title>Aspose.Cells Browser Example</title>
</head>
<body>
    <h1>Excel Processing with Aspose.Cells</h1>
    <button id="createExcel">Create Excel File</button>
    <div id="output"></div>

    <script src="./node_modules/aspose.cells.js/aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, FileFormatType, SaveFormat } = AsposeCells;

        // Initialize with license (optional, remove for trial mode)
        AsposeCells.onReady({
            license: "aspose.cells.enc"  // Path to your encrypted license
        }).then(() => {
            console.log("Aspose.Cells is ready!");

            document.getElementById('createExcel').onclick = function() {
                // Create a new workbook
                var workbook = new Workbook(FileFormatType.Xlsx);

                // Get the first worksheet
                var worksheet = workbook.worksheets.get(0);

                // Add some data
                worksheet.cells.get("A1").putValue("Hello World");
                worksheet.cells.get("A2").putValue("Created with Aspose.Cells for JavaScript");
                worksheet.cells.get("B1").putValue(42);

                // Save as Excel file
                const outputData = workbook.save(SaveFormat.Xlsx);

                // Create download link
                const blob = new Blob([outputData]);
                const downloadLink = document.createElement('a');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.textContent = 'Download Excel File';
                downloadLink.download = "my-excel-file.xlsx";
                downloadLink.style.display = 'block';

                const output = document.getElementById('output');
                output.innerHTML = '';
                output.appendChild(downloadLink);
            };
        }).catch(error => {
            console.error("Error initializing Aspose.Cells:", error);
        });
    </script>
</html>
{{< /highlight >}}

**运行浏览器示例：**

{{< highlight bash >}}
# Start HTTP server
http-server -p 8080

# Open browser and visit:
# http://localhost:8080
{{< /highlight >}}

### Node.js 使用方法

创建一个 `node-example.js` 文件：

{{< highlight javascript >}}
const { AsposeCells, Workbook, SaveFormat, FileFormatType } = require("aspose.cells.js");
const fs = require('fs');

// Initialize Aspose.Cells with license
AsposeCells.onReady({
    license: "aspose.cells.enc",  // Path to your encrypted license
    fontPath: "./fonts/"         // Optional: path to system fonts
}).then(() => {
    console.log("Aspose.Cells initialized successfully!");

    // Create a new workbook
    const workbook = new Workbook(FileFormatType.Xlsx);

    // Get the first worksheet
    const worksheet = workbook.worksheets.get(0);

    // Add data to cells
    worksheet.cells.get("A1").putValue("Product");
    worksheet.cells.get("B1").putValue("Price");
    worksheet.cells.get("A2").putValue("Apple");
    worksheet.cells.get("B2").putValue(1.99);
    worksheet.cells.get("A3").putValue("Orange");
    worksheet.cells.get("B3").putValue(2.49);

    // Save as Excel file
    const excelData = workbook.save(SaveFormat.Xlsx);
    fs.writeFileSync('output.xlsx', Buffer.from(excelData));
    console.log('Excel file saved as output.xlsx');

    // Save as PDF
    const pdfData = workbook.save(SaveFormat.Pdf);
    fs.writeFileSync('output.pdf', Buffer.from(pdfData));
    console.log('PDF file saved as output.pdf');

}).catch(error => {
    console.error("Error:", error);
});
{{< /highlight >}}

**运行 Node.js 示例：**

{{< highlight bash >}}
node node-example.js
{{< /highlight >}}

## **常用文件操作**

### 读取现有 Excel 文件

{{< highlight javascript >}}
// Browser (using File input)
const fileInput = document.getElementById('fileInput');
fileInput.addEventListener('change', (e) => {
    const file = e.target.files[0];
    const reader = new FileReader();
    reader.onload = (e) => {
        const arrayBuffer = e.target.result;
        const workbook = new Workbook(new Uint8Array(arrayBuffer));
        // Process the workbook...
    };
    reader.readAsArrayBuffer(file);
});

// Node.js
const fs = require('fs');
const fileBuffer = fs.readFileSync('input.xlsx');
const workbook = new Workbook(fileBuffer);
{{< /highlight >}}

### 格式转换

{{< highlight javascript >}}
// Convert Excel to PDF
const pdfData = workbook.save(SaveFormat.Pdf);

// Convert Excel to HTML
const htmlData = workbook.save(SaveFormat.Html);

// Convert Excel to CSV
const csvData = workbook.save(SaveFormat.Csv);

// Convert Excel to JSON
const jsonData = workbook.save(SaveFormat.Json);
{{< /highlight >}}

## **故障排查**

### 常见问题与解决方案

1. **"未找到模块" 错误**
   - 确保你从正确的目录运行HTTP服务器
   - 验证脚本 src 路径指向正确的位置

2. **许可证无法使用**
   - 确保 `aspose.cells.enc` 文件在正确的位置
   - 检查加密许可证文件是否生成正确
   - 验证原始许可证文件有效且未过期

3. **浏览器中的CORS问题**
   - 一直使用HTTP服务器，切勿直接打开HTML文件
   - 使用 `http-server` 或类似工具进行本地开发

### 获取帮助

如果遇到问题：
- 查看 [Aspose.Cells 文档](https://docs.aspose.com/cells/javascript-cpp/)
- 访问 [Aspose 论坛](https://forum.aspose.com/c/cells/9) 获取社区支持
- 联系 Aspose 支持并提供您的许可证信息

## **下一步**

- 探索 [API 参考](https://reference.aspose.com/cells/javascript-cpp/) 获取详细文档
- 了解图表、公式和格式等高级功能
- 查看文档中的更多示例和教程
- 考虑与现有的Web应用或构建工具集成
