---
title: Personnaliser les graphiques avec Golang via C++
linktitle: Personnalisation des graphiques
description: Apprenez comment personnaliser des graphiques dans Aspose.Cells for C++. Notre guide vous montrera comment modifier la mise en page du graphique, ajouter et formater des séries de données, ajuster les axes, et appliquer diverses options de mise en forme pour améliorer l apparence et la convivialité de vos graphiques.
keywords: Aspose.Cells for C++, graphiques, personnalisation, mises en page, séries de données, axes, mise en forme, apparence, convivialité.
type: docs
weight: 40
url: /fr/go-cpp/customizing-charts/
---


## **Création de graphiques personnalisés**

Jusqu'à présent, lorsque nous avons discuté de graphiques, nous avons examiné des graphiques standard avec leurs paramètres de mise en forme standards. Nous définissons simplement la source de données, réglons quelques propriétés, et le graphique est créé avec ses paramètres de format par défaut. Mais les API Aspose.Cells supportent également la création de graphiques personnalisés permettant aux développeurs de créer des graphiques avec leurs propres paramètres de format.

Les développeurs peuvent créer des graphiques personnalisés à l'exécution à l'aide d'Aspose.Cells.

Un graphique est composé d'une série de données. Chaque série de données dans Aspose.Cells est représentée par un objet [**Series**](https://reference.aspose.com/cells/go-cpp/series/) tandis que l'objet [**SeriesCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/seriescollection/) sert de collection d'objets [**Series**](https://reference.aspose.com/cells/go-cpp/series/). Lors de la création d'un graphique personnalisé, les développeurs ont la liberté d'utiliser différents types de graphiques pour différentes séries de données (collectées dans l'objet [**SeriesCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/seriescollection/)).

Le code d'exemple ci-dessous montre comment créer des graphiques personnalisés. Dans cet exemple, nous allons utiliser un graphique en colonnes pour la première série de données et un graphique linéaire pour la deuxième série. Le résultat est que nous ajoutons un graphique en colonnes, combiné à un graphique linéaire, à la feuille de calcul.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CustomizingCharts.go" >}}
{{% alert color="primary" %}}

Actuellement, Aspose.Cells ne supporte que les graphiques personnalisés combinant pie, line, column, et column stack, mais d'autres graphiques seront supportés dans les futures versions.

{{% /alert %}}
