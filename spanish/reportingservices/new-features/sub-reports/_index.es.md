---
title: Subinformes
type: docs
weight: 20
url: /es/reportingservices/sub-reports/
---
{{% alert color="primary" %}} 

Incorporamos soporte para incrustar un subinforme en una fila de grupo de tabla. El formato es:

&=subreport{ReportName=nombre de su informe; parámetro1 nombre = parámetro1 valor; parámetro2 nombre = parámetro2 valor;......} 

{{% /alert %}} 
### **Ejemplo**
**Un subinforme en una tabla** 

![todo:imagen_alternativa_texto](sub-reports_1.png)

 En el ejemplo, el nombre del subinforme es "Detalle de la orden de venta". Tiene un parámetro,*Número de orden de ventas* . El valor del parámetro es*EmpSalesDetail.SalesOrderNumber.*
#### **Restricciones en el uso de subinformes**
- El subinforme debe diseñarse con la herramienta Aspose.Cells.Reporting Services Designer.
- El subinforme solo se puede incrustar en la fila del grupo de la tabla y la fila del grupo no puede contener otros elementos excepto el subinforme. No se permite incrustar un subinforme en las filas de detalle de la tabla o en las filas de pie de página.
- Actualmente, no se admite anidar más de un nivel. El subinforme no puede contener un informe incrustado.
