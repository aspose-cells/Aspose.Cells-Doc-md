---
title: Bloquear o desbloquear formas con JavaScript vía C++
linktitle: Bloquear o desbloquear formas
type: docs
weight: 200
url: /es/javascript-cpp/lock-or-unlock-shapes/
description: Este artículo muestra un ejemplo de código que explica cómo bloquear o desbloquear formas para protegerlas usando la biblioteca Aspose.Cells para JavaScript vía C++.
keywords: Bloquear formas con JavaScript vía C++ para protegerlas, Cómo bloquear o desbloquear formas usando JavaScript vía C++, Bloquear o desbloquear formas para protegerlas en JavaScript vía C++.
---

## **Escenarios de uso posibles**

A veces, es necesario proteger todas las formas en ciertas hojas de cálculo para evitar que sean destruidas por situaciones no deseadas. En este caso, es necesario bloquear todas las formas en la hoja de cálculo especificada. 

Bloquear formas en una hoja de cálculo o documento puede ser beneficioso por varias razones:
1. Prevenir cambios accidentales: bloquear formas asegura que no sean movidas, redimensionadas o eliminadas accidentalmente por los usuarios. Esto es especialmente importante en documentos complejos donde las formas pueden usarse para anotaciones, ilustraciones o como parte del diseño del documento.
1. Mantener el diseño y la estética: las formas a menudo juegan un papel crucial en el diseño y la apariencia visual de un documento. Bloquearlas preserva la apariencia deseada, asegurando que el documento se vea profesional y atractivo.
1. Integridad de datos: en hojas de cálculo, las formas pueden usarse para resaltar puntos de datos importantes, agregar comentarios o proporcionar explicaciones visuales. Bloquear estas formas garantiza que la información contextual que proporcionan permanezca precisa e intacta.
1. Consistencia en documentos compartidos: al colaborar en documentos, diferentes usuarios pueden tener diferentes niveles de experiencia. Bloquear formas ayuda a mantener la coherencia en todo el documento evitando alteraciones no intencionadas.
1. Seguridad: en documentos sensibles, bloquear formas puede ser parte de una estrategia más amplia para proteger la información. Por ejemplo, en informes financieros o documentos legales, las formas bloqueadas pueden usarse para salvaguardar anotaciones o puntos destacados críticos.

A veces, necesitas poder modificar ciertas formas en hojas de cálculo protegidas, en cuyo caso, necesitas desbloquear estas formas. Este artículo presentará en detalle cómo bloquear y desbloquear formas específicas.

## **Cómo bloquear formas para protegerlas en Excel**

Así puedes bloquear celdas en Microsoft Excel:

1. Abre tu archivo de Excel: abre el archivo de Excel que contiene las formas que deseas bloquear.

1. Selecciona la forma: haz clic en la forma que deseas bloquear. También puedes seleccionar varias formas manteniendo presionada la tecla Ctrl y haciendo clic en cada forma.

1. Abre el panel de formato de formas: haz clic derecho en la(s) forma(s) seleccionadas y elige "Tamaño y propiedades." Alternativamente, puedes ir a la pestaña "Formato" en la cinta de opciones, y en el grupo "Tamaño", hacer clic en el lanzador de diálogo (una pequeña flecha) para abrir el panel "Formato de forma".
1. Bloquea la forma: en el panel "Formato de forma", ve a la pestaña "Tamaño y propiedades" (el ícono parece un cuadrado con flechas). En la sección "Propiedades", marca la casilla de "Bloqueado."
<br>
<img src="1.png" width=60% />
1. Protege la hoja de trabajo: Ve a la pestaña "Revisar" en la cinta de opciones. Haz clic en "Proteger hoja". Establece una contraseña (opcional) y elige los permisos que deseas permitir (por ejemplo, seleccionar celdas bloqueadas, formatear celdas, etc.). Haz clic en "Aceptar".
<br>
<img src="2.png" width=60% />

## **Cómo bloquear todas las formas en una hoja especificada**

Para proteger todas las formas en una hoja de cálculo específica, usa el método `worksheet.protect(ProtectionType.Objects)`, como se muestra en el siguiente código de ejemplo.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Lock Shapes Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ProtectionType } = AsposeCells;

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

            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            const text = "This is a test";
            const worksheet = workbook.worksheets.get(0);

            let shape = worksheet.shapes.addTextBox(1, 0, 1, 0, 30, 100);
            shape.text = text;

            shape = worksheet.shapes.addRectangle(5, 0, 1, 0, 30, 100);
            shape.text = text;

            shape = worksheet.shapes.addButton(9, 0, 1, 0, 30, 100);
            shape.text = text;

            shape = worksheet.shapes.addOval(13, 0, 1, 0, 50, 100);
            shape.text = text;

            // Protect all shapes in the specified worksheet
            shape.worksheet.protect(ProtectionType.Objects);

            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Locked.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Locked.xlsx';

            document.getElementById('result').innerHTML = '<p style="color: green;">Shapes locked successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Cómo desbloquear formas específicas en una hoja de cálculo protegida**

Para desbloquear una forma específica en una hoja protegida, usa `shape.isLocked`, como se muestra en el siguiente código de ejemplo.

Nota: `shape.isLocked` solo tiene sentido cuando la hoja de cálculo está protegida.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Unlock Shape</title>
    </head>
    <body>
        <h1>Unlock Shape Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
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
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Loads the workbook which contains hidden external links
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get protected worksheet
            const worksheet = workbook.worksheets.get(0);

            // Get the specified shape to be unlocked
            const shape = worksheet.shapes.get("TextBox 1");

            if (!shape) {
                resultDiv.innerHTML = '<p style="color: red;">Shape "TextBox 1" not found.</p>';
                return;
            }

            // Unlock the specified shape
            if (!worksheet.protection.allowEditingObject && shape.isLocked) {
                shape.isLocked = false;
            }

            // Save the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'UnLocked.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Shape unlocked successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
