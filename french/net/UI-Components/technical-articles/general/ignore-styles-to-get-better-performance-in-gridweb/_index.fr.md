---
title: Ignorer les styles pour obtenir de meilleures performances dans GridWeb
type: docs
weight: 1060
url: /fr/net/aspose-cells-gridweb/ignorestylewithnodata
description: Cet article décrit comment utiliser IgnoreStyleWithNoData pour obtenir de meilleures performances dans GridWeb.
keywords: GridWeb,performance
---

## **Scénarios d'utilisation possibles**
Veuillez utiliser la propriété [GridWeb.IgnoreStyleWithNoData](https://reference.aspose.com/cells/net/aspose.cells.gridweb/mainweb/ignorestylewithnodata) pour charger moins de lignes/colonnes requises à partir du classeur.

## **Obtenez de meilleures performances lors du chargement du classeur**
Veuillez consulter le [fichier Excel d'exemple](largerowswithstyle.xlsx) 

Lorsque IgnoreStyleWithNoData est défini sur true;

Comme vous pouvez le constater, il affiche les lignes (jusqu'à 15) et les colonnes (jusqu'à L), il n'affichera pas les dernières lignes et colonnes sans données dans les cellules. Ainsi, le temps de chargement sera réduit.

![classeur avec style ignoré](ignorestyletrue.png)


Lorsque IgnoreStyleWithNoData est défini sur false; (la valeur par défaut est false)

Comme vous pouvez le constater, il affiche beaucoup plus de lignes (jusqu'à 500) et de colonnes (jusqu'à CZ)

De la ligne 16 à la ligne 500, certaines cellules ont un style de bordure, cependant les cellules ne contiennent aucune donnée.

De la colonne M à la colonne CZ, certaines cellules ont un style de bordure, cependant les cellules ne contiennent aucune donnée.

![classeur sans style ignoré](ignorestylefalse.png)



