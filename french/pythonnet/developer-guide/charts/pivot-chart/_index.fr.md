---
title: Comment ajouter un graphique croisé dynamique avec Aspose.Cells pour Python via .NET
linktitle: Tableau croisé dynamique
type: docs
weight: 100
url: /fr/python-net/how-to-add-pivot-chart/
description: Comment ajouter un graphique croisé dynamique avec Aspose.Cells pour Python via .NET.
keywords: Tableau croisé dynamique
---
## Qu'est-ce qu'un tableau croisé dynamique

Un graphique croisé dynamique est une représentation visuelle des données dans un tableau croisé dynamique. Les graphiques croisés dynamiques offrent un moyen de résumer, analyser, explorer et présenter des données résumées. Voici quelques caractéristiques clés des graphiques croisés dynamiques :

1. Représentation dynamique des données : Les graphiques croisés dynamiques se mettent à jour automatiquement pour refléter les changements dans le tableau croisé dynamique. Si vous ajoutez ou supprimez des champs dans le tableau, le graphique croisé dynamique se met à jour en conséquence.

1. Interactif : Les graphiques croisés dynamiques sont interactifs, permettant aux utilisateurs de filtrer, trier et approfondir les données. Cela facilite l'exploration de différents aspects de l'ensemble de données.

1. Mise en page flexible : Les utilisateurs peuvent modifier la mise en page du graphique croisé dynamique en déplaçant et en déposant des champs, ce qui offre une flexibilité dans la façon dont les données sont visualisées.

1. Divers types de graphiques : Les graphiques croisés dynamiques peuvent être créés à l’aide de divers types de graphiques tels que diagrammes à barres, graphiques linéaires, graphiques en secteurs, et plus encore, selon la nature des données et les insights que vous souhaitez obtenir.

1. Résumé : Les graphiques croisés dynamiques résument de grandes quantités de données et peuvent afficher des totaux, des moyennes, des comptes ou d’autres statistiques résumées.

1. Filtrage : Ils offrent des capacités de filtrage, permettant d’afficher uniquement les données qui répondent à certains critères.

<br>
Les graphiques croisés dynamiques sont couramment utilisés dans l’intelligence d’affaires et l’analyse de données pour fournir un résumé visuel clair et concis de jeux de données complexes. Ils sont un outil puissant pour prendre des décisions basées sur les données.

## Comment ajouter un graphique croisé dynamique avec la bibliothèque Python d'Aspose.Cells

### **Ajouter un tableau croisé dynamique**

Pour créer une table pivotante à l'aide de Aspose.Cells for Python via .NET :

1. Ajoutez des données à une feuille de calcul à l'aide de la méthode PutValue/setValue d'un objet Cell. Vous pouvez également utiliser un fichier modèle déjà rempli de données. Ces données seront utilisées comme source de données du tableau croisé dynamique.
1. Ajoutez une table pivotante à la feuille de calcul en appelant la méthode add de la collection PivotTables (encapsulée dans l'objet Feuille de calcul).
1. Accédez au nouvel objet PivotTable depuis la collection PivotTables en passant son index. # Utilisez l'un des objets table pivotante encapsulés dans l'objet PivotTable pour gérer la table.

Des exemples de code sont donnés ci-dessous.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-CreatePivotTable-1.py" >}}

### **Ajout d'un graphique croisé dynamique**

Pour créer un graphique pivotant à l'aide de Aspose.Cells for Python via .NET :

1. Ajoutez un graphique.
1. Définissez la PivotSource du graphique pour qu'elle fasse référence à une table pivotante existante dans la feuille de calcul.
1. Définissez d'autres attributs.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-CreatePivotChart-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
