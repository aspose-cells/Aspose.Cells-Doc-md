---
title: Ajouter des signets PDF avec des destinations nommées
type: docs
weight: 20
url: /fr/java/add-pdf-bookmarks-with-named-destinations/
---

## **Scénarios d'utilisation possibles**

Les destinations nommées sont des sortes spéciales de signets ou de liens dans les PDF qui ne dépendent pas des pages PDF. Cela signifie que si des pages sont ajoutées ou supprimées du PDF, les signets peuvent devenir invalides mais les destinations nommées resteront intacts. Pour créer une destination nommée, veuillez définir la propriété [**PdfBookmarkEntry.DestinationName**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfbookmarkentry#DestinationName).

## **Ajouter des signets PDF avec des destinations nommées**

Veuillez consulter le code d'exemple suivant, son fichier Excel source (50528370.xlsx) et son fichier PDF de sortie (50528369.pdf). La capture d'écran montre les signets et les destinations nommées à l'intérieur du PDF de sortie. La capture d'écran décrit également comment afficher les destinations nommées et que vous avez besoin de la version Professionnelle d'Acrobat Reader.

![todo:image_alt_text](add-pdf-bookmarks-with-named-destinations_1.png)

## **Code d'exemple**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Rendering-AddPDFBookmarksWithNamedDestinations.java" >}}
{{< app/cells/assistant language="java" >}}
