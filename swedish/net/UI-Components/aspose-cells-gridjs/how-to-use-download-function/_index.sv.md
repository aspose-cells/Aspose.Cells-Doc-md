---
title: Anpassad nedladdningsfunktion för GridJs  
type: docs
weight: 260
url: /sv/net/aspose-cells-gridjs/how-to-use-download-function/
description: Den här artikeln beskriver hur du implementerar en anpassad nedladdningsfunktion för GridJs.
keywords: GridJs, nedladdning, filnedladdning, anpassad nedladdning, export, spara fil
aliases:
  - /net/aspose-cells-gridjs/download-function/
  - /net/aspose-cells-gridjs/how-to-add-download-function/
  - /net/aspose-cells-gridjs/custom-download/
---


# Hur man implementerar en anpassad nedladdningsfunktion för GridJs

GridJs erbjuder en flexibel nedladdningsmekanism som låter dig anpassa filnedladdningsbeteendet. Du kan ställa in en anpassad nedladdningsfunktion för att hantera filnedladdningar enligt dina krav.

## Ställ in anpassad nedladdningsfunktion

GridJs tillhandahåller metoden `setFileDownloadCallFunction` för att ställa in en anpassad nedladdningsfunktion. När användare klickar på nedladdningsknappen, kommer denna funktion att anropas med specifika parametrar.

### Grundläggande användning

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

## Funktionsparametrar

Den anpassade nedladdningsfunktionen tar emot tre parametrar:

### 1. toFileName
- **Typ**: String
- **Beskrivning**: Filnamnet för filen som ska laddas ner
- **Exempel**: `"minfil.xlsx"`, `"rapport.pdf"`

### 2. outputType
- **Typ**: String
- **Beskrivning**: Utdatafilformatets typ
- **Möjliga värden**:
  - `Original` - Behåll det ursprungliga filformatet
  - `XLSX` - Exportera som Excel-format
  - `PDF` - Exportera som PDF-format
  - `HTML` - Exportera som HTML-format

### 3. saveMode
- **Typ**: String
- **Beskrivning**: Sätt för sparplats
- **Möjliga värden**:
  - `Device` - Ladda ner till lokal enhet (standard)
  - `GoogleDrive` - Spara till Google Drive
  - `Dropbox` - Spara till Dropbox

## Nedladdningsscenarier

GridJs stöder flera nedladdningsscenarier baserade på olika användaraktioner:

### 1. Ladda ner i olika format

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

### 2. Spara till molnlagring

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

## Noteringar

1. **Funktion Registrering**: Se till att anropa `setFileDownloadCallFunction` innan användare interagerar med nedladdningsfunktionen.

2. **Felhantering**: Implementera alltid korrekt felhantering i din anpassade nedladdningsfunktion för att ge feedback till användarna.

3. **Asynkrona operationer**: Om din nedladdningslogik involverar asynkrona operationer (som API-anrop), se till att hantera promises korrekt.

4. **Filnamnstillägg**: När utdata-typen inte är "Original" kommer filändelsen automatiskt att justeras för att matcha utdata-typen (t.ex. `.xlsx`, `.pdf`, `.html`).

5. **Standardbeteende**: Om du inte ställer in någon anpassad nedladdningsfunktion kommer GridJs att använda sitt standardbeteende för nedladdning.

## Se även

- [Komma igång med GridJs](/net/aspose-cells-gridjs/getting-started/)
- [Hur man bygger en online Excel-redigerare](/net/aspose-cells-gridjs/how-to-build-online-excel-editor/)
- [Serverkonfiguration](/net/aspose-cells-gridjs/server-side-configuration/)
