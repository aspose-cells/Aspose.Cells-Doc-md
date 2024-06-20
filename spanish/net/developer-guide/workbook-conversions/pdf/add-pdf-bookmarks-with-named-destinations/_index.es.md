---
title: Agregar marcadores PDF con Destinos Nominados
type: docs
weight: 20
url: /es/net/add-pdf-bookmarks-with-named-destinations/
---

## **Escenarios de uso posibles**

Los Destinos Nominados son un tipo especial de marcadores o enlaces en PDF que no dependen de las páginas PDF. Esto significa que si se añaden o eliminan páginas del PDF, los marcadores pueden volverse inválidos pero los destinos nominados permanecerán intactos. Para crear un Destino Nombrado, por favor establece la propiedad [**PdfBookmarkEntry.DestinationName**](https://reference.aspose.com/cells/net/aspose.cells.rendering/pdfbookmarkentry/properties/destinationname).

## **Agregar Marcadores de PDF con Destinos Nombrados**

Por favor ve el siguiente código de ejemplo, su [archivo de Excel fuente](50528348.xlsx), y su [archivo PDF de salida](50528349.pdf). La captura de pantalla muestra los marcadores y destinos nominados dentro del PDF de salida. La captura de pantalla también describe cómo ver los Destinos Nominados y que necesitas la versión Profesional de Acrobat Reader.

![todo:image_alt_text](add-pdf-bookmarks-with-named-destinations_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Rendering-AddPDFBookmarksWithNamedDestinations.cs" >}}
