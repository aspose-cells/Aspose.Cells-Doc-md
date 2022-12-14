---
title: Adición de parámetros de informe al informe
type: docs
weight: 60
url: /es/reportingservices/adding-report-parameters-to-report/
---
{{% alert color="primary" %}} 

 La plantilla de informe Aspose.Cells admite parámetros de informe de Reporting Services como fuente de datos para celdas que contienen un marcador de parámetro de Reporting Services. Por favor refiérase a[Aspose.Cells Plantilla y marcadores inteligentes](/cells/es/reportingservices/aspose-cells-template-and-smart-markers/) para obtener información sobre los marcadores de parámetros de Reporting Services. Los parámetros del informe normalmente se colocan en el área de texto del encabezado o pie de página de la tabla.

{{% /alert %}} 
### **Adición de un parámetro de informe**
Para agregar parámetros de informe a los informes:

1.  Seleccione una celda.

   **Seleccionando una celda** 

![todo:imagen_alternativa_texto](adding-report-parameters-to-report_1.png)




1. Haga clic en Insertar fórmula en la barra de herramientas Aspose.Cells.Report.Designer (

![todo:imagen_alternativa_texto](adding-report-parameters-to-report_2.png)

).

1.  Seleccione**Parámetros** desde el panel de Parámetros a la izquierda.
 Todos los parámetros se enumeran en el panel derecho.
1. Seleccione un parámetro, en el ejemplo, hemos seleccionado EmpID.
1. Haga doble clic en el parámetro para que la expresión aparezca en el editor en la parte superior del formulario.
 Un parámetro tiene dos atributos de datos: etiqueta y valor (el atributo predeterminado es valor).

   **Selección de un parámetro** 

![todo:imagen_alternativa_texto](adding-report-parameters-to-report_3.png)




1.  En el ejemplo, la etiqueta del parámetro debe mostrarse en el informe, así que modifique la expresión a Parámetros!EmpID.Label.

   **Modificación del parámetro** 

![todo:imagen_alternativa_texto](adding-report-parameters-to-report_4.png)




1.  Hacer clic**OK**.
 La celda seleccionada contiene un marcador de parámetros de informe.

   **Un parámetro de informe insertado en la celda.** 

![todo:imagen_alternativa_texto](adding-report-parameters-to-report_5.png)
