---
title: Verificar que el valor de la celda cumple con las reglas de validación de datos
type: docs
weight: 210
url: /es/javascript-cpp/verify-that-cell-value-satisfies-data-validation-rules/
description: Aprende cómo verificar si el valor de la celda satisface las reglas de validación de datos a través de la API Aspose.Cells for JavaScript vía C++.
keywords: Obtener Valor de Validación de Celda JavaScript vía C++, Obtener Valor de Validación de Celda JavaScript vía C++, Verificar si un valor cumple con las reglas de validación de datos aplicadas a la celda JavaScript vía C++
---

{{% alert color="primary" %}} 

Microsoft Excel permite a los usuarios agregar reglas de validación de datos a las celdas. Por ejemplo, una validación decimal especifica que solo se pueden ingresar números entre 10 y 20. Si un usuario ingresa un número diferente, Excel muestra un mensaje de error y solicita ingresar un número en el rango correcto. Si copias y pegas un número, por ejemplo 3, en la celda, Excel no realiza una verificación de validación ni muestra un mensaje de error.

A veces, es necesario verificar si un valor cumple con las reglas de validación de datos aplicadas a la celda programáticamente. En el caso anterior, por ejemplo, la entrada debería fallar.

{{% /alert %}} 
## **Introducción**
Aspose.Cells for JavaScript vía C++ proporciona la propiedad [Cell.validationValue](https://reference.aspose.com/cells/javascript-cpp/cell/#validationValue--) para validar valores de celda programáticamente. Si el valor en una celda no cumple con la regla de validación de datos aplicada a esa celda, devuelve **false**, de lo contrario, **true**.

El siguiente ejemplo de código ilustra cómo funciona la propiedad [Cell.validationValue](https://reference.aspose.com/cells/javascript-cpp/cell/#validationValue--). Primero, ingresa el valor 3 en C1. Debido a que esto no satisface la regla de validación de datos, la propiedad [Cell.validationValue](https://reference.aspose.com/cells/javascript-cpp/cell/#validationValue--) devuelve **false**. Luego, ingresa el valor 15 en C1. Debido a que este valor satisface la regla de validación de datos, la propiedad [Cell.validationValue](https://reference.aspose.com/cells/javascript-cpp/cell/#validationValue--) devuelve **true**. De manera similar, devuelve **false** para el valor 30.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Validation Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Validation Example</h1>
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
            const resultDiv = document.getElementById('result');
            resultDiv.innerHTML = '';

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access Cell C1
            // Cell C1 has the Decimal Validation applied on it.
            // It can take only the values Between 10 and 20
            const cell = worksheet.cells.get("C1");

            // Enter 3 inside this cell (not between 10 and 20)
            cell.value = 3;

            // Check if number 3 satisfies the Data Validation rule applied on this cell
            const valid3 = cell.validationValue;
            console.log("Is 3 a Valid Value for this Cell: " + valid3);
            resultDiv.innerHTML += `<p>Is 3 a Valid Value for this Cell: ${valid3}</p>`;

            // Enter 15 inside this cell (between 10 and 20)
            cell.value = 15;

            // Check if number 15 satisfies the Data Validation rule applied on this cell
            const valid15 = cell.validationValue;
            console.log("Is 15 a Valid Value for this Cell: " + valid15);
            resultDiv.innerHTML += `<p>Is 15 a Valid Value for this Cell: ${valid15}</p>`;

            // Enter 30 inside this cell (not between 10 and 20)
            cell.value = 30;

            // Check if number 30 satisfies the Data Validation rule applied on this cell
            const valid30 = cell.validationValue;
            console.log("Is 30 a Valid Value for this Cell: " + valid30);
            resultDiv.innerHTML += `<p>Is 30 a Valid Value for this Cell: ${valid30}</p>`;
        });
    </script>
</html>
```


### **Salida**
{{< highlight javascript >}}

 Is 3 a Valid Value for this Cell: false

Is 15 a Valid Value for this Cell: true

Is 30 a Valid Value for this Cell: false

{{< /highlight >}}
