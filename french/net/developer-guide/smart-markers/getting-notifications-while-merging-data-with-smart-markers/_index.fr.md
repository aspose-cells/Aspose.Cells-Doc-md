---
title: Obtenir des notifications lors de la fusion de données avec des marqueurs intelligents
type: docs
weight: 20
url: /fr/net/getting-notifications-while-merging-data-with-smart-markers/
---
{{% alert color="primary" %}} 

 Aspose.Cells Les API fournissent le[WorkbookDesigner](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner) classe à[travailler avec des marqueurs intelligents](https://docs.aspose.com/cells/net/smart-markers/) où la mise en forme et les formules sont placées dans le[feuilles de calcul de concepteur](/cells/fr/net/what-is-a-designer-spreadsheet/) puis traité avec[WorkbookDesigner](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner) classe pour remplir les données selon les marqueurs intelligents spécifiés. Parfois, il peut être nécessaire d'obtenir les notifications concernant la référence de cellule ou le marqueur intelligent particulier en cours de traitement. Ceci peut être réalisé en utilisant le[WorkbookDesigner.CallBackWorkbookDesigner.CallBack](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner/properties/callback) propriété et[ISmartMarkerCallBack](https://reference.aspose.com/cells/net/aspose.cells/ismartmarkercallback) interface exposée avec la sortie de Aspose.Cells for .NET 8.6.2.

{{% /alert %}} 

 Le morceau de code suivant illustre l'utilisation de[ISmartMarkerCallBack](https://reference.aspose.com/cells/net/aspose.cells/ismartmarkercallback) interface pour définir une nouvelle classe qui gère le rappel pour[WorkbookDesigner.Process](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner/methods/process)méthode.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-GetSmartMarkerNotifications-ISmartMarkerCallBack.cs" >}}



 Le reste du processus comprend le chargement d'une feuille de calcul de concepteur contenant les marqueurs intelligents avec[WorkbookDesigner](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner)et traitez-le en définissant la source de données. Afin de garder l'exemple simple, nous avons utilisé une feuille de calcul de concepteur prédéfinie contenant seulement deux marqueurs intelligents, comme indiqué dans l'instantané ci-dessous où la source de données est créée dynamiquement pour fusionner les données en fonction des marqueurs intelligents spécifiés.

|![tâche : image_autre_texte](getting-notifications-while-merging-data-with-smart-markers_1.png)|
|:- |
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-GetSmartMarkerNotifications-1.cs" >}}
