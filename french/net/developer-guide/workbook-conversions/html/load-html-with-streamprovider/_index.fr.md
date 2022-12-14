---
title: Charger Html dans Excel avec StreamProvider
type: docs
weight: 80
url: /fr/net/convert-html-to-excel-with-streamprovider/
---
{{% alert color="primary" %}} 

Lors du chargement de fichiers html contenant des ressources externes, nous sommes souvent confrontés aux deux problèmes suivants :
1. Lorsque le flux html est chargé, les images et les ressources externes référencées par le fichier html ne peuvent pas être obtenues via des chemins relatifs.
1. Les chemins de ressources externes référencés dans les fichiers html doivent être mappés

 Cet article explique comment mettre en œuvre[IStreamProvider](https://reference.aspose.com/cells/net/aspose.cells/istreamprovider) interface de réglage du[HtmlLoadOptions.StreamProvider](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/streamprovider/) propriété. En implémentant cette interface, vous pourrez charger des ressources externes lors du chargement de flux Html ou ces ressources externes sont relatives.

{{% /alert %}} 

 Ceci est le code principal montrant l'utilisation de[HtmlLoadOptions.StreamProvider](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/streamprovider/)propriété



{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Load-Html-With-StreamProvider.cs" >}}
