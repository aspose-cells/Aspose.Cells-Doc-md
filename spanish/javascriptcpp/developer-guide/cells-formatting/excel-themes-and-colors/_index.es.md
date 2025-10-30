---
title: Temas y colores de Excel
linktitle: Temas y colores de Excel  
type: docs  
weight: 100  
url: /es/javascript-cpp/excel-themes-and-colors/  
description: Aprende a usar esquemas de color personalizados con Script Aspose.Cells for Java vía C++.  
keywords: JavaScript Crear y Aplicar Esquemas de Color, Crear un Esquema de Color Personalizado programáticamente en JavaScript, Cómo aplicar programáticamente un Esquema de Color Personalizado en JavaScript, Cómo usar Esquema de Color en Excel en JavaScript  
---

## **Cómo aplicar y crear un esquema de colores en Excel**  
Los temas de documento facilitan la coordinación de colores, fuentes y efectos de formato gráfico de los documentos de Excel y su actualización rápida.  
Los temas proporcionan una apariencia unificada con estilos nombrados, efectos gráficos y otros objetos utilizados en un libro de trabajo. Por ejemplo, el estilo Accent1 se ve diferente en los temas Office y Apex. A menudo, aplicas un tema de documento y luego lo modificas según tus necesidades.  

### **Cómo aplicar un esquema de colores en Excel**  
1. Abre Excel y ve a la pestaña "Diseño de página" en la cinta de opciones de Excel.  
1. Haz clic en el botón "Colores" en la sección de "Temas".  
<br>  
<img src="color.png" width=70% />  
1. Elige una paleta de colores que se ajuste a tus requisitos o pasa el cursor sobre un esquema para ver una vista previa en vivo.  

### **Cómo crear un esquema de colores personalizado en Excel**  
Puedes crear tu propio conjunto de colores para darle a tu documento un aspecto fresco y único o cumplir con los estándares de marca de tu organización.  

1. Abre Excel y ve a la pestaña "Diseño de página" en la cinta de opciones de Excel.  
1. Haz clic en el botón "Colores" en la sección de "Temas".  
1. Haz clic en el botón "Personalizar colores...".  
<br>  
<img src="color2.png" width=70% />  

1. En el cuadro de diálogo "Crear nuevos colores de tema", puedes seleccionar colores para cada elemento haciendo clic en las listas desplegables de colores junto a ellos. Puedes elegir colores de la paleta o definir colores personalizados usando la opción "Más colores".  
<br>  
<img src="color3.png" width=70% />  
1. Después de seleccionar todos los colores deseados, proporciona un nombre para tu esquema de colores personalizado en el campo de "Nombre".  

1. Haz clic en el botón "Guardar" para guardar tu esquema de colores personalizado. Ahora tu esquema de colores personalizado estará disponible en el menú desplegable de "Colores" para uso futuro.  

## **Cómo crear y aplicar un esquema de colores en Aspose.Cells**  
Aspose.Cells proporciona funciones para personalizar temas y colores.  

### **Cómo crear un tema de colores personalizado en Aspose.Cells**  
Si se usan colores de tema en el archivo, no es necesario modificar cada celda individualmente; solo hay que modificar los colores en el tema.  

El siguiente ejemplo muestra cómo aplicar temas personalizados con tus colores deseados. Usamos un archivo de plantilla de ejemplo creado manualmente en Microsoft Excel 2007.  

El siguiente ejemplo carga un archivo de plantilla XLSX, define colores para diferentes tipos de colores de tema, aplica los colores personalizados y guarda el archivo de Excel.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Apply Custom Theme Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Color } = AsposeCells;

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

            // Instantiating a Workbook object by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Define Color array (of 12 colors) for Theme.
            const carr = [
                new Color("AntiqueWhite"), // Background1
                new Color("Brown"), // Text1
                new Color("AliceBlue"), // Background2
                new Color("Yellow"), // Text2
                new Color("YellowGreen"), // Accent1
                new Color("Red"), // Accent2
                new Color("Pink"), // Accent3
                new Color("Purple"), // Accent4
                new Color("PaleGreen"), // Accent5
                new Color("Orange"), // Accent6
                new Color("Green"), // Hyperlink
                new Color("Gray") // Followed Hyperlink
            ];

            // Set the custom theme with specified colors.
            workbook.customTheme("CustomeTheme1", carr);

            // Save as the excel file.
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Custom theme applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```



### **Cómo aplicar colores de tema en Aspose.Cells**  
El siguiente ejemplo aplica los colores de primer plano y fuente de una celda según los tipos de colores del tema predeterminado (del libro). También guarda el archivo de Excel en disco.  


```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
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
            // Instantiate a Workbook.
            const workbook = new Workbook();

            // Get cells collection in the first (default) worksheet.
            const cells = workbook.worksheets.get(0).cells;

            // Get the D3 cell.
            const c = cells.get("D3");

            // Get the style of the cell.
            const s = c.style;

            // Set foreground color for the cell from the default theme Accent2 color.
            s.foregroundThemeColor = new AsposeCells.ThemeColor(AsposeCells.ThemeColorType.Accent2, 0.5);

            // Set the pattern type.
            s.pattern = AsposeCells.BackgroundType.Solid;

            // Get the font for the style.
            const f = s.font;

            // Set the theme color.
            f.themeColor = new AsposeCells.ThemeColor(AsposeCells.ThemeColorType.Accent4, 0.1);

            // Apply style.
            c.style = s;

            // Put a value.
            c.value = "Testing1";

            // Save the excel file and provide download link.
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created. Click the download link to save the file.</p>';
        });
    </script>
</html>
```


### **Cómo obtener y establecer colores de tema en Aspose.Cells**  
A continuación se presentan algunos métodos y propiedades que implementan los colores de tema.  

- [**Style.foregroundThemeColor**](https://reference.aspose.com/cells/javascript-cpp/style/#foregroundThemeColor-themecolor-): Se usa para establecer el color de primer plano.  
- [**Style.backgroundThemeColor**](https://reference.aspose.com/cells/javascript-cpp/style/#backgroundThemeColor-themecolor-): Se usa para establecer el color de fondo.  
- [**Font.themeColor**](https://reference.aspose.com/cells/javascript-cpp/font/#themeColor-themecolor-): Se usa para establecer el color de fuente.  
- [**Workbook.themeColor**](https://reference.aspose.com/cells/javascript-cpp/workbook/#themeColor-themecolortype-): Se usa para obtener un color de tema.  
- [**Workbook.themeColor**](https://reference.aspose.com/cells/javascript-cpp/workbook/#themeColor-themecolortype-color-): Se usa para establecer un color de tema.  

El siguiente ejemplo muestra cómo obtener y establecer colores de tema.  

El siguiente ejemplo usa un archivo de plantilla XLSX, obtiene los colores para diferentes tipos de colores de tema, cambia los colores y guarda el archivo de Microsoft Excel.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Theme Color Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Color, ThemeColorType } = AsposeCells;

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

            // Instantiating a Workbook object and opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the Background1 theme color.
            let c = workbook.themeColor(ThemeColorType.Background1);
            console.log("theme color Background1: ", c);

            // Get the Accent2 theme color.
            c = workbook.themeColor(ThemeColorType.Accent2);
            console.log("theme color Accent2: ", c);

            // Change the Background1 theme color.
            workbook.themeColor(ThemeColorType.Background1, Color.Red);

            // Get the updated Background1 theme color.
            c = workbook.themeColor(ThemeColorType.Background1);
            console.log("theme color Background1 changed to: ", c);

            // Change the Accent2 theme color.
            workbook.themeColor(ThemeColorType.Accent2, Color.Blue);

            // Get the updated Accent2 theme color.
            c = workbook.themeColor(ThemeColorType.Accent2);
            console.log("theme color Accent2 changed to: ", c);

            // Saving the updated file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Updated Excel File';

            // Display results
            let resultHtml = '';
            resultHtml += `<p>theme color Background1: ${JSON.stringify(workbook.themeColor(ThemeColorType.Background1))}</p>`;
            resultHtml += `<p>theme color Accent2: ${JSON.stringify(workbook.themeColor(ThemeColorType.Accent2))}</p>`;
            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! See console for detailed logs.</p>' + resultHtml;
        });
    </script>
</html>
```


## **Temas avanzados**  
- [Extraer datos de tema del archivo de Excel](/cells/es/javascript-cpp/extract-theme-data-from-excel-file/)
