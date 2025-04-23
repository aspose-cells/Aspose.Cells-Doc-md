---
title: Vérifiez si le classeur contient des liens externes cachés
type: docs
weight: 230
url: /fr/python-net/check-if-workbook-contains-hidden-external-links/
---

## **Scénarios d'utilisation possibles**
Parfois, le classeur contient des liens externes qui sont cachés et ne peuvent pas être visualisés dans Microsoft Excel. Aspose.Cells pour Python via .NET récupère tous les liens externes, qu'ils soient visibles ou cachés. Cependant, vous pouvez vérifier la propriété [ExternalLink.is_visible](https://reference.aspose.com/cells/python-net/aspose.cells/externallink/is_visible) pour voir si le lien externe est visible ou non.

## **Vérifiez si le classeur contient des liens externes cachés**
Le code d'exemple suivant charge le [fichier Excel source](5115413.xlsx) qui contient des liens externes cachés. Ces liens ne peuvent pas être visualisés dans Microsoft Excel mais ils sont présents dans le classeur. Après avoir imprimé la propriété [ExternalLink.data_source](https://reference.aspose.com/cells/python-net/aspose.cells/externallink/data_source) et [ExternalLink.is_referred](https://reference.aspose.com/cells/python-net/aspose.cells/externallink/is_referred), il imprime la propriété [ExternalLink.is_visible](https://reference.aspose.com/cells/python-net/aspose.cells/externallink/is_visible). Dans la sortie console ci-dessous, vous voyez que tous ses liens externes ne sont pas visibles.

### **Code d'exemple**
{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Connections-CheckHiddenExternalLinks.py" >}}

### **Sortie console**
Voici la sortie console du code d'exemple ci-dessus lors de son exécution avec le [fichier Excel d'exemple](5115413.xlsx) donné.



{{< highlight java >}}

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

