---
title: Enregistrer Html avec StreamProvider
type: docs
weight: 80
url: /fr/net/convert-excel-to-html-with-streamprovider/
---

{{% alert color="primary" %}} 

Lors de la conversion de fichiers Excel contenant des images et des formes en fichiers HTML, nous rencontrons souvent les deux problèmes suivants :
1. Où devons-nous enregistrer les images et les formes lors de l'enregistrement du fichier Excel au flux HTML.
1. Remplacer le chemin par défaut par le chemin attendu.

Cet article explique comment implémenter l'interface [IStreamProvider](https://reference.aspose.com/cells/net/aspose.cells/istreamprovider) pour définir la propriété [HtmlSaveOptions.StreamProvider](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/streamprovider). En implémentant cette interface, vous pourrez enregistrer les ressources créées lors de la génération HTML dans des emplacements spécifiques ou des flux de mémoire.

{{% /alert %}} 

Voici le code principal montrant l'utilisation de la propriété [HtmlSaveOptions.StreamProvider](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/streamprovider)



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithHTMLFormat-ImplementIStreamProvider-ImplementIStreamProvider.cs" >}}



Voici le code de la classe *ExportStreamProvider* qui implémente l'interface [IStreamProvider](https://reference.aspose.com/cells/net/aspose.cells/istreamprovider) utilisée dans le code ci-dessus.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithHTMLFormat-ImplementIStreamProvider-ExportStreamProviderClass.cs" >}}

{{< app/cells/assistant language="csharp" >}}
