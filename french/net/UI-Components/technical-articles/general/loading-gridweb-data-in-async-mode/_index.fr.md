---
title: Chargement des données de GridWeb en mode asynchrone
type: docs
weight: 40
url: /fr/net/aspose-cells-gridweb/loading-data-in-async-mode/
description: Cet article décrit comment utiliser le mode asynchrone pour obtenir de meilleures performances dans GridWeb.
keywords: GridWeb, performance, asynchrone, mode asynchrone
---

{{% alert color="primary" %}} 

Lors de la création d'un classeur avec de grands ensembles de données, ou de la lecture d'un gros fichier Microsoft Excel, cela prendra sûrement plus de temps et de ressources pour le faire. La mémoire totale que le processus prendra est toujours une préoccupation. Il existe des mesures qui peuvent être adoptées pour faire face à ce défi. Aspose.Cells.GridWeb propose certaines options et API pertinentes pour réduire et optimiser l'utilisation de la mémoire. De plus, cela peut aider le processus à fonctionner de manière plus efficace et à s'exécuter plus rapidement. Pour une feuille de travail contenant de grandes données de cellules, vous pouvez charger le jeu de données de manière asynchrone, ce qui peut améliorer les performances globales pour l'expérience de l'utilisateur.

{{% /alert %}} 

Utilisez l'option GridWeb.EnableAsync pour optimiser la mémoire et les performances pour les données de cellules. Lors de la construction d'un grand jeu de données pour les cellules. Lorsque vous définissez l'option sur vrai, le chargement des données se fera en fonction de la seule zone Windows visible actuelle. En bref, lorsque vous faites défiler les données de cellules de la feuille de calcul dans GridWeb, il chargera de nouvelles données Windows en fonction de la position de défilement actuelle uniquement.

L'exemple suivant montre comment activer le mode asynchrone de GridWeb.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Articles-EnableAsyncMode.aspx-EnableAsync.cs" >}}
