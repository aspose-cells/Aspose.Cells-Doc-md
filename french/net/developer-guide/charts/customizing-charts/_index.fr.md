---
title: Personnalisation des graphiques
description: Apprenez à personnaliser les graphiques dans Aspose.Cells for .NET. Notre guide vous montrera comment modifier les agencements de graphique, ajouter et formater des séries de données, ajuster les axes et appliquer diverses options de formatage pour améliorer l apparence et l utilité de vos graphiques.
keywords: Aspose.Cells for .NET, création de graphiques, personnalisation, agencements, séries de données, axes, mise en forme, apparence, utilité.
type: docs
weight: 40
url: /fr/net/customizing-charts/
---

{{% alert color="primary" %}}

## **Création de graphiques personnalisés**

Jusqu'à présent, lorsque nous avons discuté des graphiques, nous avons examiné des graphiques standard qui ont leurs paramètres de formatage standard. Nous définissons uniquement la source de données, définissons quelques propriétés, et le graphique est créé avec ses paramètres de formatage par défaut. Mais les API Aspose.Cells prennent également en charge la création de graphiques personnalisés qui permet aux développeurs de créer des graphiques avec leurs propres paramètres de format.

Les développeurs peuvent créer des graphiques personnalisés à l'exécution à l'aide d'Aspose.Cells.

Un graphique est composé d'une série de données. Chaque série de données dans Aspose.Cells est représentée par un objet [**Series**](https://reference.aspose.com/cells/net/aspose.cells.charts/series) tandis que l'objet [**SeriesCollection**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection) sert de collection d'objets [**Series**](https://reference.aspose.com/cells/net/aspose.cells.charts/series). Lors de la création d'un graphique personnalisé, les développeurs ont la liberté d'utiliser différents types de graphiques pour différentes séries de données (collectées dans l'objet [**SeriesCollection**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection)).

Le code d'exemple ci-dessous montre comment créer des graphiques personnalisés. Dans cet exemple, nous allons utiliser un graphique en colonnes pour la première série de données et un graphique linéaire pour la deuxième série. Le résultat est que nous ajoutons un graphique en colonnes, combiné à un graphique linéaire, à la feuille de calcul.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-HowToCreateCustomChart-1.cs" >}}

{{% alert color="primary" %}}

Actuellement, Aspose.Cells ne prend en charge que les graphiques personnalisés combinant des graphiques circulaires, linéaires, en colonnes et empilés mais d'autres graphiques seront pris en charge dans les versions futures.

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
