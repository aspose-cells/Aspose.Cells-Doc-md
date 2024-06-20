---
title: Charger du HTML dans Excel avec StreamProvider
type: docs
weight: 80
url: /fr/java/convert-html-to-excel-with-streamprovider/
---

{{% alert color="primary" %}} 

Lors du chargement de html contenant des ressources externes, nous sommes souvent confrontés aux deux problèmes suivants :
1. Lorsque le flux HTML est chargé, les images et les ressources externes référencées par le fichier HTML ne peuvent pas être obtenues via des chemins relatifs.
1. Les chemins des ressources externes référencés dans les fichiers html doivent être mappés.

Cet article explique comment implémenter l'interface [**IStreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/IStreamProvider) pour définir la propriété [**HtmlLoadOptions.StreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#StreamProvider). En implémentant cette interface, vous pourrez charger des ressources externes lors du chargement des flux html, ou lorsque ces ressources externes sont relatives.

{{% /alert %}} 

Voici le code principal montrant l'utilisation de [**HtmlLoadOptions.StreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#StreamProvider)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Load-Html-With-StreamProvider.java" >}}
