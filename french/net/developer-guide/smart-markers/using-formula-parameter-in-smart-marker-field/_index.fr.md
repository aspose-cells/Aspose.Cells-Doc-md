---
title: Utilisation du paramètre de formule dans le champ Smart Marker
type: docs
weight: 40
url: /fr/net/using-formula-parameter-in-smart-marker-field/
---


## **Scénarios d'utilisation possibles**
Parfois, vous souhaitez intégrer une formule dans le champ Smart Marker. Cet article décrit comment utiliser le paramètre *Formule* pour intégrer une formule dans le champ Smart Marker.
## **Utilisation du paramètre de formule dans le champ Smart Marker**
Le code d'exemple suivant intègre la formule dans le champ Smart Marker nommé TestFormula et son nom de la source de données est MyDataSource, de sorte que le champ complet avec le paramètre de formule ressemble à &=MyDataSource.TestFormula(formule) et après l'exécution du code, le [fichier Excel de sortie final](46465047.xlsx) aura des formules dans les cellules de A1 à A5.
## **Code d'exemple**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingFormulaParameterInSmartMarkerField.cs" >}}
