---
title: Actualizar Slicer con JavaScript a través de C++
linktitle: Actualización de Slicer
type: docs
weight: 50
url: /es/javascript-cpp/updating-slicer/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
description: Este artículo muestra cómo actualizar un slicer para filtrar los datos de la tabla dinámica o tabla vinculada usando Aspose.Cells for JavaScript via C++.
keywords: Aspose.Cells JavaScript via C++, Actualizar Slicer en JavaScript, cómo cambiar el slicer en JavaScript, cómo filtrar una tabla dinámica mediante slicer en JavaScript, Slicer selectItems, Slicer clearFilter, Slicer unselectItems.
---

## **Escenarios de uso posibles**
Actualizar un slicer significa filtrar los datos de la tabla dinámica o tabla a la que está conectado el slicer. Cuando selecciona o deselecciona elementos del slicer en Microsoft Excel, la tabla dinámica o tabla vinculada se recalcula en consecuencia. Con Aspose.Cells for JavaScript via C++, no necesita recorrer los elementos de la caché del slicer ni actualizar el slicer manualmente — el método [**Slicer.selectItems(labels, append)**](https://reference.aspose.com/cells/javascript-cpp/slicer/) actualiza el slicer y recalcula la tabla dinámica o tabla vinculada directamente a partir de los elementos de filtro:
- `Slicer.selectItems(labels, append)` — selecciona las etiquetas especificadas y recalcula la tabla dinámica o tabla vinculada. Cuando `append` es `true`, las etiquetas seleccionadas originalmente se conservan y las etiquetas especificadas se añaden a la selección; cuando `append` es `false`, todas las selecciones originales se borran y solo permanecen seleccionadas las etiquetas especificadas.
- `Slicer.unselectItems(labels)` — deselecciona parte de los elementos seleccionados actualmente.
- `Slicer.clearFilter()` — elimina el filtro y selecciona todos los elementos.

{{% alert color="primary" %}}
A partir de Aspose.Cells for JavaScript via C++ 26.10, la propiedad `SlicerCacheItem.selected` pasa a ser de solo lectura y su establecedor ya no se admite. Utilice los métodos `Slicer.selectItems`, `Slicer.unselectItems` y `Slicer.clearFilter` en lugar de establecer `SlicerCacheItem.selected` elemento por elemento.
{{% /alert %}}

## **Cómo actualizar el slicer**
El siguiente código de muestra carga el [archivo Excel de muestra](67338475.xlsx) que contiene un slicer existente conectado a una tabla dinámica. Selecciona solo los elementos "Blue" y "Pink" del slicer con `Slicer.selectItems(labels, false)` — la tabla dinámica se recalcula directamente a partir de los elementos de filtro, sin una llamada manual a `Slicer.refresh()`. A continuación, guarda el libro de trabajo como el [archivo Excel de salida](67338476.xlsx). La siguiente captura de pantalla muestra el efecto del código de muestra en el archivo Excel de muestra. Como puede ver en la captura de pantalla, la tabla dinámica muestra solo los elementos filtrados.
![todo:image_alt_text](updating-slicer_1.png)

## **Código de muestra**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Update Slicer</title>
    </head>
    <body>
        <h1>Update Slicer Example</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const ws = workbook.worksheets.get(0);

            // Access the first slicer inside the slicer collection
            const slicer = ws.slicers.get(0);

            // Select only "Blue" and "Pink"; the linked pivot table or table
            // is recalculated directly from the filter items
            slicer.selectItems(["Blue", "Pink"], false);

            // Save modified workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Slicer updated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

Conserve las etiquetas seleccionadas actualmente y seleccione elementos adicionales:

```javascript
// Keep the current selection and add "Red" to it.
slicer.selectItems(["Red"], true);
```

Deseleccione parte de los elementos seleccionados:

```javascript
// Remove "Pink" from the current selection.
slicer.unselectItems(["Pink"]);
```

Elimine el filtro (seleccione todos los elementos):

```javascript
// Clear the filter; all slicer items become selected again.
slicer.clearFilter();
```

{{< app/cells/assistant language="javascript-cpp" >}}