---
title: Aplicar formato condicional en hojas de cálculo
type: docs
weight: 40
url: /es/java/apply-conditional-formatting-in-worksheets/
---

{{% alert color="primary" %}}

Este artículo está diseñado para proporcionar una comprensión detallada de cómo agregar formato condicional a un rango de celdas en una hoja de cálculo.

El formato condicional es una función avanzada en Microsoft Excel que le permite aplicar formatos a un rango de celdas, y tener ese formato cambie dependiendo del valor de la celda o el valor de una fórmula. Por ejemplo, el fondo de una celda puede ser rojo para resaltar un valor negativo, o el color del texto podría ser verde para un valor positivo. Cuando el valor de la celda cumple con la condición del formato, se aplica el formato. Si el valor de la celda no cumple con la condición de formato, se utiliza el formato predeterminado de la celda.

Es posible aplicar formato condicional con la Automatización de Office de Microsoft, pero eso tiene sus desventajas. Hay varias razones y problemas involucrados, como la seguridad, la estabilidad, la escalabilidad y la velocidad. La razón principal para encontrar otra solución es que Microsoft en sí mismo recomienda fuertemente en contra de la Automatización de Office para soluciones de software.

Este artículo muestra cómo crear una aplicación de consola, agregar formato condicional a las celdas con algunas líneas de código más simples utilizando la API de Aspose.Cells.

{{% /alert %}}

## **Trabajando con Formato Condicional**

Este artículo explica las siguientes tareas:

1. [Usar Aspose.Cells para aplicar formato condicional basado en el valor de la celda](/cells/es/java/apply-conditional-formatting-in-worksheets/#task-1-using-asposecells-to-apply-conditional-formatting-based-on-cell-value).
1. [Usar Aspose.Cells para aplicar formato condicional basado en una fórmula](/cells/es/java/apply-conditional-formatting-in-worksheets/#task-2-using-asposecells-to-apply-conditional-formatting-based-on-a-formula).

### **Tarea 1: Usar Aspose.Cells para aplicar formato condicional basado en el valor de la celda**

1. **Descargar e instalar Aspose.Cells.zip**:
   1. [Descargar](https://downloads.aspose.com/cells/java) Aspose.Cells for Java.
   1. Descomprímelo en tu computadora de desarrollo.
      Todos los componentes de Aspose, cuando se instalan, funcionan en modo de evaluación. El modo de evaluación no tiene límite de tiempo y solo inyecta marcas de agua en los documentos producidos.
1. **Crear un proyecto**.
   Ya sea crear un proyecto usando un Editor de Java como Eclipse o crear un programa simple usando un editor de texto.
1. **Agregar ruta de clases**.
   Para configurar una Ruta de Clase usando Eclipse, por favor realiza los siguientes pasos:
   1. Extrae Aspose.Cells.jar y dom4j_1.6.1.jar de Aspose.Cells.zip.
   1. Configura la ruta de clase del proyecto en Eclipse:
      1. Selecciona tu proyecto en Eclipse y luego selecciona **Propiedades** desde el menú **Proyecto**.
      1. Seleccione "Java Build Path" a la izquierda del cuadro de diálogo.
      1. En la pestaña **Libraries**, seleccione **Add JARs** o **Add External JARs** para seleccionar Aspose.Cells.jar y dom4j_1.6.1.jar y agregarlos a las rutas de construcción.
   1. Escribe una aplicación para invocar las API de los componentes de Aspose.
      O puede configurar la ruta en tiempo de ejecución en un símbolo del sistema en Windows.

{{< highlight java >}}

  javac -classpath %classpath%;e:\Aspose.Cells.jar;  ClassName .javajava -classpath %classpath%;e:\Aspose.Cells.jar;  ClassName  

{{< /highlight >}}

1. **Aplicar formato condicional basado en el valor de la celda**.
   A continuación se muestra el código utilizado por el componente para lograr la tarea. Aplica formato condicional en una celda.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ConditionalFormattingOnCellValue-ApplyConditionalFormattingOnCellValue.java" >}}

Cuando se ejecuta el código anterior, se aplica formato condicional a la celda "A1" en la primera hoja de cálculo del archivo de salida (output.xls). El formato condicional aplicado a A1 depende del valor de la celda. Si el valor de la celda de A1 está entre 50 y 100, el color de fondo es rojo debido al formato condicional aplicado. Consulte las siguientes capturas de pantalla del archivo XLS generado.

**Archivo Excel de salida con valor de A1 menor que 50**

![todo:image_alt_text](apply-conditional-formatting-in-worksheets_1.png)

**Archivo Excel de salida con valor de A1 entre 50 y 100**

![todo:image_alt_text](apply-conditional-formatting-in-worksheets_2.png)

### **Tarea 2: Usar Aspose.Cells para Aplicar Formato Condicional Basado en una Fórmula**

1. **Aplicar formato condicional dependiendo de una fórmula**.
   A continuación se muestra el código real utilizado por el componente para lograr la tarea. Aplica formato condicional en “B3”.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ConditionalFormattingBasedOnFormula-ConditionalFormattingBasedOnFormula.java" >}}

Cuando se ejecuta el código anterior, se aplica formato condicional a la celda "B3" en la primera hoja de cálculo del archivo de salida (output.xls). El formato condicional aplicado depende de la fórmula que calcula el valor de "B3" como la suma de B1 y B2. Consulte las siguientes capturas de pantalla del archivo XLS generado.

**Archivo Excel de salida con valor de B3 menor que 100**

![todo:image_alt_text](apply-conditional-formatting-in-worksheets_3.png)

**Archivo Excel de salida con valor de B3 mayor que 100**

![todo:image_alt_text](apply-conditional-formatting-in-worksheets_4.png)

### **Conclusión**

{{% alert color="primary" %}}

Este artículo muestra cómo aplicar formato condicional a las celdas en una hoja de cálculo con la API de Aspose.Cells. Con suerte, le dará una idea para que pueda usar estas opciones en sus propios escenarios.

Aspose.Cells ofrece una gran flexibilidad para soluciones y proporciona una velocidad, eficiencia y confiabilidad sobresalientes para cumplir con requisitos específicos de aplicaciones empresariales. Aspose.Cells se beneficia de años de investigación, diseño y ajuste cuidadoso.

Damos la bienvenida a sus consultas, comentarios y sugerencias en el [Foro de Aspose.Cells](https://forum.aspose.com/c/cells/9). Garantizamos una pronta respuesta.

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
