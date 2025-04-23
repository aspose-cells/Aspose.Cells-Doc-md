---
title: Agregar marcadores PDF con Destinos Nominados
type: docs
weight: 20
url: /es/java/add-pdf-bookmarks-with-named-destinations/
---

## **Escenarios de uso posibles**

Los Destinos Nominados son un tipo especial de marcadores o enlaces en PDF que no dependen de las páginas PDF. Esto significa que si se añaden o eliminan páginas del PDF, los marcadores pueden volverse inválidos pero los destinos nominados permanecerán intactos. Para crear un Destino Nombrado, por favor establece la propiedad [**PdfBookmarkEntry.DestinationName**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfbookmarkentry#DestinationName).

## **Agregar Marcadores de PDF con Destinos Nombrados**

Consulte el siguiente código de muestra, su [archivo Excel fuente](50528370.xlsx) y su [archivo PDF de salida](50528369.pdf). La captura de pantalla muestra los marcadores y destinos nombrados dentro del PDF de salida. La captura de pantalla también describe cómo ver los Destinos Nombrados y que se necesita la versión Profesional de Acrobat Reader.

![todo:image_alt_text](add-pdf-bookmarks-with-named-destinations_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Rendering-AddPDFBookmarksWithNamedDestinations.java" >}}
{{< app/cells/assistant language="java" >}}
