---
title: Trabajando con PivotTable
type: docs
weight: 100
url: /es/reportingservices/working-with-pivottable/
---

{{% alert color="primary" %}} 

Una *tabla dinámica* es una tabla interactiva que resume datos y los presenta de manera significativa. SQL Server Reporting Services no puede exportar un informe al formato de Microsft Excel manteniendo una tabla dinámica. Los usuarios del informe tienen que crear manualmente tablas dinámicas cada vez que exportan un informe de tabla dinámica desde los Servicios de informes a Microsoft Excel. Con Aspose.Cells for Reporting Services, puede diseñar una tabla dinámica una vez en el momento del diseño del informe. Cada vez que se ejecuta el informe, Aspose.Cells for Reporting Services exporta el informe a Microsoft Excel y actualiza los datos en la tabla dinámica.

{{% /alert %}} 

Para crear un informe de tabla dinámica:

1. Cree un conjunto de datos como origen de datos para la tabla dinámica.
   A continuación, utilizamos la base de datos de ejemplo AdventureWorks que se envía con SQL Server Reporting Services 2005 y creamos un conjunto de datos llamado “ventas".
   El SQL para el conjunto de datos es el siguiente: 

**SQL**

{{< highlight csharp >}}

 SELECT  PC.Name AS ProdCat,

	    PS.Name AS SubCat,

	    DATEPART(yy, SOH.OrderDate) AS OrderYear,

	    'Q' + DATENAME(qq, SOH.OrderDate) AS OrderQtr,

         SUM(SOD.UnitPrice * SOD.OrderQty) AS Sales

FROM    Production.ProductSubcategory PS INNER JOIN

         Sales.SalesOrderHeader SOH INNER JOIN

         Sales.SalesOrderDetail SOD ON SOH.SalesOrderID = SOD.SalesOrderID INNER JOIN

         Production.Product P ON SOD.ProductID = P.ProductID ON PS.ProductSubcategoryID = P.ProductSubcategoryID INNER JOIN

         Production.ProductCategory PC ON PS.ProductCategoryID = PC.ProductCategoryID

WHERE   (SOH.OrderDate BETWEEN '1/1/2002' AND '12/31/2003')

GROUP BY  DATEPART(yy, SOH.OrderDate), PC.Name, PS.Name, 'Q' + DATENAME(qq, SOH.OrderDate), PS.ProductSubcategoryID



{{< /highlight >}}



{{% alert color="primary" %}} 

Consulte [Orígenes de datos y consultas](/cells/es/reportingservices/data-sources-and-queries/) para obtener más información sobre cómo crear un origen de datos y un conjunto de datos con Aspose.Cells.Report.Designer.

{{% /alert %}} 

1. Cree un informe de tabla según las instrucciones en [Creación de un informe tabular](/cells/es/reportingservices/creating-tabular-report/), como se muestra a continuación.
   La tabla será el origen de datos para la tabla dinámica. 

![todo:image_alt_text](working-with-pivottable_1.png)




1. En Microsoft Excel, desde el menú **Insertar**, selecciona **Nombre** y luego **Definir**.
1. Define un nombre como "ventas".
   El rango del nombre comienza con la primera celda del título del encabezado y termina en la última celda de la fila de datos de la tabla como se muestra a continuación. 

![todo:image_alt_text](working-with-pivottable_2.png)




1. Haga clic en **OK** para finalizar.
1. Crea una nueva hoja para la tabla dinámica.
1. Desde el menú **Datos**, selecciona **Informe de tabla dinámica y gráfico dinámico** para agregar una tabla dinámica.
   Se muestra un cuadro de diálogo.
1. Selecciona **Lista o base de datos de Microsoft Office Excel** como fuente de datos y **tabla dinámica** como tipo de informe.
1. Haga clic en **Siguiente** para continuar. 

![todo:image_alt_text](working-with-pivottable_3.png)




1. En el cuadro de diálogo, ingresa "ventas", el nombre que definiste anteriormente.
1. Haga clic en **Siguiente** para continuar. 

![todo:image_alt_text](working-with-pivottable_4.png)




1. Haga clic en **Terminar**. 

![todo:image_alt_text](working-with-pivottable_5.png)




1. Diseña la tabla dinámica en Excel. 

![todo:image_alt_text](working-with-pivottable_6.png)



La tabla dinámica diseñada se muestra a continuación. 

![todo:image_alt_text](working-with-pivottable_7.png)




1. Haz clic derecho en la tabla dinámica y selecciona **Opciones de Tabla**.
1. Asegúrate de que se haya seleccionado **Actualizar al abrir**. 

![todo:image_alt_text](working-with-pivottable_8.png)




1. Guarda el informe y publícalo en el servidor de informes.
1. Exporta el informe desde el servidor de informes.
   El resultado se muestra a continuación. 

![todo:image_alt_text](working-with-pivottable_9.png)
