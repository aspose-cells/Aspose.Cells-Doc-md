---
title: Convertir archivo XLS con imágenes o gráficos a PDF con JavaScript vía C++
linktitle: Convertir archivo XLS con imágenes o gráficos a PDF
type: docs
weight: 50
url: /es/javascript-cpp/convert-xls-file-with-images-or-charts-to-pdf/
---

{{% alert color="primary" %}} 

Aspose.Cells admite la conversión de archivos XLS que contienen imágenes y gráficos a documentos PDF. Aspose.Cells for JavaScript vía C++ puede trabajar independientemente para convertir una hoja de cálculo a PDF: no se requiere Aspose.PDF para JavaScript vía C++ para la conversión. El proceso puede realizarse en memoria ya que no depende de archivos XML temporales o intermediarios. Esto significa que archivos de Excel grandes, por ejemplo, que contienen imágenes, gráficos y otros objetos de dibujo, se pueden convertir rápida y eficientemente.

{{% /alert %}} 
## **Código de muestra**


```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Convert Excel to PDF Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to PDF</button>
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

            // Instantiating a Workbook object by opening the Excel file from the file input
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Save the workbook as PDF
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Output.out.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF generated successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}} 

Si la hoja de cálculo contiene fórmulas, es mejor llamar al método [Workbook.calculateFormula()](https://reference.aspose.com/cells/javascript-cpp/workbook/#calculateFormula--) justo antes de renderizar a PDF. Hacerlo asegura que los valores dependientes de la fórmula se recalculen y que los valores correctos se muestren en el PDF.

{{% /alert %}}
