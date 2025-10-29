---
title: Rechercher des données en utilisant les valeurs d origine
type: docs
weight: 380
url: /fr/python-net/search-data-using-original-values/
description: Apprenez à rechercher des données en utilisant des valeurs d origine grâce à l API Aspose.Cells pour Python via .NET.
keywords: Bibliothèque Python Excel, Rechercher des données en utilisant des valeurs d origine en Python, Trouver des données en utilisant des valeurs d origine en Python, Rechercher des données par valeurs d origine en Python, Trouver des données par valeurs d origine en Python
---

{{% alert color="primary" %}}

Parfois, la valeur des données est masquée car elle est formatée de certaine manière. Par exemple, supposons que la cellule D4 contienne la formule =Sum(A1:A2) et que sa valeur soit de 20 mais qu'elle soit formatée comme ---, alors la valeur 20 est masquée et ne peut pas être trouvée à l'aide des options de recherche de Microsoft Excel. Cependant, vous pouvez la trouver en utilisant Aspose.Cells pour Python via .NET à l'aide de [**LookInType.ORIGINAL_VALUES**](https://reference.aspose.com/cells/python-net/aspose.cells/lookintype).

{{% /alert %}}

Le code d'exemple suivant illustre le point ci-dessus. Il trouve la cellule D4 qui ne peut pas être trouvée en utilisant les options de recherche de Microsoft Excel mais Aspose.Cells peut la trouver en utilisant [**LookInType.ORIGINAL_VALUES**](https://reference.aspose.com/cells/python-net/aspose.cells/lookintype). Veuillez lire les commentaires à l'intérieur du code pour plus d'informations.

## Code Python pour rechercher des données en utilisant des valeurs d'origine

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-SearchDataUsingOriginalValues.py" >}}

## Sortie console générée par le code d'exemple

Voici la sortie de la console du code d'exemple ci-dessus.

{{< highlight java >}}

Aspose.Cells.Cell [ D4; ValueType : IsNumeric; Value : ---; Formula:=SUM(A1:A2)]

{{< /highlight >}}
{{< app/cells/assistant language="python-net" >}}
