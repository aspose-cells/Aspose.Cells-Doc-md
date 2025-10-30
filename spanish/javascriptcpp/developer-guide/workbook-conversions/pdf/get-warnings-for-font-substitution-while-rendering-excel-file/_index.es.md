---
title: Obtener advertencias sobre sustitución de fuentes al renderizar archivo Excel con JavaScript vía C++
linktitle: Obtener Advertencias por Sustitución de Fuentes al Renderizar un Archivo de Excel
type: docs
weight: 230
url: /es/javascript-cpp/get-warnings-for-font-substitution-while-rendering-excel-file/
description: Aprende cómo obtener advertencias sobre sustitución de fuentes al renderizar archivos Excel a PDF usando Aspose.Cells for JavaScript vía C++.
---

{{% alert color="primary" %}}  

A veces, al renderizar un archivo Microsoft Excel a PDF, Aspose.Cells sustituye fuentes. Aspose.Cells proporciona una característica que permite a los desarrolladores saber qué fuente específica ha sido sustituida al activar una advertencia. Esta es una característica útil que puede ayudar a identificar por qué un PDF renderizado con Aspose.Cells se ve diferente al archivo original de Microsoft Excel, para que puedan tomar las acciones apropiadas. Por ejemplo, instalar las fuentes faltantes para que los resultados de renderizado se vean igual.

{{% /alert %}}  

Para obtener advertencias por sustitución de fuente al renderizar archivos Excel a PDF, implemente la interfaz IWarningCallback y configure la propiedad PdfSaveOptions.warningCallback con su interfaz implementada.

La captura de pantalla a continuación muestra un archivo de Excel fuente que utilizaremos en el siguiente código. Tiene algo de texto en las celdas A6 y A7 en fuentes que no son renderizadas correctamente por Microsoft Excel.

|**No todas las fuentes se renderizan correctamente**|  
| :- |  
|![todo:image_alt_text](get-warnings-for-font-substitution-while-rendering-excel-file_1.png)|  
Aspose.Cells sustituirá las fuentes en las celdas A6 y A7 con fuentes adecuadas como se muestra a continuación.

|**Fuentes Sustituidas**|  
| :- |  
|![todo:image_alt_text](get-warnings-for-font-substitution-while-rendering-excel-file_2.png)|  
## **Descargar Archivo Fuente y PDF de Salida**  
Puedes descargar el archivo de Excel fuente y el PDF de salida desde los siguientes enlaces

- [source.xlsx](5112611.xlsx)  
- [output.pdf](5112616.pdf)  
## **Código**  
El siguiente código implementa IWarningCallback y configura la propiedad PdfSaveOptions.warningCallback con la interfaz implementada. Ahora, cada vez que una fuente sea sustituida en alguna celda, Aspose.Cells generará una advertencia dentro del método WarningCallback.Warning().

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - GetWarningsForFontSubstitution</title>
    </head>
    <body>
        <h1>GetWarningsForFontSubstitution Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PdfSaveOptions } = AsposeCells;

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

        class GetWarningsForFontSubstitution {
            static warning(info) {
                if (info.type === AsposeCells.WarningType.FontSubstitution) {
                    console.log("WARNING INFO: " + info.description);
                }
            }
        }

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();
            // Instantiate workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Prepare PDF save options and assign warning callback
            const options = new PdfSaveOptions();
            options.warningCallback = GetWarningsForFontSubstitution;

            // Save workbook as PDF
            const outputData = workbook.save(SaveFormat.Pdf, options);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            resultDiv.innerHTML = '<p style="color: green;">PDF generated successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```  
## **Salida**  
Después de convertir el archivo de Excel fuente a PDF, las advertencias se emiten en la consola de depuración de esta manera:

{{< highlight java >}}  

 WARNING INFO: Font substitution: Font [ Athene Logos; Regular ] has been substituted in Cell [ A6 ] in Sheet [ Sheet1 ].  

WARNING INFO: Font substitution: Font [ B Traffic; Regular ] has been substituted in Cell [ A7 ] in Sheet [ Sheet1 ].  

{{< /highlight >}}  

{{% alert color="primary" %}}  

Si tu hoja de cálculo contiene fórmulas, es mejor llamar al método Workbook.calculateFormula justo antes de renderizar la hoja de cálculo al formato PDF. Al hacerlo, te asegurarás de que los valores dependientes de la fórmula se recalculen y los valores correctos se rendericen en el PDF.

{{% /alert %}}
