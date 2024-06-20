---
title: Agregar parámetros de informe al informe
type: docs
weight: 60
url: /es/reportingservices/adding-report-parameters-to-report/
---

{{% alert color="primary" %}} 

La plantilla de informe de Aspose.Cells admite parámetros de informe de Servicios de informes como una fuente de datos para celdas que contienen un marcador de parámetro de Servicios de informes. Consulte [Marcadores de plantillas y Smart Markers de Aspose.Cells](/cells/es/reportingservices/aspose-cells-template-and-smart-markers/) para obtener más información sobre los marcadores de parámetros de Servicios de informes. Los parámetros del informe suelen ubicarse en el área de texto del encabezado o pie de tabla.

{{% /alert %}} 
### **Agregar un parámetro de informe**
Para agregar parámetros de informe a los informes:

1. Selecciona una celda. 

   **Seleccionar una celda** 

![todo:image_alt_text](adding-report-parameters-to-report_1.png)




1. Haga clic en Insertar fórmula en la barra de herramientas de Aspose.Cells.Report.Designer (

![todo:image_alt_text](adding-report-parameters-to-report_2.png)

).

1. Seleccione **Parámetros** del panel de parámetros a la izquierda.
   Todos los parámetros se enumeran en el panel de la derecha. 
1. Seleccione un parámetro, en el ejemplo, hemos seleccionado EmpID.
1. Haga doble clic en el parámetro para que aparezca la expresión en el editor en la parte superior del formulario.
   Un parámetro tiene dos atributos de datos: etiqueta y valor (el atributo predeterminado es el valor). 

   **Seleccionar un parámetro** 

![todo:image_alt_text](adding-report-parameters-to-report_3.png)




1. En el ejemplo, se debe mostrar la etiqueta del parámetro en el informe, por lo que modifique la expresión a Parameters!EmpID.Label. 

   **Modificar el parámetro** 

![todo:image_alt_text](adding-report-parameters-to-report_4.png)




1. Haz clic en **Aceptar**.
   La celda seleccionada contiene un marcador de parámetros de informe. 

   **Se insertó un parámetro de informe en la celda** 

![todo:image_alt_text](adding-report-parameters-to-report_5.png)
