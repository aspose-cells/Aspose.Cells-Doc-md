---  
title: Rechercher des données en utilisant les valeurs d origine
type: docs  
weight: 380  
url: /fr/nodejs-cpp/search-data-using-original-values/  
description: Apprenez comment rechercher des données en utilisant les valeurs originales via l API Aspose.Cells for Node.js via C++.  
keywords: Rechercher des données en utilisant les valeurs originales Node.js via C++, Rechercher des données en utilisant les valeurs originales Node.js via C++, Rechercher des données par valeurs originales Node.js via C++, Rechercher des données par valeurs originales Node.js via C++  
---  

{{% alert color="primary" %}}  

Parfois, la valeur des données est masquée car elle est formatée d'une certaine manière. Par exemple, supposons que la cellule D4 ait la formule =Somme(A1:A2) et que sa valeur soit 20 mais qu'elle soit formatée comme ---, alors la valeur 20 est masquée et ne peut pas être trouvée en utilisant les options de recherche de Microsoft Excel. Cependant, vous pouvez la trouver en utilisant Aspose.Cells avec [**LookInType.OriginalValues**](https://reference.aspose.com/cells/nodejs-cpp/lookintype)  

{{% /alert %}}  

Le code d'exemple suivant illustre le point ci-dessus. Il trouve la cellule D4 qui ne peut pas être trouvée en utilisant les options de recherche de Microsoft Excel mais Aspose.Cells peut la trouver en utilisant [**LookInType.OriginalValues**](https://reference.aspose.com/cells/nodejs-cpp/lookintype). Veuillez lire les commentaires à l'intérieur du code pour plus d'informations.  

## Code Node.js pour rechercher des données en utilisant les valeurs originales  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-SearchData-SearchDataUsingOriginalValues.js" >}}


## Sortie console générée par le code d'exemple  

Voici la sortie de la console du code d'exemple ci-dessus.  

{{< highlight java >}}  

Aspose.Cells.Cell [ D4; ValueType : IsNumeric; Value : ---; Formula:=SUM(A1:A2)]  

{{< /highlight >}}  

{{< app/cells/assistant language="nodejs-cpp" >}}
