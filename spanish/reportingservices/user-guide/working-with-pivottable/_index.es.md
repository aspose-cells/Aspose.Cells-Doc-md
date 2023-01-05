---
title: Trabajar con tabla dinámica
type: docs
weight: 100
url: /es/reportingservices/working-with-pivottable/
---
{{% alert color="primary" %}} 

 A*tabla dinámica* es una tabla interactiva que resume los datos y los presenta de manera significativa. SQL Server Reporting Services no puede exportar un informe al formato de Microsft Excel mientras mantiene una tabla dinámica. Los usuarios de informes deben crear manualmente tablas dinámicas cada vez que exportan un informe de tabla dinámica de Reporting Services a Microsoft Excel. Con Aspose.Cells for Reporting Services, puede diseñar una tabla dinámica una vez en el momento del diseño del informe. Cada vez que se ejecuta el informe, Aspose.Cells for Reporting Services exporta el informe a Microsoft Excel y actualiza los datos en la tabla dinámica.

{{% /alert %}} 

Para crear un informe de tabla dinámica:

1. Cree un conjunto de datos como fuente de datos para la tabla dinámica.
 A continuación, usamos la base de datos de ejemplo AdventureWorks que se incluye con SQL Server Reporting Services 2005 y creamos un conjunto de datos denominado "ventas".
El SQL para el conjunto de datos es el siguiente:

**sql**

{{< highlight "csharp" >}}

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

 Por favor refiérase a[Fuentes de datos y consultas](/cells/es/reportingservices/data-sources-and-queries/) para obtener más información sobre cómo crear una fuente de datos y un conjunto de datos con Aspose.Cells.Report.Designer.

{{% /alert %}} 

1.  Cree un informe de tabla de acuerdo con las instrucciones en[Crear informe tabular](/cells/es/reportingservices/creating-tabular-report/), Como se muestra abajo.
 La tabla será la fuente de datos para la tabla dinámica.

![todo:imagen_alternativa_texto](working-with-pivottable_1.png)




1.  En Microsoft Excel, de la**Insertar** menú, seleccione**Nombre** y luego**Definir**.
1. Defina un nombre como "ventas".
 El rango del nombre comienza con la primera celda del título del encabezado y termina en la última celda de la fila de datos de la tabla, como se muestra a continuación.

![todo:imagen_alternativa_texto](working-with-pivottable_2.png)




1.  Hacer clic**DE ACUERDO** para terminar.
1. Cree una nueva hoja para la tabla dinámica.
1.  Desde el**Datos** menú, seleccione**Informe de tabla dinámica y gráfico dinámico** para agregar una tabla dinámica.
 Se muestra un cuadro de diálogo.
1.  Seleccione**Microsoft Lista o base de datos de Office Excel** como fuente de datos y**tabla dinámica** como tipo de informe.
1.  Hacer clic**Próximo** continuar.

![todo:imagen_alternativa_texto](working-with-pivottable_3.png)




1. En el cuadro de diálogo, ingrese "ventas", el nombre que definió anteriormente.
1.  Hacer clic**Próximo** continuar.

![todo:imagen_alternativa_texto](working-with-pivottable_4.png)




1.  Hacer clic**Finalizar**. 

![todo:imagen_alternativa_texto](working-with-pivottable_5.png)




1.  Diseña la tabla dinámica en Excel.

![todo:imagen_alternativa_texto](working-with-pivottable_6.png)



 La tabla dinámica diseñada se muestra a continuación.

![todo:imagen_alternativa_texto](working-with-pivottable_7.png)




1.  Haga clic derecho en la tabla dinámica y seleccione**Opciones de mesa**.
1.  Asegúrate de eso**Actualizar al abrir** es seleccionado.

![todo:imagen_alternativa_texto](working-with-pivottable_8.png)




1. Guarde el informe y publíquelo en Report Server.
1. Exporte el informe desde Report Server.
 El resultado se muestra a continuación.

![todo:imagen_alternativa_texto](working-with-pivottable_9.png)
