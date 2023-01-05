---
title: Rechercher des données à l'aide des valeurs d'origine
type: docs
weight: 380
url: /fr/net/search-data-using-original-values/
---
{{% alert color="primary" %}}

 Parfois, la valeur des données est masquée car elle est formatée d'une manière ou d'une autre. Par exemple, supposons que la cellule D4 ait la formule = Somme (A1: A2) et que sa valeur soit 20 mais qu'elle soit formatée comme ---, alors la valeur 20 est masquée et ne peut pas être trouvée à l'aide des options de recherche Excel Microsoft. Cependant, vous pouvez le trouver en utilisant Aspose.Cells en utilisant[**LookInType.OriginalValues**](https://reference.aspose.com/cells/net/aspose.cells/lookintype)

{{% /alert %}}

 L'exemple de code suivant illustre le point ci-dessus. Il trouve la cellule D4 qui ne peut pas être trouvée en utilisant les options de recherche Excel Microsoft mais Aspose.Cells peut la trouver en utilisant[**LookInType.OriginalValues**](https://reference.aspose.com/cells/net/aspose.cells/lookintype). Veuillez lire les commentaires à l'intérieur du code pour plus d'informations.

## C# code pour rechercher des données en utilisant les valeurs d'origine

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-SearchDataUsingOriginalValues-SearchDataUsingOriginalValues.cs" >}}

## Sortie de la console générée par l'exemple de code

Voici la sortie console de l'exemple de code ci-dessus.

{{< highlight "java" >}}

Aspose.Cells.Cell [ D4; ValueType : IsNumeric; Value : ---; Formula:=SUM(A1:A2)]{{< /highlight >}}
