---
title: Utilisez des parties XML personnalisées dans Aspose.Cells
type: docs
weight: 390
url: /fr/python-net/use-custom-xml-parts-in-aspose-cells/
---

## Utilisation des parties XML personnalisées dans Aspose.Cells pour Python via .NET

Les parties XML personnalisées sont les données XML stockées par différentes applications comme SharePoint etc. à l'intérieur du fichier Excel. Ces données sont consommées par différentes applications qui en ont besoin. Microsoft Excel n'utilise pas ces données, il n'y a donc pas d'interface graphique pour les ajouter. Vous pouvez afficher ces données en changeant l'extension de **.xlsx** en **.zip** puis en l'ouvrant avec **WinZip**. Vous pouvez également ouvrir le fichier ZIP à l'aide de tout utilitaire de compression Windows tiers tel que WinRAR ou WinZip etc. Les données sont présentes à l'intérieur du dossier **customXml**.

Vous pouvez ajouter des parties XML personnalisées à l'aide de Aspose.Cells via la méthode [**Workbook.content_type_properties.add()**](https://reference.aspose.com/cells/python-net/aspose.cells.properties/contenttypepropertycollection/add/#str-str).

Le code d'exemple suivant utilise la méthode [**Workbook.content_type_properties.add()**](https://reference.aspose.com/cells/python-net/aspose.cells.properties/contenttypepropertycollection/add/#str-str) et ajoute le **Catalogue de livres XML** et son nom est **BookStore**. L'image suivante montre le résultat de ce code. Comme vous pouvez le voir, le Catalogue de livres XML est ajouté à l'intérieur du nœud BookStore qui est le nom de cette propriété.

![todo:image_alt_text](use-custom-xml-parts-in-aspose-cells_1.png)

![todo:image_alt_text](use-custom-xml-parts-in-aspose-cells_2.png)

## Code C# pour utiliser des parties XML personnalisées

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Workbook-UsingCustomXmlParts.py" >}}



{{< app/cells/assistant language="python-net" >}}
