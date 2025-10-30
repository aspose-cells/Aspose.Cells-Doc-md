---
title: GridJsのカスタムダウンロード機能  
type: docs
weight: 260
url: /ja/net/aspose-cells-gridjs/how-to-use-download-function/
description: この記事では、GridJsのカスタムダウンロード機能の実装方法を説明します。
keywords: GridJs、ダウンロード、ファイルダウンロード、カスタムダウンロード、エクスポート、ファイル保存
aliases:
  - /net/aspose-cells-gridjs/download-function/
  - /net/aspose-cells-gridjs/how-to-add-download-function/
  - /net/aspose-cells-gridjs/custom-download/
---


# GridJsにおけるカスタムダウンロード関数の実装方法

GridJsは、ファイルのダウンロード動作をカスタマイズできる柔軟なダウンロードメカニズムを提供します。要求に応じてカスタムダウンロード関数を設定できます。

## カスタムダウンロード関数の設定

GridJsは`setFileDownloadCallFunction`メソッドを提供し、カスタムダウンロード関数を設定します。ユーザーがダウンロードボタンをクリックすると、この関数が特定のパラメーターとともに呼び出されます。

### 基本的な使い方

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

## 関数のパラメータ

カスタムダウンロード関数は3つのパラメータを受け取ります:

### 1. toFileName
- **タイプ**: 文字列
- **説明**: ダウンロードするファイルの名前
- **例**: `"myfile.xlsx"`, `"report.pdf"`

### 2. outputType
- **タイプ**: 文字列
- **説明**: 出力ファイルフォーマットの種類
- **可能な値**:
  - `Original` - 元のファイル形式を維持
  - `XLSX` - Excel形式でエクスポート
  - `PDF` - PDF形式でエクスポート
  - `HTML` - HTML形式でエクスポート

### 3. saveMode
- **タイプ**: 文字列
- **説明**: 保存先モード
- **可能な値**:
  - `Device` - ローカルデバイスにダウンロード（デフォルト）
  - `GoogleDrive` - Googleドライブに保存
  - `Dropbox` - Dropboxに保存

## ダウンロードシナリオ

GridJsはさまざまなユーザー操作に基づくダウンロードシナリオをサポートします：

### 1. 異なるフォーマットとしてダウンロード

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

### 2. クラウドストレージに保存

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

## メモ

1. **機能登録**：ユーザーがダウンロード機能を操作する前に`setFileDownloadCallFunction`を呼び出してください。

2. **エラー処理**：カスタムダウンロード関数には適切なエラー処理を必ず実装し、ユーザーにフィードバックしてください。

3. **非同期操作**：API呼び出しなど非同期操作を含むダウンロードロジックの場合、約束（Promise）の適切な処理を行ってください。

4. **ファイル名拡張子**：出力タイプが"Original"でない場合、ファイル拡張子は出力タイプに自動的に合わせて調整されます（例：.xlsx, .pdf, .html）。

5. **デフォルトの挙動**：カスタムダウンロード関数を設定しない場合、GridJsはデフォルトのダウンロード動作を使用します。

## 関連項目

- [GridJsの始め方](/net/aspose-cells-gridjs/getting-started/)
- [オンラインExcelエディタの作り方](/net/aspose-cells-gridjs/how-to-build-online-excel-editor/)
- [サーバー側の設定](/net/aspose-cells-gridjs/server-side-configuration/)
