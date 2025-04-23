---
title: Obtenir une plage avec des liens externes
type: docs
weight: 140
url: /fr/java/get-range-with-external-links/
---

## **Obtenir une plage avec des liens externes**

Très souvent, les fichiers Excel accèdent à des données à partir d'autres fichiers Excel en utilisant des liens externes. Aspose.Cells offre la possibilité de retrouver ces liens externes en utilisant la méthode [**Name.GetReferredAreas**](https://reference.aspose.com/cells/java/com.aspose.cells/name#getReferredAreas-boolean-). La méthode [**Name.GetReferredAreas**](https://reference.aspose.com/cells/java/com.aspose.cells/name#getReferredAreas-boolean-) renvoie un tableau de type [**ReferredArea**](https://reference.aspose.com/cells/java/com.aspose.cells/ReferredArea). La classe [**ReferredArea**](https://reference.aspose.com/cells/java/com.aspose.cells/ReferredArea) fournit une propriété [**ExternalFileName**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#ExternalFileName) qui renvoie le nom du fichier externe. La classe [**ReferredArea**](https://reference.aspose.com/cells/java/com.aspose.cells/ReferredArea) expose les membres suivants.

- [**EndColumn**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#EndColumn): La colonne de fin de la zone
- [**EndRow**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#EndRow): La ligne de fin de la zone
- [**ExternalFileName**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#ExternalFileName): Obtenir le nom du fichier externe s'il s'agit d'une référence externe
- [**IsArea**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#IsArea): Indique s'il s'agit d'une zone
- [**IsExternalLink**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#IsExternalLink): Indique s'il s'agit d'un lien externe
- [**SheetName**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#SheetName): Indique dans quelle feuille cette référence se trouve
- [**StartColumn**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#StartColumn): La colonne de début de la zone
- [**StartRow**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#StartRow): La ligne de début de la zone

Le code d'exemple ci-dessous démontre l'utilisation de la méthode [**Name.GetReferredAreas**](https://reference.aspose.com/cells/java/com.aspose.cells/name#getReferredAreas-boolean-) pour obtenir des plages avec des liens externes.

## **Code d'exemple**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-GetRangeWithExternalLinks-1.java" >}}
{{< app/cells/assistant language="java" >}}
