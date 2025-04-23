---
title: Auto remplir les données de Smart Marker vers d autres feuilles de calcul si les données sont trop nombreuses
type: docs
weight: 10
url: /fr/java/auto-populate-smart-marker-data-to-other-worksheets-if-data-is-too-large/
---

## **Scénarios d'utilisation possibles**

Parfois, vous souhaitez auto-remplir les données de Smart Marker vers d'autres feuilles de calcul si elles sont trop nombreuses. Supposons que votre source de données comporte 1500000 enregistrements. Ceux-ci sont trop nombreux pour une seule feuille de calcul, vous pouvez alors déplacer le reste des enregistrements vers la feuille de calcul suivante.

## **Remplir automatiquement les données de Smart Marker dans d'autres feuilles de calcul si les données sont trop nombreuses**

Le code d'échantillon suivant a une source de données qui comporte 21 enregistrements. Nous souhaitons afficher uniquement 15 enregistrements dans une feuille de calcul, puis le reste des enregistrements sera automatiquement déplacé vers la deuxième feuille de calcul. Veuillez noter que la deuxième feuille de calcul doit également avoir la même balise de Smart Marker et vous devez appeler la méthode [**WorkbookDesigner.process(sheetIndex, isPreserved)**](https://reference.aspose.com/cells/java/com.aspose.cells/workbookdesigner#process-int-boolean-) pour les deux feuilles. Veuillez vérifier le [fichier de base de données Microsoft Access](60489777.accdb) utilisé dans ce code ainsi que le [fichier Excel de sortie](60489786.xlsx) généré par le code pour une référence.

## **Code d'exemple**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "SmartMarkers-AutoPopulateSmartMarkerDataToOtherWorksheets.java" >}}
{{< app/cells/assistant language="java" >}}
