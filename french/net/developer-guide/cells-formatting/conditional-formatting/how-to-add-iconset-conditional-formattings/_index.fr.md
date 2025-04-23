---
title: Comment ajouter des ensembles d icônes dans le formatage conditionnel
description: Comment utiliser la bibliothèque Aspose.Cells en C# pour appliquer un formatage conditionnel avec des ensembles d’icônes. En ajustant ces critères, vous contrôlez davantage l apparence des cellules.
keywords: Aspose.Cells, Formatage conditionnel avec ensembles d’icônes, C#, Conditionnel, Formatage
type: docs
weight: 70
url: /fr/net/how-to-add-icon-sets-conditional-formatting/
---

## **Scénarios d'utilisation possibles**
L’utilisation de l’icône dans le formatage conditionnel dans Excel est un excellent moyen de visualiser rapidement les tendances ou catégories de données en utilisant des symboles comme des flèches, des feux de circulation, des étoiles, des drapeaux, etc. Cela ajoute une couche supplémentaire de clarté à votre feuille de calcul sans nécessiter de graphiques ou d’analyse approfondie.

1. Informations visuelles instantanées : Les icônes facilitent la compréhension immédiate de quelles valeurs sont élevées, moyennes ou faibles sans lire chaque nombre. Idéal pour les tableaux de bord, KPIs et le suivi des performances.
1. Détection facile des tendances : Les flèches indiquent si les valeurs augmentent, diminuent ou restent neutres. Les feux de circulation ou formes aident à indiquer le statut ou l'urgence.
1. Aspect professionnel : Rend les rapports plus soignés et prêts à être présentés. Aide les spectateurs non techniques à comprendre rapidement les données.
1. Dynamique & automatique : Se met à jour automatiquement lorsque les valeurs changent — pas besoin de reformater manuellement.

## **Comment ajouter des ensembles d’icônes dans le formatage conditionnel avec Excel**
Pour ajouter un formatage conditionnel avec des ensembles d’icônes dans Excel, voici comment faire étape par étape :

1. Sélectionnez votre plage de données numériques. Exemple : B2:B20 (peut être des chiffres de vente, des scores de performance, etc.).
1. Allez à l'onglet Accueil.
1. Cliquez sur Mise en forme conditionnelle dans le groupe Styles.
1. Survolez les Icônes de jeu de symboles.
1. Choisissez un style d'icône : Flèches, Feux de circulation, Étoiles, etc.
1. Les icônes apparaîtront par défaut en fonction de la répartition des valeurs : Icône verte = 67 % supérieur, Icône jaune = 33-67 % moyen, Icône rouge = 33 % inférieur.


## **Comment ajouter des jeux d'icônes avec la mise en forme conditionnelle en utilisant Aspose.Cells for .NET**

Aspose.Cells supporte pleinement la mise en forme conditionnelle fournie par Microsoft Excel 2007 et versions ultérieures au format XLSX sur des cellules à l'exécution. Cet exemple illustre une exercice de mise en forme conditionnelle avec des jeux d'icônes avec différents ensembles d'attributs.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Formatting-Advanced-IconSets.cs" >}}

{{< app/cells/assistant language="csharp" >}}
