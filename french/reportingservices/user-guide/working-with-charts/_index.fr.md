---
title: Travailler avec des graphiques
type: docs
weight: 110
url: /fr/reportingservices/working-with-charts/
---
{{% alert color="primary" %}} 

 Aspose.Cells Le modèle de rapport prend en charge les graphiques Excel Microsoft. Chaque fois que vous exécutez un rapport, le graphique est rempli avec les données les plus récentes.

{{% /alert %}} 

Pour ajouter un graphique au modèle de rapport :

1. Tout d'abord, créez le jeu de données qui sera la source de données du graphique.
 Ci-dessous, nous utilisons l'exemple de base de données AdventureWorks fourni avec SQL Server Reporting Services 2005 et créons un jeu de données nommé Sales.
 Ce SQL définit l'ensemble de données :

**SQL**

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



 Prière de se référer à[Sources de données et requêtes](/cells/fr/reportingservices/data-sources-and-queries/) pour en savoir plus sur la création d'une source de données et d'un jeu de données dans Aspose.Cells.Report.Designer.

1. Créez un rapport tabulaire conformément aux instructions de[Création d'un rapport tabulaire](/cells/fr/reportingservices/creating-tabular-report/) . Le rapport que nous avons créé pour cet exemple est ci-dessous. Le tableau est la source de données du graphique.

![tâche : image_autre_texte](working-with-charts_1.png)




1.  Dans Microsoft Excel, cliquez sur le**Insérer** menu et sélectionnez**Graphique**.
1.  Cliquez sur**Suivant**. 

![tâche : image_autre_texte](working-with-charts_2.png)




1.  Clique le**Série** languette.

![tâche : image_autre_texte](working-with-charts_3.png)




1.  Cliquez sur**Ajouter**. 

![tâche : image_autre_texte](working-with-charts_4.png)




1. Dans la boîte de dialogue, définissez la valeur de Series1 (Quarter series) sur le premier champ de données de la table.
 Dans l'exemple, c'est "CompanySales!$C$3:$C$3". Le premier $C$3 est l'index de première ligne de "Quarter" et le second $C$3 est un espace réservé pour l'index de dernière ligne de "Quarter" et sera remplacé par l'index de ligne réel des données de la table au moment du rendu. Définissez les étiquettes de l'axe des catégories (X) sur "=CompanySales!$C$3:$C$3".

![tâche : image_autre_texte](working-with-charts_5.png)




1.  Cliquez sur**Ajouter** pour ajouter une autre série.
 Dans l'échantillon, nous avons ajouté la série des ventes.
1. Définissez la valeur de Series2 (Sales series) sur le deuxième champ de données de la table.
Dans l'exemple, il s'agit de "CompanySales !$D$3:$D$3". Le premier $D$3 est l'index de la première ligne de "Sales" et le second $D$3 est un espace réservé pour l'index de la dernière ligne de "Sales" et sera remplacé par l'index de ligne réel des données de la table au moment du rendu.
1.  Cliquez sur**Suivant** continuer.

![tâche : image_autre_texte](working-with-charts_6.png)




1. Dans la boîte de dialogue, définissez le titre du graphique et l'axe des catégories (X).
1.  Cliquez sur**Finir** pour achever le travail.

![tâche : image_autre_texte](working-with-charts_7.png)



 Le modèle ressemble à celui ci-dessous.

![tâche : image_autre_texte](working-with-charts_8.png)




1. Enregistrez le rapport et publiez-le sur Report Server.
1. Exportez le rapport depuis Report Server.
 Le résultat est comme ci-dessous.

![tâche : image_autre_texte](working-with-charts_9.png)
