---
title: Vérifiez si le classeur contient des liens externes masqués
type: docs
weight: 950
url: /fr/java/check-if-workbook-contains-hidden-external-links/
---
## **Scénarios d'utilisation possibles**
Parfois, le classeur contient des liens externes qui sont masqués et ne peuvent pas être affichés dans Microsoft Excel. Aspose.Cells récupère tous les liens externes qu'ils soient visibles ou masqués. Cependant, vous pouvez vérifier le[ExternalLink.IsVisibleExternalLink.IsVisible](https://reference.aspose.com/cells/java/com.aspose.cells/externallink#IsVisible)propriété pour vérifier si le lien externe est visible ou non
## **Vérifiez si le classeur contient des liens externes masqués**
 L'exemple de code suivant charge le[fichier excel source](5472525.xlsx) qui contient des liens externes cachés. Ces liens ne peuvent pas être visualisés dans Microsoft Excel mais ils sont présents à l'intérieur du classeur. Après l'impression[ExternalLink.DataSource](https://reference.aspose.com/cells/java/com.aspose.cells/externallink#DataSource) et[ExternalLink.IsReferredExternalLink.IsReferred](https://reference.aspose.com/cells/java/com.aspose.cells/externallink#IsReferred) propriété, il imprime la[ExternalLink.IsVisibleExternalLink.IsVisible](https://reference.aspose.com/cells/java/com.aspose.cells/externallink#IsVisible)la propriété. Dans la sortie de la console ci-dessous, vous voyez, tous ses liens externes ne sont pas visibles.
## **Exemple de code**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CheckWorkbookContainsHiddenExternalLinks-CheckWorkbookContainsHiddenExternalLinks.java" >}}
## **Sortie console**
 Voici la sortie de la console de l'exemple de code ci-dessus lorsqu'il est exécuté avec le donné[exemple de fichier excel](5472525.xlsx).



{{< highlight "java" >}}

 Data Source: C:\International\DDB\FAS 133\Swap Rates\GS_1M_3M_1_2_5_¥$_(B)IRSwaps_0400.xls

Is Referred: True

Is Visible: False

Data Source: C:\DIST DAY\MAY TEMPLATES\030601t.xls

Is Referred: True

Is Visible: False

Data Source: C:\AREVIEW\2002 Controllable\Autobrct.xls

Is Referred: True

Is Visible: False

Data Source: C:\CARDSFO\Main Files\Rate Forecast\FY 11\IFR 11 01 (New Model REPORTS 11.08.07).xls

Is Referred: True

Is Visible: False

{{< /highlight >}}
