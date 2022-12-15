---
title: Travailler avec un tableau croisé dynamique
type: docs
weight: 100
url: /fr/reportingservices/working-with-pivottable/
---
{{% alert color="primary" %}} 

 UN*tableau croisé dynamique* est un tableau interactif qui résume les données et les présente de manière significative. SQL Server Reporting Services ne peut pas exporter un rapport au format Microsoft Excel tout en conservant un tableau croisé dynamique. Les utilisateurs de rapports doivent créer manuellement des tableaux croisés dynamiques chaque fois qu'ils exportent un rapport de tableau croisé dynamique de Reporting Services vers Microsoft Excel. Avec Aspose.Cells for Reporting Services, vous pouvez concevoir un tableau croisé dynamique une seule fois au moment de la conception du rapport. Chaque fois que le rapport s'exécute, Aspose.Cells for Reporting Services exporte le rapport vers Microsoft Excel et actualise les données dans le tableau croisé dynamique.

{{% /alert %}} 

Pour créer un rapport de tableau croisé dynamique :

1. Créez un jeu de données comme source de données pour le tableau croisé dynamique.
 Ci-dessous, nous utilisons l'exemple de base de données AdventureWorks fourni avec SQL Server Reporting Services 2005 et créons un jeu de données nommé "ventes".
Le SQL du jeu de données est le suivant :

**SQL**

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

 Prière de se référer à[Sources de données et requêtes](/cells/fr/reportingservices/data-sources-and-queries/) pour en savoir plus sur la création d'une source de données et d'un jeu de données avec Aspose.Cells.Report.Designer.

{{% /alert %}} 

1.  Créez un rapport de tableau conformément aux instructions de[Création d'un rapport tabulaire](/cells/fr/reportingservices/creating-tabular-report/), comme indiqué ci-dessous.
 Le tableau sera la source de données du tableau croisé dynamique.

![tâche : image_autre_texte](working-with-pivottable_1.png)




1.  Dans Microsoft Excel, à partir du**Insérer** menu, sélectionnez**Nom** et alors**Définir**.
1. Définissez un nom comme "ventes".
 La plage du nom commence par la première cellule du titre de l'en-tête et se termine à la dernière cellule de la ligne de données du tableau, comme indiqué ci-dessous.

![tâche : image_autre_texte](working-with-pivottable_2.png)




1.  Cliquez sur**D'ACCORD** pour finir.
1. Créez une nouvelle feuille pour le tableau croisé dynamique.
1.  Du**Données** menu, sélectionnez**Tableau croisé dynamique et rapport de graphique croisé dynamique** pour ajouter un tableau croisé dynamique.
 Une boîte de dialogue s'affiche.
1.  Sélectionner**Microsoft Liste ou base de données Office Excel** comme source de données et**tableau croisé dynamique** comme type de rapport.
1.  Cliquez sur**Prochain** continuer.

![tâche : image_autre_texte](working-with-pivottable_3.png)




1. Dans la boîte de dialogue, entrez "ventes", le nom que vous avez défini ci-dessus.
1.  Cliquez sur**Prochain** continuer.

![tâche : image_autre_texte](working-with-pivottable_4.png)




1.  Cliquez sur**Finir**. 

![tâche : image_autre_texte](working-with-pivottable_5.png)




1.  Concevoir le tableau croisé dynamique dans Excel.

![tâche : image_autre_texte](working-with-pivottable_6.png)



 Le tableau croisé dynamique conçu est illustré ci-dessous.

![tâche : image_autre_texte](working-with-pivottable_7.png)




1.  Cliquez avec le bouton droit sur le tableau croisé dynamique et sélectionnez**Options de tableau**.
1.  Sois sûr que**Actualiser à l'ouverture** est sélectionné.

![tâche : image_autre_texte](working-with-pivottable_8.png)




1. Enregistrez le rapport et publiez-le sur Report Server.
1. Exportez le rapport depuis Report Server.
 Le résultat est illustré ci-dessous.

![tâche : image_autre_texte](working-with-pivottable_9.png)
