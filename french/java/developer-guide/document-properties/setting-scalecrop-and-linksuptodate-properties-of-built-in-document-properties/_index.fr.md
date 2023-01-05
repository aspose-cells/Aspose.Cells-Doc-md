---
title: Définition des propriétés ScaleCrop et LinksUpToDate des propriétés de document intégrées
type: docs
weight: 1050
url: /fr/java/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/
---
## **Scénarios d'utilisation possibles**
[ScaleCrop](https://reference.aspose.com/cells/java/com.aspose.cells/builtindocumentpropertycollection#ScaleCrop) et[Liens à jour](https://reference.aspose.com/cells/java/com.aspose.cells/builtindocumentpropertycollection#LinksUpToDate)sont deux propriétés de document intégrées étendues définies dans le format OpenXml. Le but de ces propriétés est de suivre
## **1) Mise à l'échelle**
 Cet élément indique le mode d'affichage de la vignette du document. Définissez cet élément sur**vrai** pour activer la mise à l'échelle de la vignette du document à l'écran. Définissez cet élément sur**faux** pour activer le recadrage de la vignette du document afin d'afficher uniquement les sections qui correspondent à l'affichage.

Les valeurs possibles pour cet élément sont définies par le type de données booléen W3C XML Schema.
## **2) Liens à jour**
 Cet élément indique si les hyperliens d'un document sont à jour. Définissez cet élément sur**vrai** pour indiquer que les hyperliens sont mis à jour. Définissez cet élément sur**faux**pour indiquer que les hyperliens sont obsolètes.

Les valeurs possibles pour cet élément sont définies par le type de données booléen W3C XML Schema.
## **Capture d'écran montrant ces propriétés dans le fichier app.xml**
![tâche : image_autre_texte](setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties_1.png)
## **Définition des propriétés ScaleCrop et LinksUpToDate des propriétés de document intégrées**
 L'exemple de code suivant définit le[ScaleCrop](https://reference.aspose.com/cells/java/com.aspose.cells/builtindocumentpropertycollection#ScaleCrop)et[Liens à jour](https://reference.aspose.com/cells/java/com.aspose.cells/builtindocumentpropertycollection#LinksUpToDate) propriétés de document intégrées étendues du classeur. S'il vous plaît, vérifiez le[fichier excel de sortie](5472494.xlsx)généré avec ce code, changez son extension en .zip et extrayez son contenu et affichez le aap.xml comme indiqué dans la capture d'écran ci-dessus.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SettingScaleCropLinksUpToDate-SettingScaleCropLinksUpToDate.java" >}}
