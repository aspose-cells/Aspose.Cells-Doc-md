---
title: Vergleich von Funktionalität und Leistung von Aspose.Cells for Go über C mit Excelize, Tealeg/xlsx und Go OLE.
linktitle: Vergleich von Funktionalität und Leistung
type: docs
weight: 40
url: /de/go-cpp/comparison-of-functionality-and-performance/
description: Vergleich von Funktionalität und Leistung von Aspose.Cells for Go über C mit Excelize, Tealeg/xlsx und Go OLE.
keywords: Aspose.Cells, Excel, Formel Watch Fenster, Zellen, Hinzufügen, C++
---

Im Folgenden ist ein umfassender Vergleich von Aspose.Cells für Go (über C) mit anderen gängigen Go-Excel-Verarbeitungsbibliotheken (Excelize, tealeg/xlsx, go-ole) hinsichtlich Funktionalität, Leistung und Anwendungsfälle.

## Unterschiede in grundlegender Positionierung und Struktur

| Bibliotheksname       | Typ                            | zugrunde liegende Implementierung     | CGO-Abhängigkeit        | Plattformübergreifende Bereitstellung |
| :------------------- | :----------------------------- | :--------------------------------- | :----------------------- | :-----------------------  |
| Aspose.Cells für Go  | Kommerzielle Bibliothek (MIT/Bezahlversion) | Native Engine, Go CGO Wrapper       | ✅ Ja                | Unterstützung für Windows, Linux |
| Excelize             | Open-Source-Bibliothek (MIT)              | Reine Go-Implementierung             | ❌ Nein             | Unterstützung für Windows, Linux, MacOS |
| tealeg/xlsx          | Open-Source-Bibliothek (BSD)               | Reine Go-Implementierung             | ❌ Nein             | Unterstützung für Windows, Linux, MacOS |
| go-ole               | Open-Source-Bibliothek (BSD)               | Go Windows OLE/COM-Schnittstelle     | ✅ Ja (nur Windows) | Nur Windows |

### Wesentliche Unterschiede

- Aspose.Cells for Go via C++ ist eine industrieweit einsatzfähige kommerzielle Bibliothek mit den vollständigsten Funktionen, aber es ist ein kostenpflichtiges Produkt.
- Excelize ist derzeit die aktivste und open-source Go-Bibliothek, reine Go-Implementierung.
- Tealeg/xlsx ist eine frühe Open-Source-Bibliothek mit einfacheren Funktionen und langsamer Wartung.
- Go-ole ist eine nur für Windows verfügbare COM-Automatisierung, die auf Excel-Installation angewiesen ist und für Serverumgebungen nicht empfohlen wird.

## Funktionsvergleich

### Vergleich der unterstützten Dateiformate

| Tabellenkalkulationsformat | Aspose.Cells for Go via C++ | Excelize | Tealeg/xlsx | Go-OLE (Excel-App) |
| :--------------------- | :---------------------------- | :---------- | :---------- | :-------------------  |
| Xlsx | ✅ Ja | ✅ Ja | ✅ Ja | ✅ Abhängig von Excel |
| Xlsb | ✅ Ja | ❌ Nein | ❌ Nein | ✅ Abhängig von Excel |
| Xls | ✅ Ja | ❌ Nein | ❌ Nein | ✅ Abhängig von Excel |
| Xlsm | ✅ Ja | ✅ Ja | ✅ Ja | ✅ Abhängig von Excel |
| Xltm | ✅ Ja | ✅ Ja | ✅ Ja | ✅ Abhängig von Excel |
| Xltx | ✅ Ja | ✅ Ja | ✅ Ja | ✅ Abhängig von Excel |
| Csv | ✅ Ja | ❌ Nein | ❌ Nein | ✅ Abhängig von Excel |
| Ods | ✅ Ja | ❌ Nein | ❌ Nein | ✅ Abhängig von Excel |
| Html | ✅ Ja | ❌ Nein | ❌ Nein | ❌ Nein |
| Numbers | ✅ Ja | ❌ Nein | ❌ Nein | ❌ Nein |
| Json | ✅ Ja | ❌ Nein | ❌ Nein | ❌ Nein |
| Xml | ✅ Ja | ❌ Nein | ❌ Nein | ❌ Nein |
| SpreadsheetML | ✅ Ja | ❌ Nein | ❌ Nein | ❌ Nein |

### Unterstützte Tabellenkalkulationsfunktionen

| Bibliotheksfunktionen | Aspose.Cells for Go via C++ | Excelize | Tealeg/xlsx | Go-OLE (Excel-App) |
| :----------------------------    | :---------------------------- | :--------------- | :---------- | :----------  |
| Lesen/Schreiben (Unterstützt Dateiformate) | ✅ Ja | ✅ Ja | ✅ Ja | ✅ Ja |
| Zelle/Reihe/Spalte/Arbeitsblatt | ✅ Ja | ✅ Ja | ✅ Ja | ✅ Ja |
| Stil                                | ✅ Ja                        | ✅ Ja           | ✅ Ja     | ✅ Ja     |
| Formelberechnung                  | ✅ Ja                        | ✅ Ja (Teil)    | ❌ Nein   | ✅ Ja (berechnet von Excel) |
| Diagramm/Bild                     | ✅ Ja                        | ✅ Ja (Teil)    | ❌ Nein   | ✅ Ja     |
| PivotTable                        | ✅ Ja                        | ✅ Ja           | ❌ Nein   | ✅ Ja     |
| Bedingte Formatierung             | ✅ Ja                        | ✅ Ja           | ❌ Nein   | ✅ Ja     |
| Datenüberprüfung                  | ✅ Ja                        | ✅ Ja           | ❌ Nein    | ✅ Ja     |
| Verschlüsselung/Passwortschutz    | ✅ Ja                        | ✅ Ja           | ❌ Nein   | ✅ Ja     |
| Datenüberprüfung                  | ✅ Ja                        | ✅ Ja           | ❌ Nein    | ✅ Ja     |
| VBA-Makro                          | ✅ Ja Lesen                   | ❌ Nein        | ❌ Nein    | ✅ Ja     |
| Datenüberprüfung                  | ✅ Ja                        | ✅ Ja           | ❌ Nein    | ✅ Ja     |

## Leistungsvergleich

- **Testumgebung**：
Prozessor: 12. Gen Intel(R) Core(TM) i7-12700 (2,10 GHz)
Installierter Arbeitsspeicher: 64,0 GB (63,7 GB nutzbar)
OS-Name: Microsoft Windows 11 Pro
OS-Version: 10.0.26100
OS-Architektur: 64-Bit
Go-Version: go version go1.24.5 windows/amd64
Aspose.Cells for Go via C++: 25.9.0
Excelize: 1.4.1

- **Testszenario**: Angenommen eine große Datei, 10 Arbeitsblätter, 100.000 Zeilen x 250 Spalten, einschließlich Formatierung

- **Ergebnisberichte**:
  - Excelize läuft für 35 Minuten (Startzeit: 2025-10-09T10:04:16+08:00, Endzeit: 2025-10-09T10:39:53+08:00), generierte Dateigröße: 1,11 GB.
  - Aspose.Cells for Go via C++ (Modell 1) läuft für 27 Minuten (Startzeit: 2025-10-09T10:57:55+08:00, Endzeit: 2025-10-09T11:16:24+08:00), generierte Dateigröße: 936 MB.
  - Aspose.Cells for Go via C++ (Modell 2) läuft für 16 Minuten (Startzeit: 2025-10-09T12:01:26+08:00, Endzeit: 2025-10-09T12:17:17+08:00), generierte Dateigröße: 1,16 GB.
