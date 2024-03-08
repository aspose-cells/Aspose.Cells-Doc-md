---
title: Convertir un gráfico de Excel en una imagen
type: docs
weight: 20
url: /es/python-net/convert-an-excel-chart-to-image/
description: Convierta un gráfico de Excel en una imagen utilizando Aspose.Cells for Python via .NET API.
keywords: Python Convert an Excel Chart to Image, Export an Excel Chart to Image in Python via NET, Python Save an Excel Chart to Image.
---
{{% alert color="primary" %}}

Los gráficos son visualmente atractivos y facilitan a los usuarios ver comparaciones, patrones y tendencias en los datos. Por ejemplo, en lugar de analizar columnas de números de hojas de cálculo, un gráfico muestra de un vistazo si las ventas están cayendo o aumentando, o cómo se comparan las ventas reales con las ventas proyectadas. Con frecuencia se pide a las personas que presenten información estadística y gráfica de una manera fácil de entender y mantener. Una imagen ayuda.

A veces, se necesitan gráficos en una aplicación o páginas web. O podría ser necesario para un documento de Word, un archivo PDF, una presentación PowerPoint o alguna otra aplicación. En cada caso, desea representar el gráfico como una imagen para poder utilizarlo en otro lugar.

{{% /alert %}}

##  **Convertir gráficos en imágenes**

En los ejemplos aquí, un gráfico circular y un carácter de columna se convierten en imágenes.

###  **Convertir un gráfico circular en un archivo de imagen**

Primero, cree un gráfico circular en Microsoft Excel y luego conviértalo en un archivo de imagen con Aspose.Cells for Python via .NET. El código de este ejemplo crea una imagen EMF basada en el gráfico circular de la plantilla Microsoft del archivo Excel.

|**Salida: imagen de gráfico circular**|
| :- |
|![todo:image_alt_text](convert-an-excel-chart-to-image_1.png)|

1. Cree un gráfico circular en Microsoft Excel:
 1. Abrió un nuevo libro en Microsoft Excel.
 1. Ingrese algunos datos en una hoja de trabajo.
 1. Creó un gráfico circular basado en los datos.
 1. Guarde el archivo.

|**El archivo de entrada.**|
| :- |
|![todo:image_alt_text](convert-an-excel-chart-to-image_2.png)|

Alojamos nuestros paquetes Python en repositorios PyPi.

Instale Aspose.Cells for Python desde pypi, use el comando como: $ pip install aspose-cells-python.

Y también puede seguir las instrucciones paso a paso sobre cómo instalar “Aspose.Cells for Python via .NET” en su entorno de desarrollador.
1. Descargue e instale Aspose.Cells for Python via .NET:
 1. Instale Aspose.Cells for Python via .NET desde[pipi](https://pypi.org/project/aspose-cells-python/)use el comando como: $ pip install aspose-cells-python.
 1. Y también puedes seguir el[instrucciones paso a paso](https://docs.aspose.com/cells/python-net/getting-started/)sobre cómo instalar "Aspose.Cells for Python via .NET" en su entorno de desarrollador.

 Todo[Aspose](http://www.aspose.com/) Los componentes funcionan en modo de evaluación cuando se instalan por primera vez. El modo de evaluación no tiene límite de tiempo y solo inyecta marcas de agua en los documentos de salida.

1. Crear un proyecto:
 1. Inicie Visual Studio.
 1. Agregue una referencia de biblioteca (importe la biblioteca) a su proyecto Python.
 1. Escriba el código que busca y convierte el gráfico. A continuación se muestra el código utilizado por el componente para realizar la tarea. Se utilizan muy pocas líneas de código.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ConvertingPieChartToImageFile-1.py" >}}

###  **Convertir un gráfico de columnas en un archivo de imagen**

Primero cree un gráfico de columnas en Microsoft Excel y conviértalo en un archivo de imagen, como se muestra arriba. Después de ejecutar el código de muestra, se crea un archivo JPEG basado en el gráfico de columnas en el archivo de plantilla de Excel.

|**Archivo de salida: una imagen de gráfico de columnas.**|
| :- |
|![todo:image_alt_text](convert-an-excel-chart-to-image_3.png)|

1. Cree un gráfico de columnas en Microsoft Excel:
 1. Abra un nuevo libro en Microsoft Excel.
 1. Ingrese algunos datos en una hoja de trabajo.
 1. Cree un gráfico de columnas basado en los datos.
 1. Guarde el archivo.

|**Fichero de entrada.**|
| :- |
|![todo:image_alt_text](convert-an-excel-chart-to-image_4.png)|

1. Configure un proyecto, con referencias, como se describe anteriormente.
1. Convierta el gráfico en una imagen dinámicamente. A continuación se muestra el código utilizado por el componente para realizar la tarea. El código es similar al anterior:

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ConvertingColumnChartToImage-1.py" >}}
