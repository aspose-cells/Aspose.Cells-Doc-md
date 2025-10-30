---
title: Utilizando Estilos Incorporados
linktitle: Utilizando Estilos Incorporados
type: docs
weight: 80
url: /es/javascript-cpp/using-built-in-styles/
description: Código JavaScript para usar estilos integrados de Excel con Aspose.Cells for JavaScript vía C++.
keywords: JavaScript usa estilos integrados de Excel, programa en JavaScript aplica estilos en el libro de trabajo de manera programática, aplica estilos en el libro de trabajo de manera programática, JavaScript aplica estilos integrados en Excel, JavaScript aplica estilos integrados en el libro de trabajo, código JavaScript para aplicar estilos integrados en el libro de trabajo de Excel, código JavaScript para aplicar estilos integrados en el libro de trabajo de Excel
---

{{% alert color="primary" %}}  
Aspose.Cells proporciona una vasta colección de estilos reutilizables para formatear una celda en un documento de hoja de cálculo. Podemos usar estilos incorporados en nuestro libro de trabajo y también crear estilos personalizados.  
{{% /alert %}}  

## **Cómo utilizar Estilos Incorporados**  

El método [**Workbook.createBuiltinStyle(BuiltinStyleType)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#createBuiltinStyle-builtinstyletype-) y la enumeración [**BuiltinStyleType**](https://reference.aspose.com/cells/javascript-cpp/builtinstyletype) hacen conveniente el uso de estilos incorporados. Aquí hay una lista de todos los posibles estilos incorporados:  

- TwentyPercentAccent1
- TwentyPercentAccent2
- TwentyPercentAccent3
- TwentyPercentAccent4
- TwentyPercentAccent5
- TwentyPercentAccent6
- FortyPercentAccent1
- FortyPercentAccent2
- FortyPercentAccent3
- FortyPercentAccent4
- FortyPercentAccent5
- FortyPercentAccent6
- SixtyPercentAccent1
- SixtyPercentAccent2
- SixtyPercentAccent3
- SixtyPercentAccent4
- SixtyPercentAccent5
- SixtyPercentAccent6
- Accent1
- Accent2
- Accent3
- Accent4
- Accent5
- Accent6
- Malo
- Cálculo
- CheckCell
- Coma
- Coma1
- Moneda
- Moneda1
- TextoExplicativo
- Bueno
- Encabezado1
- Encabezado2
- Encabezado3
- Encabezado4
- Hipervínculo
- EnlaceHypertextoSeguida
- Entrada
- CeldaVinculada
- Neutral
- Normal
- Nota
- Salida
- Porcentaje
- Título
- Total
- TextoDeAdvertencia
- NivelDeFila
- NivelDeColumna


## Código JavaScript para usar estilos incorporados  
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
        <a id="downloadLink1" style="display: none; margin-right: 10px;">Download Output.xlsx</a>
        <a id="downloadLink2" style="display: none;">Download Output.out.ods</a>
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

        document.getElementById('runExample').addEventListener('click', () => {
            // Creating a new Workbook
            const workbook = new Workbook();

            // Creating a built-in style (Title)
            const style = workbook.createBuiltinStyle(AsposeCells.BuiltinStyleType.Title);

            // Accessing first worksheet, its cells, and cell A1
            const worksheet = workbook.worksheets.get(0);
            const cell = worksheet.cells.get("A1");

            // Setting cell value and style (converted setter)
            cell.putValue("Aspose");
            cell.style = style;

            // Auto-fit column and row
            worksheet.autoFitColumn(0);
            worksheet.autoFitRow(0);

            // Save as XLSX
            const outputData1 = workbook.save(SaveFormat.Xlsx);
            const blob1 = new Blob([outputData1]);
            const downloadLink1 = document.getElementById('downloadLink1');
            downloadLink1.href = URL.createObjectURL(blob1);
            downloadLink1.download = 'Output.xlsx';
            downloadLink1.style.display = 'inline-block';
            downloadLink1.textContent = 'Download Output.xlsx';

            // Save as ODS
            const outputData2 = workbook.save(SaveFormat.Ods);
            const blob2 = new Blob([outputData2]);
            const downloadLink2 = document.getElementById('downloadLink2');
            downloadLink2.href = URL.createObjectURL(blob2);
            downloadLink2.download = 'Output.out.ods';
            downloadLink2.style.display = 'inline-block';
            downloadLink2.textContent = 'Download Output.out.ods';

            document.getElementById('result').innerHTML = '<p style="color: green;">Files generated. Click the download links to save them.</p>';
        });
    </script>
</html>
```
