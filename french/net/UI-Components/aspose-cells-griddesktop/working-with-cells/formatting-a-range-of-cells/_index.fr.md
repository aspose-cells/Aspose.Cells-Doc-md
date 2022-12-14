---
title: Formatage d'une plage de Cells
type: docs
weight: 60
url: /fr/net/formatting-a-range-of-cells/
---
{{% alert color="primary" %}} 

Cette rubrique appartient également à la série de rubriques liées à l'application des paramètres de police et d'autres styles de mise en forme sur les cellules. Nos derniers sujets ont bien couvert la gestion de ces fonctionnalités. Par exemple, vous pouvez vous référer à[Modification de la police et de la couleur d'un Cell](/cells/fr/net/changing-the-font-and-color-of-a-cell/) et[Application de styles sur Cells](/cells/fr/net/applying-styles-on-cells/) rubriques pour en savoir plus sur les mêmes fonctionnalités. Alors quoi de neuf dans ce sujet si nous avons déjà abordé ces notions. Eh bien, la seule différence de ce sujet avec les précédents est que nous appliquerons les paramètres de mise en forme (liés aux polices et autres styles) sur une plage de cellules au lieu d'une seule cellule. Nous espérons que vous trouverez toujours ce sujet utile pour vous.

{{% /alert %}} 
## **Définition de la police et du style d'une plage de Cells**
 Avant de parler des paramètres de mise en forme (dont nous avons déjà beaucoup parlé dans nos rubriques précédentes), nous devons savoir comment créer une plage de cellules. Eh bien, nous pouvons créer une plage de cellules en utilisant**CellRange** classe dont le constructeur prend certains paramètres pour spécifier la plage de cellules. Nous pouvons spécifier la plage de cellules en utilisant le**Des noms** ou**Indices de lignes et de colonnes** de cellules de début et de fin.

 Une fois que nous avons créé un**CellRange** objet alors nous pouvons utiliser les versions surchargées de**DéfinirStyle**, **Définir la police** & **Définir la couleur de la police** méthodes de feuille de travail qui peuvent prendre un**CellRange** objet pour appliquer les paramètres de mise en forme sur la plage de cellules spécifiée.

Voyons un exemple pour comprendre ce concept de base.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-FormattingCellRange-1.cs" >}}
