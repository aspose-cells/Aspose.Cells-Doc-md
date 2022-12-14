---
title: Remplir automatiquement les données du marqueur intelligent dans d'autres feuilles de calcul si les données sont trop volumineuses
type: docs
weight: 10
url: /fr/java/auto-populate-smart-marker-data-to-other-worksheets-if-data-is-too-large/
---
## **Scénarios d'utilisation possibles**

Parfois, vous souhaitez remplir automatiquement les données du marqueur intelligent dans d'autres feuilles de calcul si elles sont trop volumineuses. Supposons que votre source de données comporte 1500000 enregistrements. Il y a trop d'enregistrements pour une seule feuille de calcul, vous pouvez alors déplacer le reste des enregistrements vers la feuille de calcul suivante.

## **Remplir automatiquement les données du marqueur intelligent dans d'autres feuilles de calcul si les données sont trop volumineuses**

L'exemple de code suivant a une source de données qui contient 21 enregistrements. Nous voulons afficher seulement 15 enregistrements dans une feuille de calcul, puis le reste des enregistrements passera automatiquement à la deuxième feuille de calcul. Veuillez noter que la deuxième feuille de calcul doit également avoir la même balise de marqueur intelligent et vous devez appeler[**WorkbookDesigner.process(sheetIndex, isPreserved)**](https://reference.aspose.com/cells/java/com.aspose.cells/workbookdesigner#process(int,%20boolean) ) méthode pour les deux feuilles. S'il vous plaît, vérifiez le[Microsoft Fichier de base de données Access](60489777.accdb) utilisé dans ce code ainsi que le[fichier Excel de sortie](60489786.xlsx)généré par le code pour une référence.

## **Exemple de code**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "SmartMarkers-AutoPopulateSmartMarkerDataToOtherWorksheets.java" >}}
