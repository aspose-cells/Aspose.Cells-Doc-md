---
title: Auto remplir les données de Smart Marker vers d autres feuilles de calcul si les données sont trop nombreuses
type: docs
weight: 50
url: /fr/net/auto-populate-smart-marker-data-to-other-worksheets-if-data-is-too-large/
---

## **Scénarios d'utilisation possibles**
Parfois, vous souhaitez auto-populer les données du smart marker vers d'autres feuilles de calcul s'il y en a trop. Supposons, votre source de données comporte 1 500 000 enregistrements. Ce sont trop d'enregistrements pour une seule feuille de calcul, alors vous pouvez déplacer le reste des enregistrements vers la feuille de calcul suivante. 
## **Auto-peupler les données Smart Marker vers d'autres feuilles de calcul si les données sont trop volumineuses**
Le code d'exemple suivant contient une source de données avec 21 enregistrements. Nous voulons afficher seulement 15 enregistrements dans une feuille de calcul, puis le reste des enregistrements sera automatiquement déplacé vers la deuxième feuille de calcul. Veuillez noter que la deuxième feuille de calcul doit également avoir la même balise de smart marker et vous devez appeler la méthode [WorkbookDesigner.Process(sheetIndex, isPreserved)](https://reference.aspose.com/cells/net/aspose.cells.workbookdesigner/process/methods/2) pour les deux feuilles. Veuillez consulter le [fichier Excel de sortie](60489775.xlsx) généré par le code pour une référence.
## **Code d'exemple**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-AutoPopulateSmartMarkerDataToOtherWorksheets.cs" >}}
{{< app/cells/assistant language="csharp" >}}
