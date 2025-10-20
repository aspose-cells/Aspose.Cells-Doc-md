---
title: Custom Download Function for GridJs  
type: docs
weight: 260
url: /net/aspose-cells-gridjs/how-to-use-download-function/
description: This article describes how to implement custom download function for GridJs.
keywords: GridJs,download,file download,custom download,export,save file
aliases:
  - /net/aspose-cells-gridjs/download-function/
  - /net/aspose-cells-gridjs/how-to-add-download-function/
  - /net/aspose-cells-gridjs/custom-download/
---

 
# How to implement custom download function for GridJs

GridJs provides a flexible download mechanism that allows you to customize the file download behavior. You can set a custom download function to handle file downloads according to your requirements.

## Set Custom Download Function

GridJs provides the `setFileDownloadCallFunction` method to set a custom download function. When users click the download button, this function will be called with specific parameters.

### Basic Usage

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

## Function Parameters

The custom download function receives three parameters:

### 1. toFileName
- **Type**: String
- **Description**: The name of the file to be downloaded
- **Example**: `"myfile.xlsx"`, `"report.pdf"`

### 2. outputType
- **Type**: String
- **Description**: The output file format type
- **Possible Values**:
  - `Original` - Keep the original file format
  - `XLSX` - Export as Excel format
  - `PDF` - Export as PDF format
  - `HTML` - Export as HTML format

### 3. saveMode
- **Type**: String
- **Description**: The save destination mode
- **Possible Values**:
  - `Device` - Download to local device (default)
  - `GoogleDrive` - Save to Google Drive
  - `Dropbox` - Save to Dropbox

## Download Scenarios

GridJs supports multiple download scenarios based on different user actions:

### 1. Download as Different Formats

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

### 2. Save to Cloud Storage

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

## Notes

1. **Function Registration**: Make sure to call `setFileDownloadCallFunction` before users interact with the download functionality.

2. **Error Handling**: Always implement proper error handling in your custom download function to provide feedback to users.

3. **Async Operations**: If your download logic involves asynchronous operations (like API calls), make sure to handle promises appropriately.

4. **File Name Extension**: When the output type is not "Original", the file extension will be automatically adjusted to match the output type (e.g., `.xlsx`, `.pdf`, `.html`).

5. **Default Behavior**: If you don't set a custom download function, GridJs will use its default download behavior.

## See Also

- [Getting Started with GridJs](/net/aspose-cells-gridjs/getting-started/)
- [How to Build Online Excel Editor](/net/aspose-cells-gridjs/how-to-build-online-excel-editor/)
- [Server Side Configuration](/net/aspose-cells-gridjs/server-side-configuration/)
