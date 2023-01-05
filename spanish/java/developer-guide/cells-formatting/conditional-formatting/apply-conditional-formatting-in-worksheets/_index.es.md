---
title: Aplicar formato condicional en hojas de trabajo
type: docs
weight: 40
url: /es/java/apply-conditional-formatting-in-worksheets/
---
{{% alert color="primary" %}}

Este artículo está diseñado para proporcionar una comprensión detallada de cómo agregar formato condicional a un rango de celdas en una hoja de trabajo.

El formato condicional es una función avanzada en Microsoft Excel que le permite aplicar formatos a un rango de celdas y hacer que ese formato cambie según el valor de la celda o el valor de una fórmula. Por ejemplo, el fondo de una celda puede ser rojo para resaltar un valor negativo o el color del texto puede ser verde para un valor positivo. Cuando el valor de la celda cumple la condición de formato, se aplica el formato. Si el valor de la celda no cumple con la condición de formato, se utiliza el formato predeterminado de la celda.

Es posible aplicar formato condicional con Microsoft Office Automation pero eso tiene sus inconvenientes. Hay varias razones y problemas involucrados: por ejemplo, seguridad, estabilidad, escalabilidad y velocidad. La razón principal para encontrar otra solución es que Microsoft recomienda encarecidamente que no se utilice la automatización de oficinas para las soluciones de software.

Este artículo muestra cómo crear una aplicación de consola, agregar formato condicional en celdas con unas pocas líneas de código simples usando Aspose.Cells API.

{{% /alert %}}

## **Trabajar con formato condicional**

Este artículo funciona a través de las siguientes tareas:

1. [Usando Aspose.Cells para aplicar formato condicional basado en el valor de la celda](/cells/es/java/apply-conditional-formatting-in-worksheets/#task-1-using-asposecells-to-apply-conditional-formatting-based-on-cell-value).
1. [Usando Aspose.Cells para aplicar formato condicional basado en una fórmula](/cells/es/java/apply-conditional-formatting-in-worksheets/#task-2-using-asposecells-to-apply-conditional-formatting-based-on-a-formula).

### **Tarea 1: uso de Aspose.Cells para aplicar formato condicional basado en el valor Cell**

1. **Descargue e instale Aspose.Cells.zip**:
   1. [Descargar](https://downloads.aspose.com/cells/java) Aspose.Cells for Java.
 1. Descomprímalo en su computadora de desarrollo.
 Todos los componentes Aspose, cuando están instalados, funcionan en modo de evaluación. El modo de evaluación no tiene límite de tiempo y solo inyecta marcas de agua en los documentos producidos.
1. **crear un proyecto**.
 Cree un proyecto usando un editor Java como Eclipse o cree un programa simple usando un editor de texto.
1. **Agregar ruta de clase**.
 Para establecer una ruta de clase usando Eclipse, realice los siguientes pasos:
1. Extraiga Aspose.Cells.jar y dom4j_1.6.1.jar de Aspose.Cells.zip.
 1. Establezca el classpath del proyecto en Eclipse:
 1. Seleccione su proyecto en Eclipse y luego seleccione**Propiedades** desde el**Proyecto** menú.
 1. Seleccione "Java Build Path" a la izquierda del cuadro de diálogo.
 1. En el**bibliotecas** pestaña, seleccione**Agregar JAR** o**Agregar JAR externos** para seleccionar Aspose.Cells.jar y dom4j_1.6.1.jar y agregarlos a las rutas de compilación.
 1. Escriba una aplicación para invocar las API de los componentes de Aspose.
 O puede configurar la ruta en tiempo de ejecución en un indicador de DOS en Windows.

{{< highlight "java" >}}

  javac -classpath %classpath%;e:\Aspose.Cells.jar;  ClassName .javajava -classpath %classpath%;e:\Aspose.Cells.jar;  ClassName  

{{< /highlight >}}

1. **Aplicar formato condicional basado en el valor de la celda**.
 A continuación se muestra el código utilizado por el componente para realizar la tarea. Aplica formato condicional en una celda.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ConditionalFormattingOnCellValue-ApplyConditionalFormattingOnCellValue.java" >}}

Cuando se ejecuta el código anterior, se aplica formato condicional a la celda "A1" en la primera hoja de trabajo del archivo de salida (output.xls). El formato condicional aplicado a A1 depende del valor de la celda. Si el valor de la celda de A1 está entre 50 y 100, el color de fondo es rojo debido al formato condicional aplicado. Consulte las siguientes capturas de pantalla del archivo XLS generado.

**Salida de archivo de Excel con valor A1 inferior a 50**

![todo:imagen_alternativa_texto](apply-conditional-formatting-in-worksheets_1.png)

**Salida archivo Excel con A1 entre 50 y 100**

![todo:imagen_alternativa_texto](apply-conditional-formatting-in-worksheets_2.png)

### **Tarea 2: uso de Aspose.Cells para aplicar formato condicional basado en una fórmula**

1. **Aplicar formato condicional según la fórmula**.
 A continuación se muestra el código real utilizado por el componente para realizar la tarea. Aplica formato condicional en "B3".

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ConditionalFormattingBasedOnFormula-ConditionalFormattingBasedOnFormula.java" >}}

Cuando se ejecuta el código anterior, se aplica formato condicional a la celda "B3" en la primera hoja de trabajo del archivo de salida (output.xls). El formato condicional aplicado depende de la fórmula que calcula el valor de "B3" como la suma de B1 y B2. Consulte las siguientes capturas de pantalla del archivo XLS generado.

**Salida de archivo de Excel con valor B3 inferior a 100**

![todo:imagen_alternativa_texto](apply-conditional-formatting-in-worksheets_3.png)

**Archivo de salida de Excel con B3 mayor que 100**

![todo:imagen_alternativa_texto](apply-conditional-formatting-in-worksheets_4.png)

### **Conclusión**

{{% alert color="primary" %}}

Este artículo muestra cómo aplicar el formato condicional a las celdas de una hoja de trabajo con Aspose.Cells API. Con suerte, le dará una idea para que pueda usar estas opciones en sus propios escenarios.

Aspose.Cells ofrece una gran flexibilidad para las soluciones y brinda una velocidad, eficiencia y confiabilidad sobresalientes para cumplir con los requisitos específicos de las aplicaciones comerciales. Aspose.Cells se beneficia de años de investigación, diseño y ajuste cuidadoso.

 Agradecemos sus consultas, comentarios y sugerencias en el[Aspose.Cells Foro](https://forum.aspose.com/c/cells/9). Garantizamos una pronta respuesta.

{{% /alert %}}
