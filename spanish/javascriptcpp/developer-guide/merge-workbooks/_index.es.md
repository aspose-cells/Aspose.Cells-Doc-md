---
title: Combina varios libros de trabajo en un solo libro con JavaScript a través de C++
linktitle: Combinar libros de trabajo
type: docs
weight: 66
url: /es/javascript-cpp/combine-multiple-workbooks-into-a-single-workbook/
description: Aprende cómo combinar múltiples libros de trabajo en un solo libro usando Aspose.Cells for JavaScript a través de C++. 
---

{{% alert color="primary" %}}

A veces, necesitas combinar libros de trabajo con contenido variado como imágenes, gráficos y datos en un solo libro. Aspose.Cells for JavaScript a través de C++ soporta esta función. Este artículo muestra cómo crear una aplicación de consola y combinar libros de trabajo con unas pocas líneas de código sencillas usando Aspose.Cells.

{{% /alert %}}

## **Combinar libros de trabajo con imágenes y gráficos**

El código de ejemplo combina dos libros de trabajo en un solo libro usando Aspose.Cells for JavaScript a través de C++. El código carga los libros de trabajo de origen, usa el método [**Workbook.combine(Workbook)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#combine-workbook-) para combinarlos y guarda el libro de trabajo de salida.

### **Libros de trabajo de origen**

- [charts.xlsx](5473097.xlsx)
- [picture.xlsx](5473096.xlsx)

### **Libros de trabajo de salida**

- [combined.xlsx](5473095.xlsx)

### **Capturas de pantalla**

A continuación se muestran capturas de pantalla de los libros de trabajo de origen y de salida.

{{% alert color="primary" %}}

Puede utilizar cualquier libro de trabajo de origen. Estas imágenes son solo con fines ilustrativos.

{{% /alert %}}

**La primera hoja de cálculo del libro de trabajo de gráficos: apilada** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_1.jpg)

**Segunda hoja de cálculo del libro de trabajo de gráficos: línea** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_2.jpg)

**Primera hoja de cálculo del libro de trabajo de imagen: imagen** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_3.jpg)

**Las tres hojas de cálculo en el libro de trabajo combinado: apilada, línea, imagen** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_4.jpg)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Combine Workbooks Example</title>
    </head>
    <body>
        <h1>Combine Workbooks Example</h1>
        <p>Select two Excel files to combine:</p>
        <input type="file" id="fileInput1" accept=".xls,.xlsx" />
        <input type="file" id="fileInput2" accept=".xls,.xlsx" />
        <button id="runExample">Combine Workbooks</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell } = AsposeCells;

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
            const fileInput1 = document.getElementById('fileInput1');
            const fileInput2 = document.getElementById('fileInput2');

            if (!fileInput1.files.length || !fileInput2.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select two Excel files.</p>';
                return;
            }

            const file1 = fileInput1.files[0];
            const file2 = fileInput2.files[0];

            const arrayBuffer1 = await file1.arrayBuffer();
            const arrayBuffer2 = await file2.arrayBuffer();

            // Open the first excel file.
            const sourceBook1 = new Workbook(new Uint8Array(arrayBuffer1));

            // Open the second excel file.
            const sourceBook2 = new Workbook(new Uint8Array(arrayBuffer2));

            // Combining the two workbooks
            sourceBook1.combine(sourceBook2);

            // Save the combined workbook and provide download link
            const outputData = sourceBook1.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Combined.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Combined Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbooks combined successfully! Click the download link to get the combined file.</p>';
        });
    </script>
</html>
```

## **Temas avanzados**
- [Combinar múltiples hojas de cálculo en una sola hoja de cálculo](/cells/es/javascript-cpp/combine-multiple-worksheets-into-a-single-worksheet/)
- [Fusionar archivos](/cells/es/javascript-cpp/merge-files/)
