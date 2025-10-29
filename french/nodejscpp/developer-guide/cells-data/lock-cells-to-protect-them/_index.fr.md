---
title: Comment verrouiller les cellules pour les protéger
type: docs
weight: 130
url: /fr/nodejs-cpp/how-to-lock-cells-to-protect-them/
description: Cet article vous montre un code expliquant comment verrouiller des cellules pour les protéger en utilisant Aspose.Cells for Node.js via C++.
keywords: Verrouiller les cellules dans Node.js pour les protéger, Comment verrouiller des cellules pour les protéger en Node.js, Verrouiller les cellules pour les protéger dans Node.js.
---

## **Scénarios d'utilisation possibles**
Verrouiller les cellules pour les protéger est une pratique courante dans les applications de feuille de calcul, telles que Microsoft Excel ou Google Sheets, pour plusieurs raisons importantes :

1. Prévenir les modifications accidentelles : verrouiller les cellules peut empêcher les utilisateurs de modifier accidentellement des données ou des formules importantes. Cela est particulièrement utile dans les feuilles complexes où des modifications non intentionnelles peuvent entraîner des erreurs majeures.

1. Maintenir l'intégrité des données : en verrouillant les cellules, vous pouvez faire en sorte que les données critiques restent cohérentes et précises. Ceci est essentiel pour les documents financiers, les rapports, et tout autre document où l'intégrité des données est cruciale.

1. Contrôle d'accès : dans des environnements collaboratifs, verrouiller les cellules permet de contrôler qui peut modifier certaines parties d'une feuille de calcul. Par exemple, vous pourriez autoriser uniquement certains membres de l'équipe à modifier des cellules spécifiques tout en protégeant le reste de la feuille.

1. Protection des formules : les formules sont souvent cruciales pour les calculs et l'analyse des données. Verrouiller les cellules contenant des formules garantit que ces formules ne soient pas modifiées ou supprimées accidentellement, ce qui pourrait perturber la fonctionnalité de toute la feuille.

1. Application des règles commerciales : dans certains cas, des règles ou réglementations commerciales spécifiques peuvent exiger que certaines données soient protégées contre toute modification. Verrouiller les cellules aide à respecter ces exigences.

1. Guider les utilisateurs : en verrouillant les cellules et en fournissant des instructions claires sur les cellules pouvant être modifiées, vous pouvez guider les utilisateurs sur la façon d'interagir avec la feuille de calcul, réduisant ainsi la confusion et les erreurs.

## **Comment verrouiller les cellules pour les protéger dans Excel**
Voici comment verrouiller des cellules dans Microsoft Excel :

1. Sélectionnez les cellules à verrouiller : Sélectionnez les cellules que vous souhaitez verrouiller. Si vous voulez verrouiller toute la feuille, vous pouvez sauter cette étape.
1. Ouvrir la boîte de dialogue Format Cells : Faites un clic droit sur les cellules sélectionnées et choisissez "Format Cells", ou appuyez sur Ctrl+1.
<br>
<img src="1.png" width=60% />
1. Verrouiller les cellules : Dans la boîte de dialogue Format Cells, allez à l'onglet "Protection". Cochez la case "Verrouillé". Cliquez sur "OK."
1. Protéger la feuille : Allez dans l'onglet "Révision" du ruban. Cliquez sur "Protéger la feuille." Définissez un mot de passe (optionnel) et choisissez les permissions que vous souhaitez autoriser (par exemple, sélectionner des cellules verrouillées, formater des cellules, etc.). Cliquez sur "OK."
<br>
<img src="2.png" width=60% />

## **Comment verrouiller les cellules pour les protéger en utilisant Node.js**

Aspose.Cells est une bibliothèque puissante pour travailler avec des fichiers Excel de manière programmatique. Pour verrouiller des cellules avec Aspose.Cells for Node.js via C++, vous devez suivre ces étapes : charger [fichier d'exemple](sample.xlsx), déverrouiller toutes les cellules d'abord (car, par défaut, toutes les cellules sont verrouillées mais non appliquées jusqu'à ce que la feuille soit protégée), puis verrouiller les cellules spécifiques que vous souhaitez protéger, et enfin protéger la feuille pour appliquer le verrouillage.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-lock-cells-to-protect-them.js" >}}


## **Résultat de sortie**
Ce code garantit que seules les cellules spécifiées (A1 et B2 dans cet exemple) sont verrouillées, et la feuille est protégée pour faire respecter ces paramètres. Toutes les autres cellules de la feuille restent déverrouillées et modifiables.

<br>
<img src="3.png" width=60% />


{{< app/cells/assistant language="nodejs-cpp" >}}
