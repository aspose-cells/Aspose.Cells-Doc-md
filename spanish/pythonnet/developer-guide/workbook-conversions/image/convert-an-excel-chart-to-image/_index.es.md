---
title: Convertir un gráfico de Excel a imagen
type: docs
weight: 20
url: /es/python-net/convert-an-excel-chart-to-image/
description: Convertir un Gráfico de Excel a Imagen utilizando Aspose.Cells para la API de Python via .NET.
keywords: Python Convertir un gráfico de Excel a imagen, Exportar un gráfico de Excel a imagen en Python via NET, Python Guardar un gráfico de Excel como imagen.
---

{{% alert color="primary" %}}

Los gráficos son visualmente atractivos y facilitan que los usuarios vean comparaciones, patrones y tendencias en los datos. Por ejemplo, en lugar de analizar columnas de números de una hoja de cálculo, un gráfico muestra de un vistazo si las ventas están cayendo o subiendo, o cómo se comparan las ventas reales con las proyectadas. A menudo se pide a las personas que presenten información estadística y gráfica de manera fácil de entender y fácil de mantener. Una imagen ayuda.

A veces, es necesario incluir gráficos en una aplicación o páginas web. O puede ser necesario para un documento de Word, un archivo PDF, una presentación de PowerPoint u otra aplicación. En cada caso, desea representar el gráfico como una imagen para que pueda usarlo en otro lugar.

{{% /alert %}}

## **Convertir gráficos a imágenes**

En los ejemplos aquí, se convierte un gráfico circular y un gráfico de columnas a imágenes.

### **Convertir un gráfico circular a un archivo de imagen**

Primero, cree un gráfico de pastel en Microsoft Excel y luego conviértalo en un archivo de imagen con Aspose.Cells para Python via .NET. El código en este ejemplo crea una imagen EMF basada en el gráfico de pastel en la plantilla del archivo de Excel de Microsoft.

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

Alojamos nuestros paquetes de Python en repositorios PyPi.

Instale Aspose.Cells para Python desde pypi, use el comando: $ pip install aspose-cells-python.

Y también puedes seguir las instrucciones paso a paso sobre cómo instalar Aspose.Cells para Python via .NET en tu entorno de desarrollo.
1. Descargue e instale Aspose.Cells para Python via .NET:
   1. Instalar Aspose.Cells para Python via .NET desde [pypi](https://pypi.org/project/aspose-cells-python/), utilizando el comando: $ pip install aspose-cells-python.
   1. Y también puedes seguir las [instrucciones paso a paso](https://docs.aspose.com/cells/python-net/getting-started/) sobre cómo instalar "Aspose.Cells para Python via .NET" en tu entorno de desarrollo.

Todos los componentes [Aspose](http://www.aspose.com/) funcionan en modo de evaluación cuando se instalan por primera vez. El modo de evaluación no tiene límite de tiempo y solo inserta marcas de agua en los documentos de salida.

1. Cree un proyecto:
   1. Inicie Visual Studio.
   1. Agregue una referencia de biblioteca (importe la biblioteca) a su proyecto de Python.
   1. Escribir el código que encuentra y convierte el gráfico. A continuación se muestra el código utilizado por el componente para llevar a cabo la tarea. Se utilizan muy pocas líneas de código.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ConvertingPieChartToImageFile-1.py" >}}

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

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ConvertingColumnChartToImage-1.py" >}}
