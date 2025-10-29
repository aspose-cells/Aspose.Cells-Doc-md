---
title: Appliquer une Mise en Forme Conditionnelle dans une Feuille de Calcul
type: docs
weight: 40
url: /fr/cpp/apply-conditional-formatting-in-worksheet/
---

## **Scénario d'utilisation possible**
Aspose.Cells vous permet d'ajouter toutes sortes de formatage conditionnel, par exemple, formule, au-dessus de la moyenne, échelle de couleurs, barre de données, jeu d'icônes, Top10, etc. Il fournit la classe [FormatCondition](https://reference.aspose.com/cells/cpp/aspose.cells/formatcondition/) qui possède toutes les méthodes nécessaires pour appliquer le formatage conditionnel de votre choix. Voici la liste de quelques méthodes Get.

- [GetAboveAverage()](https://reference.aspose.com/cells/cpp/aspose.cells/formatcondition/getaboveaverage/)
- [GetColorScale()](https://reference.aspose.com/cells/cpp/aspose.cells/formatcondition/getcolorscale)
- [GetDataBar()](https://reference.aspose.com/cells/cpp/aspose.cells/formatcondition/getdatabar)
- [GetIconSet()](https://reference.aspose.com/cells/cpp/aspose.cells/formatcondition/geticonset)
- [GetTop10()](https://reference.aspose.com/cells/cpp/aspose.cells/formatcondition/gettop10)
## **Appliquer le formatage conditionnel dans la feuille de calcul**
Le code d'exemple suivant montre comment ajouter un formatage conditionnel de la valeur de cellule sur les cellules A1 et B2. Veuillez consulter le [fichier Excel de sortie](23167004.xlsx) généré par le code et la capture d'écran suivante qui explique l'effet du code sur le [fichier Excel de sortie](23167004.xlsx). Si vous entrez une valeur supérieure à 100 dans la cellule A2 et B2, la couleur de remplissage rouge des cellules A1 et B2 disparaîtra.

![todo:image_alt_text](apply-conditional-formatting-in-worksheet_1.png)
## **Code d'exemple**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-ApplyConditionalFormattingInWorksheet-new.cpp" >}}
{{< app/cells/assistant language="cpp" >}}
