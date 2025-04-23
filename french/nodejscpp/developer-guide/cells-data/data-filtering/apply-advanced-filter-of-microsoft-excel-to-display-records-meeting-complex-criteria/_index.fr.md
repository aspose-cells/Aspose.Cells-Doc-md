---  
title: Appliquer un filtre avancé de Microsoft Excel pour afficher les enregistrements répondant à des critères complexes
type: docs  
weight: 280  
url: /fr/nodejs-cpp/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/  
description: Apprenez comment utiliser le filtre avancé de Microsoft Excel pour afficher les enregistrements répondant à des critères complexes en utilisant l API Aspose.Cells for Node.js via C++.  
keywords: Appliquer le filtre avancé Node.js via C++, configurer le filtre avancé Node.js via C++, ajouter le filtre avancé Node.js via C++, créer le filtre avancé Node.js via C++, Comment ajouter un filtre avancé à une plage Node.js via C++  
---  

## **Scénarios d'utilisation possibles**  

Microsoft Excel vous permet d'appliquer le *Filtre avancé* sur les données de la feuille pour afficher les enregistrements répondant à des critères complexes. Vous pouvez appliquer le filtre avancé via la commande *Données > Avancé* comme montré dans cette capture d'écran.  

![todo:image_alt_text](1.png)  

Aspose.Cells for Node.js via C++ permet également d'appliquer le filtre avancé en utilisant la méthode [**Worksheet.advanced_Filter()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#advanced_Filter-boolean-string-string-string-boolean-). Tout comme Microsoft Excel, il accepte les paramètres suivants.  

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

![todo:image_alt_text](2.png)  

## **Code d'exemple**  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Autofilter-AdvancedFilter.js" >}}


