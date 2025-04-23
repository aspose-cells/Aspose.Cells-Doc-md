---
title: Obtenir une plage avec des liens externes
type: docs
weight: 120
url: /fr/net/get-range-with-external-links/
---

## **Obtenir une plage avec des liens externes**

Souvent, les fichiers Excel accèdent à des données à partir d'autres fichiers Excel à l'aide de liens externes. Aspose.Cells offre la possibilité de récupérer ces liens externes en utilisant la méthode [**Name.GetReferredAreas**](https://reference.aspose.com/cells/net/aspose.cells/name/methods/getreferredareas). La méthode [**Name.GetReferredAreas**](https://reference.aspose.com/cells/net/aspose.cells/name/methods/getreferredareas) renvoie un tableau de type [**ReferredArea**](https://reference.aspose.com/cells/net/aspose.cells/referredarea). La classe [**ReferredArea**](https://reference.aspose.com/cells/net/aspose.cells/referredarea) fournit une propriété [**ExternalFileName**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/externalfilename) qui renvoie le nom du fichier externe. La classe [**ReferredArea**](https://reference.aspose.com/cells/net/aspose.cells/referredarea) expose les membres suivants.

- [**EndColumn**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/endcolumn): La colonne de fin de la zone
- [**EndRow**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/endrow): La ligne de fin de la zone
- [**ExternalFileName**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/externalfilename): Obtenir le nom du fichier externe s'il s'agit d'une référence externe
- [**IsArea**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/isarea): Indique s'il s'agit d'une zone
- [**IsExternalLink**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/isexternallink): Indique s'il s'agit d'un lien externe
- [**SheetName**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/sheetname): Indique dans quelle feuille cette référence se trouve
- [**StartColumn**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/startcolumn): La colonne de début de la zone
- [**StartRow**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/startrow): La ligne de début de la zone

Le code d'exemple ci-dessous démontre l'utilisation de la méthode [**Name.GetReferredAreas**](https://reference.aspose.com/cells/net/aspose.cells/name/methods/getreferredareas) pour obtenir des plages avec des liens externes.

## **Code d'exemple**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-GetRangeWithExternalLinks-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
