---
title: Trabajar con gráficos
type: docs
weight: 110
url: /es/reportingservices/working-with-charts/
---
{{% alert color="primary" %}} 

 Aspose.Cells La plantilla de informe admite Microsoft gráficos de Excel. Cada vez que ejecuta un informe, el gráfico se completa con los datos más recientes.

{{% /alert %}} 

Para agregar un gráfico a la plantilla de informe:

1. Primero, cree el conjunto de datos que será la fuente de datos para el gráfico.
 A continuación, usamos la base de datos de muestra AdventureWorks que se incluye con SQL Server Reporting Services 2005 y creamos un conjunto de datos denominado Ventas.
 Este SQL define el conjunto de datos:

**sql**

{{< highlight "csharp" >}}

 SELECT DATEPART(yy,SOH.OrderDate) 'Year',

'Q'+DATENAME(qq,SOH.OrderDate) 'Quarter',

SUM(SOD.UnitPrice*SOD.OrderQty) 'Sales'

FROMAdventureWorks.Sales.SalesOrderDetail SOD,

AdventureWorks.Sales.SalesOrderHeader SOH

WHERE SOH.SalesOrderID = SOD.SalesOrderID

AND ((DATEPART(yy,SOH.OrderDate)=2002))

GROUP BY DATEPART(yy,SOH.OrderDate), 'Q'+DATENAME(qq,SOH.OrderDate)



{{< /highlight >}}



 Por favor refiérase a[Fuentes de datos y consultas](/cells/es/reportingservices/data-sources-and-queries/) para obtener más información sobre cómo crear una fuente de datos y un conjunto de datos en Aspose.Cells.Report.Designer.

1. Cree un informe tabular de acuerdo con las instrucciones de[Crear informe tabular](/cells/es/reportingservices/creating-tabular-report/) . El informe que hemos creado para este ejemplo se encuentra a continuación. La tabla es la fuente de datos del gráfico.

![todo:imagen_alternativa_texto](working-with-charts_1.png)




1.  En Microsoft Excel, haga clic en el**Insertar** menú y seleccione**Gráfico**.
1.  Hacer clic**Próximo**. 

![todo:imagen_alternativa_texto](working-with-charts_2.png)




1.  Haga clic en el**Serie** pestaña.

![todo:imagen_alternativa_texto](working-with-charts_3.png)




1.  Hacer clic**Agregar**. 

![todo:imagen_alternativa_texto](working-with-charts_4.png)




1. En el cuadro de diálogo, establezca el valor de Serie 1 (serie trimestral) en el primer campo de datos de la tabla.
 En la muestra, eso es “VentasEmpresa!$C$3:$C$3”. El primer $C$3 es el índice de la primera fila de "Trimestre" y el segundo $C$3 es un marcador de posición para el índice de la última fila de "Trimestre" y se reemplazará con el índice de fila real de los datos de la tabla en el momento de la representación. Establezca las etiquetas del eje de categoría (X) en "=VentasEmpresa!$C$3:$C$3".

![todo:imagen_alternativa_texto](working-with-charts_5.png)




1.  Hacer clic**Agregar** para agregar otra serie.
 En la muestra, hemos agregado la serie de ventas.
1. Establezca el valor de Serie2 (Serie de ventas) en el segundo campo de datos de la tabla.
En la muestra es “CompanySales!$D$3:$D$3”. El primer $D$3 es el índice de la primera fila de "Ventas" y el segundo $D$3 es un marcador de posición para el índice de la última fila de "Ventas" y se reemplazará con el índice de la fila real de los datos de la tabla en el momento de la representación.
1.  Hacer clic**Próximo** continuar.

![todo:imagen_alternativa_texto](working-with-charts_6.png)




1. En el cuadro de diálogo, establezca el título del gráfico y el eje de categoría (X).
1.  Hacer clic**Finalizar** para completar el trabajo.

![todo:imagen_alternativa_texto](working-with-charts_7.png)



 La plantilla se parece a la siguiente.

![todo:imagen_alternativa_texto](working-with-charts_8.png)




1. Guarde el informe y publíquelo en Report Server.
1. Exporte el informe desde Report Server.
 El resultado es el siguiente.

![todo:imagen_alternativa_texto](working-with-charts_9.png)
