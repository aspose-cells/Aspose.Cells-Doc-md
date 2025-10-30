---
title: Cómo insertar una imagen en una celda
type: docs
weight: 130
url: /es/javascript-cpp/how-to-insert-picture-in-cell/
description: Aprenda cómo insertar una imagen en una celda con Aspose.Cells for JavaScript vía C++.
keywords: Cómo insertar una imagen en una celda, insertar una imagen sobre celdas, colocar una imagen en una celda, colocar una imagen sobre celdas, Cómo colocar una imagen en una celda, Cómo colocar una imagen sobre celdas, Cambiar entre Imagen en celda y Imagen sobre celdas, Cambiar entre Lugar en celda y Lugar sobre celdas
---

## **Escenarios de uso posibles**
La imagen agrega un toque de brillo a tu hoja de cálculo y proporciona una representación visual del contenido. También facilitan la comprensión de los datos y la generación de ideas. Aunque ha sido posible utilizar imágenes en Excel durante muchos años, Excel solo recientemente ha habilitado la función de que las imágenes se conviertan en valores de celda reales. Incluso si se modifica el diseño del dibujo, seguirá vinculado a los datos. ¡Puedes usarlo en tablas, ordenar, filtrar, incluir en fórmulas, y más!

## **Cómo insertar una imagen en una celda utilizando Excel**
Acerca de cómo insertar una imagen en una celda en Excel, sigue estos pasos:

1. Ve a la pestaña Insertar y haz clic en la opción Imágenes.
2. Selecciona **Colocar en celda**. Selecciona una de las siguientes fuentes en el menú desplegable Insertar imagen de (**Este dispositivo**, **Imágenes de stock** y **Imágenes en línea**). Este dispositivo para insertar una imagen desde tu dispositivo. Imágenes de stock para insertar una imagen desde imágenes de stock. Imágenes en línea para insertar una imagen desde la web.
<br>
<img src="1.png" width=60% />
3. Selecciona la imagen e insértala en una celda.
<br>
<img src="8.png" width=60% />

## **Cómo insertar una imagen sobre celdas utilizando Excel**
Acerca de cómo insertar una imagen sobre celdas en Excel, sigue estos pasos:

1. Ve a la pestaña Insertar y haz clic en la opción Imágenes.
2. Selecciona **Colocar sobre celdas**. Selecciona una de las siguientes fuentes en el menú desplegable Insertar imagen de (**Este dispositivo**, **Imágenes de stock** y **Imágenes en línea**). Este dispositivo para insertar una imagen desde tu dispositivo. Imágenes de stock para insertar una imagen desde imágenes de stock. Imágenes en línea para insertar una imagen desde la web.
<br>
<img src="2.png" width=60% />
3. Selecciona la imagen e insértala sobre las celdas.
<br>
<img src="3.png" width=60% />

## **Cómo cambiar de Imagen en celda a Imagen sobre celdas utilizando Excel**
Puedes cambiar fácilmente de **Imagen en celda** a **Imagen sobre celdas**. Sigue estos pasos, por favor:
1. Haz clic derecho en la celda y selecciona **Imagen en celda** > **Colocar sobre celdas**. 
<br>
<img src="4.png" width=60% />
2. El resultado después de cambiar es el siguiente:
<br>
<img src="5.png" width=60% />

## **Cómo cambiar de Imagen sobre celdas a Imagen en celda utilizando la biblioteca de Excel Aspose.Cells para Python**
Puede cambiar fácilmente de **Imagen sobre celdas** a **Imagen en celda**. Siga estos pasos:
1. Haga clic derecho en la imagen y seleccione **Insertar en celda**. 
<br>
<img src="6.png" width=60% />
2. El resultado después de cambiar es el siguiente:
<br>
<img src="7.png" width=60% />

## **Cómo insertar una imagen en una celda usando Aspose.Cells for JavaScript vía C++**
Insertar imagen en celda usando Aspose.Cells. Consulte el siguiente código de ejemplo. Después de ejecutar el código de ejemplo, se insertará una imagen en una celda.
1. Instanciar un objeto Workbook. 
2. Obtener la celda donde desea insertar la imagen.
3. Establecer la propiedad Cell.EmbeddedImage. 
4. Finalmente, guarda el libro en formato [XLSX de salida](out.xlsx). 

## **Código de muestra**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Embed Image into New Workbook</h1>
        <p>Select an image file to embed into cell D8. A new workbook will be created with "Apple" in A2.</p>
        <input type="file" id="imageInput" accept="image/*" />
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
            const imageInput = document.getElementById('imageInput');
            const resultDiv = document.getElementById('result');

            // Create a new workbook
            const workbook = new Workbook();
            const cells = workbook.worksheets.get(0).cells;

            // Set A2 value to "Apple"
            const a2 = cells.get("A2");
            a2.value = "Apple";

            // Get D8 cell
            const d8 = cells.get("D8");

            // If an image file is selected, read it and embed into D8
            if (imageInput.files.length) {
                const file = imageInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                const imgBuf = new Uint8Array(arrayBuffer);
                d8.embeddedImage = imgBuf;
            }

            // Save workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Workbook created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
