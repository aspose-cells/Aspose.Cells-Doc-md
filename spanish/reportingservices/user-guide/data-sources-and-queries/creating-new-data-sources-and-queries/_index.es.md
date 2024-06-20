---
title: Creación de nuevas fuentes de datos y consultas
type: docs
weight: 20
url: /es/reportingservices/creating-new-data-sources-and-queries/
---

{{% alert color="primary" %}} 

Aspose.Cells.Report.Designer se integra con MS Query y utiliza MS Query como una herramienta para crear fuentes de datos y consultas. Para crear una nueva fuente de datos y consulta en Aspose.Cells.Report.Designer, siga los pasos a continuación:. 

{{% /alert %}} 

Para crear una nueva fuente de datos y consulta en Aspose.Cells.Report.Designer:

1. Abre Microsoft Excel.
1. Haga clic en **Construir conjunto de datos** en la barra de herramientas de Aspose.Cells.Report.Designer: 

![todo:image_alt_text](creating-new-data-sources-and-queries_1.png)


Todas las fuentes de datos y consultas se enumeran en el cuadro de diálogo. 

1. Un nodo de fuente de datos: 

![todo:image_alt_text](creating-new-data-sources-and-queries_2.png)

1. Un nodo de conjunto de datos: 

![todo:image_alt_text](creating-new-data-sources-and-queries_3.png)

1. Seleccione el nodo raíz del árbol.
1. Haga clic en **Agregar**. 

   **Agregar fuentes de datos y conjuntos de datos** 

![todo:image_alt_text](creating-new-data-sources-and-queries_4.png)




1. En el cuadro de diálogo, llame al origen de datos **SqlServer** y al conjunto de datos **EmpsSalesDetail**.
1. Haga clic en **Siguiente**. 

   **Agregando conjuntos de datos y origenes de datos** 

![todo:image_alt_text](creating-new-data-sources-and-queries_5.png)



Aspose.Cells.Report.Designer inicia Microsoft Query. 

1. En el cuadro de diálogo Elegir origen de datos, seleccione **Nuevo origen de datos**.
1. Haz clic en **Aceptar**.
   También puede seleccionar un origen de datos existente. 

   **Seleccionando un origen de datos** 

![todo:image_alt_text](creating-new-data-sources-and-queries_6.png)




1. Ingrese un nombre de origen de datos y seleccione SQL Server en la lista desplegable de controladores de base de datos.
1. Haga clic en **Conectar**. 

   **Creando un nuevo origen de datos** 

![todo:image_alt_text](creating-new-data-sources-and-queries_7.png)




1. En el cuadro de diálogo de inicio de sesión de SQL Server, seleccione el valor apropiado para cada elemento.
   Por ejemplo, establezca el servidor en local, seleccione la base de datos AdventureWorks y seleccione **Usar conexión de confianza**.
1. Haz clic en **Aceptar**. 

   **Iniciando sesión en el servidor SQL** 

![todo:image_alt_text](creating-new-data-sources-and-queries_8.png)




1. Haz clic en **Aceptar**. 

   **Tenga en cuenta que ahora hemos iniciado sesión en el servidor SQL** 

![todo:image_alt_text](creating-new-data-sources-and-queries_9.png)



El nuevo origen de datos aparece en el cuadro de diálogo **Elegir origen de datos**. 

1. Seleccione el nuevo origen de datos. 

   **El nuevo origen de datos** 

![todo:image_alt_text](creating-new-data-sources-and-queries_10.png)




1. Haga clic en **Aceptar** para abrir Microsoft Query.
1. Para crear una consulta en Microsoft Query, consulte el Asistente de Consultas de Microsoft. En el siguiente ejemplo, creamos una consulta con parámetros. 

   **Creación de una consulta** 

![todo:image_alt_text](creating-new-data-sources-and-queries_11.png)



El SQL es el siguiente: 

**SQL**

{{< highlight csharp >}}

 SELECT C.FirstName + ' ' + C.LastName AS Employee,

DATEPART(Month, SOH.OrderDate) AS OrderMonthNum,

PS.Name AS SubCat,

SUM(SOD.LineTotal) AS Sales,

SOH.SalesOrderNumber,

P.Name AS Product,

SUM(SOD.OrderQty) AS OrderQty,

SOD.UnitPrice,

PC.Name AS ProdCat

FROM  Sales.SalesOrderHeader SOH ,

Sales.SalesOrderDetail SOD ,

Sales.SalesPerson SP,

HumanResources.Employee E,

Person.Contact C,

Production.Product P,

Production.ProductSubcategory PS ,

Production.ProductCategory PC

where SOH.SalesOrderID = SOD.SalesOrderID

and SOH.SalesPersonID = SP.SalesPersonID

and SP.SalesPersonID = E.EmployeeID

and E.ContactID = C.ContactID

and SOD.ProductID = P.ProductID

and P.ProductSubcategoryID = PS.ProductSubcategoryID

and PS.ProductCategoryID = PC.ProductCategoryID

and  (DATEPART(Year, SOH.OrderDate) =  ?)

AND (DATEPART(Month, SOH.OrderDate) =  ?)

AND (SOH.SalesPersonID =?)

GROUP BY    C.FirstName + ' ' + C.LastName,

DATEPART(Month, SOH.OrderDate), SOH.SalesOrderNumber,

P.Name, PS.Name, SOD.UnitPrice, PC.Name



{{< /highlight >}}


La consulta tiene tres parámetros: ReportYear, ReportMonth y EmpID.

1. Desde el menú **Archivo** de Microsoft Query, seleccione **Volver a Aspose.Cells.Report.Designer**. 

   **Regresar al diseñador de informes** 

![todo:image_alt_text](creating-new-data-sources-and-queries_12.png)



El origen de datos y la consulta creada anteriormente se enumeran en el cuadro de diálogo. 

1. Haga clic en el origen de datos **SqlServer** para ver su información detallada. 

   **El nuevo origen de datos** 

![todo:image_alt_text](creating-new-data-sources-and-queries_13.png)




1. Haga clic en la consulta EmpSalesDetails para ver su información detallada. 

   **Haga clic en la pestaña SQL para ver el SQL de la consulta** 

![todo:image_alt_text](creating-new-data-sources-and-queries_14.png)



**Haga clic en la pestaña Columnas para ver las columnas de la consulta** 

![todo:image_alt_text](creating-new-data-sources-and-queries_15.png)



**Haga clic en la pestaña Parámetros para ver los parámetros de la consulta** 

![todo:image_alt_text](creating-new-data-sources-and-queries_16.png)



