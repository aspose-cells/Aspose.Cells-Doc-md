---
title: Enregistrer Html avec StreamProvider
type: docs
weight: 120
url: /fr/java/convert-excel-to-html-with-streamprovider/
---
{{% alert color="primary" %}}

Lors de la conversion de fichiers Excel contenant des images et des formes en fichiers html, nous rencontrons souvent les deux problèmes suivants :
1. Où devons-nous enregistrer les images et les formes lors de l'enregistrement du fichier Excel dans le flux HTML.
1. Remplacez le chemin par défaut par un chemin excepté.

 Cet article explique comment mettre en œuvre[**IStreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/IStreamProvider) interface de réglage du[**HtmlSaveOptions.StreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#StreamProvider) la propriété. En implémentant cette interface, vous pourrez enregistrer les ressources créées lors de la génération HTML dans vos emplacements ou flux de mémoire spécifiques.

{{% /alert %}}

## Exemple de code

 Ceci est le code principal montrant l'utilisation de[**HtmlSaveOptions.StreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#StreamProvider)la propriété

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-HtmlSaveOptions-HtmlSaveOptions.java" >}}

 Voici le code pour*ExportStreamProviderExportStreamProvider* classe qui implémente[**IStreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/IStreamProvider)interface utilisée dans le code ci-dessus.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ExportStreamProvider-ExportStreamProvider.java" >}}

