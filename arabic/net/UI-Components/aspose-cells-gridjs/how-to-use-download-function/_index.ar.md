---
title: دالة تحميل مخصصة لـ GridJs  
type: docs
weight: 260
url: /ar/net/aspose-cells-gridjs/how-to-use-download-function/
description: تصف هذه المقالة كيفية تنفيذ دالة تحميل مخصصة لـ GridJs.
keywords: GridJs، تحميل، تحميل ملف، تحميل مخصص، تصدير، حفظ ملف
aliases:
  - /net/aspose-cells-gridjs/download-function/
  - /net/aspose-cells-gridjs/how-to-add-download-function/
  - /net/aspose-cells-gridjs/custom-download/
---


# كيفية تنفيذ دالة تحميل مخصصة لـ GridJs

يقدم GridJs آلية مرنة للتحكم في تحميل الملفات تتيح لك تخصيص سلوك تنزيل الملف. يمكنك ضبط وظيفة تحميل مخصصة لمعالجة التنزيلات وفقًا لمتطلباتك.

## ضبط وظيفة تحميل مخصصة

يوفر GridJs طريقة `setFileDownloadCallFunction` لضبط وظيفة تحميل مخصصة. عند نقر المستخدمين على زر التحميل، سيتم استدعاء هذه الوظيفة بمعلمات محددة.

### الاستخدام الأساسي

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

## معلمات الوظيفة

تستقبل وظيفة التحميل المخصصة ثلاثة معلمات:

### 1. toFileName
- **النوع**: سلسلة
- **الوصف**: اسم الملف الذي سيتم تحميله
- **مثال**: `"myfile.xlsx"`، `"report.pdf"`

### 2. outputType
- **النوع**: سلسلة
- **الوصف**: نوع تنسيق ملف الإخراج
- **القيم الممكنة**:
  - `الأصلي` - الاحتفاظ بتنسيق الملف الأصلي
  - `XLSX` - تصدير بتنسيق إكسل
  - `PDF` - تصدير بصيغة PDF
  - `HTML` - تصدير بتنسيق HTML

### 3. saveMode
- **النوع**: سلسلة
- **الوصف**: وضع وجهة الحفظ
- **القيم الممكنة**:
  - `الجهاز` - التنزيل إلى الجهاز المحلي (افتراضي)
  - `GoogleDrive` - الحفظ على Google Drive
  - `Dropbox` - الحفظ على Dropbox

## سيناريوهات التنزيل

يدعم GridJs سيناريوهات تنزيل متعددة استنادًا إلى إجراءات المستخدم المختلفة:

### 1. التنزيل بصيغ مختلفة

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

### 2. الحفظ إلى التخزين السحابي

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

## ملاحظات

1. **تسجيل الوظيفة**: تأكد من استدعاء `setFileDownloadCallFunction` قبل تفاعل المستخدم مع وظيفة التنزيل.

2. **معالجة الأخطاء**: قم دائمًا بتنفيذ معالجة مناسبة للأخطاء في وظيفة التنزيل المخصصة الخاصة بك لتقديم ملاحظات للمستخدمين.

3. **العمليات غير المتزامنة**: إذا كانت منطق التنزيل الخاص بك يتضمن عمليات غير متزامنة (مثل استدعاءات API)، تأكد من معالجة الوعود بشكل مناسب.

4. **امتداد اسم الملف**: عندما يكون نوع الإخراج غير "أصلي"، سيتم تعديل امتداد الملف تلقائيًا ليتطابق مع نوع الإخراج (مثل `.xlsx`، `.pdf`، `.html`).

5. **السلوك الافتراضي**: إذا لم تقم بضبط وظيفة تنزيل مخصصة، فستستخدم GridJs السلوك الافتراضي للتنزيل.

## انظر أيضاً

- [البدء مع GridJs](/net/aspose-cells-gridjs/getting-started/)
- [كيفية بناء محرر Excel عبر الإنترنت](/net/aspose-cells-gridjs/how-to-build-online-excel-editor/)
- [إعدادات جانب الخادم](/net/aspose-cells-gridjs/server-side-configuration/)
