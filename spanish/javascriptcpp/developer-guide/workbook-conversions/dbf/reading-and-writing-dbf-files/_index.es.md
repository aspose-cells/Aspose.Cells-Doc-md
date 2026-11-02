---
title: Lectura y escritura de archivos DBF
description: Aspose.Cells es una biblioteca de JavaScript mediante C++ para trabajar con archivos de hojas de cálculo y admite la lectura y escritura de archivos dBASE III y IV (DBF). Este artículo explica cómo importar datos desde archivos DBF y exportar datos a archivos DBF con Aspose.Cells, incluidos detalles del formato de archivo, características compatibles y ejemplos paso a paso.
linktitle: Lectura y escritura de DBF
url: /es/javascript-cpp/reading-and-writing-dbf-files/
keywords: Aspose.Cells, biblioteca de JavaScript mediante C++, DBF, dBASE, leer DBF, escribir DBF, importar DBF, exportar DBF, formato de archivo, .dbf
type: docs
weight: 200
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells ofrece compatibilidad completa con la lectura y escritura de archivos DBF (dBASE). Puede cargar archivos dBASE III y dBASE IV existentes en un objeto `Workbook`, manipular los datos mediante la avanzada API de Aspose.Cells y guardar el libro de trabajo de nuevo en formato DBF para utilizarlo con aplicaciones de bases de datos heredadas.
{{% /alert %}}

## **Introducción**
DBF (archivo de base de datos) es un formato heredado de archivo de base de datos introducido originalmente por dBASE a comienzos de la década de 1980. A pesar de la antigüedad del formato, los archivos DBF todavía se utilizan ampliamente en muchos sectores para almacenar datos estructurados, especialmente en aplicaciones de contabilidad, SIG y otras aplicaciones especializadas. Aspose.Cells le permite integrar estos archivos heredados de forma transparente en los flujos de trabajo modernos de hojas de cálculo.
La biblioteca admite tanto la lectura como la escritura de archivos DBF, lo que le ofrece la posibilidad de:
- Importar datos de archivos DBF existentes en objetos `Workbook` de Aspose.Cells para su posterior procesamiento o conversión a otros formatos.
- Crear archivos DBF nuevos desde cero o transformando datos de otros formatos de hojas de cálculo.
- Conservar las definiciones de campos, los tipos de datos y las estructuras de registros al transferir datos desde y hacia el formato DBF.
Los archivos DBF también se pueden abrir directamente en Microsoft Excel y otras aplicaciones de hojas de cálculo, lo que los convierte en un puente práctico entre sistemas heredados y herramientas modernas de hojas de cálculo.

## **Versiones y características compatibles de DBF**
Aspose.Cells admite las siguientes versiones del formato DBF:
- **dBASE III** — La variante original y más ampliamente compatible del formato DBF.
- **dBASE IV** — Una versión ampliada que admite tipos de datos adicionales y campos de mayor tamaño.

### Características compatibles
La biblioteca ofrece compatibilidad completa con las siguientes operaciones:
- Leer datos DBF en un objeto `Workbook`, conservando todos los registros y las definiciones de campos.
- Escribir los datos del libro de trabajo en formato DBF para exportarlos a aplicaciones compatibles con dBASE.
- Gestionar los tipos de datos habituales utilizados en archivos DBF, incluidos campos de carácter, numéricos, de fecha y lógicos.
- Preservar definiciones de campos como el nombre, el tipo y la longitud durante las operaciones de lectura y escritura.

### Limitaciones y consideraciones
Al trabajar con archivos DBF, tenga en cuenta las siguientes restricciones:
- El número máximo de campos por archivo es **128**.
- El tamaño máximo de un registro es **4000 bytes**.
- Los nombres de campo se limitan a **10 caracteres**, deben estar en mayúsculas y no pueden contener espacios.
- Los valores de fecha de los archivos DBF se almacenan en formato `YYYYMMDD`.
- La codificación de caracteres puede variar según la aplicación de origen (normalmente Windows-1252 o páginas de códigos OEM).

## **Lectura de un archivo DBF**
Aspose.Cells facilita la carga de datos de un archivo DBF en un objeto `Workbook`. La biblioteca utiliza la clase `LoadOptions` para especificar el formato de origen, lo que garantiza que los datos se interpreten correctamente durante el proceso de carga.

### Lectura de un archivo DBF con Aspose.Cells
Para leer un archivo DBF, debe crear una instancia de `LoadOptions`, establecer su propiedad `loadFormat` en `LoadFormat.Dbf` y pasarla al constructor `Workbook` junto con la ruta del archivo. Una vez cargados, los datos están disponibles a través de la colección `Worksheets`, donde puede recorrer las celdas, extraer valores o manipular los datos según sea necesario.
El siguiente ejemplo demuestra cómo cargar un archivo DBF existente en Aspose.Cells, acceder a su primera hoja de cálculo y leer los valores de las celdas.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".dbf" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, LoadOptions } = AsposeCells;
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const downloadLink = document.getElementById('downloadLink');
            const result = document.getElementById('result');
            if (!fileInput.files.length) {
                result.innerHTML = '<p style="color: red;">Please select a DBF file.</p>';
                return;
            }
            try {
                const file = fileInput.files[0];
                const fileData = new Uint8Array(await file.arrayBuffer());
                const loadOptions = new LoadOptions(AsposeCells.LoadFormat.Dbf);
                const workbook = new Workbook(fileData, loadOptions);
                const worksheet = workbook.worksheets.get(0);
                const cells = worksheet.cells;
                const maxRow = cells.maxDataRow;
                const maxCol = cells.maxDataColumn;
                const lines = [];
                for (let i = 0; i <= maxRow; i++) {
                    let line = "";
                    for (let j = 0; j <= maxCol; j++) {
                        const cell = cells.get(i, j);
                        const value = cell.stringValue;
                        line += "|" + value;
                    }
                    line += "|";
                    lines.push(line);
                }
                const output = document.createElement('pre');
                output.textContent = lines.join("\n");
                result.replaceChildren(output);
                const outputData = workbook.save(AsposeCells.SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "output.xlsx";
                downloadLink.style.display = "block";
                const message = document.createElement('p');
                message.style.color = "green";
                message.textContent = "DBF file loaded successfully. Converted XLSX saved as output.xlsx.";
                result.appendChild(message);
            } catch (error) {
                result.innerHTML = '<p style="color: red;">An error occurred: ' + error.message + '</p>';
            }
        });
    </script>
</html>
```

{{% alert color="primary" %}}
Puede abrir archivos DBF directamente en Microsoft Excel seleccionando el archivo en el cuadro de diálogo Abrir. Excel tratará el archivo DBF como una hoja de cálculo y mostrará sus registros en una disposición tabular. Esto resulta útil para verificar rápidamente los datos después de leerlos o escribirlos con Aspose.Cells.
{{% /alert %}}

## **Escritura de un archivo DBF**
La escritura de datos en un archivo DBF sigue un patrón similar al guardado en cualquier otro formato de hoja de cálculo con Aspose.Cells. Cree o cargue un `Workbook`, rellene la hoja de cálculo con los datos y, a continuación, llame al método `save` especificando `SaveFormat.Dbf` como formato de destino.

### Escritura de un archivo DBF con Aspose.Cells
Para crear un archivo DBF, siga estos pasos:
1. Cree una nueva instancia de `Workbook`.
2. Acceda a la primera hoja de cálculo de la colección `Worksheets`.
3. Rellene la hoja de cálculo con sus datos, incluidos los encabezados en la primera fila y los registros en las filas posteriores.
4. Llame al método `Workbook.save`, pasando la ruta del archivo y `SaveFormat.Dbf` como parámetros.
El siguiente ejemplo demuestra cómo crear un archivo DBF desde cero. Rellena una hoja de cálculo con datos de ejemplo que contienen distintos tipos de datos (cadenas, números y fechas) para ilustrar cómo se gestionan los tipos de campo al exportar al formato DBF.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook } = AsposeCells;
        const readyPromise = AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;
            // Encabezados de columnas
            cells.get(0, 0).value = "ID";
            cells.get(0, 1).value = "Name";
            cells.get(0, 2).value = "Department";
            cells.get(0, 3).value = "Salary";
            cells.get(0, 4).value = "HireDate";
            // Fila de datos 1
            cells.get(1, 0).value = 101;
            cells.get(1, 1).value = "John Smith";
            cells.get(1, 2).value = "Engineering";
            cells.get(1, 3).value = 75000.50;
            cells.get(1, 4).value = new Date(2020, 2, 15);
            // Fila de datos 2
            cells.get(2, 0).value = 102;
            cells.get(2, 1).value = "Jane Doe";
            cells.get(2, 2).value = "Marketing";
            cells.get(2, 3).value = 68000.75;
            cells.get(2, 4).value = new Date(2019, 6, 22);
            // Fila de datos 3
            cells.get(3, 0).value = 103;
            cells.get(3, 1).value = "Bob Johnson";
            cells.get(3, 2).value = "Finance";
            cells.get(3, 3).value = 82000.00;
            cells.get(3, 4).value = new Date(2021, 0, 10);
            // Fila de datos 4
            cells.get(4, 0).value = 104;
            cells.get(4, 1).value = "Alice Brown";
            cells.get(4, 2).value = "Human Resources";
            cells.get(4, 3).value = 71000.25;
            cells.get(4, 4).value = new Date(2018, 10, 5);
            // Fila de datos 5
            cells.get(5, 0).value = 105;
            cells.get(5, 1).value = "Charlie Wilson";
            cells.get(5, 2).value = "Operations";
            cells.get(5, 3).value = 79500.80;
            cells.get(5, 4).value = new Date(2022, 4, 30);
            // Establecer anchos de columna para mejorar la legibilidad
            cells.setColumnWidth(0, 8);
            cells.setColumnWidth(1, 20);
            cells.setColumnWidth(2, 20);
            cells.setColumnWidth(3, 12);
            cells.setColumnWidth(4, 14);
            const outputData = workbook.save(AsposeCells.SaveFormat.Dbf);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output.dbf";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}
Al escribir datos en un archivo DBF, asegúrese de que estos se ajusten a las limitaciones del formato. Los nombres de campo no deben superar los 10 caracteres ni contener espacios. Los registros que superen los 4000 bytes en total no se guardarán correctamente. Las fechas deben ser valores de fecha válidos que puedan representarse en el formato YYYYMMDD.
{{% /alert %}}

## **Consideraciones sobre tipos de datos y formato**
Al transferir datos entre Aspose.Cells y el formato DBF, es importante comprender cómo se asignan los tipos de datos entre ambos sistemas para garantizar la integridad de los datos.

### Tipos de celda y tipos de campo de DBF
Los valores de celda de Aspose.Cells se convierten automáticamente en los tipos de campo DBF apropiados al guardar:
- **Cadenas** se asignan a campos de carácter (C).
- **Valores numéricos** (enteros y decimales) se asignan a campos numéricos (N).
- **Valores de fecha** se asignan a campos de fecha (D) en formato `YYYYMMDD`.
- **Valores booleanos** se asignan a campos lógicos (L).

### Codificación
Los archivos DBF pueden utilizar distintas codificaciones de caracteres según la aplicación que los haya creado. Aspose.Cells se ocupa de la codificación de forma transparente en la mayoría de los casos, pero si encuentra problemas de visualización de caracteres, es posible que deba verificar la codificación del archivo de origen.

### Reglas para los nombres de campo
Los nombres de campo de DBF deben cumplir las siguientes reglas:
- Longitud máxima de 10 caracteres.
- Deben comenzar por una letra.
- No pueden contener espacios ni caracteres especiales.
- Se almacenan en mayúsculas, independientemente del uso de mayúsculas o minúsculas en la entrada.

### Verificación de la salida
Tras escribir un archivo DBF, puede verificar el resultado abriéndolo en Microsoft Excel o en cualquier aplicación compatible con dBASE. Los datos deben aparecer en una disposición tabular, con los nombres de campo como encabezados de columna y los registros rellenados según los datos proporcionados.

## **Conversión entre DBF y otros formatos**
Uno de los casos de uso más prácticos de la lectura y escritura de archivos DBF con Aspose.Cells es convertir datos entre el formato DBF y formatos modernos de hojas de cálculo, como XLSX, XLS o CSV. Dado que Aspose.Cells admite una amplia variedad de formatos, puede cargar fácilmente un archivo DBF y volver a guardarlo en cualquier otro formato compatible, o viceversa.

{{< app/cells/assistant language="javascript-cpp" >}}