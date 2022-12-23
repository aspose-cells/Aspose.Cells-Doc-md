---
title: Obtenir la portée avec des liens externes
type: docs
weight: 120
url: /fr/net/get-range-with-external-links/
---
## **Obtenir la portée avec des liens externes**

Souvent, les fichiers Excel accèdent aux données d'autres fichiers Excel à l'aide de liens externes. Aspose.Cells offre la possibilité de récupérer ces liens externes en utilisant le[**Name.GetReferredAreasName.GetReferredAreas**](https://reference.aspose.com/cells/net/aspose.cells/name/methods/getreferredareas)méthode. Le[**Name.GetReferredAreasName.GetReferredAreas**](https://reference.aspose.com/cells/net/aspose.cells/name/methods/getreferredareas)la méthode renvoie un tableau de type[**ZoneRéférencée**](https://reference.aspose.com/cells/net/aspose.cells/referredarea). Le[**ZoneRéférencée**](https://reference.aspose.com/cells/net/aspose.cells/referredarea) classe offre une[**NomFichierExterne**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/externalfilename)propriété qui renvoie le nom du fichier externe. Le[**ZoneRéférencée**](https://reference.aspose.com/cells/net/aspose.cells/referredarea)classe expose les membres suivants.

- [**FinColonne**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/endcolumn): La colonne de fin de la zone
- [**EndRow**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/endrow): La ligne de fin de la zone
- [**NomFichierExterne**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/externalfilename): Récupère le nom du fichier externe s'il s'agit d'une référence externe
- [**EstZone**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/isarea): Indique s'il s'agit d'une zone
- [**EstLienExterne**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/isexternallink): Indique s'il s'agit d'un lien externe
- [**NomFeuille**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/sheetname): Indique dans quelle feuille se trouve cette référence
- [**StartColumn**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/startcolumn): La colonne de début de la zone
- [**StartRow**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/startrow): La ligne de départ de la zone

 L'exemple de code ci-dessous illustre l'utilisation de[**Name.GetReferredAreasName.GetReferredAreas**](https://reference.aspose.com/cells/net/aspose.cells/name/methods/getreferredareas)méthode pour obtenir des plages avec des liens externes.

## **Exemple de code**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-GetRangeWithExternalLinks-1.cs" >}}
