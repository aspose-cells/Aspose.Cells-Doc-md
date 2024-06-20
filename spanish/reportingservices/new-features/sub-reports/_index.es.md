---
title: Subinformes
type: docs
weight: 20
url: /es/reportingservices/sub-reports/
---

{{% alert color="primary" %}} 

Incorporamos soporte para incrustar un subinforme en una fila de grupo de tabla. El formato es:

&=subreport{ReportName=your report name; parameter1 name = parameter1 value; parameter2 name = parameter2 value;......} 

{{% /alert %}} 
### **Ejemplo**
**Un subinforme en una tabla** 

![todo:image_alt_text](sub-reports_1.png)

En el ejemplo, el nombre del subinforme es "Detalle de orden de ventas". Tiene un parámetro, *SalesOrderNumber*. El valor del parámetro es *EmpSalesDetail.SalesOrderNumber.*
#### **Restricciones sobre el uso de Subinformes**
- El subinforme debe ser diseñado con la herramienta Aspose.Cells.Reporting Services Designer.
- El Subinforme solo puede ser incrustado en la fila del grupo de la tabla y la fila del grupo no puede contener otros elementos excepto el Subinforme. No se permite incrustar un Subinforme en las filas de detalle o en las filas de pie de página de la tabla.
- Actualmente, no se admite la anidación de más de un nivel. El Subinforme no puede contener un informe incrustado.
