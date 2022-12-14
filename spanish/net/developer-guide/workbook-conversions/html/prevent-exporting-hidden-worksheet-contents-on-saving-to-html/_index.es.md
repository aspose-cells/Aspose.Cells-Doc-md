---
title: Impedir la exportación de contenido oculto de la hoja de cálculo al guardar en HTML
type: docs
weight: 210
url: /es/net/prevent-exporting-hidden-worksheet-contents-on-saving-to/
---
{{% alert color="primary" %}}

Puede guardar libros de Excel en HTML. Sin embargo, si el libro de trabajo contiene hojas de trabajo ocultas, Aspose.Cells exporta de manera predeterminada el contenido de la hoja de trabajo oculta a la salida HTML (_ files) que contiene archivos como hojas de trabajo, imágenes, tabstrip.htm, stylesheet.css, etc. A veces, exportar el contenido de las hojas de trabajo ocultas de esta manera no es apropiado. Por ejemplo, si la hoja de cálculo oculta contiene imágenes que no deben exportarse a la_directorio de archivos.

{{% /alert %}}

 Aspose.Cells proporciona el[**HtmlSaveOptions.ExportHiddenWorksheet**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exporthiddenworksheet) propiedad. De forma predeterminada, está configurado para**verdadero** y las hojas de trabajo ocultas se exportan a HTML. si lo configuras**falso**, Aspose.Cells no exportará el contenido oculto de la hoja de trabajo.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-PreventExportingHiddenContent-PreventExportingHiddenContentWhileSavingAsHTML.cs" >}}

