---
title: Personnalisation des graphiques
description: Apprenez à personnaliser les graphiques dans Aspose.Cells pour Python via .NET. Notre guide vous montrera comment modifier la disposition du graphique, ajouter et formater les séries de données, ajuster les axes et appliquer diverses options de formatage pour améliorer l apparence et la convivialité de vos graphiques.
keywords: Aspose.Cells pour Python via .NET, création de graphiques, personnalisation, dispositions, séries de données, axes, formatage, apparence, convivialité.
type: docs
weight: 40
url: /fr/python-net/customizing-charts/
---


## **Création de graphiques personnalisés**

Jusqu'à présent, lorsque nous avons parlé de graphiques, nous avons examiné des graphiques standard avec leurs réglages de formatage par défaut. Nous ne définissons que la source de données, configurons quelques propriétés, et le graphique est créé avec ses paramètres par défaut. Mais l'API Aspose.Cells pour Python via .NET prend également en charge la création de graphiques personnalisés permettant aux développeurs de créer des graphiques avec leurs propres paramètres de format.

Les développeurs peuvent créer des graphiques personnalisés à l'exécution en utilisant Aspose.Cells pour Python via .NET.

Un graphique est composé d'une série de données. Chaque série de données dans Aspose.Cells pour Python via .NET est représentée par un objet [**Series**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/series) tandis que l'objet [**SeriesCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/seriescollection) sert de collection d'objets [**Series**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/series). Lors de la création d'un graphique personnalisé, les développeurs ont la liberté d'utiliser différents types de graphiques pour différentes séries de données (collectées dans l'objet [**SeriesCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/seriescollection)).

Le code d'exemple ci-dessous montre comment créer des graphiques personnalisés. Dans cet exemple, nous allons utiliser un graphique en colonnes pour la première série de données et un graphique linéaire pour la deuxième série. Le résultat est que nous ajoutons un graphique en colonnes, combiné à un graphique linéaire, à la feuille de calcul.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ManipulateChart-HowToCreateCustomChart-1.py" >}}

{{% alert color="primary" %}}

Actuellement, Aspose.Cells pour Python via .NET ne supporte que la combinaison de graphiques en secteurs, en lignes, en colonnes et en empilement de colonnes, mais d'autres graphiques seront pris en charge dans de futures versions.

{{% /alert %}}
{{< app/cells/assistant language="python-net" >}}
