---
title: Définir le code de format de valeurs de la série de graphiques
description: Apprenez à définir le code de format des valeurs des séries de graphiques dans Aspose.Cells pour Python via .NET. Notre guide vous aidera à formater les données de vos séries de graphiques en utilisant le code de format approprié, ce qui vous permet de présenter vos données précisément et professionnellement.
keywords: Aspose.Cells pour Python via .NET, séries de graphiques, code de format des valeurs, mise en forme, présentation des données, précision, professionnalisme.
linktitle: Format numérique
type: docs
weight: 100
url: /fr/python-net/set-the-values-format-code-of-chart-series/
---

## **Scénarios d'utilisation possibles**
Vous pouvez définir le code de format des valeurs de la série de graphique en utilisant la propriété [Series.values_format_code](https://reference.aspose.com/cells/python-net/aspose.cells.charts/series/values_format_code). Cette propriété est utile non seulement pour la série basée sur la plage dans la feuille de calcul, mais aussi pour celles créées avec un tableau de valeurs.

## **Définir le code de format des valeurs de la série du graphique**
Le code d'exemple suivant ajoute une série dans un graphique vide qui n'avait pas de série auparavant. Il ajoute la série en utilisant un tableau de valeurs. Une fois la série ajoutée, elle est formatée avec le code $#,##0 utilisant la propriété [Series.values_format_code](https://reference.aspose.com/cells/python-net/aspose.cells.charts/series/values_format_code) et le nombre 10 000 devient $10,000. La capture d'écran montre l'effet du code sur le [fichier Excel d'exemple](51740712.xlsx) et le [fichier Excel de sortie](51740713.xlsx) après exécution.

![todo:image_alt_text](set-the-values-format-code-of-chart-series_1.png)

## **Code d'exemple**
{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-SetValuesFormatCodeOfChartSeries.py" >}}
