---
title: Configuración de fuentes para renderizar hojas de cálculo con JavaScript vía C++
linktitle: Configuración de fuentes para la representación de hojas de cálculo
type: docs
weight: 10
url: /es/javascript-cpp/configuring-fonts-for-rendering-spreadsheets/
description: Aprende cómo configurar fuentes para renderizar hojas de cálculo usando Aspose.Cells for JavaScript vía C++. Asegúrate de que las fuentes estén disponibles para una fidelidad de conversión óptima.
---

## **Escenarios de uso posibles**

Las APIs de Aspose.Cells ofrecen la facilidad de renderizar las hojas de cálculo en formatos de imagen así como convertirlas a formatos PDF y XPS. Para maximizar la fidelidad de conversión, es necesario que las fuentes usadas en la hoja de cálculo estén disponibles en el directorio de fuentes predeterminado del sistema operativo. En caso de que las fuentes requeridas no estén presentes, las APIs de Aspose.Cells intentarán sustituir las fuentes requeridas por otras disponibles.

## **Selección de Fuentes**

A continuación se presenta el proceso que las API de Aspose.Cells siguen detrás de escena.

1. La API intenta encontrar las fuentes en el sistema de archivos que coincidan con el nombre de fuente exacto utilizado en la hoja de cálculo.
2. Si la API no puede encontrar las fuentes con el nombre exacto, intenta utilizar la fuente predeterminada especificada en la propiedad [**DefaultStyle.font**](https://reference.aspose.com/cells/javascript-cpp/style/#font--) del libro de trabajo.
3. Si la API no puede localizar la fuente definida en la propiedad [**DefaultStyle.font**](https://reference.aspose.com/cells/javascript-cpp/style/#font--) del libro de trabajo, intenta usar la fuente especificada en la propiedad [**PdfSaveOptions.defaultFont**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#defaultFont--) o [**ImageOrPrintOptions.defaultFont**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/#defaultFont--).
4. Si la API no puede localizar la fuente definida en las propiedades [**PdfSaveOptions.defaultFont**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#defaultFont--) o [**ImageOrPrintOptions.defaultFont**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/#defaultFont--), intenta usar la fuente especificada en la propiedad [**FontConfigs.defaultFontName**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs/#defaultFontName--).
5. Si la API no puede localizar la fuente definida en la propiedad [**FontConfigs.defaultFontName**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs/#defaultFontName--), intenta seleccionar las fuentes más adecuadas de todas las fuentes disponibles.
6. Por último, si la API no puede encontrar ninguna fuente en el sistema de archivos, representa la hoja de cálculo utilizando Arial.

## **Establecer Carpetas de Fuentes Personalizadas**

Las APIs de Aspose.Cells buscan en el directorio de fuentes predeterminado del sistema operativo las fuentes requeridas. En caso de que las fuentes necesarias no estén disponibles en el directorio de fuentes del sistema, las APIs buscarán en los directorios personalizados (definidos por el usuario). La clase [**FontConfigs**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs) ha expuesto varias formas de establecer directorios personalizados de fuentes, detalladas a continuación.

1. [**FontConfigs.fontFolder(string, boolean)**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs/#fontFolder-string-boolean-): Este método es útil si solo hay una carpeta que se va a establecer.
2. [**FontConfigs.fontFolders(string[], boolean)**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs/#fontFolders-stringarray-boolean-): Este método es útil cuando las fuentes residen en varias carpetas y el usuario desea establecer todas las carpetas por separado en lugar de combinar todas las fuentes en una sola carpeta.
3. [**FontConfigs.fontSources(FontSourceBase[])**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs/#fontSources-fontsourcebasearray-): Este mecanismo es útil cuando el usuario desea cargar fuentes desde varias carpetas o un solo archivo de fuente o datos de fuente de un array de bytes.

{{% alert color="primary" %}}

Ambos métodos [**FontConfigs.fontFolder(string, boolean)**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs/#fontFolder-string-boolean-) y [**FontConfigs.fontFolders(string[], boolean)**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs/#fontFolders-stringarray-boolean-) aceptan un segundo parámetro de tipo Boolean. Pasar **true** como segundo parámetro dirigirá a las API de Aspose.Cells a buscar subcarpetas para los archivos de fuentes.

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

Por favor, utilice cualquiera de los métodos mencionados anteriormente al iniciar la aplicación, es decir, antes de invocar otros objetos de las APIs de Aspose.Cells.

{{% /alert %}} {{% alert color="primary" %}}

Si se utilizan todos los métodos mencionados anteriormente para establecer las fuentes, solo los últimos ajustes tendrán efecto.

{{% /alert %}}

## **Mecanismo de Sustitución de Fuentes**

Las APIs de Aspose.Cells también brindan la capacidad de especificar la fuente de sustitución para fines de renderizado. Este mecanismo es útil cuando una fuente requerida no está disponible en la máquina donde se realiza la conversión. Los usuarios pueden proporcionar una lista de nombres de fuentes como alternativa a la fuente originalmente requerida. Para lograr esto, las APIs de Aspose.Cells han exponido el método [**FontConfigs.fontSubstitutes(string, string[])**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs/#fontSubstitutes-string-stringarray-), que acepta 2 parámetros. El primer parámetro es de tipo **string**, que debe ser el nombre de la fuente a sustituir. El segundo parámetro es un arreglo de tipo **string**, donde los usuarios pueden proporcionar una lista de nombres de fuentes como sustitución del nombre de fuente original (especificado en el primer parámetro).

Aquí hay un escenario de uso simple.

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

## **Recopilación de información**

Además de los métodos mencionados anteriormente, las APIs de Aspose.Cells también proporcionan medios para recopilar información sobre qué fuentes y sustituciones se han establecido.

1. El método [**FontConfigs.fontSources**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs/#fontSources--) devuelve un arreglo de tipo [**FontSourceBase**](https://reference.aspose.com/cells/javascript-cpp/fontsourcebase) que contiene la lista de fuentes especificadas. En caso de que no se hayan establecido fuentes, el método [**FontConfigs.fontSources**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs/#fontSources--) devolverá un arreglo vacío.
1. El método [**FontConfigs.fontSubstitutes(string)**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs/#fontSubstitutes-string-) acepta un parámetro de tipo **string**, permitiendo especificar el nombre de la fuente para la cual se ha establecido una sustitución. En caso de que no se haya establecido una sustitución para la fuente especificada, el método [**FontConfigs.fontSubstitutes(string)**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs/#fontSubstitutes-string-) devolverá null.

## **Temas avanzados**
- [Establecer la fuente predeterminada al renderizar la hoja de cálculo a imágenes](/cells/es/javascript-cpp/set-default-font-while-rendering-spreadsheet-to-images/)
- [Establecer la propiedad DefaultFont de PdfSaveOptions e ImageOrPrintOptions para tener prioridad](/cells/es/javascript-cpp/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/)
- [Formatos de fuente soportados](/cells/es/javascript-cpp/supported-font-formats/)
- [Hoja de cálculo a imagen - Establecer formato de píxel para la imagen renderizada](/cells/es/javascript-cpp/worksheet-to-image-set-pixel-format-for-the-rendered-image/)
