---
title: Comment définir des titres d impression
type: docs
weight: 200
url: /fr/net/how-to-set-print-titles/
description: Cet article vous présente un code expliquant comment définir des titres d impression en utilisant la bibliothèque Aspose.Cells.
keywords: Imprimer les lignes et colonnes en boucle, C# Comment définir les titres d impression, Définir et effacer les titres d impression en utilisant C#, Comment effacer les titres d impression en C#, Ajouter les titres d impression en C#, supprimer les titres d impression en C#, Définir les titres d impression dans Excel, Effacer les titres d impression dans Excel.
---

## **Scénarios d'utilisation possibles**

La définition des titres d'impression dans Excel garantit que certaines lignes ou colonnes sont répétées sur chaque page imprimée, ce qui est particulièrement utile pour les grands tableaux qui s'étendent sur plusieurs pages. Voici quelques raisons pour lesquelles vous pourriez définir des titres d'impression :

1. Amélioration de la lisibilité : Les titres d'impression aident les lecteurs à comprendre les données en maintenant les en-têtes visibles sur toutes les pages, ce qui facilite l'interprétation des informations sur chaque page sans avoir à revenir à la première.

1. Présentation professionnelle : Afficher de manière cohérente les en-têtes ou étiquettes sur chaque page donne un aspect plus soigné et professionnel aux documents imprimés.

1. Navigation améliorée : Pour les documents avec beaucoup de données, répéter les en-têtes sur chaque page facilite la navigation et la référence, réduisant la nécessité de feuilleter entre les pages.

1. Réduction des erreurs : Lorsque les en-têtes sont présents sur chaque page, cela minimise les risques de mauvaise interprétation ou d'erreurs de saisie, car les utilisateurs peuvent facilement voir le contexte des données.

1. Cohérence : S'assurer que des informations importantes, telles que les en-têtes de colonnes ou les étiquettes de lignes, sont toujours visibles maintient la cohérence et la clarté dans tout le document.

## **Comment définir des titres d'impression dans Excel**

Pour définir des titres d'impression dans Excel, suivez ces étapes :

1. Ouvrir l'onglet Mise en Page : Cliquez sur l'onglet « Mise en Page » dans le ruban en haut de la fenêtre Excel.
1. Accéder aux Titres d'Impression : Dans le groupe « Mise en Page », cliquez sur « Titres d'impression ».
1. Définir les lignes à répéter : Dans la boîte de dialogue "Mise en page", allez à l'onglet "Feuille". Dans la section "Titres d'impression", spécifiez les lignes à répéter en haut en cliquant sur la case à côté de "Lignes à répéter en haut" et en sélectionnant la ou les lignes souhaitées.
1. Définir les colonnes à répéter (si nécessaire) : De même, vous pouvez spécifier les colonnes à répéter à gauche en cliquant sur la case à côté de "Colonnes à répéter à gauche" et en sélectionnant la ou les colonnes souhaitées.
<br>
<img src="3.png" width=60% />

1. Confirmer et Imprimer : Cliquez sur « OK » pour appliquer les paramètres. Lors de l'impression de la feuille de calcul, les lignes ou colonnes spécifiées apparaîtront sur chaque page imprimée.

## **Comment supprimer les titres d'impression dans Excel**

Pour supprimer les titres d'impression dans Excel, il faut retirer les lignes ou colonnes programmées pour se répéter sur chaque page imprimée. Voici comment faire :

1. Ouvrir l'onglet Mise en Page : Cliquez sur l'onglet « Mise en Page » dans le ruban en haut de la fenêtre Excel.
1. Accéder aux Titres d'Impression : Dans le groupe « Mise en Page », cliquez sur « Titres d'impression ».
1. Supprimer les Titres d'Impression : Dans la boîte de dialogue « Mise en Page », allez à l'onglet « Feuille ». Effacez le contenu des zones de texte « Répéter les lignes en haut » et « Répéter les colonnes à gauche » en supprimant leur contenu.
<br>
<img src="4.png" width=60% />

1. Confirmer et Fermer : Cliquez sur « OK » pour appliquer les modifications.


## **Comment définir des titres d'impression avec Aspose.Cells**

Pour définir des titres d'impression dans une feuille spécifique : Tout d'abord, chargez le [fichier d'exemple](input.xlsx), puis vous devez modifier les propriétés [**Worksheet.PageSetup.PrintTitleRows**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/printtitlerows/) et [**Worksheet.PageSetup.PrintTitleColumns**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/printtitlecolumns/) de l'objet [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/) pour la feuille souhaitée. Définir ces propriétés avec une chaîne de plage configurera les titres d'impression.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Worksheets-PageSetup-set-print-titles.cs" >}}

Le résultat en sortie :
<br>
<img src="1.png" width=60% />

## **Comment supprimer les titres d'impression avec Aspose.Cells**

Pour supprimer les titres d'impression dans une feuille spécifique : Tout d'abord, chargez le [fichier d'exemple](input.xlsx), puis modifiez les propriétés [**Worksheet.PageSetup.PrintTitleRows**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/printtitlerows/) et [**Worksheet.PageSetup.PrintTitleColumns**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/printtitlecolumns/) de l'objet [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/) pour la feuille souhaitée. En définissant ces propriétés comme une chaîne vide, vous supprimerez les titres d'impression.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Worksheets-PageSetup-clear-print-titles.cs" >}}

Le résultat en sortie :
<br>
<img src="2.png" width=60% />
{{< app/cells/assistant language="csharp" >}}
