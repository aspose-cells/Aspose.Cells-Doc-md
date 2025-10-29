---
title: Ajouter des parties XML personnalisées et les sélectionner par ID
type: docs
weight: 70
url: /fr/python-net/add-custom-xml-parts-and-select-them-by-id/
---

## **Scénarios d'utilisation possibles**

Les parties XML personnalisées sont des données XML stockées à l'intérieur des documents Microsoft Excel et utilisées par les applications qui les traitent. Il n'existe actuellement aucun moyen direct de les ajouter via l'interface utilisateur Microsoft Excel. Cependant, vous pouvez les ajouter de manière programmatique de différentes manières, par exemple en utilisant VSTO, Aspose.Cells, etc. Veuillez utiliser la méthode [**Workbook.custom_xml_parts.add()**](https://reference.aspose.com/cells/python-net/aspose.cells.markup/customxmlpartcollection/add/#bytes-bytes) si vous souhaitez ajouter une partie XML personnalisée en utilisant l'API Aspose.Cells pour Python via .NET. Vous pouvez également définir son ID en utilisant la propriété [**CustomXmlPart.id**](https://reference.aspose.com/cells/python-net/aspose.cells.markup/customxmlpart/id). De même, si vous souhaitez sélectionner une partie XML personnalisée par ID, vous pouvez utiliser la méthode [**Workbook.custom_xml_parts.select_by_id()**](https://reference.aspose.com/cells/python-net/aspose.cells.markup/customxmlpartcollection/select_by_id/#str).

## **Ajouter des parties XML personnalisées et les sélectionner par ID**

Le code d'exemple suivant ajoute d'abord quatre Parties XML personnalisées en utilisant la méthode [**Workbook.custom_xml_parts.add()**](https://reference.aspose.com/cells/python-net/aspose.cells.markup/customxmlpartcollection/add/#bytes-bytes). Ensuite, il définit leurs identifiants à l'aide de la propriété [**CustomXmlPart.id**](https://reference.aspose.com/cells/python-net/aspose.cells.markup/customxmlpart/id). Enfin, il trouve ou sélectionne l'une des Parties XML personnalisées ajoutées en utilisant la méthode [**Workbook.custom_xml_parts.select_by_id()**](https://reference.aspose.com/cells/python-net/aspose.cells.markup/customxmlpartcollection/select_by_id/#str). Veuillez également consulter la sortie console du code donné ci-dessous pour référence.

## **Code d'exemple**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Workbook-AddCustomXMLPartsAndSelectThemByID.py" >}}

## **Sortie console**

{{< highlight java >}}

 Found: CustomXmlPart ID Sport

{{< /highlight >}}

{{< app/cells/assistant language="python-net" >}}
