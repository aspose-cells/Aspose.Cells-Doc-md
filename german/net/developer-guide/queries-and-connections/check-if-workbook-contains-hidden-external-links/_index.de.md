---
title: Überprüfen, ob die Arbeitsmappe versteckte externe Verknüpfungen enthält
type: docs
weight: 230
url: /de/net/check-if-workbook-contains-hidden-external-links/
---

## **Mögliche Verwendungsszenarien**
Manchmal enthält die Arbeitsmappe externe Verknüpfungen, die verborgen und in Microsoft Excel nicht angezeigt werden können. Aspose.Cells ruft alle externen Verknüpfungen ab, unabhängig davon, ob sie sichtbar oder verborgen sind. Sie können jedoch die [ExternalLink.IsVisible](https://reference.aspose.com/cells/net/aspose.cells/externallink/properties/isvisible)-Eigenschaft überprüfen, um festzustellen, ob die externe Verknüpfung sichtbar ist oder nicht.
## **Überprüfen, ob die Arbeitsmappe versteckte externe Verknüpfungen enthält**
Der folgende Beispielcode lädt die [Quell-Excel-Datei](5115413.xlsx), die verborgene externe Verknüpfungen enthält. Diese Verknüpfungen können in Microsoft Excel nicht angezeigt werden, sind jedoch in der Arbeitsmappe vorhanden. Nach dem Drucken von [ExternalLink.DataSource](https://reference.aspose.com/cells/net/aspose.cells/externallink/properties/datasource)- und [ExternalLink.IsReferred](https://reference.aspose.com/cells/net/aspose.cells/externallink/properties/isreferred)-Eigenschaft wird die [ExternalLink.IsVisible](https://reference.aspose.com/cells/net/aspose.cells/externallink/properties/isvisible)-Eigenschaft gedruckt. In der folgenden Konsolenausgabe sehen Sie, dass alle externen Verknüpfungen nicht sichtbar sind.
### **Beispielcode**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CheckHiddenExternalLinks-CheckHiddenExternalLinks.cs" >}}
### **Konsolenausgabe**
Hier ist die Konsolenausgabe des obigen Beispielcodes bei Ausführung mit der angegebenen [Beispiel-Excel-Datei](5115413.xlsx).



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
{{< app/cells/assistant language="csharp" >}}
