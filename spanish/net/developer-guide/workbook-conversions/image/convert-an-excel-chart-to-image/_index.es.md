---
title: Convertir un gráfico de Excel a imagen
type: docs
weight: 20
url: /es/net/convert-an-excel-chart-to-image/
---

{{% alert color="primary" %}}

Los gráficos son visualmente atractivos y facilitan que los usuarios vean comparaciones, patrones y tendencias en los datos. Por ejemplo, en lugar de analizar columnas de números de una hoja de cálculo, un gráfico muestra de un vistazo si las ventas están cayendo o subiendo, o cómo se comparan las ventas reales con las proyectadas. A menudo se pide a las personas que presenten información estadística y gráfica de manera fácil de entender y fácil de mantener. Una imagen ayuda.

A veces, es necesario incluir gráficos en una aplicación o páginas web. O puede ser necesario para un documento de Word, un archivo PDF, una presentación de PowerPoint u otra aplicación. En cada caso, desea representar el gráfico como una imagen para que pueda usarlo en otro lugar.

{{% /alert %}}

## **Convertir gráficos a imágenes**

En los ejemplos aquí, se convierte un gráfico circular y un gráfico de columnas a imágenes.

### **Convertir un gráfico circular a un archivo de imagen**

Primero, cree un gráfico circular en Microsoft Excel y luego conviértalo en un archivo de imagen con Aspose.Cells. El código de este ejemplo crea una imagen EMF basada en el gráfico circular en el archivo de plantilla de Microsoft Excel.

|**Salida: imagen del gráfico circular**|
| :- |
|![todo:image_alt_text](convert-an-excel-chart-to-image_1.png)|

1. Crear un gráfico circular en Microsoft Excel :
   1. Abrió un nuevo libro de trabajo en Microsoft Excel.
   1. Ingrese algunos datos en una hoja de cálculo.
   1. Crear un gráfico circular basado en los datos.
   1. Guarde el archivo.

|**El archivo de entrada.**|
| :- |
|![todo:image_alt_text](convert-an-excel-chart-to-image_2.png)|

1. Descargue e instale Aspose.Cells:
   1. [Descargar Aspose.Cells for .NET](https://downloads.aspose.com/cells/net).
   1. Instálelo en su equipo de desarrollo.

Todos los componentes [Aspose](http://www.aspose.com/) funcionan en modo de evaluación cuando se instalan por primera vez. El modo de evaluación no tiene límite de tiempo y solo inserta marcas de agua en los documentos de salida.

1. Cree un proyecto:
   1. Inicia Visual Studio.Net.
   1. Crear una nueva aplicación de consola. Este ejemplo utiliza una aplicación de consola C#, pero también se puede usar VB.NET.
   1. Agregar una referencia. Este proyecto utiliza Aspose.Cells, así que agregue una referencia a Aspose.Cells, por ejemplo ...\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll
   1. Escribir el código que encuentra y convierte el gráfico. A continuación se muestra el código utilizado por el componente para llevar a cabo la tarea. Se utilizan muy pocas líneas de código.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ConvertExcelChartToImage-ConvertingPieChartToImageFile-1.cs" >}}

### **Convirtiendo un Gráfico de Columnas a un Archivo de Imagen**

Primero cree un gráfico de columnas en Microsoft Excel y conviértalo en un archivo de imagen, como se muestra arriba. Después de ejecutar el código de ejemplo, se crea un archivo JPEG basado en el gráfico de columnas en el archivo de Excel de plantilla.

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

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ConvertExcelChartToImage-ConvertingColumnChartToImage-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
