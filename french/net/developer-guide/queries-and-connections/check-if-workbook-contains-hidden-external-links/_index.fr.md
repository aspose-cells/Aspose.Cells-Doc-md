---
title: Vérifiez si le classeur contient des liens externes masqués
type: docs
weight: 230
url: /fr/net/check-if-workbook-contains-hidden-external-links/
---
## **Scénarios d'utilisation possibles**
Parfois, le classeur contient des liens externes qui sont masqués et ne peuvent pas être affichés dans Microsoft Excel. Aspose.Cells récupère tous les liens externes qu'ils soient visibles ou masqués. Cependant, vous pouvez vérifier le[ExternalLink.IsVisibleExternalLink.IsVisible](https://reference.aspose.com/cells/net/aspose.cells/externallink/properties/isvisible)propriété pour vérifier si le lien externe est visible ou non
## **Vérifiez si le classeur contient des liens externes masqués**
 L'exemple de code suivant charge le[fichier excel source](5115413.xlsx) qui contient des liens externes cachés. Ces liens ne peuvent pas être visualisés dans Microsoft Excel mais ils sont présents à l'intérieur du classeur. Après l'impression[ExternalLink.DataSource](https://reference.aspose.com/cells/net/aspose.cells/externallink/properties/datasource) et[ExternalLink.IsReferredExternalLink.IsReferred](https://reference.aspose.com/cells/net/aspose.cells/externallink/properties/isreferred) propriété, il imprime la[ExternalLink.IsVisibleExternalLink.IsVisible](https://reference.aspose.com/cells/net/aspose.cells/externallink/properties/isvisible)la propriété. Dans la sortie de la console ci-dessous, vous voyez, tous ses liens externes ne sont pas visibles.
### **Exemple de code**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CheckHiddenExternalLinks-CheckHiddenExternalLinks.cs" >}}
### **Sortie console**
 Voici la sortie de la console de l'exemple de code ci-dessus lorsqu'il est exécuté avec le donné[exemple de fichier excel](5115413.xlsx).



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
