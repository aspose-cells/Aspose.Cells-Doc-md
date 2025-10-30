---
title: Cómo bloquear celdas para protegerlas
type: docs
weight: 130
url: /es/javascript-cpp/how-to-lock-cells-to-protect-them/
description: Este artículo te muestra un código que explica cómo bloquear celdas para protegerlas usando Aspose.Cells for JavaScript vía C++.
keywords: Bloquear celdas en JavaScript para protegerlas, Cómo bloquear celdas para protegerlas usando JavaScript, Bloquear celdas en JavaScript para protegerlas.
---

## **Escenarios de uso posibles**
Bloquear celdas para protegerlas es una práctica común en aplicaciones de hojas de cálculo, como Microsoft Excel o Google Sheets, por varias razones importantes:

1. Prevención de cambios accidentales: bloquear celdas puede evitar que los usuarios modifiquen datos o fórmulas importantes accidentalmente. Esto es especialmente útil en hojas complejas donde cambios no intencionados pueden causar errores graves.

1. Mantener la integridad de los datos: al bloquear celdas, puedes asegurar que los datos críticos permanezcan consistentes y precisos. Esto es fundamental en documentos financieros, informes y otros documentos donde la integridad de los datos es esencial.

1. Acceso controlado: en entornos colaborativos, bloquear celdas permite controlar quién puede editar ciertas partes de una hoja. Por ejemplo, puedes permitir que solo ciertos miembros del equipo editen celdas específicas mientras mantienes la hoja protegida.

1. Proteger fórmulas: las fórmulas son cruciales para cálculos y análisis de datos. Bloquear celdas que contienen fórmulas asegura que estas no sean modificadas o eliminadas accidentalmente, lo que podría interrumpir la funcionalidad de toda la hoja.

1. Aplicar reglas comerciales: en algunos casos, las reglas o regulaciones empresariales específicas pueden requerir que ciertos datos estén protegidos contra modificación. Bloquear celdas ayuda a cumplir con estos requisitos.

1. Orientar a los usuarios: bloqueando celdas y proporcionando instrucciones claras sobre cuáles pueden editarse, puedes guiar a los usuarios sobre cómo interactuar con la hoja, reduciendo confusiones y errores.

## **Cómo bloquear celdas en Excel para protegerlas**
Así puedes bloquear celdas en Microsoft Excel:

1. Seleccionar las celdas a bloquear: selecciona las celdas que deseas bloquear. Si quieres bloquear toda la hoja, puedes omitir este paso.
1. Abrir el cuadro de diálogo Formato de celdas: haz clic derecho en las celdas seleccionadas y elige "Formato de celdas", o presiona Ctrl+1.
<br>
<img src="1.png" width=60% />
1. Bloquear las celdas: en el cuadro de diálogo Formato de celdas, ve a la pestaña "Protección". Marca la casilla "Bloqueado". Haz clic en "Aceptar".
1. Protege la hoja de trabajo: Ve a la pestaña "Revisar" en la cinta de opciones. Haz clic en "Proteger hoja". Establece una contraseña (opcional) y elige los permisos que deseas permitir (por ejemplo, seleccionar celdas bloqueadas, formatear celdas, etc.). Haz clic en "Aceptar".
<br>
<img src="2.png" width=60% />

## **Cómo bloquear celdas para protegerlas usando JavaScript**

Aspose.Cells es una biblioteca poderosa para trabajar con archivos de Excel de manera programática. Para bloquear celdas usando Aspose.Cells for JavaScript vía C++, debes seguir estos pasos: cargar [archivo de ejemplo](sample.xlsx), desbloquear todas las celdas primero (ya que, por defecto, todas las celdas están bloqueadas pero no se hace efectivo hasta que la hoja de cálculo esté protegida), luego bloquear las celdas específicas que deseas proteger, y finalmente proteger la hoja para hacer cumplir el bloqueo.

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
        const { Workbook, SaveFormat, StyleFlag, ProtectionType } = AsposeCells;

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

            // Instantiate Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const sheet = workbook.worksheets.get(0);

            // Unlock all cells first
            const unlockStyle = workbook.createStyle();
            unlockStyle.isLocked = false;

            const styleFlag = new StyleFlag();
            styleFlag.locked = true;
            sheet.cells.applyStyle(unlockStyle, styleFlag);

            // Lock specific cells (e.g., A1 and B2)
            const lockStyle = workbook.createStyle();
            lockStyle.isLocked = true;

            sheet.cells.get("A1").style = lockStyle;
            sheet.cells.get("B2").style = lockStyle;

            // Protect the worksheet to enforce the locking
            sheet.protect(ProtectionType.All);

            // Save the modified workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_locked.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Locked Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Worksheet protected and cells locked successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


## **Resultado de salida**
Este código asegura que solo las celdas especificadas (A1 y B2 en este ejemplo) estén bloqueadas, y la hoja de trabajo esté protegida para hacer cumplir estas configuraciones. Todas las demás celdas en la hoja permanecen desbloqueadas y se pueden editar.

<br>
<img src="3.png" width=60% />
