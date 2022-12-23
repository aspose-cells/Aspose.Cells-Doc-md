---
title: Enregistrer Html avec StreamProvider
type: docs
weight: 80
url: /fr/net/convert-excel-to-html-with-streamprovider/
---
{{% alert color="primary" %}} 

Lors de la conversion de fichiers Excel contenant des images et des formes en fichiers HTML, nous sommes souvent confrontés aux deux problèmes suivants :
1. Où devons-nous enregistrer les images et les formes lors de l'enregistrement du fichier Excel dans le flux HTML.
1. Remplacez le chemin par défaut par un chemin excepté.

 Cet article explique comment mettre en œuvre[IStreamProvider](https://reference.aspose.com/cells/net/aspose.cells/istreamprovider) interface de réglage du[HtmlSaveOptions.StreamProvider](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/streamprovider) la propriété. En implémentant cette interface, vous pourrez enregistrer les ressources créées lors de la génération HTML dans vos emplacements ou flux de mémoire spécifiques.

{{% /alert %}} 

 Ceci est le code principal montrant l'utilisation de[HtmlSaveOptions.StreamProvider](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/streamprovider)la propriété



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithHTMLFormat-ImplementIStreamProvider-ImplementIStreamProvider.cs" >}}



 Voici le code pour*ExportStreamProviderExportStreamProvider* classe qui implémente[IStreamProvider](https://reference.aspose.com/cells/net/aspose.cells/istreamprovider)interface utilisée dans le code ci-dessus.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithHTMLFormat-ImplementIStreamProvider-ExportStreamProviderClass.cs" >}}

