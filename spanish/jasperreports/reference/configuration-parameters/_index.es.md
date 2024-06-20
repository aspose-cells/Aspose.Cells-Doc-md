---
title: Parámetros de Configuración
type: docs
weight: 10
url: /es/jasperreports/configuration-parameters/
---

{{% alert color="primary" %}} 

La siguiente tabla enumera los parámetros de configuración. 

{{% /alert %}} 

|**Nombre del parámetro** |**Descripción** |
| :- | :- |
|FORMAT_TYPE |Puede establecerse en "EXCEL97TO2003" o "EXCEL2007" para generar archivos en formato Microsoft Excel 97-2003 o Excel 2007. |
|IS_ONE_PAGE_PER_SHEET |Un valor booleano que especifica si cada página del informe debe ser escrita en una hoja de trabajo XLS diferente. |
|IS_REMOVE_EMPTY_SPACE_BETWEEN_ROWS |Un valor booleano que especifica si los espacios en blanco que pueden aparecer entre las filas deben ser eliminados o no. |
|IS_REMOVE_EMPTY_SPACE_BETWEEN_COLUMNS |Un valor booleano que especifica si los espacios en blanco que pueden aparecer entre las columnas deben ser eliminados o no. |
|IS_WHITE_PAGE_BACKGROUND |Un valor booleano que especifica si el fondo de la página debe ser blanco o el color de fondo XLS predeterminado. El color de fondo XLS puede variar según las propiedades del visor XLS o el esquema de color del sistema operativo. |
|IS_DETECT_CELL_TYPE |Bandera utilizada para indicar si el exportador debe tener en cuenta el tipo de las expresiones de campo de texto originales y establecer los tipos de celda y valores en consecuencia. |
|SHEET_NAMES |Un arreglo de cadenas que representan nombres de hojas personalizadas. Esto es útil cuando se utiliza con el parámetro IS_ONE_PAGE_PER_SHEET. |
|IS_FONT_SIZE_FIX_ENABLED |Bandera para disminuir el tamaño de fuente para que el texto quepa en la altura de celda especificada. |
|MAXIMUM_ROWS_PER_SHEET |Un valor entero que especifica el número máximo de filas permitidas para mostrarse en una hoja. Cuando se establece, se crea una nueva hoja para mostrar las filas restantes. Los valores negativos o cero significan que no se ha establecido límite. |
|IS_IGNORE_GRAPHICS |Bandera para ignorar elementos gráficos y exportar solo elementos de texto. |
|IS_COLLAPSE_ROW_SPAN |Bandera para colapsar el espaciado de fila y evitar la fusión de celdas a través de filas. |
|IS_IGNORE_CELL_BORDER |Bandera para ignorar el borde de la celda. |
|IS_USE_EXCEL_CHART |Bandera para utilizar gráficos editables en formato Microsoft Excel en lugar de imágenes estáticas. El valor predeterminado es verdadero. |

