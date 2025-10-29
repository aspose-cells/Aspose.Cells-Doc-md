---
title: Travailler avec l effet de brillance de la forme ou du graphique avec Golang via C++
linktitle: Travailler avec l effet de lueur de la forme ou du graphique
type: docs
weight: 240
url: /fr/go-cpp/working-with-the-glow-effect-of-shape-or-chart/
description: Découvrez comment travailler avec l effet de glow des formes ou des graphiques en utilisant Aspose.Cells for C++.
---

## **Scénarios d'utilisation possibles**
Aspose.Cells fournit la propriété [Shape.Glow](https://reference.aspose.com/cells/go-cpp/shapepropertycollection/getgloweffect/) ainsi que la classe [GlowEffect](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/gloweffect/) pour travailler avec l'effet de brillance de la forme ou du graphique. La classe [GlowEffect](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/gloweffect/) contient les propriétés suivantes qui peuvent être configurées pour obtenir différents résultats en fonction des besoins de l'application.

- [GlowEffect.Size](https://reference.aspose.com/cells/go-cpp/gloweffect/getsize/)
- [GlowEffect.Transparency](https://reference.aspose.com/cells/go-cpp/gloweffect/gettransparency/)
- [GlowEffect.Color](https://reference.aspose.com/cells/go-cpp/gloweffect/getcolor/)

## **Travailler avec l'effet de lueur de la forme ou du graphique**
Le code suivant charge le [fichier Excel source](5115407.xlsx) et accède à la première shape dans la première feuille de calcul, puis définit les sous-propriétés de la propriété [Shape.Glow](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapepropertycollection/getgloweffect/) avant d'enregistrer le classeur dans le [fichier Excel de sortie](5115414.xlsx).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkingWithTheGlowEffectOfShapeOrChart.go" >}}
