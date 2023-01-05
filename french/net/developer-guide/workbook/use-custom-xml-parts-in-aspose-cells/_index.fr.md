---
title: Utiliser des parties XML personnalisées dans Aspose.Cells
type: docs
weight: 390
url: /fr/net/use-custom-xml-parts-in-aspose-cells/
---
## Utilisation de parties XML personnalisées dans Aspose.Cells

Les parties XML personnalisées sont les données XML stockées par différentes applications telles que SharePoint, etc. dans le fichier Excel. Ces données sont consommées par différentes applications qui en ont besoin. Microsoft Excel n'utilise pas ces données, il n'y a donc pas d'interface graphique pour les ajouter. Vous pouvez afficher ces données en modifiant l'extension de**.xlsx** dans**.Zip *: français** puis en l'ouvrant avec**WinZipName** . Vous pouvez également ouvrir le fichier ZIP à l'aide de n'importe quel utilitaire zip 3ème partie Windows tel que WinRAR ou WinZip, etc. Les données sont présentes à l'intérieur du**customXml** dossier.

 Vous pouvez ajouter des parties XML personnalisées en utilisant Aspose.Cells via le[**Classeur.ContentTypeProperties.Add()**](https://reference.aspose.com/cells/net/aspose.cells.properties/contenttypepropertycollection/methods/add/index)méthode.

 L'exemple de code suivant utilise[**Classeur.ContentTypeProperties.Add()**](https://reference.aspose.com/cells/net/aspose.cells.properties/contenttypepropertycollection/methods/add/index) méthode et ajoute la**Catalogue de livres XML** et son nom est**Librairie**. L'image suivante montre le résultat de ce code. Comme vous pouvez le voir, le XML du catalogue de livres est ajouté à l'intérieur du nœud BookStore qui est le nom de cette propriété.

![tâche : image_autre_texte](use-custom-xml-parts-in-aspose-cells_1.png)

![tâche : image_autre_texte](use-custom-xml-parts-in-aspose-cells_2.png)

## Code C# pour utiliser des parties XML personnalisées

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingCustomXmlParts-UsingCustomXmlParts.cs" >}}

## Article associé

- [Ajout de propriétés personnalisées visibles dans le panneau Informations sur le document](/cells/fr/net/adding-custom-properties-visible-inside-document-information-panel/)
