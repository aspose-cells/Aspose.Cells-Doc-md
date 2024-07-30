---
title: Comment verrouiller des cellules pour les protéger
type: docs
weight: 130
url: /fr/net/how-to-lock-cells-to-protect-them/
description: Cet article vous montre un code expliquant comment verrouiller des cellules pour les protéger en utilisant la bibliothèque Aspose.Cells.
keywords: Verrouiller des cellules pour les protéger en C#, Comment verrouiller des cellules pour les protéger en utilisant C#, Verrouiller des cellules pour les protéger en C#.
---

## **Scénarios d'utilisation possibles**
Verrouiller des cellules pour les protéger est une pratique courante dans les applications de tableur, telles que Microsoft Excel ou Google Sheets, pour plusieurs raisons importantes:

1. Éviter les modifications accidentelles : Verrouiller des cellules peut empêcher les utilisateurs de modifier accidentellement des données ou des formules importantes. Cela est particulièrement utile dans les feuilles de calcul complexes où des modifications non intentionnelles peuvent entraîner des erreurs significatives.

1. Maintien de l'intégrité des données : En verrouillant des cellules, vous pouvez garantir que les données critiques restent cohérentes et précises. C'est crucial pour les documents financiers, les rapports et tout autre document où l'intégrité des données est essentielle.

1. Accès contrôlé : Dans les environnements collaboratifs, le verrouillage des cellules vous permet de contrôler qui peut éditer certaines parties d'une feuille de calcul. Par exemple, vous pouvez vouloir autoriser uniquement certains membres de l'équipe à éditer des cellules spécifiques tout en protégeant le reste de la feuille de calcul.

1. Protection des formules : Les formules sont souvent cruciales pour les calculs et l'analyse de données. Verrouiller les cellules contenant des formules garantit que ces formules ne sont pas modifiées ou supprimées accidentellement, ce qui pourrait perturber le fonctionnement de toute la feuille de calcul.

1. Application des règles métier : Dans certains cas, des règles métier spécifiques ou des réglementations peuvent exiger que certaines données soient protégées contre toute modification. Verrouiller des cellules contribue à respecter ces exigences.

1. Guider les utilisateurs : En verrouillant des cellules et en fournissant des instructions claires sur les cellules pouvant être éditées, vous pouvez guider les utilisateurs sur la manière d'interagir avec la feuille de calcul, réduisant la confusion et les erreurs.

## **Comment verrouiller des cellules pour les protéger dans Excel**
Voici comment vous pouvez verrouiller des cellules dans Microsoft Excel:

1. Sélectionnez les cellules à verrouiller : Sélectionnez les cellules que vous voulez verrouiller. Si vous voulez verrouiller toute la feuille, vous pouvez sauter cette étape.
1. Ouvrez la boîte de dialogue Format de cellule : Cliquez avec le bouton droit sur les cellules sélectionnées et choisissez "Format de cellule", ou appuyez sur Ctrl+1.
<br>
<img src="1.png" width=60% />
1. Verrouillez les cellules : Dans la boîte de dialogue Format de cellule, allez à l'onglet "Protection". Cochez la case "Verrouillé". Cliquez sur "OK".
1. Protégez la feuille de calcul : Allez à l'onglet "Révision" dans le Ruban. Cliquez sur "Protéger la feuille". Définissez un mot de passe (facultatif) et choisissez les autorisations que vous souhaitez accorder (par exemple, sélectionner les cellules verrouillées, formater les cellules, etc.). Cliquez sur "OK".
<br>
<img src="2.png" width=60% />

## **Comment verrouiller des cellules pour les protéger en utilisant C#**

Aspose.Cells est une puissante bibliothèque pour travailler avec des fichiers Excel de manière programmable. Pour verrouiller des cellules en utilisant Aspose.Cells, vous devez suivre ces étapes : charger le [fichier d'exemple](sample.xlsx), déverrouiller toutes les cellules d'abord (puisque, par défaut, toutes les cellules sont verrouillées mais non appliquées tant que la feuille de calcul n'est pas protégée), puis verrouiller les cellules spécifiques que vous souhaitez protéger, et enfin protéger la feuille de calcul pour appliquer le verrouillage.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "CellsData-lock-cells-to-protect-them.cs" >}}

## **Résultat de la sortie**
Ce code garantit que seules les cellules spécifiées (A1 et B2 dans cet exemple) sont verrouillées, et la feuille de calcul est protégée pour appliquer ces paramètres. Toutes les autres cellules de la feuille de calcul restent déverrouillées et modifiables.

<br>
<img src="3.png" width=60% />


