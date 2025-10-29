---
title: Comment créer un graphique en entonnoir
type: docs
weight: 73
url: /fr/python-net/create-tornado-chart/
description: Apprenez comment créer un graphique en tornade avec Aspose.Cells pour Python via .NET API.
keywords: Python créer un graphique en tornade, ajouter un graphique en tornade, insérer un graphique en tornade
---

## **Introduction**
Un diagramme en forme de tornade, également connu sous le nom de diagramme en forme de tornade ou graphique en forme de tornade, est un type de visualisation de données souvent utilisé pour l'analyse de sensibilité dans Excel. Il vous aide à comprendre l'impact des variables changeantes sur un résultat particulier.

## **Comment créer un diagramme en forme de tornade dans Excel**
Vous pouvez créer un diagramme en forme de tornade dans Excel en suivant ces étapes :
1. Sélectionnez les données et allez dans Insertion --> Graphiques --> Insérer un histogramme ou un graphique à barres --> Graphique à barres empilées. Cliquez dessus.
<br>
<img src="1.png" width=70% />
2. Modifiez l'axe des Y : Cliquez avec le bouton droit sur l'axe des y. Cliquez sur formater l'axe. Dans les étiquettes, cliquez sur le menu déroulant de la position des étiquettes et sélectionnez l'élément inférieur.
<br>
<img src="2.png" width=70% />
3. Sélectionnez une barre quelconque et allez dans le formatage. Définissez une largeur d'écart appropriée.
<br>
<img src="3.png" width=70% />
4. Supprimons le signe moins (-) du diagramme en forme de tornade. Sélectionnez l'axe des x. Allez dans le formatage. Dans les options d'axe, cliquez sur le nombre. Dans la catégorie, sélectionnez personnalisé. Dans le code de format, écrivez ###0,###0. Cliquez sur ajouter.
<br>
<img src="4.png" width=70% />
5. cliquez sur l'axe des y et allez dans les options d'axe. Dans les options d'axe, cochez Catégories dans l'ordre inverse.
<br>
<img src="5.png" width=70% />

## **Comment ajouter un graphique en tornade dans Aspose.Cells pour la bibliothèque Excel Python**
Veuillez consulter l'exemple de code suivant. Il charge le [fichier Excel d'exemple](sample.xlsx) contenant quelques données d'exemple. Il crée ensuite le graphique à barres empilées basé sur les données initiales et règle les propriétés pertinentes. Enfin, il enregistre le classeur au format [XLSX de sortie](out.xlsx). La capture d'écran suivante montre le graphique en tornade créé par Aspose.Cells pour Python via .NET dans le fichier Excel de sortie.
<br>
<img src="6.png" width=70% />

### **Code d'exemple**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-create-tornado-chart.py" >}}
{{< app/cells/assistant language="python-net" >}}
