---
title: Ajouter des signets PDF avec des destinations nommées
type: docs
weight: 20
url: /fr/net/add-pdf-bookmarks-with-named-destinations/
---
## **Scénarios d'utilisation possibles**

Les destinations nommées sont des types spéciaux de signets ou de liens dans PDF qui ne dépendent pas des pages PDF. Cela signifie que si des pages sont ajoutées ou supprimées du PDF, les signets peuvent devenir invalides mais les destinations nommées resteront intactes. Pour créer une destination nommée, veuillez définir le[**PdfBookmarkEntry.DestinationName**](https://reference.aspose.com/cells/net/aspose.cells.rendering/pdfbookmarkentry/properties/destinationname)propriété.

## **Ajouter des signets PDF avec des destinations nommées**

 Veuillez consulter l'exemple de code suivant, son[fichier Excel source](50528348.xlsx) , et son[fichier PDF de sortie](50528349.pdf). La capture d'écran montre les signets et les destinations nommées dans le PDF de sortie. La capture d'écran décrit également comment afficher les destinations nommées et indique que vous avez besoin de la version professionnelle d'Acrobat Reader.

![tâche : image_autre_texte](add-pdf-bookmarks-with-named-destinations_1.png)

## **Exemple de code**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Rendering-AddPDFBookmarksWithNamedDestinations.cs" >}}
