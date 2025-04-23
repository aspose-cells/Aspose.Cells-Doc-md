---
title: Définir les propriétés ScaleCrop et LinksUpToDate des propriétés de document intégrées.
type: docs
weight: 1050
url: /fr/java/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/
---

## **Scénarios d'utilisation possibles**
[ScaleCrop](https://reference.aspose.com/cells/java/com.aspose.cells/builtindocumentpropertycollection#ScaleCrop) et [LinksUpToDate](https://reference.aspose.com/cells/java/com.aspose.cells/builtindocumentpropertycollection#LinksUpToDate) sont deux propriétés de document intégrées étendues définies dans le format OpenXml. Le but de ces propriétés est le suivant
## **1) ScaleCrop**
Cet élément indique le mode d'affichage de la vignette du document. Réglez cet élément sur **true** pour activer le redimensionnement de la vignette du document à l'affichage. Réglez cet élément sur **false** pour activer le rognage de la vignette du document pour afficher uniquement les sections qui s'adaptent à l'affichage.

Les valeurs possibles pour cet élément sont définies par le type de données booléen du schéma XML W3C.
## **2) LinksUpToDate**
Cet élément indique si les hyperliens dans un document sont à jour. Réglez cet élément sur **true** pour indiquer que les hyperliens sont mis à jour. Réglez cet élément sur **false** pour indiquer que les hyperliens sont obsolètes.

Les valeurs possibles pour cet élément sont définies par le type de données booléen du schéma XML W3C.
## **Capture d'écran montrant ces propriétés dans le fichier app.xml**
![todo:image_alt_text](setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties_1.png)
## **Définition des propriétés ScaleCrop et LinksUpToDate des propriétés de document intégrées.**
Le code d'exemple suivant définit les propriétés de document incorporées étendues [ScaleCrop] (https://reference.aspose.com/cells/java/com.aspose.cells/builtindocumentpropertycollection#ScaleCrop) and [LinksUpToDate] (https://reference.aspose.com/cells/java/com.aspose.cells/builtindocumentpropertycollection#LinksUpToDate) du classeur. Veuillez vérifier le [fichier Excel de sortie](5472494.xlsx) généré avec ce code, changer son extension en .zip, extraire son contenu et afficher aap.xml comme indiqué dans la capture d'écran ci-dessus.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SettingScaleCropLinksUpToDate-SettingScaleCropLinksUpToDate.java" >}}
{{< app/cells/assistant language="java" >}}
