---
title: Définir le code de format de valeurs de la série de graphiques
description: Apprenez comment définir le code de format de valeurs de la série de graphiques dans Aspose.Cells for .NET. Notre guide vous aidera à comprendre comment formater les données de votre série de graphiques en utilisant le code de format approprié, vous permettant de présenter vos données de manière précise et professionnelle.
keywords: Aspose.Cells for .NET, série de graphiques, code de format des valeurs, formatage, présentation des données, précision, professionnalisme.
linktitle: Format numérique
type: docs
weight: 100
url: /fr/net/set-the-values-format-code-of-chart-series/
---

## **Scénarios d'utilisation possibles**
Vous pouvez définir le code de format des valeurs de la série de graphiques en utilisant la propriété [Series.ValuesFormatCode](https://reference.aspose.com/cells/net/aspose.cells.charts/series/properties/valuesformatcode). Cette propriété est utile non seulement pour la série basée sur la plage à l'intérieur de la feuille de calcul, mais fonctionne également bien pour la série créée avec un tableau de valeurs.
## **Définir le code de format des valeurs de la série du graphique**
Le code d'exemple suivant ajoute une série dans le graphique vide qui n'a pas de série auparavant. Il ajoute la série en utilisant un tableau de valeurs. Une fois la série ajoutée, elle est formatée avec le code $#,##0 à l'aide de la propriété [Series.ValuesFormatCode](https://reference.aspose.com/cells/net/aspose.cells.charts/series/properties/valuesformatcode) et le numéro 10000 devient $10,000. La capture d'écran montre l'effet du code sur le [fichier Excel d'exemple](51740712.xlsx) et sur le [fichier Excel de sortie](51740713.xlsx) après l'exécution.

![todo:image_alt_text](set-the-values-format-code-of-chart-series_1.png)
## **Code d'exemple**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SetValuesFormatCodeOfChartSeries.cs" >}}
