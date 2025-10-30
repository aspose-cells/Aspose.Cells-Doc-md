---
title: Proteger hojas de cálculo con JavaScript a través de C++
linktitle: Protección de hojas de cálculo
type: docs
weight: 10
url: /es/javascript-cpp/protecting-worksheets/
description: Aprende cómo proteger hojas de cálculo en Excel usando Aspose.Cells for JavaScript a través de C++, incluyendo la protección de filas, columnas y celdas específicas.
---

{{% alert color="primary" %}}

Cuando una hoja de cálculo está protegida, las acciones que puede realizar un usuario están restringidas. Por ejemplo, no pueden ingresar datos, insertar o eliminar filas o columnas, etc.

{{% /alert %}}

## **Proteger hojas de cálculo**

### **Introducción**

Las opciones generales de protección en Microsoft Excel son:

- Contenidos
- Objetos
- Escenarios

Las hojas de cálculo protegidas no ocultan ni protegen datos sensibles, por lo que es diferente del cifrado de archivos. Generalmente, la protección de la hoja de cálculo es adecuada para fines de presentación. Evita que el usuario final modifique los datos, el contenido y el formato en la hoja de cálculo.

### **Proteger una hoja de cálculo**

Aspose.Cells proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) que representa un archivo de Microsoft Excel. La clase [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) contiene una colección [**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--) que permite acceder a cada hoja de cálculo en un archivo de Excel. Una hoja de cálculo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet).

La clase [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) proporciona el método [**protect(ProtectionType)**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#protect-protectiontype-) que se usa para aplicar protección en la hoja de cálculo. El método [**protect(ProtectionType)**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#protect-protectiontype-) acepta los siguientes parámetros:

- Tipo de Protección, el tipo de protección a aplicar en la hoja de cálculo. El tipo de protección se aplica con la ayuda de la enumeración [**ProtectionType**](https://reference.aspose.com/cells/javascript-cpp/protectiontype).
- Nueva contraseña, la nueva contraseña utilizada para proteger la hoja de cálculo.
- Contraseña antigua, la contraseña antigua, si la hoja de cálculo ya está protegida con contraseña. Si la hoja de cálculo no está protegida, simplemente pase nula.

La enumeración [**ProtectionType**](https://reference.aspose.com/cells/javascript-cpp/protectiontype) contiene los siguientes tipos de protección predefinidos:

|**Tipos de protección**|**Descripción**|
| :- | :- |
|All|El usuario no puede modificar nada en esta hoja de cálculo|
|Contents|El usuario no puede introducir datos en esta hoja de cálculo|
|Objects|El usuario no puede modificar objetos de dibujo|
|Scenarios|El usuario no puede modificar escenarios guardados|
|Structure|El usuario no puede modificar la estructura|
|Windows|La protección se aplica a las ventanas|
|None|No se aplica protección|

El ejemplo a continuación muestra cómo proteger una hoja de cálculo con una contraseña.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Protect Worksheet Example</title>
    </head>
    <body>
        <h1>Protect Worksheet Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ProtectionType, Utils } = AsposeCells;

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

            // Ensure Aspose.Cells is initialized before proceeding
            await AsposeCells.onReady();

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object with file buffer
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Protecting the worksheet with a password
            worksheet.protect(ProtectionType.All, "aspose", null);

            // Saving the modified Excel file in Excel 97-2003 format
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet protected successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

Después de que se use el código anterior para proteger la hoja de cálculo, puede verificar la protección en la hoja de cálculo abriéndola. Una vez que abra el archivo e intente agregar datos a la hoja de cálculo, verá el siguiente cuadro de diálogo:

|**Un aviso de diálogo de que el usuario no puede modificar la hoja de cálculo**|
| :- |
|![todo:image_alt_text](protecting-worksheets_1.png)|

Para trabajar en la hoja de cálculo, desprotege la hoja de cálculo seleccionando **Protección**, luego **Desproteger hoja** del elemento de menú **Herramientas**.

Después de seleccionar la opción Desproteger hoja, se abrirá un cuadro de diálogo que te pedirá que ingreses la contraseña para que puedas trabajar en la hoja de cálculo como se muestra a continuación:

|![todo:image_alt_text](protecting-worksheets_2.png)|

### **Proteger algunas celdas en la hoja de cálculo utilizando Microsoft Excel**

Podría ser necesario bloquear solo algunas celdas en la hoja de cálculo en ciertos escenarios. Si desea bloquear celdas específicas en la hoja, debe desbloquear todas las demás celdas. Todas las celdas en una hoja están ya inicializadas para bloqueo; puede verificar esto abriendo cualquier archivo de Excel en MS Excel y haciendo clic en **Formato | Celdas...** para mostrar el cuadro de diálogo **Formato de celdas** y luego haciendo clic en la pestaña **Protección** y viendo si la casilla "Bloqueado" está marcada por defecto.

Los siguientes puntos describen cómo bloquear algunas celdas usando MS Excel. Este método se aplica a Microsoft Office Excel 97, 2000, 2002, 2003 y versiones posteriores.

1. Selecciona toda la hoja de cálculo haciendo clic en el botón **Seleccionar todo** (el rectángulo gris directamente arriba del número de fila para la fila 1 y a la izquierda de la letra de la columna A).
2. Haga clic en **Celdas** en el menú **Formato**, haga clic en la pestaña **Protección**, y luego desmarque la casilla **Bloqueado**.
   Esto desbloquea todas las celdas de la hoja de cálculo.
   Si el comando **Celdas** no está disponible, es posible que partes de la hoja de cálculo ya estén bloqueadas. En el menú **Herramientas**, apunta a **Protección**, y luego haz clic en **Desproteger hoja**.
3. Seleccione solo las celdas que desea bloquear y repita el paso 2, pero esta vez marque la casilla **Bloqueado**.
4. En el menú **Herramientas**, apunte a **Protección**, haga clic en **Proteger hoja** y luego haga clic en **Aceptar**.
5. En el cuadro de diálogo **Proteger hoja**, tiene la opción de especificar una contraseña y seleccionar los elementos que desea que los usuarios puedan cambiar.

### **Proteja algunas celdas en la hoja de cálculo usando Aspose.Cells**

En este método, usamos la API Aspose.Cells únicamente para realizar la tarea.

Ejemplo: El siguiente ejemplo muestra cómo proteger algunas celdas en la hoja de cálculo. Primero desbloquea todas las celdas y luego bloquea 3 celdas (A1, B1, C1). Finalmente, protege la hoja de cálculo. El objeto [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) contiene una propiedad booleana, [**isLocked()**](https://reference.aspose.com/cells/javascript-cpp/style/#isLocked--). Puede establecer la propiedad [**isLocked()**](https://reference.aspose.com/cells/javascript-cpp/style/#isLocked--) en verdadero o falso y aplicar el método *Column/Row.applyStyle()* para bloquear o desbloquear la fila/columna con sus atributos deseados.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Unlock Columns and Protect Specific Cells Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, StyleFlag, ProtectionType } = AsposeCells;

        const readyPromise = AsposeCells.onReady({
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
            await readyPromise;

            // Create a new workbook.
            const wb = new Workbook();

            // Create a worksheet object and obtain the first sheet.
            const sheet = wb.worksheets.get(0);

            // Define the style object.
            let style;

            // Define the styleflag object
            const styleflag = new StyleFlag();

            // Loop through all the columns in the worksheet and unlock them.
            for (let i = 0; i <= 255; i++) {
                style = sheet.cells.columns.get(i).style;
                style.isLocked = false;
                styleflag.locked = true;
                sheet.cells.columns.get(i).applyStyle(style, styleflag);
            }

            // Lock the three cells...i.e. A1, B1, C1.
            style = sheet.cells.get("A1").style;
            style.isLocked = true;
            sheet.cells.get("A1").style = style;

            style = sheet.cells.get("B1").style;
            style.isLocked = true;
            sheet.cells.get("B1").style = style;

            style = sheet.cells.get("C1").style;
            style.isLocked = true;
            sheet.cells.get("C1").style = style;

            // Finally, Protect the sheet now.
            sheet.protect(ProtectionType.All);

            // Save the excel file and provide download link
            const outputData = wb.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **Proteger una fila en la hoja de cálculo**

Aspose.Cells permite bloquear fácilmente cualquier fila en la hoja de cálculo. Aquí, podemos usar el método [**applyStyle(Style, StyleFlag)**](https://reference.aspose.com/cells/javascript-cpp/row/#applyStyle-style-styleflag-) de la clase [**Aspose.Cells.Row**](https://reference.aspose.com/cells/javascript-cpp/row) para aplicar [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) a una fila en particular. Este método recibe dos argumentos: un objeto [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) y un objeto [**StyleFlag**](https://reference.aspose.com/cells/javascript-cpp/styleflag) que contiene todos los miembros relacionados con el formato aplicado.

El siguiente ejemplo muestra cómo proteger una fila en la hoja de cálculo. Primero desbloquea todas las celdas y luego bloquea la primera fila. Finalmente, protege la hoja de cálculo. El objeto [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) contiene una propiedad booleana, [**isLocked()**](https://reference.aspose.com/cells/javascript-cpp/style/#isLocked--). Puede establecer la propiedad [**isLocked()**](https://reference.aspose.com/cells/javascript-cpp/style/#isLocked--) en verdadero o falso para bloquear o desbloquear la fila/columna usando el objeto [**StyleFlag**](https://reference.aspose.com/cells/javascript-cpp/styleflag).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Protect Worksheet Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, StyleFlag, ProtectionType, Utils } = AsposeCells;

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
            // Create a new workbook.
            const wb = new Workbook();

            // Create a worksheet object and obtain the first sheet.
            const sheet = wb.worksheets.get(0);

            // Define the style object.
            let style;

            // Define the styleflag object.
            const flag = new StyleFlag();

            // Loop through all the columns in the worksheet and unlock them.
            for (let i = 0; i <= 255; i++) {
                style = sheet.cells.columns.get(i).style;
                style.isLocked = false;
                flag.locked = true;
                sheet.cells.columns.get(i).applyStyle(style, flag);
            }

            // Get the first row style.
            style = sheet.cells.rows.get(0).style;

            // Lock it.
            style.isLocked = true;

            // Set the lock setting.
            flag.locked = true;

            // Apply the style to the first row.
            sheet.cells.applyRowStyle(0, style, flag);

            // Protect the sheet.
            sheet.protect(ProtectionType.All);

            // Save the excel file.
            const outputData = wb.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and protected. Click the download link to get the file.</p>';
        });
    </script>
</html>
```

### **Proteger una columna en la hoja de cálculo**

Aspose.Cells permite bloquear fácilmente cualquier columna en la hoja de cálculo. Aquí, podemos usar el método [**applyStyle(Style, StyleFlag)**](https://reference.aspose.com/cells/javascript-cpp/column/#applyStyle-style-styleflag-) de la clase [**Aspose.Cells.Column**](https://reference.aspose.com/cells/javascript-cpp/column) para aplicar [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) a una columna en particular. Este método recibe dos argumentos: un objeto [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) y un objeto [**StyleFlag**](https://reference.aspose.com/cells/javascript-cpp/styleflag) que contiene todos los miembros relacionados con el formato aplicado.

El siguiente ejemplo muestra cómo proteger una columna en la hoja de cálculo. Primero desbloquea todas las celdas y luego bloquea la primera columna. Finalmente, protege la hoja de cálculo. El objeto [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) contiene una propiedad booleana, [**isLocked()**](https://reference.aspose.com/cells/javascript-cpp/style/#isLocked--). Puede establecer la propiedad [**isLocked()**](https://reference.aspose.com/cells/javascript-cpp/style/#isLocked--) en verdadero o falso para bloquear o desbloquear la fila/columna usando el objeto [**StyleFlag**](https://reference.aspose.com/cells/javascript-cpp/styleflag).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Unlock Columns and Protect Sheet</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, StyleFlag, ProtectionType } = AsposeCells;

        const readyPromise = AsposeCells.onReady({
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
                // If no file provided, a new workbook will be created
                document.getElementById('result').innerHTML = '<p style="color: orange;">No file selected. A new workbook will be created and processed.</p>';
            } else {
                document.getElementById('result').innerHTML = '<p>Processing selected file...</p>';
            }

            await readyPromise;

            // Load workbook from file if provided, otherwise create new workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Create a worksheet object and obtain the first sheet.
            const sheet = workbook.worksheets.get(0);

            // Define the style object.
            let style;

            // Define the styleflag object.
            const flag = new StyleFlag();

            // Loop through all the columns in the worksheet and unlock them.
            for (let i = 0; i <= 255; i++) {
                style = sheet.cells.columns.get(i).style;
                style.isLocked = false;
                flag.locked = true;
                sheet.cells.columns.get(i).applyStyle(style, flag);
            }

            // Get the first column style.
            style = sheet.cells.columns.get(0).style;

            // Lock it.
            style.isLocked = true;

            // Apply the style to the first column.
            sheet.cells.columns.get(0).applyStyle(style, flag);

            // Protect the sheet.
            sheet.protect(ProtectionType.All);

            // Save the excel file.
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **Permitir a los usuarios editar rangos**

El siguiente ejemplo muestra cómo permitir a los usuarios editar un rango en una hoja de cálculo protegida.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Protect Range</title>
    </head>
    <body>
        <h1>Protect Range Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ProtectionType, Utils } = AsposeCells;

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

            // Instantiate a new or loaded Workbook
            let book;
            if (fileInput.files && fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                book = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                book = new Workbook();
            }

            // Get the first (default) worksheet
            const sheet = book.worksheets.get(0);

            // Get the Allow Edit Ranges
            const allowRanges = sheet.allowEditRanges;

            // Define ProtectedRange
            let protected_range;

            // Create the range
            const idx = allowRanges.add("r2", 1, 1, 3, 3);
            protected_range = allowRanges.get(idx);

            // Specify the password
            protected_range.password = "123";

            // Protect the sheet
            sheet.protect(ProtectionType.All);

            // Save the Excel file
            const outputData = book.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'protectedrange.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Protected Range Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Protected range added and sheet protected successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
