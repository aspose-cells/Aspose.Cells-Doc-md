---
title: Obtenir une plage avec des liens externes
type: docs
weight: 60
url: /fr/python-java/get-range-with-external-links/
---

## **Obtenir une plage avec des liens externes**
Il existe de nombreuses instances où les fichiers Excel accèdent à des données provenant d'autres fichiers Excel à l'aide de liens externes. Aspose.Cells pour Python via Java offre la possibilité de récupérer ces liens externes en utilisant la méthode [Name.GetReferredAreas](https://reference.aspose.com/cells/python/asposecells.api/name#getReferredAreas\(boolean\)). La méthode [Name.GetReferredAreas](https://reference.aspose.com/cells/python/asposecells.api/name#getReferredAreas\(boolean\)) retourne un tableau de type [ReferredArea](https://reference.aspose.com/cells/python/asposecells.api/ReferredArea). La classe [ReferredArea](https://reference.aspose.com/cells/python/asposecells.api/ReferredArea) fournit une propriété [ExternalFileName](https://reference.aspose.com/cells/python/asposecells.api/referredarea#ExternalFileName) qui renvoie le nom du fichier externe.

Le code suivant montre comment obtenir des liens externes.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-GetRangeWithExternalLinks.py" >}}
