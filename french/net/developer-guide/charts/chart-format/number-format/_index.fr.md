---
title: Définir le code de format des valeurs de la série de graphiques
linktitle: Format de nombre
type: docs
weight: 100
url: /fr/net/set-the-values-format-code-of-chart-series/
---
## **Scénarios d'utilisation possibles**
Vous pouvez définir le code de format des valeurs des séries de graphiques à l'aide de la[Series.ValuesFormatCode](https://reference.aspose.com/cells/net/aspose.cells.charts/series/properties/valuesformatcode)propriété. Cette propriété n'est pas seulement utile pour la série basée sur la plage à l'intérieur de la feuille de calcul, mais fonctionne également bien pour la série créée avec un tableau de valeurs.
## **Définir le code de format des valeurs de la série de graphiques**
L'exemple de code suivant ajoute une série dans le graphique vide qui n'a pas de série avant. Il ajoute la série en utilisant le tableau de valeurs. Une fois, il ajoute la série, il la formate avec le code $#,##0 en utilisant le[Series.ValuesFormatCode](https://reference.aspose.com/cells/net/aspose.cells.charts/series/properties/valuesformatcode)propriété et le nombre 10 000 devient 10 000 $. La capture d'écran montre l'effet du code sur le[exemple de fichier Excel](51740712.xlsx) et[fichier Excel de sortie](51740713.xlsx) après exécution.

![tâche : image_autre_texte](set-the-values-format-code-of-chart-series_1.png)
## **Exemple de code**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SetValuesFormatCodeOfChartSeries.cs" >}}
