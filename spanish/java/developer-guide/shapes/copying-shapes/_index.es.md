---
title: Copiar Formas entre Hojas de Cálculo
type: docs
weight: 250
url: /es/java/copy-shapes-between-worksheets/
---

{{% alert color="primary" %}}

A veces, es necesario copiar diferentes imágenes, gráficos y otros objetos de dibujo a diferentes hojas de cálculo según sus requerimientos. Aspose.Cells admite la copia de formas entre hojas de cálculo. Los gráficos, imágenes y otros objetos se copian con el más alto grado de precisión.

Podrías intentar la Automatización de Office, pero esto tiene sus propias desventajas. Hay varias razones e problemas involucrados: por ejemplo seguridad, estabilidad, escalabilidad, velocidad, precio y características. En resumen, hay muchas razones, siendo la principal que Microsoft en sí mismo desaconseja fuertemente la automatización de Office desde soluciones de software.

En este artículo, creamos una aplicación de consola, realizamos la copia de imágenes, gráficos y otros objetos de dibujo entre hojas de cálculo de un libro con unas pocas y simples líneas de código usando Aspose.Cells.

Este documento está diseñado para proporcionar a los desarrolladores un entendimiento detallado sobre cómo copiar formas (imágenes, gráficos, controles y otros objetos de dibujo) entre hojas de cálculo.

{{% /alert %}}

## **Copia de Formas**

Este artículo explica cómo:

- [Copiar una imagen de una hoja de cálculo a otra](/cells/es/java/copy-shapes-between-worksheets/#copying-a-picture-from-one-worksheet-to-another).
- [Copiar un gráfico de una hoja de cálculo a otra](/cells/es/java/copy-shapes-between-worksheets/#task-2-copying-a-chart-from-one-worksheet-to-another).
- [Copiar controles y otros objetos de dibujo de una hoja de cálculo a otra](/cells/es/java/copy-shapes-between-worksheets/#task-3-copying-controls-and-other-drawing-objects-from-one-worksheet-to-another).

### **Copiar una Imagen de una Hoja de Cálculo a Otra**

#### **Paso 1: Crear un libro con una imagen y un gráfico en Microsoft Excel**

1. Crear un nuevo libro en Microsoft Excel.
1. Agregar una imagen en la primera hoja de cálculo y un gráfico en la segunda hoja de cálculo.

   Las siguientes capturas de pantalla muestran las dos hojas de cálculo plantilla creadas en Microsoft Excel.

   **Hoja de Cálculo 'Gráfico' con gráfico**

![todo:image_alt_text](copy-shapes-between-worksheets_1.png)

**Hoja de Cálculo 'Imagen' con imagen**

![todo:image_alt_text](copy-shapes-between-worksheets_2.png)

Ahora, copia la imagen en la hoja de trabajo llamada “Imagen” a la última hoja de trabajo “Resultado”.

#### **Paso 2: Descargar Aspose.Cells.Zip**

1. [Descargar Aspose.Cells for Java](https://downloads.aspose.com/cells/java).
1. Descomprímelo en tu computadora de desarrollo.

   Todos los componentes [Aspose](http://www.aspose.com/), cuando se instalan, funcionan en modo de evaluación. El modo de evaluación no tiene límite de tiempo y solo inserta marcas de agua en los documentos producidos.

#### **Paso 3: Crear un proyecto**

Puedes crear un proyecto usando un editor de Java, por ejemplo, Eclipse, o crear un programa simple usando NotePad.

#### **Paso 4: Agregar la ruta de clase**

Para configurar una Ruta de Clase usando Eclipse, por favor realiza los siguientes pasos:

1. Extrae Aspose.Cells.jar y dom4j_1.6.1.jar de Aspose.Cells.zip.
1. Configura la ruta de clase del proyecto en Eclipse:
1. Selecciona tu proyecto en Eclipse y luego haz clic en Proyecto-Propiedades en los menús.
1. Selecciona "Ruta de compilación de Java" en el lado izquierdo de la ventana emergente, luego selecciona la pestaña "Bibliotecas", haz clic en "Agregar archivos JAR" o "Agregar archivos JAR externos" para seleccionar Aspose.Cells.jar y dom4j_1.6.1.jar y agregarlos a las rutas de compilación.
1. Escribe una aplicación para invocar las API de los componentes de Aspose.

O puedes configurarlo en tiempo de ejecución en el símbolo del sistema en Windows. Por ejemplo:

javac -classpath %classpath%;e:\Aspose.Cells.jar; ClassName .javajava -classpath %classpath%;e:\Aspose.Cells.jar; ClassName

#### **Paso 5: Copiar una imagen de una hoja de cálculo a otra**

A continuación se presenta el código para realizar la tarea. Copia una imagen de la hoja de trabajo llamada “Imagen” a la hoja de trabajo “Resultado”.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyPicturefromOneWorksheetToAnother-CopyPicturefromOneWorksheetToAnother.java" >}}

#### **Tarea de Resultados 1:**

Después de ejecutar el código anterior, la imagen de la hoja de trabajo “Imagen” ahora se ha copiado en la última hoja de trabajo “Resultado”

**Hoja de trabajo 'Resultado' con imagen copiada**

![todo:image_alt_text](copy-shapes-between-worksheets_3.png)

### **Tarea 2: Copiar un gráfico de una hoja de trabajo a otra**

#### **Paso 1: Copiar un gráfico de una hoja de trabajo a otra**

A continuación se muestra el código real utilizado por el componente para llevar a cabo la tarea.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyChartFromOneWorksheetToAnother-CopyChartFromOneWorksheetToAnother.java" >}}

#### **Resultado Tarea 2**

Después de ejecutar el código anterior, se copia el gráfico de la hoja de trabajo 'Gráfico' a la hoja de trabajo 'Resultado'. Por favor, vea la siguiente captura de pantalla de la hoja de trabajo resultante.

**Hoja de trabajo 'Resultado' con imagen y gráfico copiados**

![todo:image_alt_text](copy-shapes-between-worksheets_4.png)

### **Tarea 3: Copiar controles y otros objetos de dibujo de una hoja de trabajo a otra**

**Hoja de trabajo 'Control' con cuadro de texto y óvalo**

![todo:image_alt_text](copy-shapes-between-worksheets_5.png)

Por favor, vea los siguientes pasos sencillos que debe realizar para obtener los resultados deseados.

#### **Paso 1: Copiar una hoja de trabajo entre libros de trabajo**

A continuación se muestra el código utilizado por el componente para llevar a cabo la tarea.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyWorksheetBetweenWorkbooks-CopyWorksheetBetweenWorkbooks.java" >}}

#### **Resultado Tarea 3**

Después de ejecutar el código anterior, los controles de la hoja de trabajo 'Control' ahora están copiados en la hoja de trabajo 'Resultado'. Por favor, vea la siguiente captura de pantalla de 'Resultado'.

**Hoja de trabajo 'Resultado' con cuadro de texto y óvalo copiados**

![todo:image_alt_text](copy-shapes-between-worksheets_6.png)

## **Conclusión**

Este artículo ha mostrado cómo copiar diferentes formas como imágenes, gráficos y otros objetos de dibujo utilizando Aspose.Cells. Con suerte, esto le dará una idea y podrá utilizar estas opciones según sus diferentes escenarios.

Aspose.Cells puede ofrecer más flexibilidad que otros para soluciones y proporciona una velocidad, eficiencia y confiabilidad sobresalientes para cumplir con los requisitos específicos de aplicaciones comerciales. Los resultados muestran que Aspose.Cells ha obtenido beneficios de años de investigación, diseño y ajustes cuidadosos.

Recibimos con gusto sus consultas, comentarios y sugerencias en el [Foro de Aspose.Cells](https://forum.aspose.com/c/cells/9).
