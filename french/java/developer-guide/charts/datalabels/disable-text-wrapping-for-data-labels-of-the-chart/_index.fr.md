---
title: Désactiver l'habillage du texte pour les étiquettes de données du graphique
type: docs
weight: 60
url: /fr/java/disable-text-wrapping-for-data-labels-of-the-chart/
---
{{% alert color="primary" %}}

Microsoft Excel 2013 permet aux utilisateurs d'envelopper ou de dérouler du texte dans les étiquettes de données d'un graphique. Par défaut, le texte de l'étiquette de données est encapsulé.

{{% /alert %}}

Aspose.Cells fournit le[**DataLabels.setTextWrapped()**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#IsTextWrapped) méthode. Mis à**Vrai** ou**Faux** pour activer ou désactiver l'habillage du texte sur les étiquettes de données respectivement.

 De même, utilisez le[**DataLabels.isTextWrapped()**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#IsTextWrapped)méthode pour savoir si une étiquette de données est déjà encapsulée.

Cette capture d'écran montre un exemple de fichier Excel Microsoft contenant un graphique dans lequel le texte des étiquettes de données est enveloppé. Comme vous pouvez le voir, vous pouvez cocher ou effacer le**Envelopper le texte dans la forme** dans la section ALIGNEMENT du panneau Format des étiquettes de données dans Microsoft Excel 2013.

**Emballage des étiquettes de données**

![tâche : image_autre_texte](disable-text-wrapping-for-data-labels-of-the-chart_1.png)

 L'exemple de code qui suit charge l'exemple de fichier Excel Microsoft à l'aide de Aspose.Cells et désactive l'habillage du texte de l'étiquette de données à l'aide de la[**DataLabels.setTextWrapped()**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#IsTextWrapped)méthode. Lorsque le code est exécuté, le graphique ressemble à ceci. Le texte précédemment enveloppé est maintenant déroulé.

**Affichage des étiquettes de données sur une seule ligne**

![tâche : image_autre_texte](disable-text-wrapping-for-data-labels-of-the-chart_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DisableTextWrapping-DisableTextWrapping.java" >}}
