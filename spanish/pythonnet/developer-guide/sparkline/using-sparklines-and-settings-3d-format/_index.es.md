---
title: Usando mini gráficos y configuraciones de formato 3D
type: docs
weight: 40
url: /es/python-net/using-sparklines-and-settings-3d-format/
---

## **Usando Sparklines**
Microsoft Excel 2010 puede analizar la información de más maneras que nunca. Permite a los usuarios realizar un seguimiento y resaltar tendencias importantes de datos con nuevas herramientas de análisis y visualización de datos. Las sparklines son mini gráficos que se pueden colocar dentro de las celdas para que puedas ver los datos y el gráfico en la misma tabla. Cuando se usan sparklines de manera adecuada, el análisis de datos es más rápido y preciso. También proporcionan una vista simple de la información, evitando hojas de cálculo sobrecargadas con una gran cantidad de gráficos ocupados.

Aspose.Cells para Python via .NET proporciona una API para manipular mini gráficos en hojas de cálculo.
### **Sparklines en Microsoft Excel**
Para insertar sparklines en Microsoft Excel 2010:

1. Selecciona las celdas donde quieres que aparezcan las sparklines. Para que sean fáciles de ver, selecciona las celdas al lado de los datos.
1. Haz clic en **Insertar** en la cinta y luego elige **columna** en el grupo de **Sparklines**.
1. Seleccione o ingrese el rango de celdas en la hoja de cálculo que contenga los datos fuente. Los gráficos aparecerán.

Los mini gráficos le ayudan a ver tendencias, por ejemplo, el registro de victorias o derrotas de una liga de softball. Incluso pueden resumir toda la temporada de cada equipo en la liga.
### **Mini gráficos usando Aspose.Cells para Python via .NET**
Los desarrolladores pueden crear, eliminar o leer mini gráficos (en el archivo de plantilla) usando la API proporcionada por Aspose.Cells para Python via .NET. Las clases que gestionan los mini gráficos están contenidas en el espacio de nombres [aspose.cells.charts](https://reference.aspose.com/cells/python-net/aspose.cells.charts), por lo que debes importar este espacio antes de usar estas funciones.

Al agregar gráficos personalizados para un determinado rango de datos, los desarrolladores tienen la libertad de agregar diferentes tipos de gráficos pequeños a áreas de celdas seleccionadas.

El siguiente ejemplo demuestra la función de Sparklines. El ejemplo muestra cómo:

1. Abrir un archivo de plantilla simple.
1. Leer la información de sparklines para una hoja de cálculo.
1. Agregar nuevas miniaturas para un rango de datos dado a un área de celdas.
1. Guarde el archivo de Excel en disco.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Sparklines-UsingSparklines-1.py" >}}
## **Configuración de formato 3D**
Es posible que necesites estilos de gráficos 3D para obtener solo los resultados para tu escenario. Aspose.Cells para Python via .NET proporciona la API relevante para aplicar el formato 3D de Microsoft Excel 2007.

A continuación se muestra un ejemplo completo para demostrar cómo crear un gráfico y aplicar el formato 3D de Microsoft Excel 2007. Después de ejecutar el código de ejemplo, se agregará un gráfico de columnas (con efectos 3D) a la hoja de cálculo.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Sparklines-Applying3DFormat-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
