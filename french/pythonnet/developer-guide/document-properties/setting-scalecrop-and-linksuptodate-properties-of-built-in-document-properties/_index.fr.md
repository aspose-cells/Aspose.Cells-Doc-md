---
title: Définir les propriétés ScaleCrop et LinksUpToDate des propriétés de document intégrées.
type: docs
weight: 320
url: /fr/python-net/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/
---

## **Scénarios d'utilisation possibles**
[scale_crop](https://reference.aspose.com/cells/python-net/aspose.cells.properties/builtindocumentpropertycollection/scale_crop) et [links_up_to_date](https://reference.aspose.com/cells/python-net/aspose.cells.properties/builtindocumentpropertycollection/links_up_to_date) sont deux propriétés intégrées étendues définies dans le format OpenXml. Leur but est le suivant
## **1) ScaleCrop**
Cet élément indique le mode d'affichage de la vignette du document. Définissez cet élément sur **TRUE** pour activer le redimensionnement de la vignette du document à l'affichage. Définissez cet élément sur **FALSE** pour activer le rognage de la vignette du document afin de montrer uniquement les sections qui s'adaptent à l'affichage.

Les valeurs possibles pour cet élément sont définies par le type de données booléen du schéma XML W3C.
## **2) LinksUpToDate**
Cet élément indique si les hyperliens dans un document sont à jour. Définissez cet élément sur **TRUE** pour indiquer que les hyperliens sont mis à jour. Définissez cet élément sur **FALSE** pour indiquer que les hyperliens sont obsolètes.

Les valeurs possibles pour cet élément sont définies par le type de données booléen du schéma XML W3C.
## **Capture d'écran montrant ces propriétés dans le fichier app.xml**
![todo:image_alt_text](setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties_1.png)
## **Définition des propriétés ScaleCrop et LinksUpToDate des propriétés de document intégrées.**
Le code d’exemple ci-dessous définit les propriétés intégrées étendues [scale_crop](https://reference.aspose.com/cells/python-net/aspose.cells.properties/builtindocumentpropertycollection/scale_crop) et [links_up_to_date](https://reference.aspose.com/cells/python-net/aspose.cells.properties/builtindocumentpropertycollection/links_up_to_date) du classeur. Veuillez vérifier le [fichier Excel généré](5115500.xlsx) avec ce code, changer son extension en .zip, extraire son contenu et voir le fichier app.xml comme illustré dans la capture d’écran ci-dessus.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Document-Properties-SettingScaleCropAndLinksUpToDateProperties.py" >}}
{{< app/cells/assistant language="python-net" >}}
