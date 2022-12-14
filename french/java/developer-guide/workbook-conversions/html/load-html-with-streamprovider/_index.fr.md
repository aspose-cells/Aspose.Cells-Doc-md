---
title: Charger Html dans Excel avec StreamProvider
type: docs
weight: 80
url: /fr/java/convert-html-to-excel-with-streamprovider/
---
{{% alert color="primary" %}} 

Lors du chargement de code HTML contenant des ressources externes, nous sommes souvent confrontés aux deux problèmes suivants :
1. Lorsque le flux html est chargé, les images et les ressources externes référencées par le fichier html ne peuvent pas être obtenues via des chemins relatifs.
1. Les chemins de ressources externes référencés dans les fichiers html doivent être mappés.

 Cet article explique comment mettre en œuvre[**IStreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/IStreamProvider) interface de réglage du[**HtmlLoadOptions.StreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#StreamProvider) propriété. En implémentant cette interface, vous pourrez charger des ressources externes lors du chargement de flux Html ou ces ressources externes sont relatives.

{{% /alert %}} 

 Ceci est le code principal montrant l'utilisation de[**HtmlLoadOptions.StreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#StreamProvider)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Load-Html-With-StreamProvider.java" >}}
