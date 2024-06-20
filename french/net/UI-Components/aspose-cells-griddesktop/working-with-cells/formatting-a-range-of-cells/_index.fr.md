---
title: Mise en forme d une plage de cellules
type: docs
weight: 60
url: /fr/net/aspose-cells-griddesktop/formatting-a-range-of-cells/
keywords: GridDesktop, format, style, cellules
description: Cet article présente comment appliquer un formatage de style sur les cellules dans GridDesktop.
---

{{% alert color="primary" %}} 

Ce sujet appartient également à la série de sujets liés à l'application des paramètres de police et autres styles de formatage sur les cellules. Nos derniers sujets ont bien couvert la manipulation de telles fonctionnalités. Par exemple, vous pouvez vous référer aux sujets [Changer la police et la couleur d'une cellule](/cells/fr/net/changing-the-font-and-color-of-a-cell/) et [Appliquer des styles sur les cellules](/cells/fr/net/applying-styles-on-cells/) pour en savoir plus sur les mêmes fonctionnalités. Alors, qu'est-ce qui est nouveau dans ce sujet si nous avons déjà abordé ces concepts. Eh bien, la seule différence de ce sujet avec les précédents est que nous appliquerons des paramètres de mise en forme (liés aux polices et autres styles) sur une plage de cellules plutôt que sur une seule cellule. Nous espérons que vous trouverez quand même ce sujet utile pour vous.

{{% /alert %}} 
## **Réglage de la police et du style d'une plage de cellules**
Avant de parler des paramètres de mise en forme (dont nous avons déjà beaucoup parlé dans nos sujets précédents), nous devrions savoir comment créer une plage de cellules. Eh bien, nous pouvons créer une plage de cellules en utilisant la classe **CellRange** dont le constructeur prend quelques paramètres pour spécifier la plage de cellules. Nous pouvons spécifier la plage de cellules en utilisant les **Noms** ou les **Indexes de lignes et de colonnes** des cellules de début et de fin.

Une fois que nous avons créé un objet **CellRange**, nous pouvons utiliser les versions surchargées des méthodes **SetStyle**, **SetFont** & **SetFontColor** de la feuille de calcul qui peuvent prendre un objet **CellRange** pour appliquer des paramètres de mise en forme sur la plage spécifiée de cellules.

Jetons un œil à un exemple pour comprendre ce concept de base.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-FormattingCellRange-1.cs" >}}
