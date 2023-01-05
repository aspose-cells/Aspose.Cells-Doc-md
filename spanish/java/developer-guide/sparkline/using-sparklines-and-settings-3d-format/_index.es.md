---
title: Uso de minigráficos y configuración de formato 3D
type: docs
weight: 40
url: /es/java/using-sparklines-and-settings-3d-format/
---
## **Uso de minigráficos**
Microsoft Excel 2010 puede analizar la información de más formas que nunca. Permite a los usuarios rastrear y resaltar tendencias de datos importantes con nuevas herramientas de visualización y análisis de datos. Los minigráficos son minigráficos que puede colocar dentro de las celdas para poder ver los datos y el gráfico en la misma tabla. Cuando los minigráficos se utilizan correctamente, el análisis de datos es más rápido y más preciso. También brindan una vista simple de la información, evitando hojas de trabajo abarrotadas con muchos gráficos ocupados.

Aspose.Cells proporciona un API para manipular minigráficos en hojas de cálculo.
### **Minigráficos en Microsoft Excel**
Para insertar minigráficos en Microsoft Excel 2010:

1. Seleccione las celdas donde desea que aparezcan los minigráficos. Para que sean fáciles de ver, seleccione celdas al lado de los datos.
1.  Hacer clic**Insertar** en la cinta y luego elija**columna** en el**minigráficos** grupo.
1. Seleccione o ingrese el rango de celdas en la hoja de cálculo que contiene los datos de origen. Aparecerán los gráficos.

Los minigráficos lo ayudan a ver tendencias, por ejemplo, el récord de victorias o derrotas de una liga de softbol. Los minigráficos pueden incluso resumir la temporada completa de cada equipo de la liga.
### **Minigráficos usando Aspose.Cells**
 Los desarrolladores pueden crear, eliminar o leer minigráficos (en el archivo de plantilla) utilizando el API proporcionado por Aspose.Cells. Las clases que administran minigráficos están contenidas en el[Aspose.Cells.Charts](https://reference.aspose.com/cells/java/com.aspose.cells/Chart)espacio de nombres, por lo que debe importar este espacio de nombres antes de usar estas funciones.

Al agregar gráficos personalizados para un rango de datos dado, los desarrolladores tienen la libertad de agregar diferentes tipos de gráficos diminutos a áreas de celdas seleccionadas.

El siguiente ejemplo demuestra la función Minigráficos. El ejemplo muestra cómo:

1. Abra un archivo de plantilla simple.
1. Leer información de minigráficos para una hoja de trabajo.
1. Agregue nuevos minigráficos para un rango de datos dado a un área de celda.
1. Guarde el archivo de Excel en el disco.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-UsingSparkLine.java" >}}
## **Configuración del formato 3D**
Es posible que necesite estilos de gráficos en 3D para poder obtener solo los resultados de su escenario. Aspose.Cells proporciona el API relevante para aplicar Microsoft formato 3D de Excel 2007.

continuación se proporciona un ejemplo completo para demostrar cómo crear un gráfico y aplicar el formato 3D Microsoft Excel 2007. Después de ejecutar el código de ejemplo, se agregará un gráfico de columnas (con efectos 3D) a la hoja de trabajo.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-Applying3DFormat.java" >}}
