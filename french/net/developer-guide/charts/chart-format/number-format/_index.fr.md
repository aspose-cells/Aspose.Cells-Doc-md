---
title: Définir le code de format des valeurs de la série de graphiques
description: Découvrez comment définir le code de format des valeurs de la série de graphiques dans Aspose.Cells for .NET. Notre guide vous aidera à comprendre comment formater les données de votre série de graphiques en utilisant le code de format approprié, vous permettant de présenter vos données avec précision et de manière professionnelle.
keywords: Aspose.Cells for .NET, chart series, values format code, formatting, data presentation, accuracy, professionalism.
linktitle: Format de nombre
type: docs
weight: 100
url: /fr/net/set-the-values-format-code-of-chart-series/
---
##  **Scénarios d'utilisation possibles**
Vous pouvez définir le code de format des valeurs des séries de graphiques à l'aide de l'option[Série.ValuesFormatCode](https://reference.aspose.com/cells/net/aspose.cells.charts/series/properties/valuesformatcode)propriété. Cette propriété est non seulement utile pour les séries basées sur la plage contenue dans la feuille de calcul, mais fonctionne également bien pour les séries créées avec un tableau de valeurs.
##  **Définir le code de format des valeurs de la série de graphiques**
 L’exemple de code suivant ajoute une série dans le graphique vide qui n’a aucune série auparavant. Il ajoute la série en utilisant le tableau de valeurs. Une fois qu'il ajoute la série, il la formate avec le code $#,##0 en utilisant le[Série.ValuesFormatCode](https://reference.aspose.com/cells/net/aspose.cells.charts/series/properties/valuesformatcode)propriété et le nombre 10 000 devient 10 000 $. La capture d'écran montre l'effet du code sur le[exemple de fichier Excel](51740712.xlsx) et[sortie du fichier Excel](51740713.xlsx) après l'exécution.

![tâche : image_alt_text](set-the-values-format-code-of-chart-series_1.png)
##  **Exemple de code**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SetValuesFormatCodeOfChartSeries.cs" >}}
