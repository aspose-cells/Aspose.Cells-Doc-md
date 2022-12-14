---
title: Crear informe tabular
type: docs
weight: 70
url: /es/reportingservices/creating-tabular-report/
---
{{% alert color="primary" %}} 

Una tabla en una plantilla de informe Aspose.Cells consta de un encabezado, filas de datos de tabla, grupos de filas y pies de página. A continuación se muestra una tabla de muestra.

**una tabla de ejemplo** 

![todo:imagen_alternativa_texto](creating-tabular-report_1.png)
#### **Encabezado de tabla**
El encabezado de la tabla normalmente contiene el título de cada columna de la tabla y otros elementos de texto, como texto estático, parámetros de informe, variables de informe global, etc. El encabezado de la tabla es opcional. Si usa un encabezado, la etiqueta del encabezado debe colocarse a la izquierda de la primera columna de datos de la tabla para indicar que la fila es un encabezado.
#### **Fila de datos de la tabla**
Una fila de datos de tabla es una fila de celdas que contienen marcadores inteligentes. Una tabla solo puede contener una única fila de datos.
#### **Grupo de filas**
El grupo de filas sigue de cerca a la fila de datos de la tabla y consta de dos partes: etiqueta de grupo y fila de datos de grupo.

La etiqueta de grupo debe colocarse a la izquierda de la primera columna de datos de la tabla para indicar que la fila es la fila de datos del grupo de filas. El formato de la etiqueta de grupo es ##group{GroupColumn}, por ejemplo ##group{SalesOrderNumber} donde SalesOrderNumber es uno de los nombres de columna del conjunto de datos. Una tabla solo puede contener un grupo de filas, pero un grupo de filas puede contener más de una fila de datos de grupo. La etiqueta de grupo se puede colocar solo en la primera fila de datos, como se muestra en el ejemplo anterior.

La etiqueta de grupo se elimina del archivo de Excel de salida Microsoft en el momento de la representación. Los grupos de filas son opcionales.
#### **Pies de página**
 Los pies de página vienen después del grupo de filas e incluyen tres partes: etiqueta de pie de página, fila de datos de pie de página y área de texto de pie de página.

La etiqueta de pie de página debe colocarse a la izquierda de la primera columna de la columna de datos de la tabla que indica que la fila es el pie de página de la tabla. Una tabla puede contener más de una fila de datos de pie de página y cada fila de pie de página debe estar marcada con una etiqueta de pie de página.

El área de texto del pie de página puede contener texto estático, parámetros de informe y variables de informe globales, como se muestra en el ejemplo anterior.

La etiqueta de pie de página se elimina del archivo de Excel de salida Microsoft en el momento de la representación. Los pies de página son opcionales.

El resultado de la plantilla de muestra se muestra a continuación.

**Plantilla de muestra** 

![todo:imagen_alternativa_texto](creating-tabular-report_2.png)

{{% /alert %}} 
###### **Esta sección incluye los siguientes temas:**
- [Preparación para crear un informe de tabla](/cells/es/reportingservices/preparing-for-creating-table-report/)
- [Adición de información base para la tabla](/cells/es/reportingservices/adding-base-information-for-table/)
- [Adición de fórmulas de Reporting Services](/cells/es/reportingservices/adding-reporting-services-formulas/)
- [Agregar grupo de tablas](/cells/es/reportingservices/adding-table-group/)
- [Adición de pies de página de tabla](/cells/es/reportingservices/adding-table-footers/)
- [Adición de parámetros de informe al informe](/cells/es/reportingservices/adding-report-parameters-to-report/)
- [Adición de variables globales de Reporting Services al informe](/cells/es/reportingservices/adding-reporting-services-global-variables-to-report/)
- [Configuración de atributos de informe](/cells/es/reportingservices/setting-report-attributes/)
- [Modificación de atributos de informe](/cells/es/reportingservices/modifying-report-attributes/)
