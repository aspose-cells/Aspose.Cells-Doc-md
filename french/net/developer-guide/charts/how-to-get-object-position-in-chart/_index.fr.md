---
title: Comment obtenir la position d’un objet dans un graphique
description: Apprenez comment obtenir la position des objets dans un graphique Excel en utilisant Aspose.Cells for .NET. 
keywords: Aspose.Cells for .NET, graphique Excel, obtenir la position des objets.
type: docs
weight: 74
url: /fr/net/how-to-get-object-position-in-chart/
---

## Scénarios d'utilisation possibles
Dans certains scénarios, lorsque vous utilisez un graphique Excel, vous pouvez avoir besoin d’obtenir la position des objets dans le graphique. Vous pouvez facilement réaliser cette opération avec Aspose.Cells.

## Exemple : obtenir la position d’un objet dans un graphique

Le code d'exemple suivant charge le [fichier Excel d'exemple](TestFile.xlsx) et génère le [fichier Excel de sortie](Output.xlsx).
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "get-object-position-in-chart.cs" >}}

Avec le code ci-dessus, vous pouvez obtenir la position du titre du graphique et de la zone de tracé. 
Avec les informations de position, les formes peuvent être placées à la position correspondante dans le graphique. 
Le résultat est montré dans l’image suivante, où une forme est placée dans le coin supérieur gauche de la zone de tracé et une autre forme est placée sous le titre du graphique.
![todo:image_alt_text](OutputResult.png)

## Explication et conversion d’unité

Il y a trois unités pour la position d’un objet dans un graphique :

1. Unités du ratio de la zone du graphique.

2. Unités de 1/4000 de la zone du graphique. C’est une unité utilisée dans les anciennes versions de fichiers Excel, et elle n’est pas recommandée.

3. Unités en pixel.

Le code de conversion d'entre eux est montré dans le code suivant : 

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "object-position-unit-in-chart.cs" >}}

{{< app/cells/assistant language="csharp" >}}
