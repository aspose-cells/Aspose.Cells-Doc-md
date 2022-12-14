---
title: Définir le code de format des valeurs de la série de graphiques
type: docs
weight: 60
url: /fr/java/set-the-values-format-code-of-chart-series/
---
## **Scénarios d'utilisation possibles**

Vous pouvez définir le code de format des valeurs des séries de graphiques à l'aide de la[**Series.ValuesFormatCode**](https://reference.aspose.com/cells/java/com.aspose.cells/series#ValuesFormatCode)propriété. Cette propriété n'est pas seulement utile pour les séries basées sur la plage à l'intérieur de la feuille de calcul, mais fonctionne également bien pour les séries créées avec un tableau de valeurs.

## **Définir le code de format des valeurs de la série de graphiques**

L'exemple de code suivant ajoute une série dans le graphique vide qui n'a pas de série avant. Il ajoute la série en utilisant le tableau de valeurs. Une fois, il ajoute la série, il la formate avec le code $#,##0 en utilisant le[**Series.ValuesFormatCode**](https://reference.aspose.com/cells/java/com.aspose.cells/series#ValuesFormatCode)propriété et le nombre 10 000 devient 10 000 $. La capture d'écran montre l'effet du code sur le[exemple de fichier Excel](51740736.xlsx)et[fichier Excel de sortie](51740735.xlsx)après exécution.

![tâche : image_autre_texte](set-the-values-format-code-of-chart-series_1.png)

## **Exemple de code**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Charts-SetValuesFormatCodeOfChartSeries.java" >}}
