---
title: Überprüfen, ob die Arbeitsmappe versteckte externe Verknüpfungen enthält
type: docs
weight: 950
url: /de/java/check-if-workbook-contains-hidden-external-links/
---

## **Mögliche Verwendungsszenarien**
Manchmal enthält die Arbeitsmappe externe Verknüpfungen, die versteckt sind und in Microsoft Excel nicht angezeigt werden können. Aspose.Cells ruft alle externen Verknüpfungen ab, unabhängig davon, ob sie sichtbar oder versteckt sind. Sie können jedoch die Eigenschaft [ExternalLink.IsVisible](https://reference.aspose.com/cells/java/com.aspose.cells/externallink#IsVisible) überprüfen, um festzustellen, ob die externe Verknüpfung sichtbar ist oder nicht.
## **Überprüfen, ob die Arbeitsmappe versteckte externe Verknüpfungen enthält**
Der folgende Beispielcode lädt die [Quell-Excel-Datei](5472525.xlsx), die versteckte externe Verknüpfungen enthält. Diese Verknüpfungen sind in Microsoft Excel nicht sichtbar, sind jedoch in der Arbeitsmappe vorhanden. Nach dem Druck der Eigenschaften [ExternalLink.DataSource](https://reference.aspose.com/cells/java/com.aspose.cells/externallink#DataSource) und [ExternalLink.IsReferred](https://reference.aspose.com/cells/java/com.aspose.cells/externallink#IsReferred), wird die Eigenschaft [ExternalLink.IsVisible](https://reference.aspose.com/cells/java/com.aspose.cells/externallink#IsVisible) gedruckt. In der folgenden Konsolenausgabe sehen Sie, dass all seine externen Verknüpfungen nicht sichtbar sind.
## **Beispielcode**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CheckWorkbookContainsHiddenExternalLinks-CheckWorkbookContainsHiddenExternalLinks.java" >}}
## **Konsolenausgabe**
Hier ist die Konsolenausgabe des obigen Beispielcodes bei Ausführung mit der gegebenen [Beispieldatei](5472525.xlsx).



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
