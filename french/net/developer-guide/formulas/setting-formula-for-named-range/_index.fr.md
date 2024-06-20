---
title: Définition de la formule pour une plage nommée
type: docs
weight: 20
url: /fr/net/setting-formula-for-named-range/
---

## **Définition de la formule pour une plage nommée**
Comme l'application Excel, les API Aspose.Cells permettent de spécifier une formule pour une plage nommée tout en utilisant sa propriété [RefersTo](https://reference.aspose.com/cells/net/aspose.cells/range/properties/refersto). Il pourrait y avoir de nombreuses utilisations pour cette fonctionnalité, certaines d'entre elles sont détaillées ci-dessous.
### **Définir une formule simple pour une plage nommée**
Une formule simple pourrait être une référence à une autre cellule dans la même feuille de calcul (ou dans une feuille de calcul différente). L'exemple suivant crée une plage nommée dans une nouvelle feuille et défini sa référence à une autre cellule.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-SettingSimpleFormula-SettingSimpleFormulaForNamedRanges.cs" >}}
### **Définir une formule complexe pour une plage nommée**
Une formule complexe pourrait être n'importe quoi, comme une plage dynamique ou une formule s'étalant sur plusieurs cellules dans différentes feuilles de calcul. L'exemple suivant crée une plage dynamique en utilisant la fonction INDEX pour obtenir la valeur d'une liste en fonction de son emplacement.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-SettingComplexFormula-SettingComplexFormulaNamedRange.cs" >}}



Voici un autre exemple qui utilise une plage nommée pour additionner les valeurs de 2 cellules dans différentes feuilles de calcul.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-CalculatingSumUsingNamedRange-CalculatingSumUsingNamedRangeOnDifferentSheets.cs" >}}
