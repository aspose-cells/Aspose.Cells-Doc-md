---
title: Evitar la exportación de contenidos ocultos de la hoja de cálculo al guardar en HTML
type: docs
weight: 210
url: /es/net/prevent-exporting-hidden-worksheet-contents-on-saving-to/
---

{{% alert color="primary" %}}

Puede guardar libros de Excel en HTML. Sin embargo, si el libro contiene hojas de cálculo ocultas, por defecto Aspose.Cells exporta los contenidos ocultos de la hoja de cálculo al directorio de salida HTML (_files) que contiene archivos como hojas de cálculo, imágenes, tabstrip.htm, stylesheet.css, etc. A veces, exportar el contenido de las hojas de cálculo ocultas de esta manera no es apropiado. Por ejemplo, si la hoja de cálculo oculta contiene imágenes que no deben ser exportadas al directorio _files.

{{% /alert %}}

Aspose.Cells proporciona la propiedad [**HtmlSaveOptions.ExportHiddenWorksheet**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exporthiddenworksheet). De forma predeterminada, está configurada en **true** y se exportan las hojas de cálculo ocultas a HTML. Si la establece en **false**, Aspose.Cells no exportará los contenidos de la hoja de cálculo oculta.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-PreventExportingHiddenContent-PreventExportingHiddenContentWhileSavingAsHTML.cs" >}}

{{< app/cells/assistant language="csharp" >}}
