---
title: Calculer des fonctions personnalisées dans GridWeb
type: docs
weight: 90
url: /fr/net/calculate-custom-functions-in-gridweb/
---
## **Scénarios d'utilisation possibles**
Aspose.Cells.GridWeb prend en charge le calcul des fonctions personnalisées avec la propriété GridWeb.CustomCalculationEngine. Cette propriété prend l'instance de l'interface GridAbstractCalculationEngine. Veuillez implémenter l'interface GridAbstractCalculationEngine et calculer vos fonctions personnalisées avec votre propre logique.
## **Calculer des fonctions personnalisées dans GridWeb**
L'exemple de code suivant ajoute une fonction personnalisée nommée MYTESTFUNC() dans la cellule B3. Ensuite, nous calculons la valeur de cette fonction en implémentant l'interface GridAbstractCalculationEngine. Nous calculons MYTESTFUNC() de telle sorte qu'il multiplie son paramètre par 2 et renvoie le résultat. Donc si son paramètre est 9, il renverra 2*9 = 18.
### **Exemple de code**


{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Articles-CalculateCustomFunction.aspx-CalculateCustomFunction.cs" >}}
