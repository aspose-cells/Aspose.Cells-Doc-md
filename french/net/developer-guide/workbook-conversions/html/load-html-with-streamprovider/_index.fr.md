---
title: Charger du HTML dans Excel avec StreamProvider
type: docs
weight: 80
url: /fr/net/convert-html-to-excel-with-streamprovider/
---

{{% alert color="primary" %}} 

Lors du chargement de fichiers HTML contenant des ressources externes, nous rencontrons souvent les deux problèmes suivants :
1. Lorsque le flux HTML est chargé, les images et les ressources externes référencées par le fichier HTML ne peuvent pas être obtenues via des chemins relatifs.
1. Les chemins des ressources externes référencés dans les fichiers HTML doivent être mappés

Cet article explique comment implémenter l'interface [IStreamProvider](https://reference.aspose.com/cells/net/aspose.cells/istreamprovider) pour définir la propriété [HtmlLoadOptions.StreamProvider](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/streamprovider/). En implémentant cette interface, vous pourrez charger des ressources externes lors du chargement de flux HTML ou ces ressources externes seront relatives.

{{% /alert %}} 

Il s'agit du code principal montrant l'utilisation de la propriété [HtmlLoadOptions.StreamProvider](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/streamprovider/)



{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Load-Html-With-StreamProvider.cs" >}}
