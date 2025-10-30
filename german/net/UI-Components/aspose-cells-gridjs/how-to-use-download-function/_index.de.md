---
title: Benutzerdefinierte Download Funktion für GridJs  
type: docs
weight: 260
url: /de/net/aspose-cells-gridjs/how-to-use-download-function/
description: Dieser Artikel beschreibt, wie man eine benutzerdefinierte Download Funktion für GridJs implementiert.
keywords: GridJs, Download, Dateidownload, benutzerdefinierter Download, Export, Datei speichern
aliases:
  - /net/aspose-cells-gridjs/download-function/
  - /net/aspose-cells-gridjs/how-to-add-download-function/
  - /net/aspose-cells-gridjs/custom-download/
---


# Wie man eine benutzerdefinierte Download-Funktion für GridJs implementiert

GridJs bietet einen flexiblen Download-Mechanismus, mit dem Sie das Verhalten beim Herunterladen von Dateien anpassen können. Sie können eine benutzerdefinierte Download-Funktion festlegen, um den Datei-Download nach Ihren Anforderungen zu steuern.

## Benutzerspezifische Download-Funktion festlegen

GridJs stellt die Methode `setFileDownloadCallFunction` bereit, um eine benutzerdefinierte Download-Funktion festzulegen. Wenn Benutzer auf die Download-Schaltfläche klicken, wird diese Funktion mit bestimmten Parametern aufgerufen.

### Grundlegende Verwendung

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

## Funktionsparameter

Die benutzerdefinierte Download-Funktion erhält drei Parameter:

### 1. toFileName
- **Typ**: String
- **Beschreibung**: Der Name der herunterzuladenden Datei
- **Beispiel**: `"meinedatei.xlsx"`, `"bericht.pdf"`

### 2. outputType
- **Typ**: String
- **Beschreibung**: Der Ausgabe-Dateityp
- **Mögliche Werte**:
  - `Original` - Beibehaltung des ursprünglichen Dateiformats
  - `XLSX` - Export im Excel-Format
  - `PDF` - Export im PDF-Format
  - `HTML` - Export im HTML-Format

### 3. saveMode
- **Typ**: String
- **Beschreibung**: Der Modus des Speicherziels
- **Mögliche Werte**:
  - `Gerät` - Download auf das lokale Gerät (Standard)
  - `GoogleDrive` - Speichern auf Google Drive
  - `Dropbox` - Speichern auf Dropbox

## Download-Szenarien

GridJs unterstützt mehrere Download-Szenarien basierend auf unterschiedlichen Benutzeraktionen:

### 1. Download in Verschiedenen Formaten

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

### 2. Speichern in Cloud-Speicher

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

## Hinweise

1. **Funktionsregistrierung**: Stellen Sie sicher, dass Sie `setFileDownloadCallFunction` aufrufen, bevor Nutzer mit der Download-Funktion interagieren.

2. **Fehlerbehandlung**: Implementieren Sie stets eine ordnungsgemäße Fehlerbehandlung in Ihrer benutzerdefinierten Download-Funktion, um Feedback an die Nutzer zu geben.

3. **Asynchrone Operationen**: Wenn Ihre Download-Logik asynchrone Operationen umfasst (wie API-Aufrufe), stellen Sie sicher, dass Sie Promises ordnungsgemäß behandeln.

4. **Dateinamen-Erweiterung**: Wenn der Ausgabetyp nicht "Original" ist, wird die Dateierweiterung automatisch an den Ausgabetyp angepasst (z.B. `.xlsx`, `.pdf`, `.html`).

5. **Standardverhalten**: Wenn Sie keine benutzerdefinierte Download-Funktion festlegen, verwendet GridJs sein Standard-Downloadverhalten.

## Siehe auch

- [Erste Schritte mit GridJs](/net/aspose-cells-gridjs/getting-started/)
- [Wie man einen Online-Excel-Editor erstellt](/net/aspose-cells-gridjs/how-to-build-online-excel-editor/)
- [Serverseitige Konfiguration](/net/aspose-cells-gridjs/server-side-configuration/)
