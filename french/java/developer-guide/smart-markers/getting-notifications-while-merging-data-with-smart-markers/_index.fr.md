---
title: Obtenir des notifications lors de la fusion de données avec des marqueurs intelligents
type: docs
weight: 460
url: /fr/java/getting-notifications-while-merging-data-with-smart-markers/
---
{{% alert color="primary" %}} 

 Aspose.Cells Les API fournissent le[WorkbookDesigner](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookDesigner) classe à[travailler avec des marqueurs intelligents](/cells/fr/java/smart-markers/) où la mise en forme et les formules sont placées dans le[feuilles de calcul de concepteur](/cells/fr/java/what-is-a-designer-spreadsheet/) puis traité avec[WorkbookDesigner](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookDesigner) classe pour remplir les données selon les marqueurs intelligents spécifiés. Parfois, il peut être nécessaire d'obtenir les notifications concernant la référence de cellule ou le marqueur intelligent particulier en cours de traitement. Ceci peut être réalisé en utilisant le[WorkbookDesigner.CallBackWorkbookDesigner.CallBack](https://reference.aspose.com/cells/java/com.aspose.cells/workbookdesigner#CallBack) propriété et[ISmartMarkerCallBack](https://reference.aspose.com/cells/java/com.aspose.cells/ISmartMarkerCallBack)interface exposée avec la sortie de Aspose.Cells for Java 8.6.2.

{{% /alert %}} 
## **Recevez des notifications lors de la fusion de données avec des marqueurs intelligents**
 Le morceau de code suivant illustre l'utilisation de[ISmartMarkerCallBack](https://reference.aspose.com/cells/java/com.aspose.cells/ISmartMarkerCallBack)interface pour définir une nouvelle classe qui gère le rappel pour[WorkbookDesigner.processWorkbookDesigner.process](https://reference.aspose.com/cells/java/com.aspose.cells/workbookdesigner#process\(\)) méthode.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SmartMarkerCallBack-SmartMarkerCallBack.java" >}}


Afin de garder l'exemple simple et précis, l'extrait de code suivant crée une feuille de calcul de concepteur vide, insère un marqueur intelligent et le traite avec la source de données créée dynamiquement.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetNotificationsWhileMergingData-GetNotificationsWhileMergingData.java" >}}
