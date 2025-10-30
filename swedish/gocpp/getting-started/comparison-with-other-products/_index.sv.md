---
title: Jämförelse av funktionalitet och prestanda för Aspose.Cells för Go via C jämfört med Excelize, Tealeg/xlsx och Go OLE.
linktitle: Jämförelse av funktionalitet och prestanda
type: docs
weight: 40
url: /sv/go-cpp/comparison-of-functionality-and-performance/
description: Jämförelse av funktionalitet och prestanda för Aspose.Cells för Go via C jämfört med Excelize, Tealeg/xlsx och Go OLE.
keywords: Aspose.Cells, Excel, Formel bevakningsfönster, Cell, Lägg till, C++
---

Nedan följer en omfattande jämförelse av Aspose.Cells för Go (via C) med andra ledande Go-språkliga bibliotek för Excel-behandling (Excelize, tealeg/xlsx, go-ole) när det gäller funktionalitet, prestanda och användningsområden.

## Skillnader i grundläggande positionering och struktur

| Biblioteksnamn       | Typ                               | Underliggande implementation       | CGO-beroende            | Plattformövergripande distribution |
| :------------------- | :----------------------------- | :--------------------------------- | :----------------------- | :-----------------------  |
| Aspose.Cells för Go  | Kommersiellt bibliotek (MIT/Betalt) | Natív motor, Go Cgo-Wrapper        |  ✅  Ja                  | Support för Windows, Linux |
| Excelize             | Öppen källkod bibliotek (MIT)     | Rent Go-implementation               |  ❌  Nej                  | Support för Windows, Linux, MacOS |
| tealeg/xlsx          | Öppen källkod bibliotek (BSD)     | Rent Go-implementation               |  ❌  Nej                  | Support för Windows, Linux, MacOS |
| go-ole               | Öppen källkod bibliotek (BSD)     | Go Windows OLE/COM-gränssnitt        |  ✅  Ja (Endast Windows)  | Endast Windows |

### Viktiga skillnader

- Aspose.Cells for Go via C++ är ett industriellt kommersiellt bibliotek med de mest kompletta funktionerna, men kräver ett betalt produkt.
- Excelize är för närvarande det mest aktiva och öppna källkodsbiblioteket för Go, rent Go.
- Tealeg/xlsx är ett tidigt öppet källkodsbibliotek med mer grundläggande funktioner och långsam underhåll.
- Go-ole är ett endast Windows COM-automation schema som förlitar sig på Excel-installation och rekommenderas inte för servermiljöer.

## Funktionjämförelse

### Jämförelse av stödda filformat

| Kalkylbladsformat     |   Aspose.Cells for Go via C++ | Excelize    | Tealeg/xlsx | Go-OLE (Excel-appen)    |
| :--------------------- | :---------------------------- | :---------- | :---------- | :-------------------  |
| Xlsx                   | ✅ Ja                        | ✅ Ja     | ✅ Ja       | ✅ Beroende av Excel |
| Xlsb                   | ✅ Ja                        | ❌ Nej     | ❌ Nej       | ✅ Beroende av Excel |
| Xls                    | ✅ Ja                        | ❌ Nej     | ❌ Nej       | ✅ Beroende av Excel |
| Xlsm                   | ✅ Ja                        | ✅ Ja     | ✅ Ja       | ✅ Beroende av Excel |
| Xltm                   | ✅ Ja                        | ✅ Ja     | ✅ Ja       | ✅ Beroende av Excel |
| Xltx                   | ✅ Ja                        | ✅ Ja     | ✅ Ja       | ✅ Beroende av Excel |
| Csv                    | ✅ Ja                        | ❌ Nej     | ❌ Nej       | ✅ Beroende av Excel |
| Ods                    | ✅ Ja                        | ❌ Nej     | ❌ Nej       | ✅ Beroende av Excel |
| Html                   | ✅ Ja                        | ❌ Nej     | ❌ Nej       | ❌ Nej              |
| Numbers                | ✅ Ja                        | ❌ Nej     | ❌ Nej       | ❌ Nej              |
| Json                   | ✅ Ja                        | ❌ Nej     | ❌ Nej       | ❌ Nej              |
| Xml                    | ✅ Ja                        | ❌ Nej     | ❌ Nej       | ❌ Nej              |
| SpreadsheetML          | ✅ Ja                        | ❌ Nej     | ❌ Nej       | ❌ Nej              |

### Stödja kalkylbladsfunktioner

| Bibliotekets funktioner            |   Aspose.Cells for Go via C++ | Excelize         | Tealeg/xlsx | Go-OLE (Excel-appen) |
| :----------------------------    | :---------------------------- | :--------------- | :---------- | :----------  |
| Läsa/skriva (stöd för filformat)  | ✅ Ja                        | ✅ Ja          | ✅ Ja     | ✅ Ja   |
| Cell/Rad/Kolumn/Arbetsblad       | ✅ Ja                        | ✅ Ja          | ✅ Ja     | ✅ Ja   |
| Stil                              | ✅ Ja                       | ✅ Ja          | ✅ Ja     | ✅ Ja   |
| Formelberäkning                  | ✅ Ja                       | ✅ Ja (Del)   | ❌ Nej     | ✅ Ja (beräknad av Excel)  |
| Diagram/Bild                     | ✅ Ja                       | ✅ Ja (Del)   | ❌ Nej     | ✅ Ja   |
| PivotTabell                      | ✅ Ja                       | ✅ Ja          | ❌ Nej     | ✅ Ja   |
| Villkorsstyrd formatering        | ✅ Ja                       | ✅ Ja          | ❌ Nej     | ✅ Ja   |
| Datavalidering                   | ✅ Ja                       | ✅ Ja          | ❌ Nej     | ✅ Ja   |
| Kryptering/lösenordsskydd        | ✅ Ja                       | ✅ Ja          | ❌ Nej     | ✅ Ja   |
| Datavalidering                   | ✅ Ja                       | ✅ Ja          | ❌ Nej     | ✅ Ja   |
| VBA-makro                         | ✅ Ja Läsning                | ❌ Nej          | ❌ Nej     | ✅ Ja   |
| Datavalidering                   | ✅ Ja                       | ✅ Ja          | ❌ Nej     | ✅ Ja   |

## Prestanda jämförelse

- **Testmiljö**：
Processor: 12:e generationen Intel(R) Core(TM) i7-12700 (2,10 GHz)
Installerat RAM: 64,0 GB (63,7 GB tillgängligt)
Operativsystemsnamn: Microsoft Windows 11 Pro
Operativsystemversion: 10.0.26100
Operativsystemarkitektur: 64-bit
Go version: go version go1.24.5 windows/amd64
Aspose.Cells for Go via C++: 25.9.0
Excelize: 1.4.1

- **Testscenario**: antaget en stor fil, 10 arbetsblad, 100 000 rader x 250 kolumner, inklusive formatering

- **Körresultat**:
  - Excelize körs i 35 minuter (Starttid: 2025-10-09T10:04:16+08:00, Sluttid: 2025-10-09T10:39:53+08:00), genererad filstorlek: 1,11 GB.
  - Aspose.Cells for Go via C++ (modell 1) körs i 27 minuter (Starttid: 2025-10-09T10:57:55+08:00, Sluttid: 2025-10-09T11:16:24+08:00), genererad filstorlek: 936 MB.
  - Aspose.Cells for Go via C++ (modell 2) körs i 16 minuter (Starttid: 2025-10-09T12:01:26+08:00, Sluttid: 2025-10-09T12:17:17+08:00), genererad filstorlek: 1,16 GB.
