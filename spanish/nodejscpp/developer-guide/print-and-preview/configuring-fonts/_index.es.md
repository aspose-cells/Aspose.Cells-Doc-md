---
title: Configurar fuentes para renderizar hojas de cálculo con Node.js a través de C++
linktitle: Configuración de fuentes para la representación de hojas de cálculo
type: docs
weight: 10
url: /es/nodejs-cpp/configuring-fonts-for-rendering-spreadsheets/
description: Aprende cómo configurar fuentes para renderizar hojas de cálculo usando Aspose.Cells for Node.js via C++. Asegúrate de que las fuentes estén disponibles para una fidelidad óptima de conversión.
---

## **Escenarios de uso posibles**

Las APIs de Aspose.Cells ofrecen la facilidad de renderizar las hojas de cálculo en formatos de imagen así como convertirlas a formatos PDF y XPS. Para maximizar la fidelidad de conversión, es necesario que las fuentes usadas en la hoja de cálculo estén disponibles en el directorio de fuentes predeterminado del sistema operativo. En caso de que las fuentes requeridas no estén presentes, las APIs de Aspose.Cells intentarán sustituir las fuentes requeridas por otras disponibles.

## **Selección de Fuentes**

A continuación se presenta el proceso que las API de Aspose.Cells siguen detrás de escena.

1. La API intenta encontrar las fuentes en el sistema de archivos que coincidan con el nombre de fuente exacto utilizado en la hoja de cálculo.
2. Si la API no puede encontrar las fuentes con el nombre exacto, intenta utilizar la fuente predeterminada especificada en la propiedad [**DefaultStyle.getFont()**](https://reference.aspose.com/cells/nodejs-cpp/style/#getFont--) del libro de trabajo.
3. Si la API no puede localizar la fuente definida en la propiedad [**DefaultStyle.getFont()**](https://reference.aspose.com/cells/nodejs-cpp/style/#getFont--) del libro de trabajo, intenta usar la fuente especificada en la propiedad [**PdfSaveOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getDefaultFont--) o [**ImageOrPrintOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getDefaultFont--).
4. Si la API no puede localizar la fuente definida en las propiedades [**PdfSaveOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getDefaultFont--) o [**ImageOrPrintOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getDefaultFont--), intenta usar la fuente especificada en la propiedad [**FontConfigs.getDefaultFontName()**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs/#getDefaultFontName--).
5. Si la API no puede localizar la fuente definida en la propiedad [**FontConfigs.getDefaultFontName()**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs/#getDefaultFontName--), intenta seleccionar las fuentes más adecuadas de todas las fuentes disponibles.
6. Por último, si la API no puede encontrar ninguna fuente en el sistema de archivos, representa la hoja de cálculo utilizando Arial.

## **Establecer Carpetas de Fuentes Personalizadas**

Las APIs de Aspose.Cells buscan en el directorio de fuentes predeterminado del sistema operativo las fuentes requeridas. En caso de que las fuentes necesarias no estén disponibles en el directorio de fuentes del sistema, las APIs buscarán en los directorios personalizados (definidos por el usuario). La clase [**FontConfigs**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs) ha expuesto varias formas de establecer directorios personalizados de fuentes, detalladas a continuación.

1. [**FontConfigs.setFontFolder(string, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs/#setFontFolder-string-boolean-): Este método es útil si solo hay una carpeta que se va a establecer.
2. [**FontConfigs.setFontFolders(string[], boolean)**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs/#setFontFolders-stringarray-boolean-): Este método es útil cuando las fuentes residen en varias carpetas y el usuario desea establecer todas las carpetas por separado en lugar de combinar todas las fuentes en una sola carpeta.
3. [**FontConfigs.setFontSources(FontSourceBase[])**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs/#setFontSources-fontsourcebasearray-): Este mecanismo es útil cuando el usuario desea cargar fuentes desde varias carpetas o un solo archivo de fuente o datos de fuente de un array de bytes.

{{% alert color="primary" %}}

Ambos métodos [**FontConfigs.setFontFolder(string, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs/#setFontFolder-string-boolean-) y [**FontConfigs.setFontFolders(string[], boolean)**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs/#setFontFolders-stringarray-boolean-) aceptan un segundo parámetro de tipo Boolean. Pasar **true** como segundo parámetro dirigirá a las API de Aspose.Cells a buscar subcarpetas para los archivos de fuentes.

{{% /alert %}}

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Defining string variables to store paths to font folders & font file
const fontFolder1 = path.join(dataDir, "Arial");
const fontFolder2 = path.join(dataDir, "Calibri");
const fontFile = path.join(dataDir, "arial.ttf"); 

// Setting first font folder with SetFontFolder method
// Second parameter directs the API to search the subfolders for font files
AsposeCells.FontConfigs.setFontFolder(fontFolder1, true);

// Setting both font folders with SetFontFolders method
// Second parameter prohibits the API to search the subfolders for font files
AsposeCells.FontConfigs.setFontFolders([fontFolder1, fontFolder2], false);

// Defining FolderFontSource
const sourceFolder = new AsposeCells.FolderFontSource(fontFolder1, false);

// Defining FileFontSource
const sourceFile = new AsposeCells.FileFontSource(fontFile);

// Defining MemoryFontSource
const sourceMemory = new AsposeCells.MemoryFontSource(require("fs").readFileSync(fontFile));

// Setting font sources
AsposeCells.FontConfigs.setFontSources([sourceFolder, sourceFile, sourceMemory]);
```

{{% alert color="primary" %}}

Por favor, utilice cualquiera de los métodos mencionados anteriormente al iniciar la aplicación, es decir, antes de invocar otros objetos de las APIs de Aspose.Cells.

{{% /alert %}} {{% alert color="primary" %}}

Si se utilizan todos los métodos mencionados anteriormente para establecer las fuentes, solo los últimos ajustes tendrán efecto.

{{% /alert %}}

## **Mecanismo de Sustitución de Fuentes**

Las APIs de Aspose.Cells también brindan la capacidad de especificar la fuente de sustitución para fines de renderizado. Este mecanismo es útil cuando una fuente requerida no está disponible en la máquina donde se realiza la conversión. Los usuarios pueden proporcionar una lista de nombres de fuentes como alternativa a la fuente originalmente requerida. Para lograr esto, las APIs de Aspose.Cells han exponido el método [**FontConfigs.setFontSubstitutes(string, string[])**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs/#setFontSubstitutes-string-stringarray-), que acepta 2 parámetros. El primer parámetro es de tipo **string**, que debe ser el nombre de la fuente a sustituir. El segundo parámetro es un arreglo de tipo **string**, donde los usuarios pueden proporcionar una lista de nombres de fuentes como sustitución del nombre de fuente original (especificado en el primer parámetro).

Aquí hay un escenario de uso simple.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Substituting the Arial font with Times New Roman & Calibri
AsposeCells.FontConfigs.setFontSubstitutes("Arial", ["Times New Roman", "Calibri"]);
```

## **Recopilación de información**

Además de los métodos mencionados anteriormente, las APIs de Aspose.Cells también proporcionan medios para recopilar información sobre qué fuentes y sustituciones se han establecido.

1. El método [**FontConfigs.getFontSources()**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs/#getFontSources--) devuelve un arreglo de tipo [**FontSourceBase**](https://reference.aspose.com/cells/nodejs-cpp/fontsourcebase) que contiene la lista de fuentes especificadas. En caso de que no se hayan establecido fuentes, el método [**FontConfigs.getFontSources()**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs/#getFontSources--) devolverá un arreglo vacío.
1. El método [**FontConfigs.getFontSubstitutes(string)**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs/#getFontSubstitutes-string-) acepta un parámetro de tipo **string**, permitiendo especificar el nombre de la fuente para la cual se ha establecido una sustitución. En caso de que no se haya establecido una sustitución para la fuente especificada, el método [**FontConfigs.getFontSubstitutes(string)**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs/#getFontSubstitutes-string-) devolverá null.

## **Temas avanzados**
- [Establecer la fuente predeterminada al renderizar la hoja de cálculo a imágenes](/cells/es/nodejs-cpp/set-default-font-while-rendering-spreadsheet-to-images/)
- [Establecer la propiedad DefaultFont de PdfSaveOptions e ImageOrPrintOptions para tener prioridad](/cells/es/nodejs-cpp/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/)
- [Formatos de fuente soportados](/cells/es/nodejs-cpp/supported-font-formats/)
- [Hoja de cálculo a imagen - Establecer formato de píxel para la imagen renderizada](/cells/es/nodejs-cpp/worksheet-to-image-set-pixel-format-for-the-rendered-image/)
{{< app/cells/assistant language="nodejs-cpp" >}}
