---
title: Calculer les fonctions personnalisées dans GridWeb
type: docs
weight: 90
url: /fr/net/aspose-cells-gridweb/calculate-custom-functions-in-gridweb/
keywords: GridWeb,custom functions,custom,function
description: Cet article présente les fonctionnalités des fonctions personnalisées dans GridWeb.
---


## **Scénarios d'utilisation possibles**
Aspose.Cells.GridWeb prend en charge le calcul des fonctions personnalisées avec la propriété GridWeb.CustomCalculationEngine. Cette propriété prend l'instance de l'interface GridAbstractCalculationEngine. Veuillez implémenter l'interface GridAbstractCalculationEngine et calculer vos fonctions personnalisées avec votre propre logique.
## **Calculer les fonctions personnalisées dans GridWeb**
Le code d'exemple suivant ajoute une fonction personnalisée nommée MYTESTFUNC() dans la cellule B3. Ensuite, nous calculons la valeur de cette fonction en implémentant l'interface GridAbstractCalculationEngine. Nous calculons MYTESTFUNC() de telle manière qu'elle multiplie son paramètre par 2 et renvoie le résultat. Ainsi, si son paramètre est 9, elle renverra 2*9 = 18.
### **Code d'exemple**


{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Articles-CalculateCustomFunction.aspx-CalculateCustomFunction.cs" >}}
