---
title: Travailler avec les graphiques
type: docs
weight: 110
url: /fr/reportingservices/working-with-charts/
---

{{% alert color="primary" %}} 

Le modèle de rapport Aspose.Cells prend en charge les graphiques Microsoft Excel. Chaque fois que vous exécutez un rapport, le graphique est rempli avec les données les plus récentes. 

{{% /alert %}} 

Pour ajouter un graphique au modèle de rapport :

1. Tout d'abord, créez l'ensemble de données qui servira de source de données pour le graphique.
   Ci-dessous, nous utilisons la base de données d'exemple AdventureWorks fournie avec SQL Server Reporting Services 2005 et nous créons un jeu de données nommé Ventes.
   Ce SQL définit l'ensemble de données : 

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



Veuillez vous référer à [Sources de données et requêtes](/cells/fr/reportingservices/data-sources-and-queries/) pour en apprendre davantage sur la création d'une source de données et d'un jeu de données dans Aspose.Cells.Report.Designer.

1. Créez un rapport tabulaire selon les instructions dans [Création de rapport tabulaire](/cells/fr/reportingservices/creating-tabular-report/). Le rapport que nous avons créé pour cet exemple est ci-dessous. Le tableau est la source de données du graphique. 

![todo:image_alt_text](working-with-charts_1.png)




1. Dans Microsoft Excel, cliquez sur le menu **Insérer** et sélectionnez **Graphique**.
1. Cliquez sur **Suivant**. 

![todo:image_alt_text](working-with-charts_2.png)




1. Cliquez sur l'onglet **Série**. 

![todo:image_alt_text](working-with-charts_3.png)




1. Cliquez sur **Ajouter**. 

![todo:image_alt_text](working-with-charts_4.png)




1. Dans la boîte de dialogue, définissez la valeur de la Série1 (série du trimestre) sur le premier champ de données du tableau.
   Dans l'exemple, c'est “VentesSociété!$C$3:$C$3”. Le premier $C$3 est l'index de la première ligne de “Trimestre” et le second $C$3 est un espace réservé pour l'index de la dernière ligne de “Trimestre” et sera remplacé par l'index réel de la ligne de données du tableau au moment du rendu. Définissez les étiquettes de l'axe des catégories(X) sur “=VentesSociété!$C$3:$C$3”. 

![todo:image_alt_text](working-with-charts_5.png)




1. Cliquez sur **Ajouter** pour ajouter une autre série.
   Dans l'exemple, nous avons ajouté la série de ventes. 
1. Définissez la valeur de la Série2 (série de ventes) sur le second champ de données du tableau.
   Dans l'exemple, c'est “VentesSociété!$D$3:$D$3”. Le premier $D$3 est l'index de la première ligne de “Ventes” et le second $D$3 est un espace réservé pour l'index de la dernière ligne de “Ventes” et sera remplacé par l'index réel de la ligne de données du tableau au moment du rendu. 
1. Cliquez sur **Suivant** pour continuer. 

![todo:image_alt_text](working-with-charts_6.png)




1. Dans la boîte de dialogue, définissez le titre du graphique et l'axe des catégories(X).
1. Cliquez sur **Terminer** pour terminer le travail. 

![todo:image_alt_text](working-with-charts_7.png)



Le modèle ressemble à ce qui suit. 

![todo:image_alt_text](working-with-charts_8.png)




1. Enregistrez le rapport et publiez-le sur le serveur de rapports.
1. Exportez le rapport à partir du serveur de rapports.
   Le résultat est comme ci-dessous. 

![todo:image_alt_text](working-with-charts_9.png)
