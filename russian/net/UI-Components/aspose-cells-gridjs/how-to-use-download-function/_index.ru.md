---
title: Пользовательская функция скачивания для GridJs  
type: docs
weight: 260
url: /ru/net/aspose-cells-gridjs/how-to-use-download-function/
description: В этой статье описывается, как реализовать пользовательскую функцию скачивания для GridJs.
keywords: GridJs, скачивание, загрузка файла, пользовательская загрузка, экспорт, сохранение файла
aliases:
  - /net/aspose-cells-gridjs/download-function/
  - /net/aspose-cells-gridjs/how-to-add-download-function/
  - /net/aspose-cells-gridjs/custom-download/
---


# Как реализовать пользовательскую функцию скачивания для GridJs

GridJs предоставляет гибкий механизм скачивания, который позволяет настроить поведение загрузки файла. Вы можете задать функцию скачивания для обработки загрузки файла в соответствии с вашими требованиями.

## Установка пользовательской функции скачивания

GridJs предоставляет метод `setFileDownloadCallFunction` для установки пользовательской функции скачивания. Когда пользователь нажимает кнопку скачивания, эта функция вызывается с определёнными параметрами.

### Основное использование

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

## Параметры функции

Пользовательская функция скачивания принимает три параметра:

### 1. toFileName
- **Тип**: Строка
- **Описание**: Имя файла для загрузки
- **Пример**: `"myfile.xlsx"`, `"report.pdf"`

### 2. outputType
- **Тип**: Строка
- **Описание**: Тип формата выходного файла
- **Возможные значения**:
  - `Original` - Оставить исходный формат файла
  - `XLSX` - Экспортировать в формате Excel
  - `PDF` - Экспортировать в формате PDF
  - `HTML` - Экспортировать в формате HTML

### 3. saveMode
- **Тип**: Строка
- **Описание**: Режим назначения сохранения
- **Возможные значения**:
  - `Device` - Загрузить на устройство (по умолчанию)
  - `GoogleDrive` - Сохранить в Google Диск
  - `Dropbox` - Сохранить в Dropbox

## Сценарии загрузки

GridJs поддерживает несколько сценариев загрузки на основе различных действий пользователя:

### 1. Загрузка в разных форматах

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

### 2. Сохранение в облачное хранилище

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

## Замечания

1. **Регистрация функции**: Убедитесь, что вызвали `setFileDownloadCallFunction` до того, как пользователь начнет взаимодействовать с функцией загрузки.

2. **Обработка ошибок**: Всегда реализуйте правильную обработку ошибок в вашей пользовательской функции загрузки, чтобы предоставлять обратную связь пользователям.

3. **Асинхронные операции**: Если логика загрузки включает асинхронные операции (например, вызовы API), убедитесь, что промисы обрабатываются правильно.

4. **Расширение имени файла**: Когда тип вывода не "Original", расширение файла автоматически подстроится под тип вывода (например, `.xlsx`, `.pdf`, `.html`).

5. **Поведение по умолчанию**: Если вы не установите пользовательскую функцию загрузки, GridJs будет использовать свое стандартное поведение загрузки.

## См. также

- [Начало работы с GridJs](/net/aspose-cells-gridjs/getting-started/)
- [Как создать онлайн-редактор Excel](/net/aspose-cells-gridjs/how-to-build-online-excel-editor/)
- [Настройка на стороне сервера](/net/aspose-cells-gridjs/server-side-configuration/)
