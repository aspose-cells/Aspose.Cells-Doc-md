---
title: 通过JavaScript via C++配置渲染电子表格的字体
linktitle: 配置字体以渲染电子表格
type: docs
weight: 10
url: /zh/javascript-cpp/configuring-fonts-for-rendering-spreadsheets/
description: 学习使用Aspose.Cells for JavaScript通过C++配置字体以渲染电子表格。确保字体可用以实现最佳转换效果。
---

## **可能的使用场景**

Aspose.Cells API提供渲染电子表格为图片格式，以及转换为PDF和XPS格式的功能。为了最大化转换的准确性，必须确保电子表格中使用的字体已在操作系统的默认字体目录中。如果缺少所需字体，Aspose.Cells API将尝试用可用的字体进行替代。

## **选择字体**

以下是 Aspose.Cells API 在幕后执行的过程。

1. API试图在文件系统中找到与电子表格中使用的确切字体名称匹配的字体。
1. 如果API无法找到具有相同名称的精确字体，则尝试使用工作簿的[**DefaultStyle.font**](https://reference.aspose.com/cells/javascript-cpp/style/#font--)属性下指定的默认字体。
1. 如果API无法找到工作簿的[**DefaultStyle.font**](https://reference.aspose.com/cells/javascript-cpp/style/#font--)属性下定义的字体，则尝试使用[**PdfSaveOptions.defaultFont**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#defaultFont--)或[**ImageOrPrintOptions.defaultFont**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/#defaultFont--)属性下指定的字体。
1. 如果API无法找到[**PdfSaveOptions.defaultFont**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#defaultFont--)或[**ImageOrPrintOptions.defaultFont**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/#defaultFont--)属性下定义的字体，则尝试使用[**FontConfigs.defaultFontName**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs/#defaultFontName--)属性下指定的字体。
1. 如果API无法找到[**FontConfigs.defaultFontName**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs/#defaultFontName--)属性下定义的字体，则尝试从所有可用字体中选择最合适的字体。
1. 最后，如果API在文件系统中找不到任何字体，则使用Arial呈现电子表格。

## **设置自定义字体文件夹**

Aspose.Cells API在操作系统的默认字体目录中搜索所需字体。如未找到，API会在自定义（用户定义）目录中搜索。[**FontConfigs**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs)类提供了多种设置自定义字体目录的方法。

1. [**FontConfigs.fontFolder(string, boolean)**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs/#fontFolder-string-boolean-)：如果只有一个要设置的文件夹，则此方法很有用。
1. [**FontConfigs.fontFolders(string[], boolean)**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs/#fontFolders-stringarray-boolean-)：当字体存在于多个文件夹中，而用户希望将所有文件夹分开设置而不是将所有字体合并到一个文件夹中时，此方法很有用。
1. [**FontConfigs.fontSources(FontSourceBase[])**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs/#fontSources-fontsourcebasearray-)：当用户希望从多个文件夹加载字体或从字节数组加载单个字体文件或字体数据时，此机制很有用。

{{% alert color="primary" %}}

Both [**FontConfigs.fontFolder(string, boolean)**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs/#fontFolder-string-boolean-) 和 [**FontConfigs.fontFolders(string[], boolean)**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs/#fontFolders-stringarray-boolean-) 方法接受一个布尔类型的第二个参数。 将 **true** 作为第二个参数传递将指示 Aspose.Cells API 在子文件夹中搜索字体文件。

{{% /alert %}}

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Font Configuration Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Font Configuration Example</h1>
        <p>Select an Excel file (optional) and font resources to configure Aspose.Cells font sources in the browser.</p>

        <label>Excel File (optional):</label>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <br/><br/>

        <label>Font File (.ttf/.otf) (optional):</label>
        <input type="file" id="fontFileInput" accept=".ttf,.otf" />
        <br/><br/>

        <label>Font Folder (optional, select a folder):</label>
        <input type="file" id="fontFolderInput" webkitdirectory directory multiple />
        <br/><br/>

        <button id="runExample">Configure Fonts</button>
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
            const fontFileInput = document.getElementById('fontFileInput');
            const fontFolderInput = document.getElementById('fontFolderInput');
            const resultDiv = document.getElementById('result');

            // Basic validation: ensure at least one font resource is provided (file or folder)
            if (!fontFileInput.files.length && !fontFolderInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select at least one font file or a font folder.</p>';
                return;
            }

            // Defining string variables to store paths/names to font folders & font file
            // (In browser environment we use simple names or uploaded file names)
            const fontFolder1 = "Arial";
            const fontFolder2 = "Calibri";
            const fontFile = "arial.ttf";

            // Setting first font folder (converted from setFontFolder)
            AsposeCells.FontConfigs.fontFolder = fontFolder1;
            // Preserve the subfolder-search flag from original API call as a separate property
            AsposeCells.FontConfigs.fontFolderSearchSubFolders = true;

            // Setting both font folders (converted from setFontFolders)
            AsposeCells.FontConfigs.fontFolders = [fontFolder1, fontFolder2];
            // Preserve the subfolder-search flag as a separate property
            AsposeCells.FontConfigs.fontFoldersSearchSubFolders = false;

            // Defining FolderFontSource
            const sourceFolder = new AsposeCells.FolderFontSource(fontFolder1, false);

            // Defining FileFontSource
            const sourceFile = new AsposeCells.FileFontSource(fontFile);

            // Defining MemoryFontSource
            let memoryFontBytes = new Uint8Array([]);
            if (fontFileInput.files.length) {
                const ff = fontFileInput.files[0];
                const arrayBuffer = await ff.arrayBuffer();
                memoryFontBytes = new Uint8Array(arrayBuffer);
            } else if (fontFolderInput.files.length) {
                // If a folder was provided, try to find a .ttf/.otf inside it and use the first found
                const files = Array.from(fontFolderInput.files);
                const fontCandidate = files.find(f => f.name.toLowerCase().endsWith('.ttf') || f.name.toLowerCase().endsWith('.otf'));
                if (fontCandidate) {
                    const arrayBuffer = await fontCandidate.arrayBuffer();
                    memoryFontBytes = new Uint8Array(arrayBuffer);
                }
            }
            const sourceMemory = new AsposeCells.MemoryFontSource(memoryFontBytes);

            // Setting font sources (converted from setFontSources)
            AsposeCells.FontConfigs.fontSources = [sourceFolder, sourceFile, sourceMemory];

            // Provide feedback to the user
            resultDiv.innerHTML = '<p style="color: green;">Font configuration applied successfully.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}

请在应用程序启动时使用以上任一方法，在调用 Aspose.Cells API 的其他对象之前使用。

{{% /alert %}} {{% alert color="primary" %}}

如果使用所有上述方法设置字体源，则只有最后一次设置将生效。

{{% /alert %}}

## **字体替换机制**

Aspose.Cells API还提供了指定替代字体以便渲染的能力。当目标机器上没有所需字体时，此机制非常有用。用户可以提供一份字体名称列表作为替代。为实现此功能，Aspose.Cells API提供了接受两个参数的[**FontConfigs.fontSubstitutes(string, string[])**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs/#fontSubstitutes-string-stringarray-)方法，第一个参数为**string**类型，表示需要替代的字体名称，第二个参数为**string**数组，列出作为原字体替代的字体名称。

这里是一个简单的使用场景。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Example Title</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
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

            // Instantiating a Workbook object by opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Substituting the Arial font with Times New Roman & Calibri
            // Converted from: AsposeCells.FontConfigs.setFontSubstitutes("Arial", ["Times New Roman", "Calibri"]);
            AsposeCells.FontConfigs.fontSubstitutes = { "Arial": ["Times New Roman", "Calibri"] };

            // Saving the (possibly modified) workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the processed file.</p>';
        });
    </script>
</html>
```

## **信息收集**

除上述方法外，Aspose.Cells API还提供了收集已设置的源和替代信息的方式。

 1. [**FontConfigs.fontSources**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs/#fontSources--)方法返回一个包含指定字体源列表的[**FontSourceBase**](https://reference.aspose.com/cells/javascript-cpp/fontsourcebase)类型数组。如果未设置任何源，[**FontConfigs.fontSources**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs/#fontSources--)方法将返回空数组。
 1. [**FontConfigs.fontSubstitutes(string)**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs/#fontSubstitutes-string-)方法接受一个**string**类型的参数，可以用来指定已设置替代的字体名。如未为该字体名设置替代，则[**FontConfigs.fontSubstitutes(string)**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs/#fontSubstitutes-string-)方法返回null。

## **高级主题**
- [在将电子表格呈现为图像时设置默认字体](/cells/zh/javascript-cpp/set-default-font-while-rendering-spreadsheet-to-images/)
- [设置 PdfSaveOptions 和 ImageOrPrintOptions 的 DefaultFont 属性具有优先级](/cells/zh/javascript-cpp/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/)
- [支持的字体格式](/cells/zh/javascript-cpp/supported-font-formats/)
- [电子表格转图像 - 设置呈现图像的像素格式](/cells/zh/javascript-cpp/worksheet-to-image-set-pixel-format-for-the-rendered-image/)
