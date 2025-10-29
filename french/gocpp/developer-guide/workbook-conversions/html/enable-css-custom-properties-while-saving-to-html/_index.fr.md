---
title: Activer les propriétés personnalisées CSS lors de l enregistrement en HTML avec Golang via C++
linktitle: Activer les propriétés CSS personnalisées lors de l enregistrement en HTML
type: docs
weight: 320
url: /fr/go-cpp/enable-css-custom-properties-while-saving-to-html/
description: Découvrez comment activer les propriétés CSS personnalisées lors de l enregistrement des fichiers Excel en HTML en utilisant Aspose.Cells for C++. Améliorez la performance en réduisant les données d image redondantes.
---

## **Scénarios d'utilisation possibles**

Lorsque vous enregistrez votre fichier Excel en HTML, dans le scénario où il y a plusieurs occurrences d'une même image en base64, avec la propriété personnalisée, les données de l'image n'ont besoin d'être sauvegardées qu'une seule fois, ce qui peut améliorer la performance de l'HTML résultant. Veuillez utiliser la propriété [**HtmlSaveOptions.GetEnableCssCustomProperties()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getenablecsscustomproperties/) et la définir à **true** lors de l'enregistrement en HTML.

![todo:image_alt_text](enable-css-custom-properties-while-saving-to-html-1.jpg)

## **Activer les propriétés personnalisées CSS lors de l'enregistrement en HTML**

Le code d'exemple ci-dessous montre l'utilisation de la propriété [**HtmlSaveOptions.GetEnableCssCustomProperties()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getenablecsscustomproperties/). La capture d'écran montre l'effet de cette propriété lorsqu'elle n'est pas définie à **true**. Veuillez télécharger le [fichier Excel d'exemple](50528260.xlsx) utilisé dans ce code et le [HTML généré](50528261.zip) pour référence.

## **Code d'exemple**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-EnableCssCustomPropertiesWhileSavingToHtml.go" >}}
