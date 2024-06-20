---
title: Appliquer un filtre avancé de Microsoft Excel pour afficher les enregistrements répondant à des critères complexes
type: docs
weight: 280
url: /fr/python-net/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/
description: Apprenez comment appliquer un filtre avancé de Microsoft Excel pour afficher les enregistrements répondant à des critères complexes en utilisant l API Aspose.Cells pour Python via .NET.
keywords: Bibliothèque Excel Python, Appliquer un filtre avancé Python, Définir un filtre avancé Python, Ajouter un filtre avancé Python, Créer un filtre avancé Python, Comment ajouter un filtre avancé à une plage à l aide de Python.
---

## **Scénarios d'utilisation possibles**

Microsoft Excel vous permet d'appliquer un *Filtre avancé* sur les données de la feuille de calcul pour afficher des enregistrements répondant à des critères complexes. Vous pouvez appliquer un filtre avancé avec Microsoft Excel via sa commande *Données > Avancé* comme indiqué dans cette capture d'écran.

![todo:image_alt_text](1.png)

Aspose.Cells pour Python via .NET vous permet également d'appliquer le filtre avancé en utilisant la méthode [**Worksheet.advancedFilter()**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/advanced_filter/#bool-str-str-str-bool). Tout comme Microsoft Excel, il accepte les paramètres suivants.

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

![todo:image_alt_text](2.png)

## **Code d'exemple**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-ApplyAdvancedFilterOfMicrosoftExcel.py" >}}
