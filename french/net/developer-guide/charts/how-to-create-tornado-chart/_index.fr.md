---
title: Comment créer un graphique de tornade
type: docs
weight: 73
url: /fr/net/create-tornado-chart/
description: Apprenez à créer une carte des tornades avec le Aspose.Cells for .NET API.
keywords: C# create a tornado chart, add a tornado chart, insert a tornado chart
---
##  **Introduction**
Un graphique de tornade, également appelé diagramme de tornade ou graphique de tornade, est un type de visualisation de données souvent utilisé pour l'analyse de sensibilité dans Excel. Il vous aide à comprendre l'impact de la modification des variables sur un résultat ou un résultat particulier.

##  **Comment créer un graphique tornade dans Excel**
Vous pouvez créer un graphique tornade dans Excel en suivant ces étapes :
1. Sélectionnez les données et accédez à Insertion -> Graphiques -> Insérer une colonne ou un graphique à barres -> Graphique à barres empilées. Clique dessus.
<br>
<img src="1.png" width=70% />
2. Modifiez l'axe Y : cliquez avec le bouton droit sur l'axe Y. Cliquez sur l'axe de format. Dans les étiquettes, cliquez sur la liste déroulante de position de l’étiquette et sélectionnez Élément faible.
<br>
<img src="2.png" width=70% />
3. Sélectionnez n'importe quelle barre et accédez au formatage. Définissez une largeur d’espace appropriée.
<br>
<img src="3.png" width=70% />
4. Supprimons le signe moins (-) du graphique des tornades. Sélectionnez l'axe des x. Allez au formatage. Dans les options de l'axe, cliquez sur le numéro. Dans la catégorie, sélectionnez personnalisé. Dans le code de format, écrivez ###0,###0. Cliquez sur ajouter.
<br>
<img src="4.png" width=70% />
5. cliquez sur l'axe y et accédez aux options de l'axe. Dans les options de l'axe, cochez Catégories dans l'ordre inverse.
<br>
<img src="5.png" width=70% />

##  **Comment ajouter une carte de tornade dans Aspose.Cells**
 Veuillez consulter l'exemple de code suivant. Il charge le[exemple de fichier Excel](sample.xlsx) qui contient des exemples de données. Il crée ensuite le graphique à barres empilées sur la base des données initiales et définit les propriétés pertinentes. Enfin, il enregistre le classeur dans[sortie au format XLSX](out.xlsx). La capture d'écran suivante montre le graphique de tornade créé par Aspose.Cells dans le fichier Excel de sortie.
<br>
<img src="6.png" width=70% />

###  **Exemple de code**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "create-tornado-chart.cs" >}}