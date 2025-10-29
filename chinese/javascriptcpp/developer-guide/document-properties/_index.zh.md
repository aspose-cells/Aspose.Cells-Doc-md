---
title: 使用 C++ 的 JavaScript 管理文档属性
linktitle: 文档属性
type: docs
weight: 80
url: /zh/javascript-cpp/managing-document-properties/
description: 学习如何通过 C++ API 管理文档属性。
keywords: 如何用 C++ 的 JavaScript 管理文档属性，获取或设置文档属性，使用 C++ 添加或删除文档属性，插入或移除文档属性，如何使用 C++ API 访问文档属性。
---

## **介绍**

Microsoft Excel提供了向电子表格文件添加属性的功能。这些文档属性提供有用信息，分为以下2类。

- 系统定义（内置）属性：内置属性包含有关文档的一般信息，如文档标题、作者姓名、文档统计信息等。
- 用户定义（自定义）属性：最终用户以名称-值对的形式定义的自定义属性。

{{% alert color="primary" %}}

关于内建属性和自定义属性，最重要的一点是内建属性可以被访问和修改，但不能被创建或移除。然而，自定义属性可以被创建和管理。

{{% /alert %}}

## **如何使用Microsoft Excel管理文档属性**

Microsoft Excel允许以WYSIWYG方式管理Excel文件的文档属性。请按照以下步骤在Excel 2016中打开**属性**对话框。

1. 从**文件**菜单中选择**信息**。

|**选择信息菜单**|
| :- |
|![todo:image_alt_text](managing-document-properties_1.png)|
1. 点击**属性**标题并选择"高级属性"。

|**单击高级属性选择**|
| :- |
|![todo:image_alt_text](managing-document-properties_2.png)|
1. 管理文件的文档属性。

|**属性对话框**|
| :- |
|![todo:image_alt_text](managing-document-properties_3.png)|
在属性对话框中，有不同的选项卡，如常规、摘要、统计、内容和自定义。每个选项卡都可以帮助配置文件相关的不同信息。自定义选项卡用于管理自定义属性。

## **如何使用Aspose.Cells处理文档属性**

开发人员可以使用Aspose.Cells API动态管理文档属性。此功能帮助开发人员存储有用信息，如文件接收时间、处理时间戳等。

{{% alert color="primary" %}}

 C++ 版的 Script 直接在输出文件中写入 API 和版本信息。例如，在导出 PDF 时，Script 会将 **Application** 字段填充为 'Aspose.Cells'，**PDF 生产者** 字段为例如 'Aspose.Cells v17.9'。

请注意，不能指示 C++ 版的 Script 从输出文档中更改或删除此信息。

{{% /alert %}}

### **如何访问文档属性**

Aspose.Cells API支持内置和自定义两种类型的文档属性。Aspose.Cells的[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)类代表Excel文件，类似Excel文件，[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)类可以包含多个工作表，每个由[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)类表示，而工作表集合由[**WorksheetCollection**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection)类表示。

使用[**WorksheetCollection**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection)访问文件的文档属性，如下所示。

- 要访问内建文档属性，请使用[**WorksheetCollection.builtInDocumentProperties()**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection/#builtInDocumentProperties--)。
- 要访问自定义文档属性，请使用[**WorksheetCollection.customDocumentProperties()**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection/#customDocumentProperties--)。

[**WorksheetCollection.builtInDocumentProperties()**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection/#builtInDocumentProperties--)和[**WorksheetCollection.customDocumentProperties()**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection/#customDocumentProperties--)都返回[**Aspose.Cells.Properties.DocumentPropertyCollection**](https://reference.aspose.com/cells/javascript-cpp/documentpropertycollection/)的实例。该集合包含[**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/javascript-cpp/documentproperty/)对象，每个对象代表一个内置或自定义文档属性。

应用程序需求决定如何访问属性，即通过索引或属性名，比如在下面的示例中演示。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Document Properties</title>
    </head>
    <body>
        <h1>Document Properties Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Load Document Properties</button>
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
            const resultEl = document.getElementById('result');
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                resultEl.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object and opening the Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Retrieve a list of all custom document properties of the Excel file
            const customProperties = workbook.customDocumentProperties;

            // Accessing a custom document property by using the property name
            const customProperty1 = customProperties.get("ContentTypeId");
            // Accessing the same custom document property by using the property index
            const customProperty2 = customProperties.get(0);

            const outputs = [];
            if (customProperty1) {
                outputs.push(`<p>${customProperty1.name} ${customProperty1.value}</p>`);
            }
            if (customProperty2) {
                outputs.push(`<p>${customProperty2.name} ${customProperty2.value}</p>`);
            }
            if (!outputs.length) {
                resultEl.innerHTML = '<p style="color: orange;">No custom document properties found.</p>';
            } else {
                resultEl.innerHTML = outputs.join('');
            }
        });
    </script>
</html>
```

[**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/javascript-cpp/documentproperty/)类允许检索文档属性的名称、值和类型：

- 要获取属性名称，请使用[**DocumentProperty.name()**](https://reference.aspose.com/cells/javascript-cpp/documentproperty/#name--)。
- 要获取属性值，使用[**DocumentProperty.value()**](https://reference.aspose.com/cells/javascript-cpp/documentproperty/#value--)。[**DocumentProperty.value()**](https://reference.aspose.com/cells/javascript-cpp/documentproperty/#value--)返回值作为对象。
- 要获取属性类型，使用[**DocumentProperty.type()**](https://reference.aspose.com/cells/javascript-cpp/documentproperty/#type--)。这返回[**PropertyType**](https://reference.aspose.com/cells/javascript-cpp/propertytype/)枚举值之一。当你获取属性类型后，可以使用**DocumentProperty.ToXXX**方法获得相应类型的值，而不是使用[**DocumentProperty.value()**](https://reference.aspose.com/cells/javascript-cpp/documentproperty/#value--)。**DocumentProperty.ToXXX**方法在下表中描述。

{{% alert color="primary" %}}

[**DocumentProperty**](https://reference.aspose.com/cells/javascript-cpp/documentproperty/)类还提供一组方法，返回其他数据类型的值。

{{% /alert %}}

|**成员名称**|**描述**|**ToXXX方法**|
| :- | :- | :- |
|Boolean|属性数据类型为布尔值|ToBool|
|Date|属性数据类型为日期时间。请注意，Microsoft Excel仅存储日期部分，无法在此类型的自定义属性中存储时间|ToDateTime|
|Float|属性数据类型为双精度浮点数|ToDouble|
|Number|属性数据类型为Int32|ToInt|
|String|属性数据类型为字符串|ToString|

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Retrieve Custom Document Properties Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell } = AsposeCells;

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
            resultDiv.innerHTML = '';

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate a Workbook object by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Retrieve a list of all custom document properties of the Excel file
            const customProperties = workbook.customDocumentProperties;

            let outputHtml = '<h2>Custom Document Properties</h2>';

            // Accessing a custom document property (first)
            const customProperty1 = customProperties.get(0);
            if (customProperty1) {
                // Storing the value of the document property as an object
                const objectValue = customProperty1.value;
                outputHtml += `<p><strong>${customProperty1.name}</strong> (type: ${customProperty1.type}) : ${objectValue}</p>`;
            } else {
                outputHtml += '<p>No first custom property found.</p>';
            }

            // Accessing a custom document property (second)
            const customProperty2 = customProperties.get(1);
            if (customProperty2) {
                // Checking the type of the document property and then storing the value according to that type
                if (customProperty2.type === AsposeCells.PropertyType.String) {
                    const value = customProperty2.value.toString();
                    outputHtml += `<p>${customProperty2.name} : ${value}</p>`;
                } else {
                    outputHtml += `<p>${customProperty2.name} (type: ${customProperty2.type}) : ${customProperty2.value}</p>`;
                }
            } else {
                outputHtml += '<p>No second custom property found.</p>';
            }

            resultDiv.innerHTML = outputHtml;
        });
    </script>
</html>
```

### **如何添加或删除自定义文档属性**

正如我们在本主题开头所述的那样，开发人员无法添加或删除内置属性，因为这些属性是系统定义的，但可以添加或删除自定义属性，因为这些是用户定义的。

### **如何添加自定义属性**

Aspose.Cells API已暴露[**add(string, string)**](https://reference.aspose.com/cells/javascript-cpp/customdocumentpropertycollection/#add-string-string-)方法，用于向集合中添加自定义属性。[**add(string, string)**](https://reference.aspose.com/cells/javascript-cpp/customdocumentpropertycollection/#add-string-string-)方法将属性添加到Excel文件中，并返回新文档属性的引用，为[**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/javascript-cpp/documentproperty/)对象。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Add Custom Document Property</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
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

            document.getElementById('runExample').addEventListener('click', async () => {
                const fileInput = document.getElementById('fileInput');
                if (!fileInput.files.length) {
                    document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                    return;
                }

                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();

                // Instantiating a Workbook object and opening the Excel file
                const workbook = new Workbook(new Uint8Array(arrayBuffer));

                // Retrieve a list of all custom document properties of the Excel file
                const customProperties = workbook.customDocumentProperties;

                // Adding a custom document property to the Excel file
                customProperties.add("Publisher", "Aspose");

                // Saving the modified Excel file
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = 'out_sample-document-properties.xlsx';
                downloadLink.style.display = 'block';
                downloadLink.textContent = 'Download Modified Excel File';

                document.getElementById('result').innerHTML = '<p style="color: green;">Custom property added successfully! Click the download link to get the modified file.</p>';
            });
        });
    </script>
</html>
```

### **如何配置'链接到内容'自定义属性**

要创建一个与给定范围内容关联的自定义属性，请调用[**CustomDocumentPropertyCollection.addLinkToContent(string, string)**](https://reference.aspose.com/cells/javascript-cpp/customdocumentpropertycollection/#addLinkToContent-string-string-)方法并传递属性名和源。可以通过[**DocumentProperty.isLinkedToContent()**](https://reference.aspose.com/cells/javascript-cpp/documentproperty/#isLinkedToContent--)属性检查是否将属性配置为与内容关联。此外，也可以使用[**source()**](https://reference.aspose.com/cells/javascript-cpp/documentproperty/#source--)属性和[**DocumentProperty**](https://reference.aspose.com/cells/javascript-cpp/documentproperty/)类获取源范围。

我们在示例中使用了一个简单的模板Microsoft Excel文件。工作簿有一个命名范围标记为**MyRange**，它指向单元格值。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Custom Document Properties</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
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
            const resultEl = document.getElementById('result');
            if (!fileInput.files.length) {
                resultEl.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate a Workbook by loading the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Retrieve a list of all custom document properties of the Excel file
            const customProperties = workbook.worksheets.customDocumentProperties;

            // Add link to content.
            customProperties.addLinkToContent("Owner", "MyRange");

            // Accessing the custom document property by using the property name
            const customProperty1 = customProperties.get("Owner");

            // Check whether the property is linked to content
            const isLinkedToContent = customProperty1.isLinkedToContent;

            // Get the source for the property
            const source = customProperty1.source;

            // Save the file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out_sample-document-properties.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultEl.innerHTML = `<p style="color: green;">Operation completed successfully! Property linked: ${isLinkedToContent}. Source: ${source}. Click the download link to get the modified file.</p>`;
        });
    </script>
</html>
```

### **如何移除自定义属性**

要使用Aspose.Cells删除自定义属性，请调用[**DocumentPropertyCollection.remove(string)**](https://reference.aspose.com/cells/javascript-cpp/documentpropertycollection/#remove-string-)方法并传递要删除的文档属性名称。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Remove Custom Document Property Example</title>
    </head>
    <body>
        <h1>Remove Custom Document Property Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
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

            // Instantiate a Workbook object by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Retrieve a list of all custom document properties of the Excel file
            const customProperties = workbook.customDocumentProperties;

            // Removing a custom document property named "Publisher"
            customProperties.remove("Publisher");

            // Save the file and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out_sample-document-properties.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Custom property removed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **高级主题**
- [在文档信息面板中可见的自定义属性](/cells/zh/javascript-cpp/adding-custom-properties-visible-inside-document-information-panel/)
- [设置内置文档属性的ScaleCrop和LinksUpToDate属性](/cells/zh/javascript-cpp/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/)
- [使用内置文档属性指定Excel文件的文档版本](/cells/zh/javascript-cpp/specify-document-version-of-the-excel-file-using-builtin-document-properties/)
- [使用内置文档属性指定Excel文件的语言](/cells/zh/javascript-cpp/specify-the-language-of-the-excel-file-using-builtin-document-properties/)
