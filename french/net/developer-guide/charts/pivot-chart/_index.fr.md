---
title: Comment ajouter un tableau croisé dynamique à l aide d Aspose.Cells
linktitle: Tableau croisé dynamique
type: docs
weight: 100
url: /fr/net/how-to-add-pivot-chart/
description: Comment ajouter un tableau croisé dynamique à l aide d Aspose.Cells.
keywords: Tableau croisé dynamique
---
## Qu'est-ce qu'un tableau croisé dynamique

Un graphique croisé dynamique est une représentation visuelle des données dans un tableau croisé dynamique. Les graphiques croisés dynamiques permettent de résumer, d'analyser, d'explorer et de présenter des données récapitulatives. Voici quelques caractéristiques clés et aspects des graphiques croisés dynamiques :

1. Représentation dynamique des données : Les graphiques croisés dynamiques se mettent à jour automatiquement pour refléter les modifications dans le tableau croisé dynamique. Si vous ajoutez ou supprimez des champs dans le tableau croisé dynamique, le graphique croisé dynamique est mis à jour en conséquence.

1. Interactif : Les graphiques croisés dynamiques sont interactifs, permettant aux utilisateurs de filtrer, de trier et de creuser dans les données. Cela facilite l'exploration des différents aspects de l'ensemble de données.

1. Mise en page flexible : Les utilisateurs peuvent modifier la disposition du graphique croisé dynamique en faisant glisser et déposer des champs, ce qui offre une flexibilité dans la visualisation des données.

1. Divers types de graphiques : Les graphiques croisés dynamiques peuvent être créés en utilisant divers types de graphiques tels que les graphiques en barres, les graphiques linéaires, les graphiques circulaires, etc., en fonction de la nature des données et des informations que vous souhaitez obtenir.

1. Résumé : Les graphiques croisés dynamiques résument de grandes quantités de données et peuvent afficher des totaux, des moyennes, des comptages ou d'autres statistiques récapitulatives.

1. Filtrage : Ils offrent des capacités de filtrage, vous permettant d'afficher uniquement les données qui répondent à certains critères.

<br>
Les graphiques croisés dynamiques sont couramment utilisés dans l'intelligence commerciale et l'analyse de données pour fournir un résumé visuel clair et concis d'ensembles de données complexes. Ils sont un outil puissant pour prendre des décisions basées sur les données.

## Comment ajouter un tableau croisé dynamique à l'aide d'Aspose.Cells

### **Ajouter un tableau croisé dynamique**

Pour créer un tableau croisé dynamique en utilisant Aspose.Cells:

1. Ajoutez des données à une feuille de calcul à l'aide de la méthode PutValue/setValue d'un objet Cell. Vous pouvez également utiliser un fichier modèle déjà rempli de données. Ces données seront utilisées comme source de données du tableau croisé dynamique.
1. Ajoutez une table pivotante à la feuille de calcul en appelant la méthode add de la collection PivotTables (encapsulée dans l'objet Feuille de calcul).
1. Accédez au nouvel objet PivotTable depuis la collection PivotTables en passant son index. # Utilisez l'un des objets table pivotante encapsulés dans l'objet PivotTable pour gérer la table.

Des exemples de code sont donnés ci-dessous.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CreatePivotTablesPivotCharts-CreatePivotTable-1.cs" >}}

### **Ajout d'un graphique croisé dynamique**

Pour créer un graphique croisé dynamique en utilisant Aspose.Cells :

1. Ajoutez un graphique.
1. Définissez la PivotSource du graphique pour qu'elle fasse référence à une table pivotante existante dans la feuille de calcul.
1. Définissez d'autres attributs.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CreatePivotTablesPivotCharts-CreatePivotChart-1.cs" >}}

