---
title: Appliquer le filtre avancé de Microsoft Excel pour afficher les enregistrements répondant à des critères complexes avec Golang via C++
linktitle: Appliquer un filtre avancé de Microsoft Excel pour afficher les enregistrements répondant à des critères complexes
type: docs
weight: 280
url: /fr/go-cpp/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/
description: Apprenez comment appliquer le filtre avancé de Microsoft Excel pour afficher les enregistrements répondant à des critères complexes en utilisant l API Aspose.Cells for C++.
keywords: Appliquer un filtre avancé, Définir un filtre avancé, Ajouter un filtre avancé, Créer un filtre avancé, Comment ajouter un filtre avancé à une plage
---

## **Scénarios d'utilisation possibles**

Microsoft Excel vous permet d'appliquer le *Filtre avancé* sur les données de la feuille pour afficher les enregistrements répondant à des critères complexes. Vous pouvez appliquer le filtre avancé via la commande *Données > Avancé* comme montré dans cette capture d'écran.

![todo:image_alt_text](apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria_1.png)

Aspose.Cells vous permet également d'appliquer le filtre avancé en utilisant la méthode [**GetAdvancedFilter()**](https://reference.aspose.com/cells/go-cpp/worksheet/getadvancedfilter/). Tout comme Microsoft Excel, elle accepte les paramètres suivants.

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

Le code exemple suivant applique le filtre avancé sur le [Fichier Excel d'exemple](48496692.xlsx) et génère le [Fichier Excel de sortie](48496691.xlsx). La capture d'écran montre les deux fichiers pour comparaison. Comme vous pouvez le voir dans la capture, les données ont été filtrées dans le fichier Excel de sortie selon des critères complexes.

![todo:image_alt_text](apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria_2.png)

## **Code d'exemple**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ApplyAdvancedFilterOfMicrosoftExcelToDisplayRecordsMeetingComplexCriteria.go" >}}
