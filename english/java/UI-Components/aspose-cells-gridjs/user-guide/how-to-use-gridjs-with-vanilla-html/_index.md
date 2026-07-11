---
title: How to use GridJs with Vanilla HTML
description: Run the Vanilla HTML examples included with the GridJs npm package and understand their npm, CDN, Java backend, URL parameter, workbook loading, and runtime configuration.
keywords: x_spreadsheet, Vanilla HTML, vanilla-gridjs, gridjs-spreadsheet, JSZip, Vite, startGridJsDemo, permanent, highlight, GridJs2
type: docs
weight: 1
url: /java/aspose-cells-gridjs/user-guide/how-to-use-gridjs-with-vanilla-html/
---

## Introduction

The npm package includes two complete Vanilla HTML examples: `node_modules/gridjs-spreadsheet/example/vanilla-gridjs/npm` and `node_modules/gridjs-spreadsheet/example/vanilla-gridjs/script`. The npm version imports GridJs and JSZip as modules, while the script version loads them from CDN script tags. Both use `vanilla-gridjs/shared/demo-app.js` for the UI and workbook flow and use the Spring Boot backend at the root of the packaged `example` directory.

## How to use

### Get the examples from npm

Install `gridjs-spreadsheet`, then copy the packaged example outside `node_modules`:

```shell
npm install gridjs-spreadsheet
cp -R node_modules/gridjs-spreadsheet/example ./gridjs-example
cd gridjs-example
```

On Windows, copy `node_modules/gridjs-spreadsheet/example` to a writable project directory. The examples require Java 8 or newer, Node.js 18 or newer, and npm.

### Configure and start the Java backend

For a direct local run, change the `/app/...` values in `src/main/resources/application.properties` to absolute paths:

```properties
testconfig.ListDir=/absolute/path/gridjs-example/wb
testconfig.CachePath=/absolute/path/gridjs-example/grid_cache
testconfig.UploadPath=/absolute/path/gridjs-example/upload
testconfig.AsposeLicensePath=/absolute/path/Aspose.Cells.lic
```

`ListDir` provides the workbooks displayed by the Vanilla start page. `CachePath` and `UploadPath` must be writable. The current Java startup code checks whether the license file exists before applying it.

Start Spring Boot from `gridjs-example`:

```shell
./mvnw spring-boot:run -Dmaven.test.skip=true
```

On Windows:

```bat
mvnw.cmd spring-boot:run -Dmaven.test.skip=true
```

Verify the backend at `http://127.0.0.1:8080/gridjsdemo/api/health`.

### Run the Vanilla HTML npm example

Open another terminal in `gridjs-example`:

```shell
cd vanilla-gridjs/npm
npm install
npm run dev
```

Open `http://127.0.0.1:5175`.

`npm/main.js` imports the runtime, JSZip, and stylesheet from npm:

```javascript
import xSpreadsheet from 'gridjs-spreadsheet';
import JSZip from 'jszip';
import 'gridjs-spreadsheet/xspreadsheet.css';

window.JSZip = JSZip;
```

It passes the imported `xSpreadsheet` function to the shared demo code with the client name `vanilla-npm`.

### Run the Vanilla HTML script example

Open a terminal in the copied example directory:

```shell
cd vanilla-gridjs/script
npm install
npm run dev
```

Open `http://127.0.0.1:5176`.

`script/index.html` loads JSZip and GridJs from CDN URLs. `script/main.js` checks that `window.x_spreadsheet` is a function, then passes it to the same shared demo code with the client name `vanilla-script`. In this project, npm installs Vite for the development server; GridJs itself is loaded by the browser script tag.

Both Vite configurations proxy `/GridJs2` and `/gridjsdemo` to `http://127.0.0.1:8080`.

### Follow the shared demo flow

1. `startGridJsDemo` requests `/gridjsdemo/api/files` and creates one button for each workbook.
2. Select `permanent url load demo` or `highlight and custom context menu demo`.
3. Click a workbook. `pushRoute` records the workbook selection in the URL and `mountWorkbook` changes to the editor page.
4. `workbookEndpoint` chooses `/GridJs2/DetailStreamJsonWithUid` for `permanent`, `/GridJs2/DetailStreamJson` for `highlight`, or `/GridJs2/DetailStreamJsonWithUidFromUpload` for an uploaded file.
5. The example creates GridJs in `#grid-host`, loads `payload.data`, and applies the active worksheet and cell returned by Java.
6. Uploading an `.xlsx` file posts to `/gridjsdemo/api/upload`; the response supplies a generated server filename and UID used by the upload load endpoint.
7. The shared code listens for browser `popstate`, so back, forward, and refreshed URLs reopen the selected workbook.

The current source implements the second mode's load-path difference through `/DetailStreamJson` without UID. The visible label also mentions highlight and a custom context menu.

### Files used by the two examples

| File | Purpose |
| --- | --- |
| `vanilla-gridjs/npm/index.html` | Defines the npm demo start and editor pages. |
| `vanilla-gridjs/npm/main.js` | Imports GridJs, JSZip, CSS, and starts the shared application. |
| `vanilla-gridjs/script/index.html` | Defines the script demo UI and loads the CDN assets. |
| `vanilla-gridjs/script/main.js` | Validates and passes `window.x_spreadsheet` to the shared application. |
| `vanilla-gridjs/shared/demo-app.js` | Implements routing, file listing, upload, workbook loading, GridJs setup, and events. |
| `vanilla-gridjs/shared/styles.css` | Styles both start pages and editors. |
| `vanilla-gridjs/npm/vite.config.js` and `script/vite.config.js` | Proxy the relative API requests to Java. |

## JavaScript API

### Difference between the npm and script entries

| Form | GridJs source | Factory passed to `startGridJsDemo` | Development port |
| --- | --- | --- | --- |
| npm | `import xSpreadsheet from 'gridjs-spreadsheet'` | `xSpreadsheet` | 5175 |
| script | CDN `xspreadsheet.js` | `window.x_spreadsheet` | 5176 |

After the entry point supplies a factory, both examples execute the same call:

```javascript
startGridJsDemo({ clientName, createSpreadsheet });
```

`clientName` is included in generated UIDs and upload namespaces. `createSpreadsheet` must create the GridJs instance for `#grid-host`.

### Options used to create GridJs

| Option | Value in `demo-app.js` | Meaning in this example |
| --- | --- | --- |
| `updateMode` | `'server'` | Sends workbook edits to the configured server update URL. |
| `updateUrl` | `'/GridJs2/UpdateCell'` | Receives edited cell data. |
| `showToolbar` | `true` | Displays the toolbar. |
| `showContextmenu` | `true` | Enables the context menu. |
| `mode` | `'edit'` | Opens the workbook in editing mode. |
| `local` | `'en'` | Uses the English GridJs UI locale. |

The spreadsheet is created and loaded with the active worksheet returned by Java:

```javascript
spreadsheet = createSpreadsheet('#grid-host', options)
  .loadData(payload.data, payload.actname);
```

### Runtime methods used by the examples

| Method | Purpose in `demo-app.js` |
| --- | --- |
| `setUniqueId(payload.uniqueid)` | Stores the server UID on the GridJs instance. |
| `setFileName(current.file)` | Keeps the user-facing workbook name. |
| `setImageInfo(...)` | Configures image URL, upload, URL upload, and copy endpoints. |
| `setFileDownloadInfo('/GridJs2/Download')` | Configures workbook download. |
| `setOleDownloadInfo('/GridJs2/Ole')` | Configures OLE object download. |
| `setLazyLoadingUrl('/GridJs2/LazyLoadingStreamJson')` | Configures lazy worksheet loading. |
| `setOpenFileUrl('/')` | Returns the GridJs open-file action to the demo start page. |
| `setActiveSheetByName(...).setActiveCell(...)` | Restores the active sheet and cell returned by Java. |
| `change(...)` and `on(...)` | Log workbook, cell, and sheet events. |
| `updateCellError(...)` | Reports update errors in the console. |

### URL parameters

| Parameter | Meaning in the Vanilla examples |
| --- | --- |
| `file` | Original workbook name displayed in the UI. Without it, the start page is shown. |
| `storedFile` | Generated Java upload filename; defaults to `file` for listed workbooks. |
| `demo` | `permanent` or `highlight`. |
| `uid` | Cache identifier prefixed with `vanilla-npm` or `vanilla-script`. |
| `fromUpload` | A non-empty value chooses the upload load endpoint. |

### Backend endpoints used by the examples

| Endpoint | Purpose |
| --- | --- |
| `/gridjsdemo/api/health` | Checks the Java backend. |
| `/gridjsdemo/api/files` | Returns the workbook list. |
| `/gridjsdemo/api/upload` | Stores an uploaded workbook and returns route values. |
| `/GridJs2/DetailStreamJson` | Loads a listed workbook in `highlight` mode. |
| `/GridJs2/DetailStreamJsonWithUid` | Loads a listed workbook in `permanent` mode. |
| `/GridJs2/DetailStreamJsonWithUidFromUpload` | Loads an uploaded workbook. |
| `/GridJs2/UpdateCell` | Receives cell edits. |
| `/GridJs2/ImageUrl`, `/GridJs2/AddImage`, `/GridJs2/AddImageByURL`, `/GridJs2/CopyImage` | Support workbook image operations. |
| `/GridJs2/Download` and `/GridJs2/Ole` | Download the workbook or an OLE object. |
| `/GridJs2/LazyLoadingStreamJson` | Supplies lazy-loaded worksheet data. |

## Common Questions

Q: Where are the two complete Vanilla HTML projects in the npm package?
A: Use `node_modules/gridjs-spreadsheet/example/vanilla-gridjs/npm` and `node_modules/gridjs-spreadsheet/example/vanilla-gridjs/script`, after copying the complete `example` directory.

Q: Why does the script example still run `npm install`?
A: Its `package.json` installs Vite only. GridJs and JSZip are loaded from CDN tags in `script/index.html`.

Q: Why do the npm and script examples behave the same after startup?
A: Both pass a GridJs factory to `startGridJsDemo`, and all file, upload, route, option, and event behavior is implemented in `shared/demo-app.js`.

Q: Why does the file list fail while the HTML page still loads?
A: Vite can serve the frontend without Java. Start Spring Boot on port 8080 and verify `/gridjsdemo/api/health`.
