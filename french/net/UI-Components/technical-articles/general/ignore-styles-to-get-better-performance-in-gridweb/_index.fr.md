---
title: Ignorer les styles pour obtenir de meilleures performances dans GridWeb
type: docs
weight: 1060
url: /fr/net/aspose-cells-gridweb/ignorestylewithnodata
description: Cet article décrit comment utiliser IgnoreStyleWithNoData pour obtenir de meilleures performances pour la bibliothèque Aspose.Cells.GridWeb.
keywords: performance
---
## **Scénarios d'utilisation possibles**
 Veuillez utiliser[GridWeb.IgnoreStyleWithNoDataGridWeb.IgnoreStyleWithNoData](https://reference.aspose.com/cells/net/aspose.cells.gridweb/mainweb/ignorestylewithnodata)propriété pour charger moins de lignes/colonnes requises à partir du classeur.
 
## **Obtenez de meilleures performances lors du chargement du classeur**
 S'il vous plaît, vérifiez le[exemple de fichier excel](largerowswithstyle.xlsx) 

Lorsqu'il est défini IgnoreStyleWithNoData = true ;

Comme vous pouvez le voir, il affiche les lignes (jusqu'à 15) et les colonnes (jusqu'à L), il n'affichera pas les dernières lignes et colonnes continues sans données dans les cellules. Ainsi, le temps de chargement sera moindre.

![classeur avec style ignoré](ignorestyletrue.png)


Lorsqu'il est défini IgnoreStyleWithNoData = false ; (la valeur par défaut est false)

Comme vous pouvez le voir, il affiche beaucoup plus de lignes (jusqu'à 500) et de colonnes (jusqu'à CZ)

De la ligne 16 à la ligne 500, certaines des cellules ont défini le style de bordure, mais les cellules ne contiennent aucune donnée.

De la colonne M à la colonne CZ, certaines des cellules ont défini le style de bordure, mais les cellules ne contiennent aucune donnée.

![classeur sans style ignorer](ignorestylefalse.png)
 
 
 