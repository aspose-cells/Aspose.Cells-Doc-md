---
title: Prefacio
type: docs
weight: 20
url: /es/reportingservices/preface/
---
{{% alert color="primary" %}} 

Aspose.Cells for Reporting Services contiene principalmente dos componentes: Aspose.Cells.Report.Designer y Aspose.Cells.Renderer for Reporting Services. El primero se usa para diseñar informes directamente en Microsoft Excel y el segundo es responsable de generar un informe RDL en Microsoft Excel.

{{% /alert %}} 
### **Diseño de un informe con el diseñador de informes**
Los pasos principales para diseñar un informe usando Aspose.Cells.Report.Designer son:

1. **Crear fuentes de datos y consultas**.
 Microsoft Query está integrado con Aspose.Cells.Report.Designer y se utiliza como una herramienta gráfica para crear fuentes de datos y consultas. Los usuarios también pueden hacer uso de un archivo RDL existente en el que las fuentes de datos y las consultas están disponibles para las operaciones.
1. **Parámetros del mapa**.
 Si las declaraciones SQL de una consulta incluyen parámetros, los usuarios deben crear parámetros de informe y asignar parámetros SQL a parámetros de informe. Puede designar valores válidos para un parámetro de informe en Aspose.Cells.Report.Designer.
1. **Diseño Microsoft Contenidos, estilos y formatos de la plantilla de informe de Excel**.
Una plantilla de informe Aspose.Cells puede contener cualquier número de los siguientes tipos de elementos de informe:
 1. Mesa
 1. Mesa dinámica
 1. Gráfico
 1. Cuadro de texto
 1. Matriz
 Normalmente, una consulta (es decir, un conjunto de datos) se utiliza como origen de datos para el elemento de informe. También puede usar parámetros, fórmulas y variables globales de Reporting Services como fuente de datos para algunos tipos de elementos de informe. Los estilos y formatos de los elementos del informe se especifican simplemente configurando los estilos y formatos de las celdas que componen los elementos del informe.
1. **Publicar informe**.
 Después de los pasos anteriores, el informe está listo para publicarse. Los usuarios pueden designar en qué carpeta se publica el informe. Si es necesario, puede asignar una fuente de datos compartida en el servidor de informes como fuente de datos para el informe.
1. **Informe de vista previa**.
Al seleccionar un informe para obtener una vista previa en el servidor de informes, se le solicita que especifique a qué formato de archivo exportarlo (por ejemplo, Microsoft Excel 97-2003 formato binario XLS, SpreadsheetML o Microsoft formato Excel 2007 XLSX), y cualquier parámetro de informe de entrada creado durante el diseño del informe. Después de esto, el informe se completa con los datos proporcionados por Reporting Services.
