---
title: Recevoir des notifications lors de la fusion de données avec des marqueurs intelligents
type: docs
weight: 20
url: /fr/net/getting-notifications-while-merging-data-with-smart-markers/
---

{{% alert color="primary" %}} 

Les API Aspose.Cells fournissent la classe [WorkbookDesigner](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner) pour [travailler avec les marqueurs intelligents](https://docs.aspose.com/cells/net/smart-markers/) où la mise en forme et les formules sont placées dans les [feuilles de calcul du concepteur](/cells/fr/net/what-is-a-designer-spreadsheet/) et ensuite traitées avec la classe [WorkbookDesigner](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner) pour remplir les données selon les marqueurs intelligents spécifiés. Parfois, il peut être nécessaire de recevoir des notifications sur la référence de la cellule ou sur le marqueur intelligent particulier en cours de traitement. Cela peut être réalisé en utilisant la propriété [WorkbookDesigner.CallBack](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner/properties/callback) et l'interface [ISmartMarkerCallBack](https://reference.aspose.com/cells/net/aspose.cells/ismartmarkercallback) exposée avec la version Aspose.Cells for .NET 8.6.2.

{{% /alert %}} 

Le code suivant démontre l'utilisation de l'interface [ISmartMarkerCallBack](https://reference.aspose.com/cells/net/aspose.cells/ismartmarkercallback) pour définir une nouvelle classe qui gère le rappel pour la méthode [WorkbookDesigner.Process](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner/methods/process).



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-GetSmartMarkerNotifications-ISmartMarkerCallBack.cs" >}}



Le reste du processus consiste à charger la feuille de calcul du concepteur contenant les marqueurs intelligents avec [WorkbookDesigner](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner) et à la traiter en définissant la source de données. Afin de simplifier l'exemple, nous avons utilisé une feuille de calcul du concepteur prédéfinie contenant uniquement deux marqueurs intelligents comme indiqué dans la capture d'écran ci-dessous où la source de données est créée dynamiquement pour fusionner les données selon les marqueurs intelligents spécifiés.

|![todo:image_alt_text](getting-notifications-while-merging-data-with-smart-markers_1.png)|
| :- |
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-GetSmartMarkerNotifications-1.cs" >}}
