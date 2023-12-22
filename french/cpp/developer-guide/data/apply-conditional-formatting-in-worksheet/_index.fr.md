---
title: Appliquer une mise en forme conditionnelle dans une feuille de calcul
type: docs
weight: 40
url: /fr/cpp/apply-conditional-formatting-in-worksheet/
---
##  **Scénario d'utilisation possible**
 Aspose.Cells vous permet d'ajouter toutes sortes de formatage conditionnel, par exemple Formule, Au-dessus de la moyenne, Échelle de couleurs, Barre de données, Jeu d'icônes, Top10, etc. Il fournit le[FormatCondition](https://reference.aspose.com/cells/cpp/aspose.cells/formatcondition/)classe qui possède toutes les méthodes nécessaires pour appliquer la mise en forme conditionnelle de votre choix. Voici la liste de quelques méthodes Get.

- [GetAboveAverage()](https://reference.aspose.com/cells/cpp/aspose.cells/formatcondition/getaboveaverage/)
- [GetColorScale()](https://reference.aspose.com/cells/cpp/aspose.cells/formatcondition/getcolorscale)
- [GetDataBar()](https://reference.aspose.com/cells/cpp/aspose.cells/formatcondition/getdatabar)
- [GetIconSet()](https://reference.aspose.com/cells/cpp/aspose.cells/formatcondition/geticonset)
- [GetTop10()](https://reference.aspose.com/cells/cpp/aspose.cells/formatcondition/gettop10)
##  **Appliquer une mise en forme conditionnelle dans une feuille de calcul**
 L’exemple de code suivant montre comment ajouter une mise en forme conditionnelle de valeur Cell sur les cellules A1 et B2. Veuillez consulter le[sortie du fichier Excel](23167004.xlsx) généré par le code et la capture d'écran suivante qui explique l'effet du code sur le[sortie du fichier Excel](23167004.xlsx)Si vous mettez une valeur supérieure à 100 dans les cellules A2 et B2, la couleur de remplissage rouge des cellules A1 et B2 disparaîtra.

![tâche : image_alt_text](apply-conditional-formatting-in-worksheet_1.png)
##  **Exemple de code**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-ApplyConditionalFormattingInWorksheet-new.cpp" >}}
