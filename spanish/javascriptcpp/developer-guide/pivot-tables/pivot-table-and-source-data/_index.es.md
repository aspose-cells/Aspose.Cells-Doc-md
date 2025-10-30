---
title: Tabla dinámica y datos fuente
type: docs
weight: 30
url: /es/javascript-cpp/pivot-table-and-source-data/
---

## **Datos fuente de la tabla dinámica**

Hay momentos en los que deseas crear informes de Microsoft Excel con tablas dinámicas que toman datos de diferentes fuentes de datos (como una base de datos) que no se conocen en el momento del diseño. Este artículo proporciona un enfoque para cambiar dinámicamente la fuente de datos de una tabla dinámica.

### **Cambio de la fuente de datos de una tabla dinámica**

1. Crear una nueva plantilla de diseño.
   1. Crea un nuevo archivo de plantilla de diseñador como se muestra en la captura de pantalla a continuación.
   1. Luego define un rango nombrado, **DataSource**, que se refiere a este rango de celdas.

      **Creando una plantilla de diseñador y definiendo un rango nombrado, DataSource** 

![todo:image_alt_text](pivot-table-and-source-data_1.png)

1. Crear una tabla dinámica basada en este rango nombrado.
   1. En Microsoft Excel, elige **Datos**, luego **Tabla Dinámica** y **Informe de Tabla Dinámica**.
   1. Crear una tabla dinámica basada en el rango nombrado creado en el primer paso.

      **Creando una tabla dinámica basada en el rango nombrado, DataSource** 

![todo:image_alt_text](pivot-table-and-source-data_2.png)


   1. Arrastra el campo correspondiente a la fila y columna de la tabla dinámica, luego crea la tabla dinámica resultante como en la captura de pantalla a continuación.

   **Creando una tabla dinámica basada en un campo correspondiente** 

![todo:image_alt_text](pivot-table-and-source-data_3.png)


1. Haz clic derecho en la tabla dinámica y selecciona **Opciones de Tabla**.
   1. Marca **Actualizar al abrir** en la configuración de **Opciones de Datos**.

      **Configuración de las opciones de la tabla dinámica** 

![todo:image_alt_text](pivot-table-and-source-data_4.png)


Ahora, puedes guardar este archivo como tu archivo de plantilla de diseñador.

1. Poblar nuevos datos y cambiar la fuente de datos de una tabla dinámica.
   1. Una vez que se haya creado la plantilla de diseñador, utiliza el siguiente código para cambiar la fuente de datos de la tabla dinámica.

La ejecución del código de ejemplo a continuación cambia los datos fuente de la tabla dinámica.

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

            // Instantiating a Workbook object using uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Populating new data to the worksheet cells
            worksheet.cells.get("A9").value = "Golf";
            worksheet.cells.get("B9").value = "Qtr4";
            worksheet.cells.get("C9").value = 7000;

            // Changing named range "DataSource"
            const range = worksheet.cells.createRange(0, 0, 9, 3);
            range.name = "DataSource";

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
