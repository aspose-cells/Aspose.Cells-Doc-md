---
title: Appliquer un filtre avancé de Microsoft Excel pour afficher les enregistrements répondant à des critères complexes
type: docs
weight: 190
url: /fr/java/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/
---

## **Scénarios d'utilisation possibles**
Microsoft Excel vous permet d'appliquer un *Filtre avancé* sur les données de la feuille de calcul pour afficher des enregistrements répondant à des critères complexes. Vous pouvez appliquer un filtre avancé avec Microsoft Excel via sa commande *Données > Avancé* comme indiqué dans cette capture d'écran.

![todo:image_alt_text](apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria_1.png)

Aspose.Cells permet également d'appliquer le filtre avancé à l'aide de la méthode [Worksheet.advancedFilter()](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#advancedFilter\(boolean,%20java.lang.String,%20java.lang.String,%20java.lang.String,%20boolean\)). Tout comme Microsoft Excel, elle accepte les paramètres suivants.

**isFilter**

Indique s'il y a filtrage de la liste sur place.

**plageListe**

La plage de liste.

**criteriaRange**

La plage de critères.

**copyTo**

La plage où copier les données.

**uniqueRecordOnly**

Afficher ou copier uniquement les lignes uniques.
## **Appliquer un filtre avancé de Microsoft Excel pour afficher les enregistrements répondant à des critères complexes**
Le code d'exemple suivant applique le filtre avancé sur le [Fichier Excel d'exemple](48496702.xlsx) et génère le [Fichier Excel de sortie](48496705.xlsx). La capture d'écran montre les deux fichiers pour comparaison. Comme vous pouvez le voir dans la capture d'écran, les données ont été filtrées dans le fichier Excel de sortie selon des critères complexes.

![todo:image_alt_text](apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria_2.png)
## **Code d'exemple**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-ApplyAdvancedFilterOfMicrosoftExcel.java" >}}
