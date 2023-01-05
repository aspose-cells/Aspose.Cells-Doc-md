---
title: Appliquer le filtre avancé de Microsoft Excel pour afficher les enregistrements répondant à des critères complexes
type: docs
weight: 190
url: /fr/java/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/
---
## **Scénarios d'utilisation possibles**
 Microsoft Excel vous permet de postuler*Filtre avancé* sur les données de la feuille de calcul pour afficher les enregistrements qui répondent à des critères complexes. Vous pouvez appliquer le filtre avancé avec Microsoft Excel via son*Données > Avancé*commande comme indiqué dans cette capture d'écran.

![tâche : image_autre_texte](apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria_1.png)

Aspose.Cells vous permet également d'appliquer le filtre avancé à l'aide du[Feuille de travail.advancedFilter()](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#advancedFilter\(boolean,%20java.lang.String,%20java.lang.String,%20java.lang.String,%20boolean\)) méthode. Tout comme Microsoft Excel, il accepte les paramètres suivants.

**estFiltre**

Indique si le filtrage de la liste est en place.

**listePlage**

La plage de la liste.

**Plage de critères**

La gamme de critères.

**copier**

La plage dans laquelle copier les données.

**uniqueRecordOnly**

Afficher ou copier uniquement des lignes uniques.
## **Appliquer le filtre avancé de Microsoft Excel pour afficher les enregistrements répondant à des critères complexes**
L'exemple de code suivant applique le filtre avancé sur le[Exemple de fichier Excel](48496702.xlsx) et génère le[Fichier Excel de sortie](48496705.xlsx). La capture d'écran montre les deux fichiers pour comparaison. Comme vous pouvez le voir dans la capture d'écran, les données ont été filtrées dans le fichier Excel de sortie selon des critères complexes.

![tâche : image_autre_texte](apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria_2.png)
## **Exemple de code**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-ApplyAdvancedFilterOfMicrosoftExcel.java" >}}
