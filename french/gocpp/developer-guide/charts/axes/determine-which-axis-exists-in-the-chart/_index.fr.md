---
title: Déterminer quelle(s) origine(s) de l axe existe(nt) dans le graphique avec Golang via C++
description: Apprenez comment déterminer quels axes existent dans un graphique créé avec Aspose.Cells for C++. Notre guide vous aidera à comprendre comment identifier et accéder aux différents axes dans un graphique, y compris les axes de catégorie, de valeur et secondaires.
keywords: Aspose.Cells for C++, graphique, axe, existence, catégorie, valeur, secondaire.
type: docs
weight: 140
url: /fr/go-cpp/determine-which-axis-exists-in-the-chart/
---

{{% alert color="primary" %}}

Parfois, l'utilisateur a besoin de savoir si un axe particulier existe dans le graphique. Par exemple, il veut savoir si un axe de valeurs secondaires existe à l'intérieur du graphique ou non. Certains graphiques comme Camembert, CamembertExploded, CamembertCamembert, CamembertBarre, Camembert3D, Camembert3DExploded, Anneau, AnneauExploded, etc. n'ont pas d'axe.

Aspose.Cells fournit [**Chart.HasAxis(AxisType axisType, bool isPrimary)**](https://reference.aspose.com/cells/go-cpp/chart/hasaxis/) méthode pour déterminer si le graphique a un axe particulier ou non.

{{% /alert %}}

Le code d'exemple suivant montre comment utiliser [**Chart.HasAxis(AxisType axisType, bool isPrimary)**](https://reference.aspose.com/cells/go-cpp/chart/hasaxis/) pour déterminer si le graphique d'exemple possède un axe de catégorie et de valeur principal et secondaire.

## Code C++ pour déterminer quels axes existent dans le graphique

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DetermineWhichAxisExistsInTheChart.go" >}}
## Sortie console générée par le code d'exemple

La sortie de la console du code est affichée ci-dessous, affichant true pour la Catégorie Principale et Axe de Valeur, et false pour la Catégorie Secondaire et Axe de Valeur.

{{< highlight java >}}

Has Primary Category Axis: True

Has Secondary Category Axis: False

Has Primary Value Axis: True

Has Secondary Value Axis: False

{{< /highlight >}}
