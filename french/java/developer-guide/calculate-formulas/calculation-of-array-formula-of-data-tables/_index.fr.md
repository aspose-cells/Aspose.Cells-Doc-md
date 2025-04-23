---
title: Calcul de la formule de tableau de données
type: docs
weight: 550
url: /fr/java/calculation-of-array-formula-of-data-tables/
---

{{% alert color="primary" %}} 

Vous pouvez créer un tableau de données dans Microsoft Excel en utilisant Données > Analyse de scénario > Tableau de données.... Aspose.Cells vous permet désormais de calculer la formule matricielle du tableau de données. Veuillez utiliser [Workbook.calculateFormula()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula--) comme d'habitude pour calculer tout type de formules.

{{% /alert %}} 
## **Calcul de la formule de tableau de données**
Dans le code d'exemple suivant, nous avons utilisé ce [fichier Excel source](5472579.xlsx) qui est également affiché dans l'image suivante.

![todo:image_alt_text](calculation-of-array-formula-of-data-tables_1.png)

Si vous changez la valeur de la cellule B1 à 100, les valeurs du tableau de données qui sont remplies en jaune deviendront 120. Le code d'exemple génère le [PDF de sortie](5472577.pdf) qui montre 120 comme valeurs dans le tableau de données comme indiqué dans cette image.

![todo:image_alt_text](calculation-of-array-formula-of-data-tables_2.png)

Voici le code d'exemple utilisé pour générer le [PDF de sortie](5472577.pdf) à partir du [fichier Excel source](5472579.xlsx). Veuillez lire les commentaires pour plus d'informations.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CalculationOfArrayFormula-CalculationOfArrayFormula.java" >}}
{{< app/cells/assistant language="java" >}}
