---
title: Informe Parametrizado
type: docs
weight: 60
url: /es/reportingservices/parameterized-report/
---

{{% alert color="primary" %}} 

Un *informe parametrizado* es un informe que acepta valores de entrada que se utilizan cuando se procesa el informe. 

Con un informe parametrizado, se puede variar la salida de un informe en función de los valores establecidos en tiempo de ejecución. Los Servicios de Informes admiten dos tipos de parámetros: parámetros de consulta y parámetros de informe. 

- **Los parámetros de consulta** se utilizan para seleccionar o filtrar datos durante el procesamiento de datos. Si se especifica un parámetro de consulta, se debe proporcionar un valor ya sea por el usuario o por propiedades predeterminadas para completar la instrucción SELECT o procedimiento almacenado que recupera los datos para un informe.
- **Los parámetros de informe** se utilizan durante el procesamiento del informe para mostrar un aspecto diferente de los datos. Un parámetro de informe se utiliza generalmente para filtrar un gran conjunto de registros, pero puede tener otros usos dependiendo de las consultas y expresiones en el informe.

Los parámetros de informe difieren de los parámetros de consulta en que se definen en un informe y son procesados por el servidor de informes, mientras que los parámetros de consulta se definen como parte de la consulta del conjunto de datos y se procesan en el servidor de la base de datos. En Aspose.Cells.Report.Designer, los parámetros de consulta se especifican en el momento de creación de la consulta en Microsoft Query. 

Puede crear parámetros de informe y asignar parámetros de consulta al parámetro de informe correspondiente en Aspose.Cells.Report.Designer. De esta manera, es posible seleccionar valores para los parámetros de informe y hacer que se pasen en la consulta para limitar los datos recuperados de la fuente de datos.

{{% /alert %}} 
###### **Esta sección incluye los siguientes temas:** 
- [Creando Parámetros de Informe](/cells/es/reportingservices/creating-report-parameters/)
- [Modificando Parámetros de Informe](/cells/es/reportingservices/modifying-report-parameters/)
- [Mapeando Parámetros de Consulta a Parámetros de Informe](/cells/es/reportingservices/mapping-query-parameters-to-report-parameters/)
