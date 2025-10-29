---
title: Obtenir une plage avec des liens externes
type: docs
weight: 120
url: /fr/python-net/get-range-with-external-links/
description: Cet article montre comment obtenir une plage avec des liens externes avec Aspose.Cells pour l API Python via .NET.
keywords: Bibliothèque Excel Python, Obtenez une plage avec des liens externes en Python.
---

## **Obtenir une plage avec des liens externes**

Souvent, les fichiers Excel accèdent à des données d'autres fichiers Excel en utilisant des liens externes. Aspose.Cells pour Python via .NET offre la possibilité de récupérer ces liens externes en utilisant la méthode [**Name.get_referred_areas**](https://reference.aspose.com/cells/python-net/aspose.cells/name/get_referred_areas/#bool). La méthode [**Name.get_referred_areas**](https://reference.aspose.com/cells/python-net/aspose.cells/name/get_referred_areas/#bool) renvoie un tableau de type [**ReferredArea**](https://reference.aspose.com/cells/python-net/aspose.cells/referredarea). La classe [**ReferredArea**](https://reference.aspose.com/cells/python-net/aspose.cells/referredarea) fournit une propriété [**external_file_name**](https://reference.aspose.com/cells/python-net/aspose.cells/referredarea/external_file_name/) qui renvoie le nom du fichier externe. La classe [**ReferredArea**](https://reference.aspose.com/cells/python-net/aspose.cells/referredarea) expose les membres suivants.

- [**end_column**](https://reference.aspose.com/cells/python-net/aspose.cells/referredarea/end_column/): La colonne de fin de la zone
- [**end_row**](https://reference.aspose.com/cells/python-net/aspose.cells/referredarea/end_row/): La ligne de fin de la zone
- [**external_file_name**](https://reference.aspose.com/cells/python-net/aspose.cells/referredarea/external_file_name/): Obtenir le nom du fichier externe s'il s'agit d'une référence externe
- [**is_area**](https://reference.aspose.com/cells/python-net/aspose.cells/referredarea/is_area/): Indique s'il s'agit d'une zone
- [**is_external_link**](https://reference.aspose.com/cells/python-net/aspose.cells/referredarea/is_external_link/): Indique s'il s'agit d'un lien externe
- [**sheet_name**](https://reference.aspose.com/cells/python-net/aspose.cells/referredarea/sheet_name/): Indique dans quelle feuille cette référence se trouve
- [**start_column**](https://reference.aspose.com/cells/python-net/aspose.cells/referredarea/start_column): La colonne de début de la zone
- [**start_row**](https://reference.aspose.com/cells/python-net/aspose.cells/referredarea/start_row): La ligne de début de la zone

Le code d'exemple ci-dessous démontre l'utilisation de la méthode [**Name.get_referred_areas**](https://reference.aspose.com/cells/python-net/aspose.cells/name/get_referred_areas/#bool) pour obtenir des plages avec des liens externes.

## **Code d'exemple**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-Worksheets-GetRangeWithExternalLinks-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
