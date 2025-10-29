---
title: Exporter un style de bordure similaire lorsque le style de bordure n est pas pris en charge par les navigateurs Web avec Golang via C++
linktitle: Exporter un style de bordure similaire lorsque le style de bordure n est pas pris en charge par les navigateurs Web
type: docs
weight: 70
url: /fr/go-cpp/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/
description: Apprenez comment exporter des styles de bordure similaires lorsque non supportés par les navigateurs Web en utilisant Aspose.Cells avec Golang via C++.
---

## **Scénarios d'utilisation possibles**

Microsoft Excel supporte certains types de bordures en pointillés qui ne sont pas supportés par les navigateurs Web. Lors de la conversion d’un tel fichier Excel en HTML avec Aspose.Cells, ces bordures sont supprimées. Cependant, Aspose.Cells peut également supporter l’affichage de telles bordures avec la propriété [**HtmlSaveOptions.GetExportSimilarBorderStyle()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getexportsimilarborderstyle/). Veuillez définir sa valeur sur **true** et les bordures non supportées seront également exportées dans le fichier HTML.

## **Exporter un style de bordure similaire lorsque le style de bordure n'est pas pris en charge par les navigateurs Web**

Le code d’exemple suivant charge le [fichier Excel d'exemple](64716806.xlsx) qui contient certaines bordures non supportées comme illustré dans la capture d’écran suivante. La capture montre également l’effet de la propriété [**HtmlSaveOptions.GetExportSimilarBorderStyle()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getexportsimilarborderstyle/) dans l’[HTML de sortie](64716804.zip).

![todo:image_alt_text](export-similar-border-style-when-border-style-is-not-supported-by-web-browsers_1.png)

## **Code d'exemple**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ExportSimilarBorderStyleWhenBorderStyleIsNotSupportedByWebBrowsers.go" >}}
