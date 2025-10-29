---
title: Configurer le code de format des valeurs de la série du graphique avec Golang via C++
linktitle: Format numérique
type: docs
weight: 100
url: /fr/go-cpp/set-the-values-format-code-of-chart-series/
description: Apprenez à définir le code du format des valeurs de la série de graphique dans Aspose.Cells for C++. Notre guide vous aidera à comprendre comment formater les données de votre série de graphique en utilisant le code de format approprié, pour présenter vos données de manière précise et professionnelle.
keywords: Aspose.Cells for C++, série de graphique, code de format des valeurs, mise en forme, présentation des données, précision, professionnalisme.
---

## **Scénarios d'utilisation possibles**
Vous pouvez définir le code de format des valeurs de la série du graphique en utilisant la propriété [Series.GetValuesFormatCode()](https://reference.aspose.com/cells/go-cpp/series/getvaluesformatcode/). Cette propriété est utile non seulement pour les séries basées sur la plage dans la feuille de calcul, mais aussi pour celles créées avec un tableau de valeurs.

## **Définir le code de format des valeurs de la série du graphique**
Le code d'échantillon suivant ajoute une série dans le graphique vide qui n'avait aucune série auparavant. Il ajoute la série en utilisant le tableau de valeurs. Une fois la série ajoutée, il la formate avec le code `$#,##0` en utilisant la propriété [Series.GetValuesFormatCode()](https://reference.aspose.com/cells/go-cpp/series/getvaluesformatcode/) et le nombre `10000` devient `$10,000`. La capture d'écran montre l'effet du code sur le [fichier Excel d'échantillon](51740712.xlsx) et le [fichier Excel de sortie](51740713.xlsx) après exécution.

![todo:image_alt_text](set-the-values-format-code-of-chart-series_1.png)

## **Code d'exemple**
{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-NumberFormat.go" >}}
