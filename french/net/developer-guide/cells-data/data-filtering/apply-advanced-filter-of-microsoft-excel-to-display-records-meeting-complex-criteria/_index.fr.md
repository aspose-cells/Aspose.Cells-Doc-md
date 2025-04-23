---
title: Appliquer un filtre avancé de Microsoft Excel pour afficher les enregistrements répondant à des critères complexes
type: docs
weight: 280
url: /fr/net/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/
description: Apprenez comment appliquer un filtre avancé de Microsoft Excel pour afficher les enregistrements répondant à des critères complexes en utilisant l API Aspose.Cells for .NET.
keywords: Appliquer un filtre avancé, Définir un filtre avancé, Ajouter un filtre avancé, Créer un filtre avancé, Comment ajouter un filtre avancé à une plage 
---

## **Scénarios d'utilisation possibles**

Microsoft Excel vous permet d'appliquer un *Filtre avancé* sur les données de la feuille de calcul pour afficher des enregistrements répondant à des critères complexes. Vous pouvez appliquer un filtre avancé avec Microsoft Excel via sa commande *Données > Avancé* comme indiqué dans cette capture d'écran.

![todo:image_alt_text](apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria_1.png)

Aspose.Cells vous permet également d'appliquer le filtre avancé en utilisant la méthode [**Worksheet.AdvancedFilter()**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/advancedfilter). Tout comme Microsoft Excel, il accepte les paramètres suivants.

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

Le code d'exemple suivant applique le filtre avancé sur le [Fichier Excel d'exemple](48496692.xlsx) et génère le [Fichier Excel de sortie](48496691.xlsx). La capture d'écran montre les deux fichiers pour comparaison. Comme vous pouvez le voir dans la capture d'écran, les données ont été filtrées dans le fichier Excel de sortie en fonction de critères complexes.

![todo:image_alt_text](apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria_2.png)

## **Code d'exemple**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-ApplyAdvancedFilterOfMicrosoftExcel.cs" >}}
{{< app/cells/assistant language="csharp" >}}
