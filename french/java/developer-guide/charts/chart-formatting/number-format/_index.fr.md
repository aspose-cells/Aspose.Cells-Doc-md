---
title: Définir le code de format de valeurs de la série de graphiques
description: Apprenez à définir le format des valeurs de série de graphique dans Aspose.Cells for Java. Notre guide vous aidera à comprendre comment formater les données de votre série de graphique à l aide du code de format approprié, vous permettant de présenter vos données de manière précise et professionnelle.
keywords: Aspose.Cells for Java, série de graphique, code de format des valeurs, formatage, présentation des données, précision, professionnalisme.
linktitle: Format numérique
type: docs
weight: 100
url: /fr/java/set-the-values-format-code-of-chart-series/
---

## **Scénarios d'utilisation possibles**
Vous pouvez définir le code de format des valeurs de la série de graphique en utilisant la méthode [Series.setValuesFormatCode](https://reference.aspose.com/cells/java/com.aspose.cells/series/#setValuesFormatCode-java.lang.String-). Cette méthode est non seulement utile pour la série basée sur la plage à l'intérieur de la feuille de calcul mais fonctionne également bien pour la série créée avec un tableau de valeurs.
## **Définir le code de format des valeurs de la série du graphique**
Le code d'exemple suivant ajoute une série dans le graphique vide qui n'a pas de série avant. Il ajoute la série à l'aide du tableau de valeurs. Une fois que la série est ajoutée, elle est formatée avec le code $#,##0 en utilisant la méthode [Series.setValuesFormatCode](https://reference.aspose.com/cells/java/com.aspose.cells/series/#setValuesFormatCode-java.lang.String-) et le nombre 10000 devient $10,000. La capture d'écran montre l'effet du code sur le [fichier Excel d'exemple](51740712.xlsx) et le [fichier Excel de sortie](51740713.xlsx) après l'exécution.

![todo:image_alt_text](set-the-values-format-code-of-chart-series_1.png)
## **Code d'exemple**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "SetValuesFormatCodeOfChartSeries.java" >}}
{{< app/cells/assistant language="java" >}}
