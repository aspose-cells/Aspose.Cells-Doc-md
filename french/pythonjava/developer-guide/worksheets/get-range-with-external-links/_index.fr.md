---
title: Obtenir la portée avec des liens externes
type: docs
weight: 60
url: /fr/python-java/get-range-with-external-links/
---
## **Obtenir la portée avec des liens externes**
Il existe de nombreux cas où les fichiers Excel accèdent aux données d'autres fichiers Excel en utilisant des liens externes. Aspose.Cells for Python via Java offre la possibilité de récupérer ces liens externes en utilisant le[Name.GetReferredAreasName.GetReferredAreas](https://reference.aspose.com/cells/python/asposecells.api/name#getReferredAreas\(boolean\)) méthode. Le[Name.GetReferredAreasName.GetReferredAreas](https://reference.aspose.com/cells/python/asposecells.api/name#getReferredAreas\(boolean\)) renvoie un tableau de type[ZoneRéférencée](https://reference.aspose.com/cells/python/asposecells.api/ReferredArea). Le[ZoneRéférencée](https://reference.aspose.com/cells/python/asposecells.api/ReferredArea)classe offre une[NomFichierExterne](https://reference.aspose.com/cells/python/asposecells.api/referredarea#ExternalFileName)propriété qui renvoie le nom du fichier externe.

L'extrait de code suivant montre comment obtenir des liens externes.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-GetRangeWithExternalLinks.py" >}}
