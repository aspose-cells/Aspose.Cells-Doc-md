---
title: Appliquer la mise en forme conditionnelle dans la feuille de calcul
type: docs
weight: 40
url: /fr/cpp/apply-conditional-formatting-in-worksheet/
---
## **Scénario d'utilisation possible**
 Aspose.Cells vous permet d'ajouter toutes sortes de formatage conditionnel, par exemple Formule, Au-dessus de la moyenne, Échelle de couleurs, Barre de données, Jeu d'icônes, Top10, etc. Il fournit le[IFormatCondition](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_format_condition)classe qui possède toutes les méthodes nécessaires pour appliquer la mise en forme conditionnelle de votre choix. Voici la liste de quelques-unes des méthodes Get.

- [GetIAboveAverage()](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_format_condition#aff550fd834cd78967ec440492ff012d5)
- [GetIColorScale()](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_format_condition#a3348a7c447dc564ceabc22c9c89bd6f5)
- [GetIDataBar()](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_format_condition#a4415a87833c41386ed1595e742485e07)
- [GetIIconSet()](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_format_condition#a011b2c7dbaaf671819d09f5d1df865e3)
- [GetITop10()](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_format_condition#a64388aaf1b43811f5ee1ee3090c9bd4a)
## **Appliquer la mise en forme conditionnelle dans la feuille de calcul**
 L'exemple de code suivant montre comment ajouter une mise en forme conditionnelle de valeur Cell sur les cellules A1 et B2. Veuillez consulter le[fichier excel de sortie](23167004.xlsx) généré par le code et la capture d'écran suivante qui explique l'effet du code sur le[fichier excel de sortie](23167004.xlsx). Si vous mettez une valeur supérieure à 100 dans les cellules A2 et B2, la couleur de remplissage rouge des cellules A1 et B2 disparaîtra.

![tâche : image_autre_texte](apply-conditional-formatting-in-worksheet_1.png)
## **Exemple de code**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-ApplyConditionalFormattingInWorksheet.cpp" >}}
