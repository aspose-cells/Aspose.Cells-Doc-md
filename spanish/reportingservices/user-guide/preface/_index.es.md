---
title: Prefacio
type: docs
weight: 20
url: /es/reportingservices/preface/
---

{{% alert color="primary" %}} 

Aspose.Cells for Reporting Services contiene principalmente dos componentes: Aspose.Cells.Report.Designer y Aspose.Cells.Renderer para los Servicios de Informes. El primero se utiliza para diseñar informes directamente en Microsoft Excel y el segundo es responsable de renderizar un informe RDL en Microsoft Excel. 

{{% /alert %}} 
### **Diseñando un Informe con el Diseñador de Informes**
Los principales pasos para diseñar un informe utilizando Aspose.Cells.Report.Designer son:

1. **Crear fuentes de datos y consultas**.
   Microsoft Query está integrado con Aspose.Cells.Report.Designer y se utiliza como una herramienta gráfica para crear fuentes de datos y consultas. Los usuarios también pueden hacer uso de un archivo RDL existente en el que están disponibles las fuentes de datos y las consultas para operaciones.
1. **Mapear parámetros**.
   Si las sentencias SQL de una consulta incluyen parámetros, los usuarios deben crear parámetros de informe y mapear los parámetros de SQL a los parámetros de informe. Puede designar valores válidos para un parámetro de informe en Aspose.Cells.Report.Designer.
1. **Diseñar el contenido, estilos y formatos de la plantilla de informe de Microsoft Excel**.
   Una plantilla de informe de Aspose.Cells puede contener cualquier número de los siguientes tipos de elementos de informe: 
   1. Tabla
   1. Tabla dinámica
   1. Gráfico
   1. Cuadro de texto
   1. Matriz
      Normalmente, una consulta (es decir, DataSet) se utiliza como una fuente de datos para el elemento de informe. También puede utilizar parámetros de Servicios de Informes, fórmulas y variables globales como una fuente de datos para algunos tipos de elementos de informe. Los estilos y formatos de los elementos de informe se especifican simplemente estableciendo los estilos y formatos de las celdas que componen los elementos de informe.
1. **Publicar informe**.
   Después de los pasos anteriores, el informe está listo para publicarse. Los usuarios pueden designar en qué carpeta se publicará el informe. Si es necesario, puede asignar una fuente de datos compartida en el servidor de informes como fuente de datos para el informe.
1. **Vista previa del informe**.
   Al seleccionar un informe para previsualizarlo en el servidor de informes, se le pedirá especificar a qué formato de archivo exportarlo (por ejemplo, formato binario XLS de Microsoft Excel 97-2003, SpreadsheetML o formato XLSX de Microsoft Excel 2007), y cualquier parámetro de informe de entrada creado durante el diseño del informe. Después de esto, el informe se completa con los datos suministrados por los Servicios de Informes.
