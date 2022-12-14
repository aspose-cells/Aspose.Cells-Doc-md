---
title: Création de nouvelles sources de données et requêtes
type: docs
weight: 20
url: /fr/reportingservices/creating-new-data-sources-and-queries/
---
{{% alert color="primary" %}} 

 Aspose.Cells.Report.Designer s'intègre à MS Query et utilise MS Query comme outil de création de sources de données et de requêtes. Pour créer une nouvelle source de données et une nouvelle requête dans Aspose.Cells.Report.Designer, suivez les étapes ci-dessous :.

{{% /alert %}} 

Pour créer une nouvelle source de données et une nouvelle requête dans Aspose.Cells.Report.Designer :

1. Ouvrez Microsoft Excel.
1.  Cliquez sur**Construire un ensemble de données** dans la barre d'outils Aspose.Cells.Report.Designer :

![tâche : image_autre_texte](creating-new-data-sources-and-queries_1.png)


Toutes les sources de données et les requêtes sont répertoriées dans la boîte de dialogue.

1.  Un nœud de source de données :

![tâche : image_autre_texte](creating-new-data-sources-and-queries_2.png)

1.  Un nœud d'ensemble de données :

![tâche : image_autre_texte](creating-new-data-sources-and-queries_3.png)

1. Sélectionnez le nœud racine de l'arborescence.
1.  Cliquez sur**Ajouter**. 

   **Ajout de sources de données et d'ensembles de données** 

![tâche : image_autre_texte](creating-new-data-sources-and-queries_4.png)




1.  Dans la boîte de dialogue, appelez la source de données**Serveur SQL** et l'ensemble de données**EmpsSalesDetail**.
1.  Cliquez sur**Prochain**. 

   **Ajout d'ensembles de données et de sources de données** 

![tâche : image_autre_texte](creating-new-data-sources-and-queries_5.png)



 Aspose.Cells.Report.Designer démarre la requête Microsoft.

1.  Dans la boîte de dialogue Choisir une source de données, sélectionnez**Nouvelle source de données**.
1.  Cliquez sur**D'ACCORD**.
 Vous pouvez également sélectionner une source de données existante.

   **Choisir une source de données** 

![tâche : image_autre_texte](creating-new-data-sources-and-queries_6.png)




1. Entrez un nom de source de données et sélectionnez SQL Server dans la liste déroulante des pilotes de base de données.
1.  Cliquez sur**Relier**. 

   **Création d'une nouvelle source de données** 

![tâche : image_autre_texte](creating-new-data-sources-and-queries_7.png)




1. Dans la boîte de dialogue de connexion SQL Server, sélectionnez la valeur appropriée pour chaque élément.
 Par exemple, définissez le serveur sur local, sélectionnez la base de données AdventureWorks et sélectionnez**Utiliser une connexion sécurisée**.
1.  Cliquez sur**D'ACCORD**. 

   **Connexion au serveur SQL** 

![tâche : image_autre_texte](creating-new-data-sources-and-queries_8.png)




1.  Cliquez sur**D'ACCORD**. 

   **Notez que nous sommes maintenant connectés au serveur SQL** 

![tâche : image_autre_texte](creating-new-data-sources-and-queries_9.png)



La nouvelle source de données apparaît dans le**Choisissez la source de données** dialogue.

1.  Sélectionnez la nouvelle source de données.

   **La nouvelle source de données** 

![tâche : image_autre_texte](creating-new-data-sources-and-queries_10.png)




1.  Cliquez sur**D'ACCORD** pour ouvrir la requête Microsoft.
1.  Pour créer une requête dans Microsoft Query, reportez-vous à l'assistant de requête Microsoft. Dans l'exemple suivant, nous créons une requête avec des paramètres.

   **Construire une requête** 

![tâche : image_autre_texte](creating-new-data-sources-and-queries_11.png)



 Le SQL est le suivant :

**SQL**

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


La requête a trois paramètres : ReportYear, ReportMonth et EmpID.

1.  De Microsoft Requêtes**Dossier** menu, sélectionnez**Retour à Aspose.Cells.Report.Designer**. 

   **Revenir au concepteur de rapports** 

![tâche : image_autre_texte](creating-new-data-sources-and-queries_12.png)



 La source de données et la requête créées ci-dessus sont répertoriées dans la boîte de dialogue.

1.  Cliquez sur la source de données**Serveur SQL** pour afficher ses informations détaillées.

   **La nouvelle source de données** 

![tâche : image_autre_texte](creating-new-data-sources-and-queries_13.png)




1.  Cliquez sur la requête EmpSalesDetails pour afficher ses informations détaillées.

   **Cliquez sur l'onglet SQL pour afficher le sql de la requête** 

![tâche : image_autre_texte](creating-new-data-sources-and-queries_14.png)



**Cliquez sur l'onglet Colonnes pour afficher les colonnes de la requête** 

![tâche : image_autre_texte](creating-new-data-sources-and-queries_15.png)



**Cliquez sur l'onglet Paramètres pour afficher les paramètres de la requête** 

![tâche : image_autre_texte](creating-new-data-sources-and-queries_16.png)



