---
title: Confronto delle funzionalità e delle prestazioni di Aspose.Cells per Go via C con Excelize, Tealeg/xlsx e Go OLE.
linktitle: Confronto delle funzionalità e delle prestazioni
type: docs
weight: 40
url: /it/go-cpp/comparison-of-functionality-and-performance/
description: Confronto delle funzionalità e delle prestazioni di Aspose.Cells per Go via C con Excelize, Tealeg/xlsx e Go OLE.
keywords: Aspose.Cells, Excel, finestra di watch della formula, celle, aggiunta, C++
---

Il seguente è un confronto completo di Aspose.Cells per Go (via C) con altre librerie principali di elaborazione Excel in linguaggio Go (Excelize, tealeg/xlsx, go-ole) in termini di funzionalità, prestazioni e casi d'uso.

## Differenze di posizionamento e struttura di base

| Nome della libreria    |   Tipo                         | Implementazione sottostante        | Dipendenza CGO         | Distribuzione multipiattaforma |
| :------------------- | :----------------------------- | :--------------------------------- | :----------------------- | :-----------------------  |
| Aspose.Cells per Go   | Libreria commerciale (MIT/Pagata) | Motore nativo, Wrapper CGO Go      |  ✅  Sì                 | Supporto per Windows, Linux |
| Excelize             | Libreria open source (MIT)      | Implementazione pura in Go            |  ❌  No                  | Supporto per Windows, Linux, MacOS |
| tealeg/xlsx          | Libreria open source (BSD)      | Implementazione pura in Go            |  ❌  No                  | Supporto per Windows, Linux, MacOS |
| go-ole               | Libreria open source (BSD)      | Interfaccia OLE/COM di Windows in Go  |  ✅  Sì (solo Windows)  | Solo Windows |

### Differenze chiave

- Aspose.Cells for Go via C++ è una libreria commerciale di livello industriale con le funzioni più complete, ma è necessario un prodotto a pagamento.
- Excelize è attualmente la libreria Go open source più attiva, in pura Go.
- Tealeg/xlsx è una libreria open source precoce con funzioni più basilari e manutenzione lenta.
- Go-ole è uno schema di automazione COM solo Windows che si basa sull'installazione di Excel e non è raccomandato per ambienti server.

## Confronto delle funzionalità

### Confronto dei formati di file supportati

| Formato Foglio di Calcolo |   Aspose.Cells for Go via C++ | Excelize | Tealeg/xlsx | Go-OLE (Applicazione Excel) |
| :--------------------- | :---------------------------- | :---------- | :---------- | :-------------------  |
| Xlsx | ✅ Sì | ✅ Sì | ✅ Sì | ✅ Dipende da Excel |
| Xlsb | ✅ Sì | ❌ No | ❌ No | ✅ Dipende da Excel |
| Xls | ✅ Sì | ❌ No | ❌ No | ✅ Dipende da Excel |
| Xlsm | ✅ Sì | ✅ Sì | ✅ Sì | ✅ Dipende da Excel |
| Xltm | ✅ Sì | ✅ Sì | ✅ Sì | ✅ Dipende da Excel |
| Xltx | ✅ Sì | ✅ Sì | ✅ Sì | ✅ Dipende da Excel |
| Csv | ✅ Sì | ❌ No | ❌ No | ✅ Dipende da Excel |
| Ods | ✅ Sì | ❌ No | ❌ No | ✅ Dipende da Excel |
| Html | ✅ Sì | ❌ No | ❌ No | ❌ No |
| Numbers | ✅ Sì | ❌ No | ❌ No | ❌ No |
| Json | ✅ Sì | ❌ No | ❌ No | ❌ No |
| Xml | ✅ Sì | ❌ No | ❌ No | ❌ No |
| SpreadsheetML | ✅ Sì | ❌ No | ❌ No | ❌ No |

### Funzionalità supportate dei fogli di calcolo

| Funzioni della libreria |   Aspose.Cells for Go via C++ | Excelize | Tealeg/xlsx | Go-OLE (Applicazione Excel) |
| :----------------------------    | :---------------------------- | :--------------- | :---------- | :----------  |
| Lettura/Scrittura (supporto formato file) | ✅ Sì | ✅ Sì | ✅ Sì | ✅ Sì |
| Cella/Riga/Colonna/Foglio di lavoro | ✅ Sì | ✅ Sì | ✅ Sì | ✅ Sì |
| Stile                            | ✅ Sì                        | ✅ Sì          | ✅ Sì     | ✅ Sì   |
| Calcolo formula                  | ✅ Sì                        | ✅ Sì (parte)   | ❌ No     | ✅ Sì (calcolato da Excel)  |
| Grafico/Immagine                | ✅ Sì                        | ✅ Sì (parte)   | ❌ No     | ✅ Sì   |
| Tabella pivot                    | ✅ Sì                        | ✅ Sì          | ❌ No     | ✅ Sì   |
| Formattazione condizionale       | ✅ Sì                        | ✅ Sì          | ❌ No     | ✅ Sì   |
| Convalida dati                  | ✅ Sì                        | ✅ Sì          | ❌ No     | ✅ Sì   |
| Crittografia/protezione con password | ✅ Sì                      | ✅ Sì          | ❌ No     | ✅ Sì   |
| Convalida dati                  | ✅ Sì                        | ✅ Sì          | ❌ No     | ✅ Sì   |
| Macro VBA                        | ✅ Sì Lettura                | ❌ No          | ❌ No     | ✅ Sì   |
| Convalida dati                  | ✅ Sì                        | ✅ Sì          | ❌ No     | ✅ Sì   |

## Confronto delle prestazioni

- **Ambiente di test**：
Processore: Intel(R) Core(TM) i7-12700 di 12a generazione (2,10 GHz)
RAM installata: 64,0 GB (63,7 GB utilizzabili)
OsNome: Microsoft Windows 11 Pro
Versione Os: 10.0.26100
Architettura Os: 64-bit
Versione Go: go versione go1.24.5 windows/amd64
Aspose.Cells for Go via C++: 25.9.0
Excelize: 1.4.1

- **Scenario di test**: assumendo un file di grandi dimensioni, 10 fogli di lavoro, 100.000 righe x 250 colonne, inclusa la formattazione

- **Risultati dell'esecuzione**:
  - Excelize viene eseguito per 35 minuti (Ora di inizio: 2025-10-09T10:04:16+08:00, Ora di fine: 2025-10-09T10:39:53+08:00), dimensione del file generato: 1,11 GB.
  - Aspose.Cells for Go via C++(richieste 1) eseguito per 27 minuti (Ora di inizio: 2025-10-09T10:57:55+08:00, Ora di fine: 2025-10-09T11:16:24+08:00), dimensione del file generato: 936MB.
  - Aspose.Cells for Go via C++(richieste 2) eseguito per 16 minuti (Ora di inizio: 2025-10-09T12:01:26+08:00, Ora di fine: 2025-10-09T12:17:17+08:00), dimensione del file generato: 1,16GB.
