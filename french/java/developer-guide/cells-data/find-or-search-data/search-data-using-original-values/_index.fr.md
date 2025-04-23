---
title: Rechercher des données en utilisant les valeurs d origine
type: docs
weight: 540
url: /fr/java/search-data-using-original-values/
---

{{% alert color="primary" %}} 

Parfois, la valeur des données est masquée car elle est formatée d'une certaine manière. Par exemple, supposons que la cellule D4 a la formule =Sum(A1:A2) et que sa valeur est 20 mais qu'elle est formatée comme ---, alors la valeur 20 est masquée et ne peut pas être trouvée via les options de recherche de Microsoft Excel. Cependant, vous pouvez la trouver en utilisant Aspose.Cells avec [LookInType.ORIGINAL_VALUES](https://reference.aspose.com/cells/java/com.aspose.cells/lookintype#ORIGINAL-VALUES)

{{% /alert %}} 
## **Rechercher des données en utilisant des valeurs originales**
Le code exemple ci-dessous illustre le point précédent. Il trouve la cellule D4 qui ne peut pas être trouvée avec les options de recherche de Microsoft Excel mais que Aspose.Cells peut localiser en utilisant [LookInType.ORIGINAL_VALUES](https://reference.aspose.com/cells/java/com.aspose.cells/lookintype#ORIGINAL-VALUES). Veuillez lire les commentaires dans le code pour plus d'informations.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SearchDataUsingOriginalValues-SearchDataUsingOriginalValues.java" >}}
## **Sortie console**
Voici la sortie de la console du code d'exemple ci-dessus.

{{< highlight java >}}

 Aspose.Cells.Cell [ D4; ValueType : IsNumeric; Value : ---; Formula:=SUM(A1:A2)]

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
