---
title: Configuring Fonts for Rendering Spreadsheets with JavaScript via C++
linktitle: Configuring Fonts for Rendering Spreadsheets
type: docs
weight: 10
url: /javascript-cpp/configuring-fonts-for-rendering-spreadsheets/
description: Learn how to configure fonts for rendering spreadsheets using Aspose.Cells for JavaScript via C++. Ensure fonts are available for optimal conversion fidelity.
---

## **Possible Usage Scenarios**

Aspose.Cells APIs provide the facility to render the spreadsheets in image formats as well as convert them to PDF & XPS formats. In order to maximize the conversion fidelity, it is necessary that the fonts used in the spreadsheet should be available in the operating system's default font directory. In case the required fonts are not present, then the Aspose.Cells APIs will try to substitute the required fonts with the ones available.

## **Selection of Fonts**

Below is the process that Aspose.Cells APIs follow behind the scenes.

1. The API tries to find the fonts on the file system matching the exact font name used in the spreadsheet.  
2. If the API cannot find the fonts with the exact same name, it attempts to use the default font specified under the Workbook's [**DefaultStyle.font**](https://reference.aspose.com/cells/javascript-cpp/style/#font--) property.  
3. If the API cannot locate the font defined under the workbook's [**DefaultStyle.font**](https://reference.aspose.com/cells/javascript-cpp/style/#font--) property, it attempts to use the font specified under [**PdfSaveOptions.defaultFont**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#defaultFont--) or [**ImageOrPrintOptions.defaultFont**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/#defaultFont--) property.  
4. If the API cannot locate the font defined under [**PdfSaveOptions.defaultFont**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#defaultFont--) or [**ImageOrPrintOptions.defaultFont**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/#defaultFont--) property, it attempts to use the font specified under [**FontConfigs.defaultFontName**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs/#defaultFontName--) property.  
5. If the API cannot locate the font defined under [**FontConfigs.defaultFontName**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs/#defaultFontName--) property, it attempts to select the most suitable fonts from all of the available fonts.  
6. Finally, if the API cannot find any fonts on the file system, it renders the spreadsheet using Arial.

## **Set Custom Font Folders**

Aspose.Cells APIs search the operating system's default font directory for the required fonts. In case the required fonts are not available in the system's font directory, then the APIs search through the custom (user-defined) directories. The [**FontConfigs**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs) class has exposed a number of ways to set custom font directories as detailed below.

1. [**FontConfigs.fontFolder(string, boolean)**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs/#fontFolder-string-boolean-): This method is useful if there is only one folder to be set.  
2. [**FontConfigs.fontFolders(string[], boolean)**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs/#fontFolders-stringarray-boolean-): This method is useful when the fonts reside in multiple folders and the user wishes to set all folders separately rather than combining all fonts in a single folder.  
3. [**FontConfigs.fontSources(FontSourceBase[])**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs/#fontSources-fontsourcebasearray-): This mechanism is useful when the user wishes to load fonts from multiple folders or a single font file or font data from an array of bytes.

{{% alert color="primary" %}}

Both [**FontConfigs.fontFolder(string, boolean)**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs/#fontFolder-string-boolean-) & [**FontConfigs.fontFolders(string[], boolean)**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs/#fontFolders-stringarray-boolean-) methods accept a Boolean second parameter. Passing **true** as the second parameter will direct the Aspose.Cells APIs to search the subfolders for the font files.

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

Please use any of the above‑mentioned methods at the start of the application, that is, before invoking any other objects of Aspose.Cells APIs.

{{% /alert %}} {{% alert color="primary" %}}

If all of the above‑mentioned methods are used to set the font sources, only the last settings will take effect.

{{% /alert %}}

## **Font Substitution Mechanism**

Aspose.Cells APIs also provide the ability to specify a substitute font for rendering purposes. This mechanism is helpful when a required font is not available on the machine where conversion has to take place. Users can provide a list of font names as an alternative to the originally required font. In order to achieve this, the Aspose.Cells APIs have exposed the [**FontConfigs.fontSubstitutes(string, string[])**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs/#fontSubstitutes-string-stringarray-) method, which accepts two parameters. The first parameter is a **string** that should be the name of the font to be substituted. The second parameter is an array of **strings** representing alternative font names.

Here is a simple usage scenario.

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

## **Information Gathering**

In addition to the above‑mentioned methods, the Aspose.Cells APIs have also provided means to gather information on what sources and substitutions have been set.

1. The [**FontConfigs.fontSources**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs/#fontSources--) method returns an array of type [**FontSourceBase**](https://reference.aspose.com/cells/javascript-cpp/fontsourcebase) containing the list of specified font sources. In case no sources have been set, the method will return an empty array.  
2. The [**FontConfigs.fontSubstitutes(string)**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs/#fontSubstitutes-string-) method accepts a **string** parameter that specifies the font name for which substitution has been set. If no substitution has been set for the specified font name, the method will return `null`.

## **Advanced topics**
- [Set Default Font while rendering spreadsheet to images](/cells/javascript-cpp/set-default-font-while-rendering-spreadsheet-to-images/)
- [Set DefaultFont property of PdfSaveOptions and ImageOrPrintOptions to have priority](/cells/javascript-cpp/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/)
- [Supported Font Formats](/cells/javascript-cpp/supported-font-formats/)
- [Worksheet to Image - Set Pixel Format for the Rendered Image](/cells/javascript-cpp/worksheet-to-image-set-pixel-format-for-the-rendered-image/)