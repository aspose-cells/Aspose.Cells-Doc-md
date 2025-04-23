---
title: Versioning
type: docs
weight: 40
url: /it/go-cpp/versioning/
description: Come installare Aspose Cells per Go tramite C++ e creare un applicazione Hello World.
---

**github.com/aspose-cells/aspose-cells-go-cpp/v25** è un percorso del modulo Go che specifica una versione particolare di una libreria di terze parti. Analizziamo questo percorso del modulo e ne spieghiamo il significato:
Analisi del percorso del modulo

1. **Indirizzo del repository GitHub**: github.com/aspose-cells/aspose-cells-go-cpp

- Questa parte indica che la libreria è ospitata su GitHub, sotto l'organizzazione o l'utente aspose-cells, nel repository denominato aspose-cells-go-cpp.
- Aspose.Cells è una suite di API per la gestione e la manipolazione di file di fogli di calcolo (come Excel).

1. **Numero di versione**: /v25

- /v25 indica che questa è la versione 24 della libreria. Nei moduli Go, è supportata la versione semantica (SemVer), dove i percorsi contenenti /vN vengono usati per specificare esplicitamente il numero di versione principale.
- Quando la versione principale è maggiore o uguale a 2, il percorso del modulo deve includere il numero di versione per garantire compatibilità e isolamento tra diverse versioni principali.

### **Significato**

- **aspose-cells-go-cpp**: Questo è un binding del linguaggio Go per una libreria C++, che permette di usare le funzionalità di Aspose.Cells all'interno dei programmi Go per leggere, scrivere e manipolare file Excel, tra le altre operazioni.
- **v25**: Questo indica che si fa riferimento alla versione 24 della libreria. Versioni principali diverse possono introdurre cambiamenti incompatibili, quindi specificare il numero di versione è fondamentale per assicurarsi che il progetto dipenda dall'API e dal comportamento corretti.

### **Utilizzo**

Per usare v25 di aspose-cells-go-cpp nel tuo progetto Go, devi aggiungere la seguente riga al file go.mod del progetto:

```Go
require github.com/aspose-cells/aspose-cells-go-cpp/v25 v25.x.x
```

Sostituisci v25.x.x con i numeri specifici di versione minore e di patch, come v25.0.0. Puoi aggiungere e scaricare automaticamente questa dipendenza usando il comando go get:

```Go
go get github.com/aspose-cells/aspose-cells-go-cpp/v25@v25.x.x
```
