---
title: Utilisation du paramètre de formule dans le champ Smart Marker
type: docs
weight: 30
url: /fr/java/using-formula-parameter-in-smart-marker-field/
---

## **Scénarios d'utilisation possibles**
Parfois, vous voulez intégrer une formule dans le champ smart marker. Cet article décrit comment utiliser le paramètre de formule pour intégrer une formule dans un champ smart marker.
## **Utilisation du paramètre de formule dans le champ Smart Marker**
Le code d'exemple suivant intègre la formule dans la variable de smart marker nommée Test et son nom de source de données est également Test, donc le champ complet avec le paramètre de formule ressemble à **&=$Test(fomule)** et après l'exécution du code, le [fichier Excel de sortie final](47153156.xlsx) aura des formules dans les cellules de A1 à A5.
## **Code d'exemple**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-SmartMarkers-UsingFormulaParameterInSmartMarkerField.java" >}}
