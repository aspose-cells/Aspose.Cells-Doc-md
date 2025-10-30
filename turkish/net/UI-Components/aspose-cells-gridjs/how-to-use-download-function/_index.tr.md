---
title: GridJs için Özel İndirme Fonksiyonu  
type: docs
weight: 260
url: /tr/net/aspose-cells-gridjs/how-to-use-download-function/
description: Bu makale GridJs için nasıl özel indirme fonksiyonu uygulanacağını anlatmaktadır.
keywords: GridJs, indirme, dosya indirme, özel indirme, dışa aktarım, dosya kaydetme
aliases:
  - /net/aspose-cells-gridjs/download-function/
  - /net/aspose-cells-gridjs/how-to-add-download-function/
  - /net/aspose-cells-gridjs/custom-download/
---


# GridJs için özel indirme fonksiyonu nasıl uygulanır

GridJs, dosya indirme davranışını özelleştirmenize izin veren esnek bir indirme mekanizması sağlar. Dosya indirme işlemini ihtiyaçlarınıza göre ayarlamak için özel bir indirme fonksiyonu belirleyebilirsiniz.

## Özel İndirme Fonksiyonu Ayarlama

GridJs, `setFileDownloadCallFunction` metodunu kullanarak özel bir indirme fonksiyonu ayarlamanıza imkan tanır. Kullanıcılar indirme düğmesine tıkladığında, bu fonksiyon belirli parametrelerle çağrılır.

### Temel Kullanım

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

## Fonksiyon Parametreleri

Özel indirme fonksiyonu üç parametre alır:

### 1. toFileName
- **Türü**: String
- **Açıklama**: İndirilecek dosyanın adı
- **Örnek**: `"myfile.xlsx"`, `"rapor.pdf"`

### 2. outputType
- **Türü**: String
- **Açıklama**: Çıktı dosya formatı tipi
- **Olası Değerler**:
  - `Original` - Orijinal dosya formatını koru
  - `XLSX` - Excel formatında dışa aktar
  - `PDF` - PDF formatında dışa aktar
  - `HTML` - HTML formatında dışa aktar

### 3. saveMode
- **Türü**: String
- **Açıklama**: Kaydetme hedef modu
- **Olası Değerler**:
  - `Device` - Yerel cihaza indir (varsayılan)
  - `GoogleDrive` - Google Drive'a kaydet
  - `Dropbox` - Dropbox'a kaydet

## İndirme Senaryoları

GridJs farklı kullanıcı eylemlerine dayalı çoklu indirme senaryolarını destekler:

### 1. Farklı Formatlarda İndir

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

### 2. Bulut Depolamaya Kaydet

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

## Notlar

1. **Fonksiyon Kaydı**: Kullanıcılar indirme fonksiyonuyla etkileşime geçmeden önce `setFileDownloadCallFunction` çağrısını yaptığınızdan emin olun.

2. **Hata Yönetimi**: Özelleştirilmiş indirme fonksiyonunuzda uygun hata yönetimi uygulayarak kullanıcılara geri bildirim sağlayın.

3. **Async İşlemler**: İndirme mantığınız asenkron işlemler (API çağrıları gibi) içeriyorsa, promise'leri uygun şekilde yönetin.

4. **Dosya Adı Uzantısı**: Çıktı tipi "Original" değilse, dosya uzantısı otomatik olarak çıktı tipine uygun hale getirilecektir (örneğin `.xlsx`, `.pdf`, `.html`).

5. **Varsayılan Davranış**: Özelleştirilmiş bir indirme fonksiyonu ayarlamazsanız, GridJs varsayılan indirme davranışını kullanır.

## Ayrıca Bakınız

- [GridJs ile Başlarken](/net/aspose-cells-gridjs/getting-started/)
- [Çevrimiçi Excel Düzenleyici Nasıl Oluşturulur](/net/aspose-cells-gridjs/how-to-build-online-excel-editor/)
- [Sunucu Tarafı Konfigürasyonu](/net/aspose-cells-gridjs/server-side-configuration/)
