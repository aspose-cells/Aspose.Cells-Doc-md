---
title: Définition de la formule pour une plage nommée
type: docs
weight: 20
url: /fr/python-net/setting-formula-for-named-range/
---

## **Définition de la formule pour une plage nommée**
Comme l'application Excel, les API Aspose.Cells pour Python via .NET offrent la possibilité de spécifier une formule pour une plage nommée en utilisant sa propriété [**Range.refers_to**](https://reference.aspose.com/cells/python-net/aspose.cells/range/refers_to). Il pourrait y avoir de nombreux scénarios d'utilisation pour cette fonctionnalité, dont quelques-uns sont détaillés ci-dessous.
### **Définir une formule simple pour une plage nommée**
Une formule simple pourrait être une référence à une autre cellule dans la même feuille de calcul (ou dans une feuille de calcul différente). L'exemple suivant crée une plage nommée dans une nouvelle feuille et défini sa référence à une autre cellule.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Formulas-SettingSimpleFormulaForNamedRanges.py" >}}
### **Définir une formule complexe pour une plage nommée**
Une formule complexe pourrait être n'importe quoi, comme une plage dynamique ou une formule s'étalant sur plusieurs cellules dans différentes feuilles de calcul. L'exemple suivant crée une plage dynamique en utilisant la fonction INDEX pour obtenir la valeur d'une liste en fonction de son emplacement.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Formulas-SettingComplexFormulaNamedRange.py" >}}



Voici un autre exemple qui utilise une plage nommée pour additionner les valeurs de 2 cellules dans différentes feuilles de calcul.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Formulas-CalculatingSumUsingNamedRangeOnDifferentSheets.py" >}}
{{< app/cells/assistant language="python-net" >}}
