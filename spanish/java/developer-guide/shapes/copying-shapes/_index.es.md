---
title: Copiar formas entre hojas de trabajo
type: docs
weight: 250
url: /es/java/copy-shapes-between-worksheets/
---
{{% alert color="primary" %}}

A veces, necesita copiar diferentes imágenes, gráficos y otros objetos de dibujo en diferentes hojas de trabajo según sus requisitos. Aspose.Cells admite la copia de formas entre hojas de trabajo. Los gráficos, imágenes y otros objetos se copian con el mayor grado de precisión.

Puede probar la automatización de oficinas, pero eso tiene sus propios inconvenientes. Hay varias razones y problemas involucrados: por ejemplo, seguridad, estabilidad, escalabilidad, velocidad, precio y características. En resumen, hay muchas razones, siendo la principal que Microsoft recomienda enfáticamente contra la automatización de Office de las soluciones de software.

En este artículo, creamos una aplicación de consola, realizamos la copia de imágenes, gráficos y otros objetos de dibujo entre hojas de trabajo de un libro de trabajo con unas pocas y más simples líneas de código usando Aspose.Cells.

Este documento está diseñado para proporcionar a los desarrolladores una comprensión detallada de cómo copiar formas (imágenes, gráficos, controles y otros objetos de dibujo) entre hojas de trabajo.

{{% /alert %}}

## **Copiar formas**

Este artículo explica cómo:

- [Copie una imagen de una hoja de trabajo a otra](/cells/es/java/copy-shapes-between-worksheets/#copying-a-picture-from-one-worksheet-to-another).
- [Copie un gráfico de una hoja de cálculo a otra](/cells/es/java/copy-shapes-between-worksheets/#task-2-copying-a-chart-from-one-worksheet-to-another).
- [Copie controles y otros objetos de dibujo de una hoja de cálculo a otra](/cells/es/java/copy-shapes-between-worksheets/#task-3-copying-controls-and-other-drawing-objects-from-one-worksheet-to-another).

### **Copiar una imagen de una hoja de trabajo a otra**

#### **Paso 1: Creación de un libro de trabajo con imagen y gráfico en Microsoft Excel**

1. Creó un nuevo libro de trabajo en Microsoft Excel.
1. Agregue una imagen en la primera hoja de trabajo y un gráfico en la segunda hoja de trabajo.

 Las siguientes capturas de pantalla muestran las dos plantillas de hojas de trabajo creadas en Microsoft Excel.

   **Hoja de trabajo "Gráfico" con gráfico**

![todo:imagen_alternativa_texto](copy-shapes-between-worksheets_1.png)

**Hoja de trabajo "Imagen" con imagen**

![todo:imagen_alternativa_texto](copy-shapes-between-worksheets_2.png)

Ahora, copie la imagen en la hoja de trabajo llamada "Imagen" a la última hoja de trabajo "Resultado".

#### **Paso 2: Descarga Aspose.Cells.Zip**

1. [Descargar Aspose.Cells for Java](https://downloads.aspose.com/cells/java).
1. Descomprímalo en su computadora de desarrollo.

 Todos[Aspose](http://www.aspose.com/) Los componentes, cuando están instalados, funcionan en modo de evaluación. El modo de evaluación no tiene límite de tiempo y solo inyecta marcas de agua en los documentos producidos.

#### **Paso 3: crea un proyecto**

Puede crear un proyecto usando algún editor Java, por ejemplo, Eclipse o crear un programa simple usando un Bloc de notas.

#### **Paso 4: agregar ruta de clase**

Para establecer una ruta de clase usando Eclipse, realice los siguientes pasos:

1. Extraiga Aspose.Cells.jar y dom4j_1.6.1.jar de Aspose.Cells.zip.
1. Establezca el classpath del proyecto en Eclipse:
1. Seleccione su proyecto en Eclipse y luego haga clic en los menús Proyecto-Propiedades.
1. Seleccione "Java Ruta de compilación" en el lado izquierdo de la ventana emergente, luego seleccione la pestaña "Bibliotecas", haga clic en "Agregar JAR" o "Agregar JAR externos" para seleccionar Aspose.Cells.jar y dom4j_1.6.1.jar y agregarlos a la compilación rutas.
1. Escriba una aplicación para invocar las API de los componentes de Aspose.

O puede configurarlo en tiempo de ejecución en el indicador de DOS en Windows. Por ejemplo:

javac -classpath %classpath%;e:\Aspose.Cells.jar; ClassName .javajava -classpath %classpath%;e:\Aspose.Cells.jar; Nombre de la clase

#### **Paso 5: Copiar una imagen de una hoja de trabajo a otra**

A continuación se muestra el código para realizar la tarea. Copia una imagen de la hoja de trabajo denominada "Imagen" a la hoja de trabajo "Resultado".

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyPicturefromOneWorksheetToAnother-CopyPicturefromOneWorksheetToAnother.java" >}}

#### **Resultado Tarea 1:**

Después de ejecutar el código anterior, la imagen de la hoja de trabajo "Imagen" ahora se copia a la última hoja de trabajo "Resultado"

**Hoja de trabajo "Resultado" con imagen copiada**

![todo:imagen_alternativa_texto](copy-shapes-between-worksheets_3.png)

### **Tarea 2: Copiar un gráfico de una hoja de cálculo a otra**

#### **Paso 1: copie un gráfico de una hoja de trabajo a otra**

A continuación se muestra el código real utilizado por el componente para realizar la tarea.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyChartFromOneWorksheetToAnother-CopyChartFromOneWorksheetToAnother.java" >}}

#### **Resultado Tarea 2**

Después de ejecutar el código anterior, el gráfico de la hoja de trabajo "Gráfico" se copia en la hoja de trabajo "Resultado". Consulte la siguiente instantánea de la hoja de trabajo resultante.

**Hoja de trabajo "Resultado" con imagen y gráfico copiados**

![todo:imagen_alternativa_texto](copy-shapes-between-worksheets_4.png)

### **Tarea 3: Copiar controles y otros objetos de dibujo de una hoja de cálculo a otra**

**Hoja de trabajo "Control" con cuadro de texto y óvalo**

![todo:imagen_alternativa_texto](copy-shapes-between-worksheets_5.png)

Consulte los siguientes pasos simples que debe realizar para obtener los resultados deseados.

#### **Paso 1: Copiar una hoja de trabajo entre libros de trabajo**

El siguiente es el código utilizado por el componente para realizar la tarea.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyWorksheetBetweenWorkbooks-CopyWorksheetBetweenWorkbooks.java" >}}

#### **Resultado Tarea 3**

Después de ejecutar el código anterior, los controles de la hoja de trabajo "Control" ahora se copian en la hoja de trabajo "Resultado". Por favor, vea la siguiente instantánea de "Resultado".

**Hoja de cálculo "Resultado" con cuadro de texto copiado y óvalo**

![todo:imagen_alternativa_texto](copy-shapes-between-worksheets_6.png)

## **Conclusión**

Este artículo ha mostrado cómo copiar diferentes formas como imágenes, gráficos y otros objetos de dibujo entre el uso de Aspose.Cells. Con suerte, le dará una idea y podrá utilizar estas opciones de acuerdo con sus diferentes escenarios.

Aspose.Cells puede ofrecer más flexibilidad que otras soluciones y proporciona una velocidad, eficiencia y confiabilidad sobresalientes para cumplir con los requisitos de aplicaciones comerciales específicas. Los resultados muestran que Aspose.Cells se ha beneficiado de años de investigación, diseño y ajuste cuidadoso.

 Agradecemos sus consultas, comentarios y sugerencias en el[Aspose.Cells Foro](https://forum.aspose.com/c/cells/9).
