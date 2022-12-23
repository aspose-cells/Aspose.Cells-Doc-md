---
title: Définition de la formule pour la plage nommée
type: docs
weight: 20
url: /fr/net/setting-formula-for-named-range/
---
## **Définition de la formule pour la plage nommée**
 Comme l'application Excel, les API Aspose.Cells offrent la possibilité de spécifier une formule pour une plage nommée tout en utilisant son[Fait référence à](https://reference.aspose.com/cells/net/aspose.cells/range/properties/refersto)la propriété. Il peut y avoir de nombreux scénarios d'utilisation pour cette fonctionnalité, dont quelques-uns sont détaillés ci-dessous.
### **Définition d'une formule simple pour une plage nommée**
Une formule simple peut être une référence à une autre cellule dans la même feuille de calcul (ou différente). L'exemple suivant crée une plage nommée dans une nouvelle feuille de calcul et définit sa référence à une autre cellule.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-SettingSimpleFormula-SettingSimpleFormulaForNamedRanges.cs" >}}
### **Définition d'une formule complexe pour une plage nommée**
Une formule complexe peut être quelque chose comme une plage dynamique ou une formule couvrant plusieurs cellules dans différentes feuilles de calcul. L'exemple suivant crée une plage dynamique à l'aide de la fonction INDEX pour obtenir la valeur d'une liste en fonction de son emplacement.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-SettingComplexFormula-SettingComplexFormulaNamedRange.cs" >}}



Voici un autre exemple qui utilise une plage nommée pour additionner les valeurs de 2 cellules dans différentes feuilles de calcul.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-CalculatingSumUsingNamedRange-CalculatingSumUsingNamedRangeOnDifferentSheets.cs" >}}
