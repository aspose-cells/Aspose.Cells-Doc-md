---
title: Evitar exportar contenidos de hojas de trabajo ocultas al guardar en HTML con Golang a través de C++
linktitle: Prevenir la exportación de contenido oculto de la hoja de trabajo
type: docs
weight: 210
url: /es/go-cpp/prevent-exporting-hidden-worksheet-contents-on-saving-to/
description: Aprende cómo prevenir la exportación de contenido oculto de la hoja de trabajo al guardar libros de trabajo de Excel en HTML usando Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Puede guardar libros de Excel en HTML. Sin embargo, si el libro contiene hojas de cálculo ocultas, por defecto Aspose.Cells exporta los contenidos ocultos de la hoja de cálculo al directorio de salida HTML (_files) que contiene archivos como hojas de cálculo, imágenes, tabstrip.htm, stylesheet.css, etc. A veces, exportar el contenido de las hojas de cálculo ocultas de esta manera no es apropiado. Por ejemplo, si la hoja de cálculo oculta contiene imágenes que no deben ser exportadas al directorio _files.

{{% /alert %}}

Aspose.Cells proporciona la propiedad [**HtmlSaveOptions.GetExportHiddenWorksheet()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getexporthiddenworksheet/). De forma predeterminada, está configurada en **true** y se exportan las hojas de cálculo ocultas a HTML. Si la establece en **false**, Aspose.Cells no exportará los contenidos de la hoja de cálculo oculta.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-PreventExportingHiddenWorksheetContentsOnSavingToHtml.go" >}}
