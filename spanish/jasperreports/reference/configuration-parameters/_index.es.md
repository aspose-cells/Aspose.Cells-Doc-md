---
title: Parámetros de configuración
type: docs
weight: 10
url: /es/jasperreports/configuration-parameters/
---
{{% alert color="primary" %}} 

 La siguiente tabla enumera los parámetros de configuración.

{{% /alert %}} 

|**Nombre del parámetro** |**Descripción** |
|:- |:- |
| FORMATO_TIPO| Se puede configurar en "EXCEL97TO2003" o "EXCEL2007" para generar archivos de formato Microsoft Excel 79 0 2003 o Excel 2007.|
|ES_UNA_PÁGINA_POR_ SÁBANA| Un valor booleano que especifica si cada página del informe debe escribirse en una hoja de trabajo XLS diferente.|
|ES_RETIRAR_VACÍO_ESPACIO_ ENTRE_FILAS| Un valor booleano que especifica si los espacios vacíos que pueden aparecer entre filas deben eliminarse o no.|
|ES_RETIRAR_VACÍO_ESPACIO_ ENTRE_COLUMNAS| Un valor booleano que especifica si los espacios vacíos que pueden aparecer entre columnas deben eliminarse o no.|
|ES_BLANCO_ FONDO DE LA PÁGINA| Un valor booleano que especifica si el fondo de la página debe ser blanco o el color de fondo XLS predeterminado. El color de fondo XLS puede variar según las propiedades del visor XLS o el esquema de color del sistema operativo.|
|ES_DETECTAR_ TIPO DE CÉLULA| Marca utilizada para indicar si el exportador debe tener en cuenta el tipo de las expresiones del campo de texto original y establecer los tipos y valores de celda en consecuencia.|
| HOJA_NOMBRES|Una matriz de cadenas que representan nombres de hojas personalizados. Esto es útil cuando se usa con el IS_UNA_PÁGINA_POR_ parámetro HOJA.|
|ES_FUENTE_TALLA_ARREGLAR_ ACTIVADO|Indicador para disminuir el tamaño de fuente para que el texto se ajuste a la altura de celda especificada.|
|MÁXIMO_FILAS_ POR HOJA| Un valor entero que especifica el número máximo de filas que se pueden mostrar en una hoja. Cuando se establece, se crea una nueva hoja para que se muestren las filas restantes. Los valores negativos o cero significa que no se ha establecido ningún límite.|
|ES_PASAR POR ALTO_ GRÁFICOS| Indicador para ignorar elementos gráficos y exportar solo elementos de texto.|
|ES_COLAPSAR_ ROW_SPAN| Marque para colapsar el intervalo de filas y evite fusionar celdas entre filas.|
|ES_PASAR POR ALTO_ CELL_BORDER| Indicador para ignorar el borde de la celda.|
|ES_USAR_ EXCEL_CHART| Marcar para usar un gráfico editable en formato Excel Microsoft en lugar de imágenes estáticas. El valor por defecto es verdadero.|

