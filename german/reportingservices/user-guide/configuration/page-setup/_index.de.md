---
title: Seiteneinrichtung
type: docs
weight: 80
url: /de/reportingservices/page-setup/
---
Die Konfiguration umfasst zwei Abschnitte und 8 Arten von Seiteneinrichtungseigenschaften. Zu diesen Eigenschaften gehören name, index, FitToPagesTall, FitToPagesWide, TopMargin, FooterMargin, HeaderMargin, BottomMargin, LeftMargin und RightMargin.

- **Name** stellt den Berichtsnamen dar, stellt es den gesamten Bericht dar, wenn der Name leer ist.
- **Index** stellt den Arbeitsblattindex der exportierten Excel-Datei dar.
- **FitToPagesTall** stellt die Anzahl der Seiten dar, auf die das Arbeitsblatt beim Drucken skaliert wird.
- **FitToPagesWide** stellt die Anzahl der Seiten dar, auf die das Arbeitsblatt beim Drucken skaliert wird.
- **Fußzeilenrand**stellt den Abstand vom unteren Rand der Seite zur Fußzeile in der Einheit Zentimeter dar.
- **Kopfzeilenrand** stellt den Abstand vom oberen Rand der Seite zur Kopfzeile in der Einheit Zentimeter dar.
- **Linker Rand** stellt die Größe des linken Randes in Zentimetern dar.
- **Rechter Rand** stellt die Größe des rechten Randes in Zentimetern dar.
- **Oberer Rand** stellt die Größe des oberen Rands in der Einheit Zentimeter dar.
- **Unterer Rand** stellt die Größe des unteren Randes in Zentimetern dar.

PageSetup-Konfigurationsbeispiel:

{{code  lang="xml" }}
<PageSetup>
<Report name=”report name” FitToPagesTall=”0” FitToPagesWide =”1” TopMargin =”1.0” FooterMargin =” 1.0” HeaderMargin =” 1.0” BottomMargin =” 1.0” LeftMargin =” 1.0” RightMargin =” 1.0”>
<Sheet index=”0” FitToPagesTall=”1” FitToPagesWide =”1” TopMargin =”1.0” FooterMargin =” 1.0” HeaderMargin =” 1.0” BottomMargin =” 1.0” LeftMargin =” 1.0” RightMargin =” 1.0”/>
<Sheet index=”1” FitToPagesTall=”0” FitToPagesWide =”1” TopMargin =”1.0” FooterMargin =” 1.0” HeaderMargin =” 1.0” BottomMargin =” 1.0” LeftMargin =” 1.0” RightMargin =” 1.0”/>
</Report>
</PageSetup>

{{code}}
