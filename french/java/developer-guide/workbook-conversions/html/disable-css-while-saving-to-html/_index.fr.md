---
title: Désactiver le CSS lors de l enregistrement en HTML
type: docs
weight: 320
url: /fr/java/disable-css-while-saving-to-html/
---

## **Scénarios d'utilisation possibles**

Lorsque vous enregistrez votre fichier Excel en HTML sur une seule page, généralement les éléments CSS seront intégrés dans le fichier HTML et situés dans la section HEAD. Si vous attachez ce fichier en tant que contenu/corps d’un email, les éléments CSS seront supprimés par la plupart des clients email, ce qui entraîne un rendu incorrect. La version 24.12 d'Aspose.Cells introduit une option qui vous permet désactiver optionnellement le CSS, afin que les styles soient directement appliqués aux éléments HTML eux-mêmes. Si vous souhaitez définir le HTML comme contenu/corps de l’email, veuillez utiliser la propriété [**HtmlSaveOptions.DisableCss**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions/properties/#DisableCss) et la définir sur **true**.



## **Désactiver le CSS lors de l'enregistrement en HTML**

Le code d'exemple suivant montre l'utilisation de la propriété [**HtmlSaveOptions.DisableCss**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions/properties/#DisableCss). 



## **Code d'exemple**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-java-HTML-DisableCss-1.java" >}}
{{< app/cells/assistant language="java" >}}
