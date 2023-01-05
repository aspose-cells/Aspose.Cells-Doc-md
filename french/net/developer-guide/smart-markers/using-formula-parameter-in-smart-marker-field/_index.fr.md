---
title: Utilisation du paramètre Formule dans le champ Smart Marker
type: docs
weight: 40
url: /fr/net/using-formula-parameter-in-smart-marker-field/
---
## **Scénarios d'utilisation possibles**
Parfois, vous souhaitez intégrer une formule dans le champ du marqueur intelligent. Cet article explique comment utiliser le*Formule*paramètre pour intégrer la formule dans le champ du marqueur intelligent.
## **Utilisation du paramètre Formule dans le champ Smart Marker**
 L'exemple de code suivant intègre la formule dans le champ de marqueur intelligent nommé TestFormula et son nom de source de données est MyDataSource, de sorte que le champ complet avec le paramètre de formule ressemble à &=MyDataSource.TestFormula(formula) et après l'exécution du code, le[fichier Excel de sortie finale](46465047.xlsx) aura des formules dans les cellules de A1 à A5.
## **Exemple de code**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingFormulaParameterInSmartMarkerField.cs" >}}
