---
title: Filtrer le projet VBA lors du chargement d un classeur avec Golang via C++
linktitle: Filtrer le projet VBA lors du chargement d un classeur
type: docs
weight: 140
url: /fr/go-cpp/filter-vba-project-while-loading-a-workbook/
description: Apprenez comment filtrer les projets VBA lors du chargement d un classeur Excel en utilisant Aspose.Cells avec Golang via C++.
---

## **Filtrer le projet VBA lors du chargement d'un classeur Excel en C++**

Certains fichiers .xlsm/.xslb contiennent un nombre extrêmement élevé de macros (ou des macros très longues). Aspose.Cells chargera inconditionnellement ces données (métadonnées) lors de l'ouverture de tels classeurs. Vous pourriez nécessiter de contrôler cela via [**LoadDataFilterOptions**](https://reference.aspose.com/cells/go-cpp/loaddatafilteroptions) lorsque vous souhaitez uniquement extraire les noms des feuilles pour un grand nombre de classeurs, en évitant ainsi le contenu non nécessaire. Ce filtre est fourni en introduisant une nouvelle option, [**LoadDataFilterOptions.VBA**](https://reference.aspose.com/cells/go-cpp/loaddatafilteroptions).

## **Code d'exemple**

Le code d'exemple suivant charge un classeur de telle sorte que seul le VBA est filtré. Un fichier exemple pour tester cette fonctionnalité peut être téléchargé à partir du lien suivant :

[sampleMacroEnabledWorkbook.xlsm](79527938.xlsm)

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FilterVbaProjectWhileLoadingAWorkbook.go" >}}
