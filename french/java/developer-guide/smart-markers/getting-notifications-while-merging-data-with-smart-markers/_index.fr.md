---
title: Recevoir des notifications lors de la fusion de données avec des marqueurs intelligents
type: docs
weight: 460
url: /fr/java/getting-notifications-while-merging-data-with-smart-markers/
---

{{% alert color="primary" %}} 

Les API Aspose.Cells fournissent la classe [WorkbookDesigner](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookDesigner) pour [travailler avec les Smart Markers](/cells/fr/java/smart-markers/) où la mise en forme et les formules sont placées dans les [feuilles de calcul du concepteur](/cells/fr/java/what-is-a-designer-spreadsheet/) puis traitées avec la classe [WorkbookDesigner](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookDesigner) pour remplir les données selon les Smart Markers spécifiés. Parfois, il peut être nécessaire de recevoir des notifications sur la référence de cellule ou le Smart Marker particulier en cours de traitement. Cela peut être réalisé en utilisant la propriété [WorkbookDesigner.CallBack](https://reference.aspose.com/cells/java/com.aspose.cells/workbookdesigner#CallBack) et l'interface [ISmartMarkerCallBack](https://reference.aspose.com/cells/java/com.aspose.cells/ISmartMarkerCallBack) exposée avec la version Aspose.Cells for Java 8.6.2.

{{% /alert %}} 
## **Recevoir des notifications lors de la fusion des données avec les Smart Markers**
Le morceau de code suivant démontre l'utilisation de l'interface [ISmartMarkerCallBack](https://reference.aspose.com/cells/java/com.aspose.cells/ISmartMarkerCallBack) pour définir une nouvelle classe qui gère le rappel pour la méthode [WorkbookDesigner.process](https://reference.aspose.com/cells/java/com.aspose.cells/workbookdesigner#process\(\)).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SmartMarkerCallBack-SmartMarkerCallBack.java" >}}


Afin de simplifier l'exemple et d'aller droit au but, le snippet suivant crée une feuille de calcul du concepteur vide, insère un Smart Marker et la traite avec la source de données créée dynamiquement.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetNotificationsWhileMergingData-GetNotificationsWhileMergingData.java" >}}
