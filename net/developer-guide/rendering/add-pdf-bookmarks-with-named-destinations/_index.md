---
title: Add PDF Bookmarks with Named Destinations
type: docs
weight: 20
url: /net/add-pdf-bookmarks-with-named-destinations/
---

## **Possible Usage Scenarios**

Named Destinations are special kinds of bookmarks or links in PDF that do not depend on PDF pages. It means, if pages are added or deleted from PDF, bookmarks may become invalid but named destinations will remain intact. To create Named Destination, please set the [**PdfBookmarkEntry.DestinationName**](https://apireference.aspose.com/cells/net/aspose.cells.rendering/pdfbookmarkentry/properties/destinationname) property.

## **Add PDF Bookmarks with Named Destinations**

Please see the following sample code, its [source Excel file](50528348.xlsx), and its [output PDF file](50528349.pdf). The screenshot shows the bookmarks and named destinations inside the output PDF. The screenshot also describes how to view Named Destinations and that you need Professional version of Acrobat Reader.

![todo:image_alt_text](add-pdf-bookmarks-with-named-destinations_1.png)

## **Sample Code**

{{< gist "aspose-com-gists" "24a8eac23c3325e20dababecf735a43b" "Examples-CSharp-Rendering-AddPDFBookmarksWithNamedDestinations.cs" >}}
