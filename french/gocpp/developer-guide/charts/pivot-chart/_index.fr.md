---
title: Comment ajouter un PivotChart avec Golang via C++
linktitle: Tableau croisé dynamique
type: docs
weight: 100
url: /fr/go-cpp/how-to-add-pivot-chart/
description: Comment ajouter un PivotChart en utilisant Aspose.Cells avec Golang via C++.
keywords: Tableau croisé dynamique
---

## Qu'est-ce qu'un tableau croisé dynamique

Un graphique croisé dynamique est une représentation visuelle des données dans un tableau croisé dynamique. Les graphiques croisés dynamiques offrent un moyen de résumer, analyser, explorer et présenter des données résumées. Voici quelques caractéristiques clés des graphiques croisés dynamiques :

1. **Représentation dynamique des données** : Les graphiques croisés dynamiques se mettent automatiquement à jour pour refléter les changements dans le tableau croisé dynamique. Si vous ajoutez ou retirez des champs dans le tableau croisé dynamique, le graphique croisé dynamique se met à jour en conséquence.

1. **Interactif** : Les graphiques croisés dynamiques sont interactifs, permettant aux utilisateurs de filtrer, trier et explorer les données. Cela facilite l'exploration de différents aspects de l'ensemble de données.

1. **Disposition flexible** : Les utilisateurs peuvent changer la disposition du graphique croisé dynamique en faisant glisser et déposant des champs, ce qui offre une flexibilité dans la visualisation des données.

1. **Différents types de graphiques** : Les graphiques croisés dynamiques peuvent être créés à l'aide de divers types de graphiques tels que des graphiques à barres, à lignes, en secteurs, etc., en fonction de la nature des données et des insights que vous souhaitez obtenir.

1. **Résumé** : Les graphiques croisés dynamiques résument de grandes quantités de données et peuvent afficher des totaux, des moyennes, des comptages ou d'autres statistiques résumées.

1. **Filtrage** : Ils offrent des capacités de filtrage, vous permettant d'afficher uniquement les données qui répondent à certains critères.

<br>
Les graphiques croisés dynamiques sont couramment utilisés dans l’intelligence d’affaires et l’analyse de données pour fournir un résumé visuel clair et concis de jeux de données complexes. Ils sont un outil puissant pour prendre des décisions basées sur les données.

## Comment ajouter un tableau croisé dynamique à l'aide d'Aspose.Cells

### **Ajouter un tableau croisé dynamique**

Pour créer un tableau croisé dynamique en utilisant Aspose.Cells:

1. Ajoutez des données dans les cellules d'une feuille de calcul en utilisant la méthode `PutValue` ou `SetValue` d'un objet `Cell`. Vous pouvez également utiliser un fichier modèle déjà rempli de données. Les données seront utilisées comme source de données pour le tableau croisé dynamique.
1. Ajoutez un tableau croisé dynamique à la feuille en appelant la méthode `Add` de la collection `PivotTables` (encapsulée dans l'objet `Worksheet`).
1. Accédez au nouvel objet `PivotTable` dans la collection `PivotTables` en passant son index. Utilisez l'un des objets de tableau croisé dynamique encapsulés dans l'objet `PivotTable` pour gérer le tableau.

Des exemples de code sont donnés ci-dessous.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-PivotChart.go" >}}
### **Ajout d'un graphique croisé dynamique**

Pour créer un graphique croisé dynamique en utilisant Aspose.Cells :

1. Ajoutez un graphique.
1. Définissez le `PivotSource` du graphique pour référencer un tableau croisé dynamique existant dans la feuille de calcul.
1. Définissez d'autres attributs.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-PivotChart-1.go" >}}
