---
title: Exportar estilos de borde similares cuando el estilo de borde no sea compatible con los navegadores web con Golang a través de C++
linktitle: Exportar un Estilo de Borde Similar cuando el Estilo de Borde no es compatible con los Navegadores Web
type: docs
weight: 70
url: /es/go-cpp/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/
description: Aprende cómo exportar estilos de borde similares cuando no sean soportados por navegadores web usando Aspose.Cells con Golang a través de C++.
---

## **Escenarios de uso posibles**

Microsoft Excel soporta algunos tipos de bordes discontinuos que no son compatibles con navegadores web. Cuando conviertes dicho archivo de Excel en HTML usando Aspose.Cells, dichos bordes se eliminan. Sin embargo, Aspose.Cells también puede soportar mostrar estos bordes usando la propiedad [**HtmlSaveOptions.GetExportSimilarBorderStyle()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getexportsimilarborderstyle/). Configure su valor en **true** y los bordes no soportados también se exportarán en el archivo HTML.

## **Exportar un estilo de borde similar cuando el estilo de borde no es soportado por los navegadores web**

El siguiente código de ejemplo carga el [archivo de Excel de muestra](64716806.xlsx) que contiene algunos bordes no soportados, como se muestra en la siguiente captura de pantalla. La captura ilustra además el efecto de la propiedad [**HtmlSaveOptions.GetExportSimilarBorderStyle()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getexportsimilarborderstyle/) en el [HTML de salida](64716804.zip).

![todo:image_alt_text](export-similar-border-style-when-border-style-is-not-supported-by-web-browsers_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ExportSimilarBorderStyleWhenBorderStyleIsNotSupportedByWebBrowsers.go" >}}
