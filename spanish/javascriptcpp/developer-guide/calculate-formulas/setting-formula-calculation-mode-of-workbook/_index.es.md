---
title: Configurar el modo de cálculo de fórmulas del libro de trabajo con JavaScript mediante C++
linktitle: Configuración del modo de cálculo de fórmulas del libro de trabajo
description: Este artículo presenta cómo establecer el modo de cálculo de fórmulas en un libro de trabajo en Microsoft Excel con Aspose.Cells for JavaScript en C++. Cargue un archivo Excel existente o cree uno nuevo, utilice la propiedad proporcionada por Aspose.Cells para establecer el modo de cálculo de fórmulas y obtener el resultado. Finalmente, guardamos el archivo de Excel modificado en disco.
keywords: Aspose.Cells, Excel, libro, modo de cálculo de fórmulas, configuraciones, JavaScript a través de C++
type: docs
weight: 110
url: /es/javascript-cpp/setting-formula-calculation-mode-of-workbook/
---

{{% alert color="primary" %}}  
Microsoft Excel te permite establecer el modo de cálculo de fórmulas, es decir, la forma en que se calculan las fórmulas. Hay tres valores posibles:  

- Automático: recalcula cada vez que algo cambia, y cada vez que se abre un libro.  
- Automático excepto para tablas de datos: recalcula cada vez que algo cambia, pero deja fuera las tablas de datos.  
- Manual: recalcula solo cuando el usuario lo solicita explícitamente presionando F9 o CTRL+ALT+F9, o cuando se guarda el libro.  
{{% /alert %}}  

Para establecer el modo de cálculo de fórmulas en Microsoft Excel:  

1. Selecciona **Fórmulas** y luego **Opciones de cálculo**.  
1. Selecciona una de las opciones.  

Aspose.Cells for JavaScript a través de C++ también te permite establecer el **Modo de Cálculo de Fórmulas** usando [**FormulaSettings.calculationMode**](https://reference.aspose.com/cells/javascript-cpp/formulasettings/#calculationMode--) propiedad de modo. Puedes asignarle la enumeración [**CalcModeType**](https://reference.aspose.com/cells/javascript-cpp/calcmodetype) que tiene uno de los siguientes valores:  

- CalcModeType.Automatic  
- CalcModeType.AutomaticExceptTable  
- CalcModeType.Manual  

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
            // Creating a workbook
            const workbook = new Workbook();

            // Set the Formula Calculation Mode to Manual
            workbook.settings.formulaSettings.calculationMode = AsposeCells.CalcModeType.Manual;

            // Save the workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and saved successfully. Click the download link to get the file.</p>';
        });
    </script>
</html>
```
