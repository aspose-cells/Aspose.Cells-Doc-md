---
title: Enregistrer Html avec StreamProvider
type: docs
weight: 120
url: /fr/java/convert-excel-to-html-with-streamprovider/
---

{{% alert color="primary" %}}

Lors de la conversion de fichiers Excel contenant des images et des formes en fichiers HTML, nous rencontrons souvent les deux problèmes suivants:
1. Où devons-nous enregistrer les images et les formes lors de l'enregistrement du fichier Excel au flux HTML.
1. Remplacer le chemin par défaut par le chemin attendu.

Cet article explique comment implémenter l'interface [**IStreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/IStreamProvider) pour définir la propriété [**HtmlSaveOptions.StreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#StreamProvider). En implémentant cette interface, vous pourrez sauvegarder les ressources créées lors de la génération HTML dans des emplacements spécifiques ou des flux de mémoire.

{{% /alert %}}

## Code d'exemple

Voici le code principal montrant l'utilisation de la propriété [**HtmlSaveOptions.StreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#StreamProvider)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-HtmlSaveOptions-HtmlSaveOptions.java" >}}

Voici le code de la classe *ExportStreamProvider* qui implémente l'interface [**IStreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/IStreamProvider) utilisée dans le code ci-dessus.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ExportStreamProvider-ExportStreamProvider.java" >}}

{{< app/cells/assistant language="java" >}}
