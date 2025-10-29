---
title: Définir les propriétés ScaleCrop et LinksUpToDate des propriétés de document intégrées avec Golang via C++
linktitle: Définir les propriétés ScaleCrop et LinksUpToDate
type: docs
weight: 320
url: /fr/go-cpp/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/
description: Apprenez comment définir les propriétés ScaleCrop et LinksUpToDate des propriétés de document intégrées en utilisant Aspose.Cells for C++.
---

## **Scénarios d'utilisation possibles**
[GetScaleCrop()](https://reference.aspose.com/cells/go-cpp/builtindocumentpropertycollection/getscalecrop/) et [GetLinksUpToDate()](https://reference.aspose.com/cells/cpp/aspose.cells.properties/builtindocumentpropertycollection/getlinksuptodate/) sont deux propriétés étendues intégrées dans le format OpenXml. Leur but est le suivant :

## **1) ScaleCrop**
Cet élément indique le mode d'affichage de la vignette du document. Définissez cet élément sur **TRUE** pour activer le redimensionnement de la vignette du document à l'affichage. Définissez cet élément sur **FALSE** pour activer le rognage de la vignette du document afin de montrer uniquement les sections qui s'adaptent à l'affichage.

Les valeurs possibles pour cet élément sont définies par le type de données booléen du schéma XML W3C.

## **2) LinksUpToDate**
Cet élément indique si les hyperliens dans un document sont à jour. Définissez cet élément sur **TRUE** pour indiquer que les hyperliens sont mis à jour. Définissez cet élément sur **FALSE** pour indiquer que les hyperliens sont obsolètes.

Les valeurs possibles pour cet élément sont définies par le type de données booléen du schéma XML W3C.

## **Capture d'écran montrant ces propriétés dans le fichier app.xml**
![todo:image_alt_text](setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties_1.png)

## **Définir les propriétés ScaleCrop et LinksUpToDate des propriétés de document intégrées**
 Le code d'exemple suivant définit les propriétés intégrées étendues [GetScaleCrop()](https://reference.aspose.com/cells/go-cpp/builtindocumentpropertycollection/getscalecrop/) et [GetLinksUpToDate()](https://reference.aspose.com/cells/cpp/aspose.cells.properties/builtindocumentpropertycollection/getlinksuptodate/) du classeur. Veuillez vérifier le fichier excel de sortie (5115500.xlsx) généré avec ce code, changer son extension en .zip, extraire son contenu et consulter le fichier app.xml comme montré dans la capture d'écran ci-dessus.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SettingScalecropAndLinksuptodatePropertiesOfBuiltInDocumentProperties.go" >}}
