---
title: Creación de nuevas fuentes de datos y consultas
type: docs
weight: 20
url: /es/reportingservices/creating-new-data-sources-and-queries/
---
{{% alert color="primary" %}} 

 Aspose.Cells.Report.Designer se integra con MS Query y utiliza MS Query como herramienta para crear fuentes de datos y consultas. Para crear una nueva fuente de datos y una consulta en Aspose.Cells.Report.Designer, siga los pasos a continuación:.

{{% /alert %}} 

Para crear una nueva fuente de datos y una consulta en Aspose.Cells.Report.Designer:

1. Abra Microsoft Excel.
1.  Hacer clic**Construir conjunto de datos** en la barra de herramientas Aspose.Cells.Report.Designer:

![todo:imagen_alternativa_texto](creating-new-data-sources-and-queries_1.png)


Todas las fuentes de datos y consultas se enumeran en el cuadro de diálogo.

1.  Un nodo de fuente de datos:

![todo:imagen_alternativa_texto](creating-new-data-sources-and-queries_2.png)

1.  Un nodo de conjunto de datos:

![todo:imagen_alternativa_texto](creating-new-data-sources-and-queries_3.png)

1. Seleccione el nodo raíz del árbol.
1.  Hacer clic**Agregar**. 

   **Adición de fuentes de datos y conjuntos de datos** 

![todo:imagen_alternativa_texto](creating-new-data-sources-and-queries_4.png)




1.  En el cuadro de diálogo, llame a la fuente de datos**Servidor SQL** y el conjunto de datos**EmpsVentasDetalle**.
1.  Hacer clic**Próximo**. 

   **Adición de conjuntos de datos y fuentes de datos** 

![todo:imagen_alternativa_texto](creating-new-data-sources-and-queries_5.png)



 Aspose.Cells.Report.Designer inicia Microsoft Consulta.

1.  En el cuadro de diálogo Elegir origen de datos, seleccione**Nueva fuente de datos**.
1.  Hacer clic**DE ACUERDO**.
 También puede seleccionar una fuente de datos existente.

   **Elegir una fuente de datos** 

![todo:imagen_alternativa_texto](creating-new-data-sources-and-queries_6.png)




1. Ingrese un nombre de fuente de datos y seleccione SQL Server de la lista desplegable de controladores de base de datos.
1.  Hacer clic**Conectar**. 

   **Creación de una nueva fuente de datos** 

![todo:imagen_alternativa_texto](creating-new-data-sources-and-queries_7.png)




1. En el cuadro de diálogo Inicio de sesión de SQL Server, seleccione el valor adecuado para cada elemento.
 Por ejemplo, establezca el servidor en local, seleccione la base de datos AdventureWorks y seleccione**Usar conexión de confianza**.
1.  Hacer clic**DE ACUERDO**. 

   **Iniciar sesión en el servidor SQL** 

![todo:imagen_alternativa_texto](creating-new-data-sources-and-queries_8.png)




1.  Hacer clic**DE ACUERDO**. 

   **Tenga en cuenta que ahora estamos conectados al servidor SQL** 

![todo:imagen_alternativa_texto](creating-new-data-sources-and-queries_9.png)



La nueva fuente de datos aparece en la**Elija fuente de datos** diálogo.

1.  Seleccione la nueva fuente de datos.

   **La nueva fuente de datos** 

![todo:imagen_alternativa_texto](creating-new-data-sources-and-queries_10.png)




1.  Hacer clic**DE ACUERDO** para abrir Microsoft Consulta.
1.  Para crear una consulta en Microsoft Query, consulte el Microsoft Query Helper. En el siguiente ejemplo, creamos una consulta con parámetros.

   **Construyendo una consulta** 

![todo:imagen_alternativa_texto](creating-new-data-sources-and-queries_11.png)



 El SQL es el siguiente:

**sql**

{{< highlight "csharp" >}}

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

1.  Desde Microsoft Consultas**Archivo** menú, seleccione**Volver a Aspose.Cells.Report.Designer**. 

   **Volviendo al diseñador de informes** 

![todo:imagen_alternativa_texto](creating-new-data-sources-and-queries_12.png)



 La fuente de datos y la consulta creada anteriormente se enumeran en el cuadro de diálogo.

1.  Haga clic en la fuente de datos**Servidor SQL** para ver su información detallada.

   **La nueva fuente de datos** 

![todo:imagen_alternativa_texto](creating-new-data-sources-and-queries_13.png)




1.  Haga clic en la consulta EmpSalesDetails para ver su información detallada.

   **Haga clic en la pestaña SQL para ver el sql de la consulta** 

![todo:imagen_alternativa_texto](creating-new-data-sources-and-queries_14.png)



**Haga clic en la pestaña Columnas para ver las columnas de la consulta** 

![todo:imagen_alternativa_texto](creating-new-data-sources-and-queries_15.png)



**Haga clic en la pestaña Parámetros para ver los parámetros de la consulta** 

![todo:imagen_alternativa_texto](creating-new-data-sources-and-queries_16.png)



