---
title: Convertir un gráfico de Excel en imagen
type: docs
weight: 20
url: /es/net/convert-an-excel-chart-to-image/
---
{{% alert color="primary" %}}

Los gráficos son visualmente atractivos y facilitan que los usuarios vean comparaciones, patrones y tendencias en los datos. Por ejemplo, en lugar de analizar columnas de números de hojas de trabajo, un gráfico muestra de un vistazo si las ventas están cayendo o subiendo, o cómo se comparan las ventas reales con las ventas proyectadas. Con frecuencia se pide a las personas que presenten información estadística y gráfica de una manera fácil de entender y de mantener. Una imagen ayuda.

A veces, se necesitan gráficos en una aplicación o páginas web. O puede ser necesario para un documento de Word, un archivo PDF, una presentación PowerPoint o alguna otra aplicación. En cada caso, desea representar el gráfico como una imagen para poder usarlo en cualquier otro lugar.

{{% /alert %}}

## **Convertir gráficos en imágenes**

En los ejemplos aquí, un gráfico circular y un carácter de columna se convierten en imágenes.

### **Convertir un gráfico circular en un archivo de imagen**

Primero, cree un gráfico circular en Microsoft Excel y luego conviértalo en un archivo de imagen con Aspose.Cells. El código de este ejemplo crea una imagen EMF basada en el gráfico circular en el archivo de plantilla Microsoft Excel.

|**Salida: imagen de gráfico circular**|
|:- |
|![todo:imagen_alternativa_texto](convert-an-excel-chart-to-image_1.png)|

1. Cree un gráfico circular en Microsoft Excel:
 1. Abrió un nuevo libro de trabajo en Microsoft Excel.
 1. Ingrese algunos datos en una hoja de trabajo.
 1. Creó un gráfico circular basado en los datos.
 1. Guarde el archivo.

|**El archivo de entrada.**|
|:- |
|![todo:imagen_alternativa_texto](convert-an-excel-chart-to-image_2.png)|

1. Descargar e instalar Aspose.Cells:
   1. [Descargar Aspose.Cells for .NET](https://downloads.aspose.com/cells/net).
 1. Instálelo en su computadora de desarrollo.

 Todos[Aspose](http://www.aspose.com/) los componentes funcionan en modo de evaluación cuando se instalan por primera vez. El modo de evaluación no tiene límite de tiempo y solo inyecta marcas de agua en los documentos de salida.

1. Crear un proyecto:
 1. Inicie Visual Studio.Net.
 1. Cree una nueva aplicación de consola. Este ejemplo usa una aplicación de consola C#, pero también puede usar VB.NET.
 1. Agregue una referencia. Este proyecto usa Aspose.Cells, así que agregue una referencia a Aspose.Cells, por ejemplo ...\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll
1. Escriba el código que encuentra y convierte el gráfico. A continuación se muestra el código utilizado por el componente para realizar la tarea. Se utilizan muy pocas líneas de código.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ConvertExcelChartToImage-ConvertingPieChartToImageFile-1.cs" >}}

### **Convertir un gráfico de columnas en un archivo de imagen**

Primero cree un gráfico de columnas en Microsoft Excel y conviértalo en un archivo de imagen, como se indica arriba. Después de ejecutar el código de muestra, se crea un archivo JPEG basado en el gráfico de columnas en el archivo de plantilla de Excel.

|**Archivo de salida: una imagen de gráfico de columnas.**|
|:- |
|![todo:imagen_alternativa_texto](convert-an-excel-chart-to-image_3.png)|

1. Cree un gráfico de columnas en Microsoft Excel:
 1. Abra un nuevo libro de trabajo en Microsoft Excel.
 1. Ingrese algunos datos en una hoja de trabajo.
 1. Cree un gráfico de columnas basado en los datos.
 1. Guarde el archivo.

|**Fichero de entrada.**|
|:- |
|![todo:imagen_alternativa_texto](convert-an-excel-chart-to-image_4.png)|

1. Configure un proyecto, con referencias, como se describe anteriormente.
1. Convierta el gráfico en una imagen dinámicamente. A continuación se muestra el código utilizado por el componente para realizar la tarea. El código es similar al anterior:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ConvertExcelChartToImage-ConvertingColumnChartToImage-1.cs" >}}
