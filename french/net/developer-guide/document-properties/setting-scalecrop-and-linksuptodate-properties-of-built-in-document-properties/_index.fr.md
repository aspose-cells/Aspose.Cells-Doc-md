---
title: Définir les propriétés ScaleCrop et LinksUpToDate des propriétés de document intégrées.
type: docs
weight: 320
url: /fr/net/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/
---

## **Scénarios d'utilisation possibles**
[ScaleCrop](https://reference.aspose.com/cells/net/aspose.cells.properties/builtindocumentpropertycollection/properties/scalecrop) et [LinksUpToDate](https://reference.aspose.com/cells/net/aspose.cells.properties/builtindocumentpropertycollection/properties/linksuptodate) sont deux propriétés de document intégrées étendues définies dans le format OpenXml. Le but de ces propriétés est le suivant
## **1) ScaleCrop**
Cet élément indique le mode d'affichage de la vignette du document. Définissez cet élément sur **TRUE** pour activer le redimensionnement de la vignette du document à l'affichage. Définissez cet élément sur **FALSE** pour activer le rognage de la vignette du document afin de montrer uniquement les sections qui s'adaptent à l'affichage.

Les valeurs possibles pour cet élément sont définies par le type de données booléen du schéma XML W3C.
## **2) LinksUpToDate**
Cet élément indique si les hyperliens dans un document sont à jour. Définissez cet élément sur **TRUE** pour indiquer que les hyperliens sont mis à jour. Définissez cet élément sur **FALSE** pour indiquer que les hyperliens sont obsolètes.

Les valeurs possibles pour cet élément sont définies par le type de données booléen du schéma XML W3C.
## **Capture d'écran montrant ces propriétés dans le fichier app.xml**
![todo:image_alt_text](setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties_1.png)
## **Définition des propriétés ScaleCrop et LinksUpToDate des propriétés de document intégrées.**
Le code d'exemple suivant définit les propriétés de document intégrées étendues [ScaleCrop](https://reference.aspose.com/cells/net/aspose.cells.properties/builtindocumentpropertycollection/properties/scalecrop) et [LinksUpToDate](https://reference.aspose.com/cells/net/aspose.cells.properties/builtindocumentpropertycollection/properties/linksuptodate) du classeur. Veuillez vérifier le [fichier Excel de sortie](5115500.xlsx) généré avec ce code, changer son extension en .zip et extraire son contenu et voir le app.xml comme indiqué dans la capture d'écran ci-dessus.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-SettingScaleCropAndLinksUpToDateProperties.cs" >}}
