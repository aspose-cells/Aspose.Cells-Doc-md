---
title: Obtenir la portée avec des liens externes
type: docs
weight: 140
url: /fr/java/get-range-with-external-links/
---
## **Obtenir la portée avec des liens externes**

Souvent, les fichiers Excel accèdent aux données d'autres fichiers Excel à l'aide de liens externes. Aspose.Cells offre la possibilité de récupérer ces liens externes en utilisant le[**Name.GetReferredAreasName.GetReferredAreas**](https://reference.aspose.com/cells/java/com.aspose.cells/name#getReferredAreas(boolean)) méthode. Le[**Name.GetReferredAreasName.GetReferredAreas**](https://reference.aspose.com/cells/java/com.aspose.cells/name#getReferredAreas(boolean)) renvoie un tableau de type[**ZoneRéférencée**](https://reference.aspose.com/cells/java/com.aspose.cells/ReferredArea). Le[**ZoneRéférencée**](https://reference.aspose.com/cells/java/com.aspose.cells/ReferredArea)classe offre une[**NomFichierExterne**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#ExternalFileName)propriété qui renvoie le nom du fichier externe. Le[**ZoneRéférencée**](https://reference.aspose.com/cells/java/com.aspose.cells/ReferredArea)classe expose les membres suivants.

- [**FinColonne**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#EndColumn): La colonne de fin de la zone
- [**EndRow**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#EndRow): La ligne de fin de la zone
- [**NomFichierExterne**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#ExternalFileName): Récupère le nom du fichier externe s'il s'agit d'une référence externe
- [**EstZone**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#IsArea): Indique s'il s'agit d'une zone
- [**EstLienExterne**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#IsExternalLink): Indique s'il s'agit d'un lien externe
- [**NomFeuille**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#SheetName): Indique dans quelle feuille se trouve cette référence
- [**StartColumn**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#StartColumn): La colonne de début de la zone
- [**StartRow**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#StartRow): La ligne de départ de la zone

L'exemple de code ci-dessous illustre l'utilisation de[**Name.GetReferredAreasName.GetReferredAreas**](https://reference.aspose.com/cells/java/com.aspose.cells/name#getReferredAreas(boolean)) méthode pour obtenir des plages avec des liens externes.

## **Exemple de code**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-GetRangeWithExternalLinks-1.java" >}}
