---
title: Gestionar configuraciones de archivos de hojas de cálculo de Excel con JavaScript via C++
linktitle: Configuraciones de libros de trabajo
type: docs
weight: 185
url: /es/javascript-cpp/workbook-settings/
description: Gestionar configuraciones de archivos de Excel usando Aspose.Cells for JavaScript via C++.
---

## **Resumen de configuración del libro de trabajo**
Trabajar con archivos de Excel implica varias configuraciones que se pueden manipular programáticamente usando Aspose.Cells for JavaScript via C++. Este documento describe cómo gestionar estas configuraciones de manera efectiva.

## **Escenarios de uso posibles**
Los siguientes escenarios ilustran cuándo puede ser necesario administrar las configuraciones del libro de trabajo:
- Ajustar opciones de pantalla
- Configurar modo de cálculo
- Configurar parámetros de configuración de página

## **Gestionar configuraciones del libro de trabajo usando Aspose.Cells for JavaScript via C++**
Este ejemplo demuestra cómo administrar configuraciones del libro de trabajo como opciones de cálculo y configuraciones de pantalla.

1. Cree un nuevo libro de trabajo o cargue uno existente.
2. Modifique las configuraciones del libro de acuerdo a sus requisitos.
3. Guarde el libro de trabajo para mantener los cambios.

### **Código de ejemplo**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Workbook Settings Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
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
            // Create a new workbook
            const workbook = new Workbook();

            // Access the settings of the workbook
            const settings = workbook.settings;
            settings.calculationMode = 1; // Manual calculation

            // Display options
            settings.showGridLines = false; // Disable gridlines

            // Save the workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'WorkbookSettingsExample.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

## **Propiedades y métodos clave de configuración del libro de trabajo**
Aspose.Cells for JavaScript via C++ proporciona varias propiedades y métodos para ajustar la configuración del libro de trabajo:
- **Workbook.settings**: Accede a las configuraciones del libro de trabajo.
- **Settings.calculationMode**: Establece el modo de cálculo para el libro de trabajo.
- **Settings.showGridLines**: Habilita o deshabilita las líneas de cuadrícula en la pantalla.

## **Conclusión**
Gestionar las configuraciones del libro de trabajo en Aspose.Cells for JavaScript via C++ es sencillo y ofrece muchas opciones para personalizar los comportamientos del archivo de Excel. Al utilizar las configuraciones disponibles, puede adaptar el libro de trabajo a sus necesidades específicas.
