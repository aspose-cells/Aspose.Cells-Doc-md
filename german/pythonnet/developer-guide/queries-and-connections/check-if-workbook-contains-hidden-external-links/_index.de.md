---
title: Überprüfen, ob die Arbeitsmappe versteckte externe Verknüpfungen enthält
type: docs
weight: 230
url: /de/python-net/check-if-workbook-contains-hidden-external-links/
---

## **Mögliche Verwendungsszenarien**
Manchmal enthält die Arbeitsmappe externe Links, die versteckt sind und in Microsoft Excel nicht angezeigt werden können. Aspose.Cells für Python via .NET ruft alle externen Links ab, egal ob sichtbar oder versteckt. Sie können jedoch die Eigenschaft [ExternalLink.is_visible](https://reference.aspose.com/cells/python-net/aspose.cells/externallink/is_visible) überprüfen, um festzustellen, ob der externe Link sichtbar ist.

## **Überprüfen, ob die Arbeitsmappe versteckte externe Verknüpfungen enthält**
Der folgende Beispielcode lädt die [Quell-Excel-Datei](5115413.xlsx), die versteckte externe Links enthält. Diese Links können in Microsoft Excel nicht angezeigt werden, sind aber im Arbeitsbuch vorhanden. Nach Ausgabe von [ExternalLink.data_source](https://reference.aspose.com/cells/python-net/aspose.cells/externallink/data_source) und [ExternalLink.is_referred](https://reference.aspose.com/cells/python-net/aspose.cells/externallink/is_referred) wird die Eigenschaft [ExternalLink.is_visible](https://reference.aspose.com/cells/python-net/aspose.cells/externallink/is_visible) ausgegeben. Im folgenden Konsolenausgang sehen Sie, dass alle externen Links nicht sichtbar sind.

### **Beispielcode**
{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Connections-CheckHiddenExternalLinks.py" >}}

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

{{< app/cells/assistant language="python-net" >}}
