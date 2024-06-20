---
title: Seiteneinrichtung
type: docs
weight: 80
url: /de/reportingservices/page-setup/
---

Die Konfiguration umfasst zwei Abschnitte und 8 Arten von Seiteneinrichtungseigenschaften. Diese Eigenschaften umfassen Name, Index, FitToPagesTall, FitToPagesWide, TopMargin, FooterMargin, HeaderMargin, BottomMargin, LeftMargin und RightMargin.

- **name** repräsentiert den Berichtsnamen. Es repräsentiert den gesamten Bericht, wenn der Name leer ist.
- **index** repräsentiert den Arbeitsblattindex der exportierten Excel-Datei.
- **FitToPagesTall** repräsentiert die Anzahl der vertikalen Seiten, auf die das Arbeitsblatt skaliert wird, wenn es gedruckt wird.
- **FitToPagesWide** repräsentiert die Anzahl der horizontalen Seiten, auf die das Arbeitsblatt skaliert wird, wenn es gedruckt wird.
- **FooterMargin** repräsentiert den Abstand vom unteren Rand der Seite zum Fußzeilenbereich in Zentimetern.
- **HeaderMargin** repräsentiert den Abstand vom oberen Rand der Seite zum Kopfbereich in Zentimetern.
- **LeftMargin** repräsentiert die Größe des linken Seitenrandes in Zentimetern.
- **RightMargin** repräsentiert die Größe des rechten Seitenrandes in Zentimetern.
- **TopMargin** repräsentiert die Größe des oberen Seitenrandes in Zentimetern.
- **BottomMargin** repräsentiert die Größe des unteren Seitenrandes in Zentimetern.

Beispiel für die Konfiguration von Seiteneinrichtungen:

{{code  lang="xml" }}
<PageSetup>
<Report name=”report name” FitToPagesTall=”0” FitToPagesWide =”1” TopMargin =”1.0” FooterMargin =” 1.0” HeaderMargin =” 1.0” BottomMargin =” 1.0” LeftMargin =” 1.0” RightMargin =” 1.0”>
<Sheet index=”0” FitToPagesTall=”1” FitToPagesWide =”1” TopMargin =”1.0” FooterMargin =” 1.0” HeaderMargin =” 1.0” BottomMargin =” 1.0” LeftMargin =” 1.0” RightMargin =” 1.0”/>
<Sheet index=”1” FitToPagesTall=”0” FitToPagesWide =”1” TopMargin =”1.0” FooterMargin =” 1.0” HeaderMargin =” 1.0” BottomMargin =” 1.0” LeftMargin =” 1.0” RightMargin =” 1.0”/>
</Report>
</PageSetup>

{{code}}
