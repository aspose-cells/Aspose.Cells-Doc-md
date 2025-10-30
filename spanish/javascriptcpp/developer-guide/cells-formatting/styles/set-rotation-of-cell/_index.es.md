---
title: Cómo rotar el texto de la celda
linktitle: Cómo rotar el texto de la celda  
type: docs  
weight: 80  
url: /es/javascript-cpp/how-to-rotate-text-of-cell/  
description: Aprende cómo rotar el texto de una celda programáticamente usando Aspose.Cells for JavaScript vía C++.  
keywords: JavaScript vía C++ rotar texto de la celda, rotar texto de la celda en un libro de trabajo programáticamente en JavaScript, establecer programáticamente el ángulo de rotación de la celda en el libro, JavaScript cómo rotar el texto de la celda en Excel  
---

## **Rotar texto de la celda en Aspose.Cells for JavaScript vía C++**

Aspose.Cells es un componente potente de JavaScript que permite a los desarrolladores trabajar con hojas de cálculo de Excel programáticamente. Una de las funciones proporcionadas por Aspose.Cells es la capacidad de rotar celdas, permitiéndote personalizar la orientación del texto y mejorar la presentación visual de tus datos. En este documento, exploraremos cómo rotar celdas usando Aspose.Cells.

## **Cómo rotar el texto de la celda en Excel**
Para rotar una celda en Excel, puedes seguir los siguientes pasos:
1. Abre Excel y selecciona la celda o rango de celdas que deseas rotar.
1. Haz clic derecho en la(s) celda(s) seleccionada(s) y elige "Formato de celdas" en el menú contextual. Alternativamente, puedes ir a la pestaña "Inicio" en la cinta de Excel, hacer clic en el menú desplegable "Formato" en el grupo "Celdas" y seleccionar "Formato de celdas".
1. En el cuadro de diálogo "Formato de celdas", ve a la pestaña "Alineación".
1. En la sección "Orientación", verás las opciones para rotar el texto. Puedes ingresar directamente el ángulo de rotación deseado en grados en el cuadro "Grados". Los valores positivos rotan el texto en sentido contrario a las agujas del reloj, y los valores negativos lo rotan en sentido de las agujas del reloj.
<br>
![todo:image_alt_text](alignment.png)
1. Una vez que hayas seleccionado la rotación deseada, haz clic en "Aceptar" para aplicar los cambios. La(s) celda(s) seleccionada(s) ahora se rotarán según el ángulo de rotación u orientación elegido.

## **Cómo rotar el texto de la celda utilizando la API Aspose.Cells**

La propiedad [**Style.rotationAngle(number)**](https://reference.aspose.com/cells/javascript-cpp/style/#rotationAngle-number-) hace que sea conveniente rotar celdas. Para rotar celdas en Aspose.Cells, debes seguir estos pasos:
1. Cargar el libro de trabajo de Excel  
<br>
Primero, necesitas cargar el libro de Excel usando Aspose.Cells. Puedes usar la clase Workbook para abrir un archivo de Excel existente o crear uno nuevo. 

1. Accede a la hoja de cálculo  
<br>
Una vez cargado el libro de trabajo, necesitas acceder a la hoja de cálculo donde quieres rotar las celdas. Puedes acceder a la hoja de cálculo por su índice o nombre. 

1. Rota el texto de la celda  
<br>
Ahora que tienes acceso a la hoja de cálculo, puedes rotar las celdas modificando el objeto Style de las celdas deseadas. El objeto Style te permite establecer varias opciones de formato, incluida la rotación. 

1. Guarda el libro de trabajo  
<br>
Después de rotar las celdas, puedes guardar el libro de trabajo modificado en un archivo o flujo usando el método Save.

## **Código de ejemplo en JavaScript**

Por favor, vea el siguiente código, crea un objeto de libro de trabajo y establece diferentes ángulos de rotación para varias celdas. La captura de pantalla muestra el resultado después de la ejecución del código de ejemplo.
<br>
<img src="rotation.png" width=80% />

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Rotate Text in Cells Example</h1>
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
            // Creating a new Workbook (blank)
            const workbook = new Workbook();

            // Obtaining the reference of the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Row index of the cell
            let row = 0;
            // Column index of the cell
            let column = 0; 

            let a1 = worksheet.cells.get(row, column);
            a1.putValue("a1 rotate text");
            let a1Style = a1.style;

            // Set the rotation angle in degrees
            a1Style.rotationAngle = 45; 
            a1.style = a1Style;

            // set Column index of the cell
            column = 1;
            let b1 = worksheet.cells.get(row, column);
            b1.putValue("b1 rotate text");
            let b1Style = b1.style;

            // Set the rotation angle in degrees
            b1Style.rotationAngle = 255;
            b1.style = b1Style;

            // set Column index of the cell
            column = 2;
            let c1 = worksheet.cells.get(row, column);
            c1.putValue("c1 rotate text");
            let c1Style = c1.style;

            // Set the rotation angle in degrees
            c1Style.rotationAngle = -90;
            c1.style = c1Style;

            // set Column index of the cell
            column = 3;
            let d1 = worksheet.cells.get(row, column);
            d1.putValue("d1 rotate text");
            let d1Style = d1.style;

            // Set the rotation angle in degrees
            d1Style.rotationAngle = -90;
            d1.style = d1Style;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
