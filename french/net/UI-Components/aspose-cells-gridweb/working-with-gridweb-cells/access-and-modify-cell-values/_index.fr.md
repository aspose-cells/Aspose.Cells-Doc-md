---
title: Accéder et modifier les valeurs Cell
type: docs
weight: 20
url: /fr/net/access-and-modify-cell-values/
---
{{% alert color="primary" %}} 

[Accéder à la feuille de travail Cells](/cells/fr/net/access-worksheet-cells/) discuté de l'accès aux cellules. Cette rubrique étend cette discussion pour montrer comment accéder aux valeurs de cellule et les modifier à l'aide de Aspose.Cells.GridWeb API.

{{% /alert %}} 
## **Accéder et modifier la valeur d'un Cell**
### **Valeurs de chaîne**
 Avant d'accéder et de modifier la valeur d'une cellule, vous devez savoir comment accéder aux cellules. Pour plus de détails sur les différentes approches d'accès aux cellules, reportez-vous à[Accéder à la feuille de travail Cells](/cells/fr/net/access-worksheet-cells/).

Chaque cellule a une propriété nommée StringValue. Une fois qu'une cellule est accédée, les développeurs peuvent utiliser la propriété StringValue pour accéder à la valeur de chaîne des cellules. Pour modifier les valeurs des cellules, une méthode spéciale PutValue est fournie, qui peut être utilisée pour mettre à jour la valeur de chaîne de la cellule.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ModifyCells.aspx-AddCellStringValue.cs" >}}
### **Tous les types de valeurs**
La méthode PutValue d'un objet de cellule a 8 surcharges disponibles qui peuvent être utilisées pour modifier n'importe quel type de valeur (Boolean, int, double, DateTime et string) dans une cellule.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ModifyCells.aspx-AddCellIntValue.cs" >}}



Il existe également une version surchargée de la méthode PutValue qui peut prendre n'importe quel type de valeur au format chaîne et la convertir automatiquement en un type de données approprié. Pour ce faire, transmettez la valeur booléenne true à un autre paramètre de la méthode PutValue, comme indiqué ci-dessous dans l'exemple.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ModifyCells.aspx-AddCellDoubleValue.cs" >}}
