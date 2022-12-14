---
title: Chargement des données GridWeb en mode asynchrone
type: docs
weight: 40
url: /fr/net/loading-gridweb-data-in-async-mode/
---
{{% alert color="primary" %}} 

Lors de la création d'un classeur avec de grands ensembles de données ou de la lecture d'un gros fichier Excel Microsoft, cela prendra sûrement plus de temps et de ressources pour le faire. La mémoire totale que le processus prendra est toujours une préoccupation. Il existe des mesures qui peuvent être adoptées pour relever le défi. Aspose.Cells.GridWeb fournit des options et des API pertinentes pour réduire, réduire et optimiser l'utilisation de la mémoire. En outre, cela peut aider le processus à fonctionner plus efficacement et plus rapidement. Pour une feuille de calcul contenant des données de grandes cellules, vous pouvez charger le jeu de données de manière asynchrone, ce qui peut améliorer les performances globales pour l'expérience de l'utilisateur.

{{% /alert %}} 

Utilisez l'option GridWeb.EnableAsync pour optimiser la mémoire et les performances des données des cellules. Lors de la création d'un grand ensemble de données pour les cellules. Lorsque vous définissez l'option sur true, le chargement des données sera basé uniquement sur la zone Windows actuellement visible. En bref, lorsque vous faites défiler les données des cellules de la feuille de calcul dans GridWeb, il chargera de nouvelles données Windows en fonction de la position de défilement actuelle uniquement.

L'exemple suivant montre comment activer le mode asynchrone de GridWeb.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Articles-EnableAsyncMode.aspx-EnableAsync.cs" >}}
