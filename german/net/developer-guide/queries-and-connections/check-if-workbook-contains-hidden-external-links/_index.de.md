---
title: Überprüfen Sie, ob die Arbeitsmappe versteckte externe Links enthält
type: docs
weight: 230
url: /de/net/check-if-workbook-contains-hidden-external-links/
---
## **Mögliche Nutzungsszenarien**
Manchmal enthält die Arbeitsmappe externe Links, die ausgeblendet sind und in Microsoft Excel nicht angezeigt werden können. Aspose.Cells ruft alle externen Links ab, unabhängig davon, ob sie sichtbar oder ausgeblendet sind. Sie können dies jedoch überprüfen[ExternalLink.IsVisible](https://reference.aspose.com/cells/net/aspose.cells/externallink/properties/isvisible)-Eigenschaft, um zu prüfen, ob der externe Link sichtbar ist oder nicht
## **Überprüfen Sie, ob die Arbeitsmappe versteckte externe Links enthält**
 Der folgende Beispielcode lädt die[Excel-Quelldatei](5115413.xlsx) die versteckte externe Links enthält. Diese Links können in Microsoft Excel nicht angezeigt werden, sie sind jedoch in der Arbeitsmappe vorhanden. Nach dem Drucken[ExternalLink.DataSource](https://reference.aspose.com/cells/net/aspose.cells/externallink/properties/datasource) und[ExternalLink.IsReferred](https://reference.aspose.com/cells/net/aspose.cells/externallink/properties/isreferred) Eigenschaft, druckt es die[ExternalLink.IsVisible](https://reference.aspose.com/cells/net/aspose.cells/externallink/properties/isvisible)Eigentum. In der Konsolenausgabe unten sehen Sie, dass alle externen Links nicht sichtbar sind.
### **Beispielcode**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CheckHiddenExternalLinks-CheckHiddenExternalLinks.cs" >}}
### **Konsolenausgabe**
 Hier ist die Konsolenausgabe des obigen Beispielcodes, wenn er mit dem angegebenen ausgeführt wird[Excel-Beispieldatei](5115413.xlsx).



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
