---  
title: Convertir un gráfico de Excel a imagen con Node.js mediante C++  
linktitle: Convertir un gráfico de Excel a imagen  
type: docs  
weight: 20  
url: /es/nodejs-cpp/convert-an-excel-chart-to-image/  
description: Aprende cómo convertir gráficos de Excel a imágenes usando Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  

Los gráficos son visualmente atractivos y facilitan que los usuarios vean comparaciones, patrones y tendencias en los datos. Por ejemplo, en lugar de analizar columnas de números de una hoja de cálculo, un gráfico muestra de un vistazo si las ventas están cayendo o subiendo, o cómo se comparan las ventas reales con las proyectadas. A menudo se pide a las personas que presenten información estadística y gráfica de manera fácil de entender y fácil de mantener. Una imagen ayuda.  

A veces, se necesitan gráficos en una aplicación o páginas web. O puede que se necesiten para un documento Word, un archivo PDF, una presentación PowerPoint u otra aplicación. En cada caso, quieres renderizar el gráfico como una imagen para poder usarlo en otro lugar.  

{{% /alert %}}  

## **Convertir gráficos a imágenes**  

En los ejemplos aquí, un gráfico circular y un gráfico de columnas se convierten en imágenes.  

### **Convertir un gráfico circular a un archivo de imagen**  

Primero, crea un gráfico circular en Microsoft Excel y luego conviértelo en un archivo de imagen con Aspose.Cells for Node.js via C++. El código en este ejemplo crea una imagen EMF basada en el gráfico circular en el archivo Excel plantilla.  

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
   1. [Descarga Aspose.Cells for Node.js via C++](https://downloads.aspose.com/cells/nodejs-cpp).  
   1. Instálelo en su equipo de desarrollo.  

Todos los componentes [Aspose](http://www.aspose.com/) funcionan en modo de evaluación cuando se instalan por primera vez. El modo de evaluación no tiene límite de tiempo y solo inserta marcas de agua en los documentos de salida.  

1. Cree un proyecto:  
   1. Inicia tu IDE preferido.  
   1. Crea una nueva aplicación de consola. Este ejemplo usa una aplicación Node.js, pero puedes crearla usando cualquier entorno de ejecución JavaScript.  
   1. Agrega una referencia. Este proyecto usa Aspose.Cells, así que agrega una referencia a Aspose.Cells for Node.js via C++.  
   1. Escribir el código que encuentra y convierte el gráfico. A continuación se muestra el código utilizado por el componente para llevar a cabo la tarea. Se utilizan muy pocas líneas de código.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Open the existing excel file which contains the pie chart.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "PieChart.xlsx"));

// Get the designer chart (first chart) in the first worksheet of the workbook.
const chart = workbook.getWorksheets().get(0).getCharts().get(0);

// Convert the chart to an image file.
chart.toImage(path.join(dataDir, "PieChart.out.emf"), AsposeCells.ImageType.Emf);
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

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Open the existing excel file which contains the column chart.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "ColumnChart.xlsx"));

// Get the designer chart (first chart) in the first worksheet of the workbook.
const chart = workbook.getWorksheets().get(0).getCharts().get(0);

// Convert the chart to an image file.
chart.toImage(path.join(dataDir, "ColumnChart.out.jpeg"), AsposeCells.ImageType.Jpeg);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
