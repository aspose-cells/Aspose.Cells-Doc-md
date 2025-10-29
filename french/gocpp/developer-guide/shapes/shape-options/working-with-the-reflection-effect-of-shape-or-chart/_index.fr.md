---
title: Travailler avec l effet de réflexion de la forme ou du graphique avec Golang via C++
linktitle: Travailler avec l effet de réflexion de la forme ou du graphique
type: docs
weight: 210
url: /fr/go-cpp/working-with-the-reflection-effect-of-shape-or-chart/
description: Apprenez comment travailler avec l effet de réflexion des formes ou des graphiques en utilisant Aspose.Cells avec Golang via C++.
---

## **Scénarios d'utilisation possibles**
Aspose.Cells fournit la propriété [Shape.Reflection](https://reference.aspose.com/cells/go-cpp/shape/getreflection/) ainsi que la classe [ReflectionEffect](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/reflectioneffect/) pour travailler avec l'effet de réflexion de la forme ou du graphique. La classe [ReflectionEffect](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/reflectioneffect/) contient les propriétés suivantes qui peuvent être configurées pour obtenir différents résultats en fonction des besoins de l'application.

- [Flou](https://reference.aspose.com/cells/go-cpp/reflectioneffect/getblur/)
- [Direction](https://reference.aspose.com/cells/go-cpp/reflectioneffect/getdirection/)
- [Distance](https://reference.aspose.com/cells/go-cpp/reflectioneffect/getdistance/)
- [DirectionDeFondu](https://reference.aspose.com/cells/go-cpp/reflectioneffect/getfadedirection/)
- [RotationAvecForme](https://reference.aspose.com/cells/go-cpp/reflectioneffect/getrotwithshape/)
- [Taille](https://reference.aspose.com/cells/go-cpp/reflectioneffect/getsize/)
- [Transparence](https://reference.aspose.com/cells/go-cpp/reflectioneffect/gettransparency/)
- [Type](https://reference.aspose.com/cells/go-cpp/reflectioneffect/gettype/)

## **Travailler avec l'effet de réflexion de la forme ou du graphique**
 Le code suivant charge le [fichier Excel source](5115424.xlsx) et accède à la première forme dans la feuille de travail par défaut, puis définit différentes propriétés de la classe [Shape.Reflection](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getreflection/) avant d'enregistrer le classeur dans le [fichier Excel de sortie](5115423.xlsx).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkingWithTheReflectionEffectOfShapeOrChart.go" >}}
