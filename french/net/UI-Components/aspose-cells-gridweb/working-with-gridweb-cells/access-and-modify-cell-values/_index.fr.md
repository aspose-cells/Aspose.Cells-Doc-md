---
title: Accéder et Modifier la Valeur de la Cellule
type: docs
weight: 20
url: /fr/net/aspose-cells-gridweb/access-and-modify-cell-value/
keywords: GridWeb,valeur de la cellule,modifier,valeur
description: Cet article présente comment obtenir et modifier la valeur de la cellule dans GridWeb.
---

{{% alert color="primary" %}} 

La section [Accéder aux cellules de feuille de calcul](/cells/fr/net/aspose-cells-gridweb/access-worksheet-cells/) traite de l'accès aux cellules. Ce sujet étend cette discussion pour montrer comment accéder et modifier les valeurs des cellules à l'aide de l'API Aspose.Cells.GridWeb.

{{% /alert %}} 
## **Accès & Modification de la Valeur d'une Cellule**
### **Valeurs de Chaîne**
Avant d'accéder et de modifier la valeur d'une cellule, vous devez savoir comment accéder aux cellules. Pour obtenir des détails sur les différentes approches pour accéder aux cellules, consultez [Accéder aux cellules de feuille de calcul](/cells/fr/net/aspose-cells-gridweb/access-worksheet-cells/).

Chaque cellule a une propriété nommée StringValue. Une fois qu'une cellule est accédée, les développeurs peuvent utiliser la propriété StringValue pour accéder à la valeur de la chaîne des cellules. Pour modifier les valeurs des cellules, une méthode spéciale PutValue est fournie, qui peut être utilisée pour mettre à jour la valeur de la chaîne de la cellule.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ModifyCells.aspx-AddCellStringValue.cs" >}}
### **Tous Types de Valeurs**
La méthode PutValue d'un objet de cellule dispose de 8 surcharges disponibles qui peuvent être utilisées pour modifier tout type de valeur (booléen, entier, double, DateTime et chaîne) dans une cellule.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ModifyCells.aspx-AddCellIntValue.cs" >}}



Il existe également une version surchargée de la méthode PutValue qui peut prendre n'importe quel type de valeur au format de chaîne et le convertir automatiquement en un type de données approprié. Pour ce faire, passez la valeur booléenne true à un autre paramètre de la méthode PutValue comme indiqué ci-dessous dans l'exemple.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ModifyCells.aspx-AddCellDoubleValue.cs" >}}
