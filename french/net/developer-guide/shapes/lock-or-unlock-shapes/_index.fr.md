---
title: Verrouiller ou déverrouiller les formes
linktitle: Verrouiller ou déverrouiller les formes
type: docs
weight: 200
url: /fr/net/lock-or-unlock-shapes/
description: Cet article vous montre du code expliquant comment verrouiller ou déverrouiller des formes pour les protéger en utilisant la bibliothèque Aspose.Cells.
keywords: Verrouiller les formes pour les protéger, Comment verrouiller ou déverrouiller des formes en utilisant C#, Verrouiller ou déverrouiller des formes pour les protéger en C#.
---

## **Scénarios d'utilisation possibles**

Parfois, vous devez protéger toutes les formes dans certaines feuilles de calcul pour les empêcher d'être détruites par des situations non désirées. Dans ce cas, vous devez verrouiller toutes les formes dans la feuille de calcul spécifiée. 

La sécurisation des formes dans une feuille de calcul ou un document peut être bénéfique pour plusieurs raisons :
1. Prévenir les modifications accidentelles : Verrouiller les formes garantit qu'elles ne sont pas déplacées, redimensionnées ou supprimées par inadvertance par les utilisateurs. Cela est particulièrement important dans des documents complexes où les formes peuvent être utilisées pour des annotations, des illustrations ou comme partie de la conception du document.
1. Maintenir la mise en page et le design: Les formes jouent souvent un rôle crucial dans la mise en page et le design visuel d'un document. Les verrouiller permet de préserver l'apparence voulue, garantissant que le document reste professionnel et attrayant visuellement.
1. Intégrité des données: Dans les feuilles de calcul, les formes peuvent être utilisées pour mettre en évidence des points de données importants, ajouter des commentaires ou fournir des explications visuelles. En verrouillant ces formes, on s'assure que les informations contextuelles qu'elles fournissent restent exactes et intactes.
1. Cohérence dans les documents partagés: Lors de la collaboration sur des documents, les différents utilisateurs peuvent avoir des niveaux d'expertise variables. Verrouiller les formes aide à maintenir la cohérence dans le document en évitant les altérations non intentionnelles.
1. Sécurité: Dans des documents sensibles, verrouiller les formes peut faire partie d'une stratégie plus large visant à protéger les informations. Par exemple, dans des rapports financiers ou des documents juridiques, les formes verrouillées peuvent être utilisées pour protéger des annotations spécifiques ou des points saillants qui fournissent un contexte critique.

Parfois, il peut être nécessaire de pouvoir modifier certaines formes dans certaines feuilles de calcul protégées, auquel cas, vous devez déverrouiller ces formes. Cet article expliquera en détail comment verrouiller et déverrouiller des formes spécifiées.

## **Comment verrouiller les formes pour les protéger dans Excel**

Voici comment vous pouvez verrouiller des cellules dans Microsoft Excel:

1. Ouvrez votre fichier Excel: Ouvrez le fichier Excel contenant les formes que vous souhaitez verrouiller.

1. Sélectionnez la forme: Cliquez sur la forme que vous souhaitez verrouiller. Vous pouvez également sélectionner plusieurs formes en maintenant la touche Ctrl enfoncée et en cliquant sur chaque forme.

1. Ouvrez le volet de mise en forme de la forme: Cliquez avec le bouton droit sur la(es) forme(s) sélectionnée(s) et choisissez "Taille et propriétés". Sinon, vous pouvez aller à l'onglet "Format" dans le Ruban, puis dans le groupe "Taille", cliquez sur le lanceur de boîte de dialogue (une petite flèche) pour ouvrir le volet "Format de la forme".
1. Verrouillez la forme: Dans le volet "Format de la forme", allez à l'onglet "Taille et propriétés" (l'icône ressemble à un carré avec des flèches). Sous la section "Propriétés", cochez la case "Verrouillé".
<br>
<img src="1.png" width=60% />
1. Protégez la feuille de calcul : Allez à l'onglet "Révision" dans le Ruban. Cliquez sur "Protéger la feuille". Définissez un mot de passe (facultatif) et choisissez les autorisations que vous souhaitez accorder (par exemple, sélectionner les cellules verrouillées, formater les cellules, etc.). Cliquez sur "OK".
<br>
<img src="2.png" width=60% />

## **Comment verrouiller toutes les formes dans une feuille de calcul spécifiée**

Pour protéger toutes les formes dans une feuille de calcul spécifiée, utilisez la méthode [Worksheet.Protect( ProtectionType.Objects)](https://reference.aspose.com/cells/net/aspose.cells/worksheet/protect/#protect), comme indiqué dans le code d'exemple suivant.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Lock-Or-Unlock-Shapes-1.cs" >}}

## **Comment déverrouiller des formes spécifiées dans une feuille de calcul protégée**

Pour déverrouiller une forme spécifiée dans une feuille de calcul protégée, utilisez [shape.IsLocked](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/islocked/), comme indiqué dans le code d'exemple suivant.

Remarque : [shape.IsLocked](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/islocked/) n'a de sens que lorsque la feuille de calcul est protégée.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Lock-Or-Unlock-Shapes-2.cs" >}}

