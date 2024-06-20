---
title: Creación de informe tabular
type: docs
weight: 70
url: /es/reportingservices/creating-tabular-report/
---

{{% alert color="primary" %}} 

Una tabla en una plantilla de informe Aspose.Cells consiste en un encabezado, filas de datos de la tabla, grupos de filas y pies de página. A continuación, se muestra una tabla de ejemplo.

**Un ejemplo de tabla** 

![todo:image_alt_text](creating-tabular-report_1.png)
#### **Encabezado de tabla**
El encabezado de la tabla normalmente contiene el título de cada columna de la tabla y otros elementos de texto como texto estático, parámetros de informe, variables de informe global, etc. El encabezado de la tabla es opcional. Si se utiliza un encabezado, la etiqueta de encabezado debe colocarse a la izquierda de la primera columna de datos de la tabla para indicar que la fila es un encabezado.
#### **Fila de datos de la tabla**
Una fila de datos de la tabla es una fila de celdas que contienen marcadores inteligentes. Una tabla solo puede contener una fila de datos.
#### **Grupo de filas**
El grupo de filas sigue de cerca a la fila de datos de la tabla y comprende dos partes: etiqueta de grupo y fila de datos de grupo. 

La etiqueta de grupo debe colocarse a la izquierda de la primera columna de datos de la tabla para indicar que la fila es la fila de datos del grupo. El formato de la etiqueta de grupo es ##group{GroupColumn}, por ejemplo, ##group{SalesOrderNumber} donde SalesOrderNumber es uno de los nombres de columna del conjunto de datos. Una tabla solo puede contener un grupo de filas, pero un grupo de filas puede contener más de una fila de datos de grupo. La etiqueta de grupo solo se puede colocar en la primera fila de datos, como se muestra en el ejemplo anterior.

La etiqueta de grupo se elimina del archivo de Microsoft Excel de salida en el momento de la representación. Los grupos de filas son opcionales.
#### **Pies de página**
Los pies de página vienen después del grupo de filas e incluyen tres partes: etiqueta de pie de página, fila de datos de pie de página y área de texto del pie de página. 

La etiqueta de pie de página debe colocarse a la izquierda de la primera columna de la columna de datos de la tabla que indica que la fila es el pie de página de la tabla. Una tabla puede contener más de una fila de datos de pie de página y cada fila de pie de página debe estar marcada con una etiqueta de pie de página. 

El área de texto del pie de página puede contener texto estático, parámetros de informe y variables de informe global, como se muestra en el ejemplo anterior.

La etiqueta de pie de página se elimina del archivo de Microsoft Excel de salida en el momento de la representación. Los pies de página son opcionales.

La salida de la plantilla de muestra se muestra a continuación.

**Plantilla de muestra** 

![todo:image_alt_text](creating-tabular-report_2.png)

{{% /alert %}} 
###### **Esta sección incluye los siguientes temas:** 
- [Preparando para crear informe de tabla](/cells/es/reportingservices/preparing-for-creating-table-report/)
- [Agregando información base para la tabla](/cells/es/reportingservices/adding-base-information-for-table/)
- [Agregando fórmulas de Servicios de Informes](/cells/es/reportingservices/adding-reporting-services-formulas/)
- [Agregando Grupo de Tabla](/cells/es/reportingservices/adding-table-group/)
- [Agregando pies de tabla](/cells/es/reportingservices/adding-table-footers/)
- [Agregando parámetros de informe al informe](/cells/es/reportingservices/adding-report-parameters-to-report/)
- [Agregando variables globales de Servicios de Informes al informe](/cells/es/reportingservices/adding-reporting-services-global-variables-to-report/)
- [Estableciendo atributos del informe](/cells/es/reportingservices/setting-report-attributes/)
- [Modificando atributos del informe](/cells/es/reportingservices/modifying-report-attributes/)
