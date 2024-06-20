---
title: Subinforme
type: docs
weight: 90
url: /es/reportingservices/sub-report/
---

{{% alert color="primary" %}} 

Un subinforme puede estar incrustado en un elemento de tabla. El formato es: &=subreport{ReportName=nombre de su informe; nombre del parámetro1 = valor del parámetro1; nombre del parámetro2 = valor del parámetro2; ...}

**Un subinforme en una definición de informe** 

![todo:image_alt_text](sub-report_1.png)

En el ejemplo, el nombre del subinforme es “Detalles del pedido de venta”. Tiene un parámetro, SalesOrderNumber. El valor del parámetro es EmpSalesDetail.SalesOrderNumber.
### **Restricciones en Subinformes**
1. El subinforme debe estar diseñado con Aspose.Cells.ReportingServices Designer.
1. El subinforme solo se puede incrustar en la fila del grupo de la tabla, y la fila del grupo no puede contener ningún elemento excepto el subinforme. No se permite incrustar un subinforme en las filas de detalle o las filas de pie de la tabla.
1. Actualmente, no se admite anidar más de un nivel. El subinforme no puede contener un informe incrustado.

{{% /alert %}} 
###### **Esta sección incluye los siguientes temas:** 
- [Creación de Elemento de Tabla](/cells/es/reportingservices/creating-table-item/)
- [Agregar Elemento de Subinforme](/cells/es/reportingservices/add-sub-report-item/)
