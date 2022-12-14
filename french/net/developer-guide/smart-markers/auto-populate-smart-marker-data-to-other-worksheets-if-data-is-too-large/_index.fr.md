---
title: Remplir automatiquement les données du marqueur intelligent dans d'autres feuilles de calcul si les données sont trop volumineuses
type: docs
weight: 50
url: /fr/net/auto-populate-smart-marker-data-to-other-worksheets-if-data-is-too-large/
---
## **Scénarios d'utilisation possibles**
Parfois, vous souhaitez remplir automatiquement les données du marqueur intelligent dans d'autres feuilles de calcul si elles sont trop volumineuses. Supposons que votre source de données comporte 1500000 enregistrements. Il y a trop d'enregistrements pour une seule feuille de calcul, vous pouvez alors déplacer le reste des enregistrements vers la feuille de calcul suivante.
## **Remplir automatiquement les données du marqueur intelligent dans d'autres feuilles de calcul si les données sont trop volumineuses**
 L'exemple de code suivant a une source de données qui contient 21 enregistrements. Nous voulons afficher seulement 15 enregistrements dans une feuille de calcul, puis le reste des enregistrements passera automatiquement à la deuxième feuille de calcul. Veuillez noter que la deuxième feuille de calcul doit également avoir la même balise de marqueur intelligent et vous devez appeler[WorkbookDesigner.Process(sheetIndex, isPreserved)](https://reference.aspose.com/cells/net/aspose.cells.workbookdesigner/process/methods/2) méthode pour les deux feuilles. Veuillez consulter le[fichier Excel de sortie](60489775.xlsx) généré par le code pour une référence.
## **Exemple de code**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-AutoPopulateSmartMarkerDataToOtherWorksheets.cs" >}}
