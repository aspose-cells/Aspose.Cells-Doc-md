---
title: Calcul de la formule matricielle des tableaux de données
type: docs
weight: 550
url: /fr/java/calculation-of-array-formula-of-data-tables/
---
{{% alert color="primary" %}} 

Vous pouvez créer un tableau de données dans Microsoft Excel à l'aide de Données> Analyse de simulation> Tableau de données.... Aspose.Cells vous permet désormais de calculer la formule matricielle du tableau de données. Veuillez utiliser[Workbook.calculateFormula()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula\(\)) comme d'habitude pour calculer tout type de formules.

{{% /alert %}} 
## **Calcul de la formule matricielle des tableaux de données**
 Dans l'exemple de code suivant, nous avons utilisé ce[fichier excel source](5472579.xlsx) qui est également montré dans l'image suivante.

![tâche : image_autre_texte](calculation-of-array-formula-of-data-tables_1.png)

 Si vous modifiez la valeur de la cellule B1 à 100, les valeurs de la table de données remplies de couleur jaune deviendront 120. L'exemple de code génère le[sortie PDF](5472577.pdf) qui affiche 120 comme valeurs dans le tableau de données, comme indiqué dans cette image.

![tâche : image_autre_texte](calculation-of-array-formula-of-data-tables_2.png)

 Voici l'exemple de code utilisé pour générer le[sortie PDF](5472577.pdf) du[fichier excel source](5472579.xlsx). Veuillez lire les commentaires pour plus d'informations.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CalculationOfArrayFormula-CalculationOfArrayFormula.java" >}}
