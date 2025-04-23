---
title: Utilisez des parties XML personnalisées dans Aspose.Cells
type: docs
weight: 390
url: /fr/net/use-custom-xml-parts-in-aspose-cells/
---

## Utilisation de parties XML personnalisées dans Aspose.Cells

Les parties XML personnalisées sont les données XML stockées par différentes applications comme SharePoint etc. à l'intérieur du fichier Excel. Ces données sont consommées par différentes applications qui en ont besoin. Microsoft Excel n'utilise pas ces données, il n'y a donc pas d'interface graphique pour les ajouter. Vous pouvez afficher ces données en changeant l'extension de **.xlsx** en **.zip** puis en l'ouvrant avec **WinZip**. Vous pouvez également ouvrir le fichier ZIP à l'aide de tout utilitaire de compression Windows tiers tel que WinRAR ou WinZip etc. Les données sont présentes à l'intérieur du dossier **customXml**.

Vous pouvez ajouter des parties XML personnalisées à l'aide de Aspose.Cells via la méthode [**Workbook.ContentTypeProperties.Add()**](https://reference.aspose.com/cells/net/aspose.cells.properties/contenttypepropertycollection/methods/add/index).

Le code d'exemple suivant utilise la méthode [**Workbook.ContentTypeProperties.Add()**](https://reference.aspose.com/cells/net/aspose.cells.properties/contenttypepropertycollection/methods/add/index) et ajoute le **Catalogue de livres XML** et son nom est **BookStore**. L'image suivante montre le résultat de ce code. Comme vous pouvez le voir, le Catalogue de livres XML est ajouté à l'intérieur du nœud BookStore qui est le nom de cette propriété.

![todo:image_alt_text](use-custom-xml-parts-in-aspose-cells_1.png)

![todo:image_alt_text](use-custom-xml-parts-in-aspose-cells_2.png)

## Code C# pour utiliser des parties XML personnalisées

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingCustomXmlParts-UsingCustomXmlParts.cs" >}}

## Article connexe

- [Ajout de propriétés personnalisées visibles dans le volet Informations sur le document](/cells/fr/net/adding-custom-properties-visible-inside-document-information-panel/)
{{< app/cells/assistant language="csharp" >}}
