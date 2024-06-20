---
title: Trabajando con Gráficos
type: docs
weight: 110
url: /es/reportingservices/working-with-charts/
---

{{% alert color="primary" %}} 

La plantilla de informe de Aspose.Cells admite gráficos de Microsoft Excel. Cada vez que ejecuta un informe, el gráfico se rellena con los datos más recientes. 

{{% /alert %}} 

Para agregar un gráfico a la plantilla de informe:

1. Primero, cree el conjunto de datos que será el origen de datos del gráfico.
   A continuación, usamos la base de datos de ejemplo AdventureWorks que se incluye con SQL Server Reporting Services 2005 y creamos un conjunto de datos llamado Ventas.
   Este SQL define el conjunto de datos: 

**SQL**

{{< highlight csharp >}}

 SELECT DATEPART(yy,SOH.OrderDate) 'Year',

'Q'+DATENAME(qq,SOH.OrderDate) 'Quarter',

SUM(SOD.UnitPrice*SOD.OrderQty) 'Sales'

FROMAdventureWorks.Sales.SalesOrderDetail SOD,

AdventureWorks.Sales.SalesOrderHeader SOH

WHERE SOH.SalesOrderID = SOD.SalesOrderID

AND ((DATEPART(yy,SOH.OrderDate)=2002))

GROUP BY DATEPART(yy,SOH.OrderDate), 'Q'+DATENAME(qq,SOH.OrderDate)



{{< /highlight >}}



Consulte [Orígenes de datos y consultas](/cells/es/reportingservices/data-sources-and-queries/) para obtener más información sobre cómo crear un origen de datos y un conjunto de datos en el diseñador de informes Aspose.Cells.

1. Cree un informe tabular de acuerdo con las instrucciones en [Creación de un Informe Tabular](/cells/es/reportingservices/creacion-de-un-informe-tabular/). El informe que hemos creado para este ejemplo está a continuación. La tabla es el origen de datos del gráfico. 

![todo:image_alt_text](working-with-charts_1.png)




1. En Microsoft Excel, haga clic en el menú **Insertar** y seleccione **Gráfico**.
1. Haga clic en **Siguiente**. 

![todo:image_alt_text](working-with-charts_2.png)




1. Haga clic en la pestaña **Serie**. 

![todo:image_alt_text](working-with-charts_3.png)




1. Haga clic en **Agregar**. 

![todo:image_alt_text](working-with-charts_4.png)




1. En el cuadro de diálogo, configure el valor de Serie1 (serie de trimestres) al primer campo de datos de la tabla.
   En el ejemplo, eso es “CompanySales!$C$3:$C$3”. El primer $C$3 es el índice de la primera fila de “Trimestre” y el segundo $C$3 es un marcador de posición para el último índice de fila real de “Trimestre” y será reemplazado por el índice de fila real de los datos de la tabla en el momento de la representación. Configure las etiquetas del eje de categoría(X) como “=CompanySales!$C$3:$C$3” 

![todo:image_alt_text](working-with-charts_5.png)




1. Haga clic en **Agregar** para agregar otra serie.
   En el ejemplo, hemos agregado la serie de ventas. 
1. Establezca el valor de Series2 (serie de ventas) en el segundo campo de datos de la tabla.
   En el ejemplo es “CompanySales!$D$3:$D$3”. El primer $D$3 es el índice de la primera fila de “Ventas” y el segundo $D$3 es un marcador de posición para el índice de la última fila de “Ventas” y será reemplazado por el índice real de la fila de datos en el momento de la representación. 
1. Haga clic en **Siguiente** para continuar. 

![todo:image_alt_text](working-with-charts_6.png)




1. En el cuadro de diálogo, establezca el título del gráfico y el eje de categoría (X).
1. Haga clic en **Finalizar** para completar el trabajo. 

![todo:image_alt_text](working-with-charts_7.png)



La plantilla se ve así. 

![todo:image_alt_text](working-with-charts_8.png)




1. Guarda el informe y publícalo en el servidor de informes.
1. Exporta el informe desde el servidor de informes.
   El resultado es el siguiente. 

![todo:image_alt_text](working-with-charts_9.png)
