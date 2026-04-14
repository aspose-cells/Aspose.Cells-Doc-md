---
title: How to configure token authentication
description: Configure a GridJs token so supported server requests add an Authorization Bearer header, and refresh the token on the spreadsheet instance when it changes.
keywords: token, authToken, refreshToken, Authorization, Bearer, AjaxTask, setLazyLoadingUrl, setImageInfo, setFileDownloadInfo
type: docs
weight: 1
url: /java/aspose-cells-gridjs/user-guide/how-to-configure-token-authentication/
aliases:
- /java/aspose-cells-gridjs/user-guide/how-to-configure-token-authentication/
---

## Introduction

GridJs stores the constructor option `token` as `authToken` on the spreadsheet instance. When `authToken` has a value, the inspected request code adds an `Authorization` header with the value `Bearer ${authToken}`. The same instance also exposes `refreshToken(token)`, which replaces the stored token value.

## How to use

No UI operation entry was found in the inspected code. Token authentication is configured from JavaScript when the spreadsheet instance is created or when the token value changes.

1. Create the spreadsheet instance with a `token` option.

```js
const xs = x_spreadsheet('#gridjs-demo-uid', {
  token: accessToken,
});
```

2. Configure the server URLs that your page uses. The inspected code applies the stored token only on request paths that read `authToken`.

```js
xs.setLazyLoadingUrl('/GridJs2/LazyLoading');
xs.setImageInfo('/GridJs2/GetImage', '/GridJs2/UploadImage', '/GridJs2/UploadImageByUrl', '/GridJs2/CopyImage', 0);
xs.setFileDownloadInfo('/GridJs2/Download');
```

3. When the token changes, call `refreshToken(token)` on the same spreadsheet instance.

```js
xs.refreshToken(newAccessToken);
```

4. When a supported request runs and the stored token is not empty, GridJs sends the request with this header:

```text
Authorization: Bearer <token>
```

## JavaScript API

Pass `token` in the options object when creating the spreadsheet. The constructor stores it as `this.authToken`; if no token is provided, `authToken` is set to `null`.

```js
const xs = x_spreadsheet('#gridjs-demo-uid', {
  token: accessToken,
});
```

Use `refreshToken(token)` to replace the stored token after the spreadsheet has already been created.

```js
xs.refreshToken(newAccessToken);
```

### Relevant functions
| Function / Location | Description | Parameters | Returns |
|----------|-------------|------------|---------|
| `Spreadsheet(selectors, options = {})` (`index.js`) | Stores `options.token` as `this.authToken`, or stores `null` when no token is provided. | `selectors`: container selector or element; `options.token`: token value | `Spreadsheet` instance |
| `refreshToken(token)` (`index.js`) | Replaces the stored `authToken` value on the spreadsheet instance. | `token`: new token value | `void` |
| `AjaxTask(item, url, token, callback, callbackerror)` (`index.js`) | Stores the token passed by server-update code before the task is handled. | `item`, `url`, `token`, `callback`, `callbackerror` | `AjaxTask` instance |
| `taskHandler(task, cb)` (`index.js`) | Sends the queued Ajax task and sets `Authorization: Bearer ${task.token}` before send when `task.token` exists. | `task`: `AjaxTask`; `cb`: completion callback | `void` |
| `d.updateCellServer(operationdata)` (`index.js`) | When `settings.updateMode === 'server'` and the sheet is not collaborative, appends an `AjaxTask` to `settings.updateUrl` with `authToken`. | `operationdata`: operation payload | `void` |
| `loadSheetDataLazily(data)` (`index.js`) | Posts lazy-loaded sheet data to `lazyLoadingUrl` and includes the Bearer header when `this.authToken` exists. | `data`: sheet data object | `Promise` |
| `downloadFile(toFileName, saveType)` (`component/sheet.js`) | Posts export data to `fileDownloadUrl` and includes the Bearer header when `authToken` exists. | `toFileName`, `saveType` | `Promise<void>` |
| `fileLinkToStreamDownload(url, fileName, authToken)` (`component/sheet.js`) | Downloads a returned file URL with `XMLHttpRequest` and includes the Bearer header when `authToken` exists. | `url`, `fileName`, `authToken` | `void` |
| `postImageReq(sheet, reqdata, cb)` (`component/imageOperations/paste.js`) | Posts image upload data to `sheet.imageUploadByLocalUrl` and includes the Bearer header when `authToken` exists. | `sheet`, `reqdata`, `cb` | `void` |
| `Paste.addImageToData(clonedObj)` (`component/imageOperations/paste.js`) | Posts copied image data to `sheet.imageCopyUrl` and includes the Bearer header when `authToken` exists. | `clonedObj`: copied image object | `Promise` |

The inspected `index.d.ts` file does not declare `token` in the `Options` interface and does not declare `refreshToken(token)` on the `Spreadsheet` class, but the `index.js` implementation reads `options.token` and exposes `refreshToken(token)` directly.

## Common Questions

Q: Where is the initial token configured?
A: The inspected constructor reads `options.token` and stores it as `this.authToken`.

Q: Can the token be changed after the spreadsheet is created?
A: Yes. The inspected `refreshToken(token)` method assigns the new value to `this.authToken`.

Q: What request header does GridJs add?
A: When the relevant request path has a token value, GridJs sets `Authorization` to `Bearer ${token}`.

Q: Does every request in the inspected code use this token?
A: No. The tutorial only lists request paths where the inspected code reads `authToken` or passes it into `AjaxTask`.
