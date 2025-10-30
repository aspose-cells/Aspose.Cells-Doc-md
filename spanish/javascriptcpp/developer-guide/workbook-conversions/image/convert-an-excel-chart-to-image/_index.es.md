---
title: Convertir un gráfico de Excel a imagen con JavaScript mediante C++
linktitle: Convertir un gráfico de Excel a imagen
type: docs
weight: 20
url: /es/javascript-cpp/convert-an-excel-chart-to-image/
description: Aprenda a convertir gráficos de Excel a imágenes usando Aspose.Cells for JavaScript via C++.
---

{{% alert color="primary" %}}  

Los gráficos son visualmente atractivos y facilitan que los usuarios vean comparaciones, patrones y tendencias en los datos. Por ejemplo, en lugar de analizar columnas de números de una hoja de cálculo, un gráfico muestra de un vistazo si las ventas están cayendo o subiendo, o cómo se comparan las ventas reales con las proyectadas. A menudo se pide a las personas que presenten información estadística y gráfica de manera fácil de entender y fácil de mantener. Una imagen ayuda.  

A veces, se necesitan gráficos en una aplicación o páginas web. O puede que se necesiten para un documento Word, un archivo PDF, una presentación PowerPoint u otra aplicación. En cada caso, quieres renderizar el gráfico como una imagen para poder usarlo en otro lugar.  

{{% /alert %}}  

## **Convertir gráficos a imágenes**  

En los ejemplos aquí, un gráfico circular y un gráfico de columnas se convierten en imágenes.  

### **Convertir un gráfico circular a un archivo de imagen**  

Primero, cree un gráfico circular en Microsoft Excel y luego conviértalo en un archivo de imagen con Aspose.Cells for JavaScript via C++. El código en este ejemplo crea una imagen EMF basada en el gráfico circular en el archivo de Excel de plantilla.  

|**Salida: imagen del gráfico circular**|  
| :- |  
|![todo:image_alt_text](convert-an-excel-chart-to-image_1.png)|  

1. Crear un gráfico circular en Microsoft Excel:  
   1. Abra un nuevo libro en Microsoft Excel.  
   1. Ingrese algunos datos en una hoja de cálculo.  
   1. Crear un gráfico circular basado en los datos.  
   1. Guarde el archivo.  

|**El archivo de entrada.**|  
| :- |  
|![todo:image_alt_text](convert-an-excel-chart-to-image_2.png)|  

1. Descargue e instale Aspose.Cells:  
   1. [Descargue Aspose.Cells for JavaScript via C++](https://downloads.aspose.com/cells/javascript-cpp).  
   1. Instálelo en su equipo de desarrollo.  

Todos los componentes [Aspose](http://www.aspose.com/) funcionan en modo de evaluación cuando se instalan por primera vez. El modo de evaluación no tiene límite de tiempo y solo inserta marcas de agua en los documentos de salida.  

1. Cree un proyecto:  
   1. Inicia tu IDE preferido.  
   1. Cree una nueva aplicación de consola. Este ejemplo usa una aplicación JavaScript, pero puede crearla usando cualquier entorno de ejecución de JavaScript.  
   1. Agregue una referencia. Este proyecto utiliza Aspose.Cells, así que añada una referencia a Aspose.Cells for JavaScript via C++.  
   1. Escribir el código que encuentra y convierte el gráfico. A continuación se muestra el código utilizado por el componente para llevar a cabo la tarea. Se utilizan muy pocas líneas de código.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Convert Chart to Image Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the designer chart (first chart) in the first worksheet of the workbook.
            const chart = workbook.worksheets.get(0).charts.get(0);

            // Convert the chart to an image (EMF) and prepare download link
            const imageData = chart.toImage(AsposeCells.ImageType.Emf);
            const blob = new Blob([imageData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'PieChart.out.emf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Chart Image';

            document.getElementById('result').innerHTML = '<p style="color: green;">Chart converted to EMF successfully! Click the download link to get the image.</p>';
        });
    </script>
</html>
```  

### **Convirtiendo un Gráfico de Columnas a un Archivo de Imagen**  

Primero, cree un gráfico de columnas en Microsoft Excel y conviértalo en un archivo de imagen, como se mencionó anteriormente. Después de ejecutar el código de ejemplo, se crea un archivo JPEG basado en el gráfico de columnas en el archivo de Excel plantilla.  

|**Archivo de salida: una imagen de gráfico de columnas.**|  
| :- |  
|![todo:image_alt_text](convert-an-excel-chart-to-image_3.png)|  

1. Crear un gráfico de columnas en Microsoft Excel:  
   1. Abra un nuevo libro en Microsoft Excel.  
   1. Ingrese algunos datos en una hoja de cálculo.  
   1. Cree un gráfico de columnas basado en los datos.  
   1. Guarde el archivo.  

|**Archivo de entrada.**|  
| :- |  
|![todo:image_alt_text](convert-an-excel-chart-to-image_4.png)|  

1. Configure un proyecto, con referencias, como se describe arriba.  
1. Convierta dinámicamente el gráfico en una imagen. A continuación se muestra el código utilizado por el componente para completar la tarea. El código es similar al anterior:  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Convert Chart to Image</title>
    </head>
    <body>
        <h1>Convert Chart to Image</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ImageType, Utils } = AsposeCells;

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

            // Get the designer chart (first chart) in the first worksheet of the workbook.
            const chart = workbook.worksheets.get(0).charts.get(0);

            // Convert the chart to an image (JPEG)
            const imageData = await chart.toImage(ImageType.Jpeg);

            // Create a Blob and provide a download link
            const blob = new Blob([imageData], { type: 'image/jpeg' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'ColumnChart.out.jpeg';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Chart Image';

            document.getElementById('result').innerHTML = '<p style="color: green;">Chart converted to image successfully! Click the download link to get the image.</p>';
        });
    </script>
</html>
```
