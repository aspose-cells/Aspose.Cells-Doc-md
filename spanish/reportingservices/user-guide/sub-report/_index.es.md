---
title: Subinforme
type: docs
weight: 90
url: /es/reportingservices/sub-report/
---
{{% alert color="primary" %}} 

Un subinforme se puede incrustar en un elemento de tabla. El formato es: &=subinforme{ReportName=nombre de su informe; parámetro1 nombre = parámetro1 valor; parámetro2 nombre = parámetro2 valor; ...}

**Un subinforme en una definición de informe** 

![todo:imagen_alternativa_texto](sub-report_1.png)

En el ejemplo, el nombre del subinforme es "Detalle de la orden de venta". Tiene un parámetro, SalesOrderNumber. El valor del parámetro es EmpSalesDetail.SalesOrderNumber.
### **Restricciones en los subinformes**
1. El subinforme debe diseñarse con Aspose.Cells.ReportingServices Designer.
1. El subinforme solo se puede incrustar en la fila del grupo de la tabla, y la fila del grupo no puede contener ningún elemento excepto el subinforme. No se permite incrustar un subinforme en las filas de detalles de la tabla o en las filas de pie de página.
1. Actualmente, no se admite anidar más de un nivel. El subinforme no puede contener un informe incrustado.

{{% /alert %}} 
###### **Esta sección incluye los siguientes temas:**
- [Crear elemento de tabla](/cells/es/reportingservices/creating-table-item/)
- [Añadir elemento de subinforme](/cells/es/reportingservices/add-sub-report-item/)
