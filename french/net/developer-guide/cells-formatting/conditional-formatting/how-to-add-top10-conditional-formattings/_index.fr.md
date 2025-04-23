---
title: Comment ajouter un formatage conditionnel Top10
description: Comment utiliser la bibliothèque Aspose.Cells en C# pour appliquer un formatage conditionnel Top10. En ajustant ces critères, vous avez plus de contrôle sur l apparence et la présentation des cellules.
keywords: Aspose.Cells, Formatage conditionnel Top10, C#, Conditionnel, Formatage
type: docs
weight: 70
url: /fr/net/how-to-add-top10-conditional-formatting/
---

## **Scénarios d'utilisation possibles**
L'utilisation du Top 10 en mise en forme conditionnelle dans Excel permet de mettre en évidence rapidement les valeurs les plus performantes dans un jeu de données — pas seulement les 10 valeurs les plus élevées, mais souvent les N premières ou les N% (vous pouvez choisir !).

1. Repérer les tendances et les valeurs aberrantes : Identifier instantanément les meilleurs performeurs (par exemple, les 10 meilleurs représentants commerciaux, les meilleures notes, les mois de chiffre d'affaires le plus élevé).Facilite l'analyse sans trier les données.
1. Visualisation des données : Ajoute des repères couleur qui font ressortir visuellement les points de données importants.Aide les lecteurs du tableau à comprendre rapidement les valeurs clés.
1. Comparaisons rapides : Utile dans les tableaux de bord et rapports où vous souhaitez mettre en évidence l'excellence ou les pics.
1. Mises à jour dynamiques : Si vos données changent, la mise en forme conditionnelle se met à jour automatiquement pour refléter les nouvelles valeurs principales.

## **Comment ajouter la mise en forme conditionnelle Top10 dans Excel**
Voici comment ajouter la mise en forme conditionnelle Top10 dans Excel, étape par étape :

1. Sélectionnez la plage de cellules que vous souhaitez analyser. Par exemple : Sélectionnez B2:B100 si vous travaillez avec des scores ou des chiffres de ventes.
1. Allez dans l'onglet Accueil du ruban Excel.
1. Cliquez sur Mise en forme conditionnelle dans le groupe Styles.
1. Survolez Règles Top/Bottom dans le menu déroulant.
1. Cliquez sur Top 10…
1. Une boîte de dialogue apparaîtra : Elle dira : Mettre en forme les cellules qui occupent le rang des 10 premiers. Vous pouvez modifier le nombre (par exemple, Top 5, Top 3, etc.). Choisissez un format (comme un remplissage rouge clair, du texte en gras, ou cliquez sur Format personnalisé pour plus d'options).
1. Cliquez sur OK


## **Comment ajouter la mise en forme conditionnelle Top10 en utilisant Aspose.Cells for .NET**

Aspose.Cells supporte intégralement la mise en forme conditionnelle fournie par Microsoft Excel 2007 et versions ultérieures en format XLSX sur les cellules à l'exécution. Cet exemple illustre un exercice de mise en forme conditionnelle Top 10 avec différents ensembles d'attributs.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Formatting-Advanced-Top10.cs" >}}

{{< app/cells/assistant language="csharp" >}}
