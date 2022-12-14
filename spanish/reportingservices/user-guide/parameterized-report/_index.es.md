---
title: Informe parametrizado
type: docs
weight: 60
url: /es/reportingservices/parameterized-report/
---
{{% alert color="primary" %}} 

 A*informe parametrizado* es un informe que acepta valores de entrada que se utilizan cuando se procesa el informe.

 Con un informe parametrizado, puede variar la salida de un informe en función de los valores que se establecen en tiempo de ejecución. Reporting Services admite dos tipos de parámetros: parámetros de consulta y parámetros de informe.

- **Parámetros de consulta** se utilizan para seleccionar o filtrar datos durante el procesamiento de datos. Si se especifica un parámetro de consulta, el usuario o las propiedades predeterminadas deben proporcionar un valor para completar la instrucción SELECT o el procedimiento almacenado que recupera datos para un informe.
- **Informe de parámetros**se utilizan durante el procesamiento de informes para mostrar un aspecto diferente de los datos. Un parámetro de informe generalmente se usa para filtrar un gran conjunto de registros, pero puede tener otros usos según las consultas y expresiones del informe.

 Los parámetros de informe se diferencian de los parámetros de consulta en que se definen en un informe y los procesa el servidor de informes, mientras que los parámetros de consulta se definen como parte de la consulta del conjunto de datos y se procesan en el servidor de la base de datos. En Aspose.Cells.Report.Designer, los parámetros de consulta se especifican en el momento de crear la consulta en Microsoft Query.

Puede crear parámetros de informe y asignar parámetros de consulta al parámetro de informe correspondiente en Aspose.Cells.Report.Designer. De esta forma, es posible seleccionar valores para los parámetros del informe y hacer que se pasen en la consulta para limitar los datos recuperados de la fuente de datos.

{{% /alert %}} 
###### **Esta sección incluye los siguientes temas:**
- [Creación de parámetros de informe](/cells/es/reportingservices/creating-report-parameters/)
- [Modificación de los parámetros del informe](/cells/es/reportingservices/modifying-report-parameters/)
- [Asignación de parámetros de consulta a parámetros de informe](/cells/es/reportingservices/mapping-query-parameters-to-report-parameters/)
