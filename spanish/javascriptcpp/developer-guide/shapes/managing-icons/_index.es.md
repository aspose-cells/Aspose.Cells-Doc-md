---
title: Agregar iconos a la hoja de cálculo con JavaScript vía C++
linktitle: Gestionar iconos
type: docs
weight: 100
url: /es/javascript-cpp/insert-svg-to-excel/
---

## Agregar iconos a la hoja de cálculo en Aspose.Cells for JavaScript vía C++

Si necesita usar [Aspose.Cells](https://products.aspose.com/cells/) para agregar 'iconos' en un archivo de Excel, este documento puede ofrecerle ayuda.

La interfaz de Excel correspondiente a la operación de insertar icono es la siguiente:

![](1.png)

- Seleccione la posición del icono a insertar en la hoja de cálculo
- Haga clic izquierdo *Insertar*->*Iconos*
- En la ventana que se abre, seleccione el icono en el rectángulo rojo en la figura anterior
- Haz clic izquierdo en *Insertar*, se insertará en el archivo de Excel.

El efecto es el siguiente:

![](2.png)

Aquí, hemos preparado *código de ejemplo* para ayudarte a insertar íconos usando [Aspose.Cells](https://products.aspose.com/cells/). También hay un [archivo de ejemplo](sample.xlsx) y un [archivo de recursos](icon.zip). Usamos la interfaz de Excel para insertar un ícono con el mismo efecto visual que el [archivo de recursos](icon.zip) en el [archivo de ejemplo](sample.xlsx).

### JavaScript

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Add Icon to Worksheet Example</h1>
        <p>Select an Excel file and an SVG icon file, then click "Run Example".</p>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <input type="file" id="iconInput" accept=".svg" />
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
            const iconInput = document.getElementById('iconInput');
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }
            if (!iconInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an SVG icon file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const iconFile = iconInput.files[0];

            const arrayBuffer = await file.arrayBuffer();
            const iconArrayBuffer = await iconFile.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet from the collection
            const sheet = workbook.worksheets.get(0);

            // Add the icon to the worksheet
            const iconBytes = new Uint8Array(iconArrayBuffer);
            sheet.shapes.addIcons(3, 0, 7, 0, 100, 100, iconBytes, null);

            // Set a prompt message
            const c = sheet.cells.get(8, 7);
            c.value = "Insert via Aspose.Cells";
            const s = c.style;
            s.font.color = Color.Blue;
            c.style = s;

            // Save and prepare download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'sample2.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Icon added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

Cuando ejecute el código anterior en su proyecto, obtendrá los siguientes resultados:

![](3.png)
