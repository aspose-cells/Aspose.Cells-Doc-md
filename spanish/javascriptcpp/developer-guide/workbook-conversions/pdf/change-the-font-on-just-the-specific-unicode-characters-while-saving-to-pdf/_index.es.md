---
title: Cambiar la fuente solo en caracteres Unicode específicos al guardar como PDF con JavaScript vía C++
linktitle: Cambiar la fuente solo de los caracteres Unicode específicos al guardar en PDF
type: docs
weight: 260
url: /es/javascript-cpp/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/
description: Aprende cómo cambiar la fuente de caracteres Unicode específicos al guardar en PDF usando Aspose.Cells for JavaScript vía C++. 
---

{{% alert color="primary" %}} 

Algunos caracteres Unicode no se pueden mostrar con la fuente especificada por el usuario. Uno de estos caracteres Unicode es **Guión no separable** (U+2011) y su número Unicode es 8209. Este carácter no se puede mostrar con **Times New Roman**, pero se puede mostrar con otras fuentes como **Arial Unicode MS**.

Cuando aparece un carácter así dentro de alguna palabra o frase en una fuente específica como Times New Roman, Aspose.Cells cambia toda la fuente de la palabra o frase a una que pueda mostrar ese carácter, como Arial Unicode o MS.

Sin embargo, este comportamiento no es deseado para algunos usuarios y solo quieren que la fuente de ese carácter específico cambie en lugar de toda la palabra o frase.

Para solucionar este problema, Aspose.Cells ofrece la propiedad `PdfSaveOptions.isFontSubstitutionCharGranularity` que debe establecerse en true para que solo la fuente de los caracteres no visibles sea cambiada a una fuente visible, mientras que el resto de la palabra o frase permanecen en la fuente original.

{{% /alert %}} 

## **Ejemplo**
La siguiente captura de pantalla compara los dos PDF generados por el código de muestra a continuación.

Una se genera sin configurar la propiedad `PdfSaveOptions.isFontSubstitutionCharGranularity` y la otra después de establecerla en true.

Como se puede ver en el primer PDF, la fuente de toda la frase cambió de Times New Roman a Arial Unicode MS debido al guion no separable. Mientras que en el segundo PDF, solo cambió la fuente del guion no separable.

|**Primer archivo PDF**|
| :- |
|![todo:image_alt_text](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_1.png)|


|**Segundo archivo PDF**|
| :- |
|![todo:image_alt_text](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_2.png)|
### **Código de muestra**


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
        <a id="downloadLink1" style="display: none; margin-right: 10px;">Download Result PDF 1</a>
        <a id="downloadLink2" style="display: none;">Download Result PDF 2</a>
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

        document.getElementById('runExample').addEventListener('click', async () => {
            const resultDiv = document.getElementById('result');
            resultDiv.innerHTML = '<p>Running example...</p>';

            // Create workbook object
            const workbook = new Workbook();

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access cells
            const cell1 = worksheet.cells.get("A1");
            const cell2 = worksheet.cells.get("B1");

            // Set the styles of both cells to Times New Roman
            let style = cell1.style;
            style.font.name = "Times New Roman";
            cell1.style = style;
            cell2.style = style;

            // Put the values inside the cell
            cell1.value = "Hello without Non-Breaking Hyphen";
            cell2.value = "Hello" + String.fromCharCode(8209) + " with Non-Breaking Hyphen";

            // Autofit the columns
            worksheet.autoFitColumns();

            // Save to Pdf without setting PdfSaveOptions.IsFontSubstitutionCharGranularity
            const outputData1 = workbook.save(SaveFormat.Pdf);
            const blob1 = new Blob([outputData1]);
            const downloadLink1 = document.getElementById('downloadLink1');
            downloadLink1.href = URL.createObjectURL(blob1);
            downloadLink1.download = 'SampleOutput_out.pdf';
            downloadLink1.style.display = 'inline-block';
            downloadLink1.textContent = 'Download SampleOutput_out.pdf';

            // Save to Pdf after setting PdfSaveOptions.IsFontSubstitutionCharGranularity to true
            const opts = new PdfSaveOptions();
            opts.isFontSubstitutionCharGranularity = true;
            const outputData2 = workbook.save(SaveFormat.Pdf, opts);
            const blob2 = new Blob([outputData2]);
            const downloadLink2 = document.getElementById('downloadLink2');
            downloadLink2.href = URL.createObjectURL(blob2);
            downloadLink2.download = 'SampleOutput2_out.pdf';
            downloadLink2.style.display = 'inline-block';
            downloadLink2.textContent = 'Download SampleOutput2_out.pdf';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Use the download links to get the generated PDFs.</p>';
        });
    </script>
</html>
```
