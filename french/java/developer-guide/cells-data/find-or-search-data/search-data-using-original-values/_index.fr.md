---
title: Rechercher des données en utilisant les valeurs d origine
type: docs
weight: 540
url: /fr/java/search-data-using-original-values/
---

{{% alert color="primary" %}} 

Parfois, la valeur des données est cachée parce qu'elle est formatée de quelque manière. Par exemple, supposons que la cellule D4 ait la formule =Sum(A1:A2) et que sa valeur soit 20 mais qu'elle soit formatée comme ---, alors la valeur 20 est cachée et ne peut pas être trouvée en utilisant les options de recherche de Microsoft Excel. Cependant, vous pouvez la trouver en utilisant Aspose.Cells en utilisant [LookInType.ORIGINAL_VALUES](https://reference.aspose.com/cells/java/com.aspose.cells/lookintype#ORIGINAL_VALUES)

{{% /alert %}} 
## **Rechercher des données en utilisant des valeurs originales**
Le code d'exemple suivant illustre le point ci-dessus. Il trouve la cellule D4 qui ne peut pas être trouvée en utilisant les options de recherche de Microsoft Excel mais Aspose.Cells peut la trouver en utilisant [LookInType.ORIGINAL_VALUES](https://reference.aspose.com/cells/java/com.aspose.cells/lookintype#ORIGINAL_VALUES). Veuillez lire les commentaires à l'intérieur du code pour plus d'informations.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SearchDataUsingOriginalValues-SearchDataUsingOriginalValues.java" >}}
## **Sortie console**
Voici la sortie de la console du code d'exemple ci-dessus.

{{< highlight java >}}

 Aspose.Cells.Cell [ D4; ValueType : IsNumeric; Value : ---; Formula:=SUM(A1:A2)]

{{< /highlight >}}
