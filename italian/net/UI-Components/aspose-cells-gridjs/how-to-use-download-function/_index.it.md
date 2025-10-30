---
title: Funzione di download personalizzata per GridJs  
type: docs
weight: 260
url: /it/net/aspose-cells-gridjs/how-to-use-download-function/
description: Questo articolo descrive come implementare una funzione di download personalizzata per GridJs.
keywords: GridJs,download,download file,download personalizzato, esporta, salva file
aliases:
  - /net/aspose-cells-gridjs/download-function/
  - /net/aspose-cells-gridjs/how-to-add-download-function/
  - /net/aspose-cells-gridjs/custom-download/
---


# Come implementare una funzione di download personalizzata per GridJs

GridJs fornisce un meccanismo di download flessibile che permette di personalizzare il comportamento di download dei file. Puoi impostare una funzione di download personalizzata per gestire i download dei file secondo le tue esigenze.

## Imposta funzione di download personalizzata

GridJs fornisce il metodo `setFileDownloadCallFunction` per impostare una funzione di download personalizzata. Quando gli utenti cliccano sul pulsante di download, questa funzione verrà chiamata con parametri specifici.

### Uso di base

```javascript
// Define your custom download function
function customDownloadHandler(toFileName, outputType, saveMode) {
    console.log('File Name:', toFileName);
    console.log('Output Type:', outputType);
    console.log('Save Mode:', saveMode);

    // Implement your custom download logic here
    // For example: upload to cloud storage, save to custom location, etc.
}

// Set the custom download function
xs.setFileDownloadCallFunction(customDownloadHandler);
```

## Parametri della funzione

La funzione di download personalizzata riceve tre parametri:

### 1. toFileName
- **Tipo**: Stringa
- **Descrizione**: Il nome del file da scaricare
- **Esempio**: `"miofile.xlsx"`, `"report.pdf"`

### 2. outputType
- **Tipo**: Stringa
- **Descrizione**: Il tipo di formato del file di output
- **Valori Possibili**:
  - `Originale` - Mantieni il formato originale del file
  - `XLSX` - Esporta in formato Excel
  - `PDF` - Esporta in formato PDF
  - `HTML` - Esporta in formato HTML

### 3. saveMode
- **Tipo**: Stringa
- **Descrizione**: La modalità di destinazione del salvataggio
- **Valori Possibili**:
  - `Device` - Scarica sul dispositivo locale (predefinito)
  - `GoogleDrive` - Salva su Google Drive
  - `Dropbox` - Salva su Dropbox

## Scenari di download

GridJs supporta molteplici scenari di download basati su diverse azioni utente:

### 1. Scarica in formati diversi

```javascript
function customDownloadHandler(toFileName, outputType, saveMode) {
    switch(outputType) {
        case 'Original':
            // Handle original format download
            downloadAsOriginal(toFileName);
            break;
        case 'XLSX':
            // Handle Excel format download
            downloadAsExcel(toFileName);
            break;
        case 'PDF':
            // Handle PDF format download
            downloadAsPDF(toFileName);
            break;
        case 'HTML':
            // Handle HTML format download
            downloadAsHTML(toFileName);
            break;
    }
}

xs.setFileDownloadCallFunction(customDownloadHandler);
```

### 2. Salva nel cloud storage

```javascript
function customDownloadHandler(toFileName, outputType, saveMode) {
    if (saveMode === 'GoogleDrive') {
        // Implement Google Drive upload logic
        uploadToGoogleDrive(toFileName, outputType);
    } else if (saveMode === 'Dropbox') {
        // Implement Dropbox upload logic
        uploadToDropbox(toFileName, outputType);
    } else {
        // Default: download to device
        downloadToDevice(toFileName, outputType);
    }
}

xs.setFileDownloadCallFunction(customDownloadHandler);
```

## Note

1. **Registrazione funzione**: assicurarsi di chiamare `setFileDownloadCallFunction` prima che gli utenti interagiscano con la funzionalità di download.

2. **Gestione errori**: implementare sempre una corretta gestione degli errori nella funzione di download personalizzata per fornire feedback agli utenti.

3. **Operazioni asincrone**: se la logica di download coinvolge operazioni asincrone (come chiamate API), assicurarsi di gestire correttamente le promesse.

4. **Estensione del nome del file**: quando il tipo di output non è "Originale", l'estensione del file sarà automaticamente regolata per corrispondere al tipo di output (ad esempio, `.xlsx`, `.pdf`, `.html`).

5. **Comportamento di default**: se non si impostano funzioni di download personalizzate, GridJs utilizzerà il suo comportamento di download predefinito.

## Vedi Anche

- [Inizia con GridJs](/net/aspose-cells-gridjs/getting-started/)
- [Come costruire un editor Excel online](/net/aspose-cells-gridjs/how-to-build-online-excel-editor/)
- [Configurazione del lato server](/net/aspose-cells-gridjs/server-side-configuration/)
