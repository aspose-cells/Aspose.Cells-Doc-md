---
title: Establecer borde de rango con JavaScript mediante C++
linktitle: Establecer Borde de Rango
type: docs
weight: 600
url: /es/javascript-cpp/set-range-border/
---

## **Escenarios de uso posibles**  
 Cuando desees establecer el borde para un rango, no es necesario configurar cada celda individualmente. Puedes establecer el borde en todo el rango. Aspose.Cells for JavaScript mediante C++ ofrece esta función.  
 Este artículo proporciona un código de ejemplo que usa Aspose.Cells for JavaScript mediante C++ para establecer el borde del rango.  

## **Establecer borde de rango en Excel**  
Para establecer el borde de un rango en Excel, puedes seguir estos pasos:  
1. Selecciona el rango de celdas al que deseas aplicarle el borde.  
2. En la pestaña "Inicio" de la cinta, busca el grupo "Fuente".  
3. Dentro del grupo "Fuente", haz clic en el botón desplegable "Bordes".  
<br>  
<img src="border.png" />  
4. Elige el tipo de borde que deseas aplicar de las opciones en el menú desplegable. Puedes elegir entre estilos de borde preestablecidos o personalizar tu propio borde.  
5. Una vez que hayas seleccionado el estilo de borde deseado, el borde se aplicará al rango seleccionado de celdas.  

## ** Establecer borde de rango usando Aspose.Cells for JavaScript mediante C++**  
Este ejemplo muestra cómo:  

1. Crear un libro de trabajo.  
2. Agregar datos a las celdas en la primera hoja de trabajo.  
3. Crear un [**Range**](https://reference.aspose.com/cells/javascript-cpp/range).  
4. Establecer borde interior del rango.  
5. Establecer borde exterior del rango.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Create Workbook Example</h1>
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
            // Instantiate a new workbook
            const workbook = new Workbook();
            // Obtaining the reference of the newly added worksheet
            const ws = workbook.worksheets.get(0);
            const cells = ws.cells;

            // Setting the value to the cells
            let cell = cells.get("A1");
            cell.putValue("Fruit");
            cell = cells.get("B1");
            cell.putValue("Count");
            cell = cells.get("C1");
            cell.putValue("Price");

            cell = cells.get("A2");
            cell.putValue("Apple");
            cell = cells.get("A3");
            cell.putValue("Mango");
            cell = cells.get("A4");
            cell.putValue("Blackberry");
            cell = cells.get("A5");
            cell.putValue("Cherry");

            cell = cells.get("B2");
            cell.putValue(5);
            cell = cells.get("B3");
            cell.putValue(3);
            cell = cells.get("B4");
            cell.putValue(6);
            cell = cells.get("B5");
            cell.putValue(4);

            cell = cells.get("C2");
            cell.putValue(5);
            cell = cells.get("C3");
            cell.putValue(20);
            cell = cells.get("C4");
            cell.putValue(30);
            cell = cells.get("C5");
            cell.putValue(60);

            // Create a range (A1:C5).
            const range = cells.createRange("A1", "C5");

            // set inner border of range
            const innerColor = workbook.createCellsColor();
            innerColor.color = AsposeCells.Color.Red;
            range.insideBorders = {
                borderType: AsposeCells.BorderType.Vertical,
                cellBorderType: AsposeCells.CellBorderType.Thin,
                color: innerColor
            };
            innerColor.color = AsposeCells.Color.Green;
            range.insideBorders = {
                borderType: AsposeCells.BorderType.Horizontal,
                cellBorderType: AsposeCells.CellBorderType.Thin,
                color: innerColor
            };

            // set outer border of range
            const outerColor = workbook.createCellsColor();
            outerColor.color = AsposeCells.Color.Blue;
            range.outlineBorders = {
                cellBorderType: AsposeCells.CellBorderType.Thin,
                color: outerColor
            };

            // Saving the modified Excel file and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
