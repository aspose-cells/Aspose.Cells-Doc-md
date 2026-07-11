---
title: How to use GridJs in Vue
description: Run the Vue example included with the GridJs npm package and understand how it uses a shared Java backend for workbook listing, upload, loading, editing, and URL routing.
keywords: GridJsSpreadsheet, Vue, vue-gridjs, gridjs-spreadsheet, Java, Vite, ref, watch, permanent, highlight, GridJs2
type: docs
weight: 1
url: /java/aspose-cells-gridjs/user-guide/how-to-use-gridjs-in-vue/
---

## Introduction

The complete Vue 3 example is included in the npm package at `node_modules/gridjs-spreadsheet/example/vue-gridjs`. The Spring Boot application at the root of the packaged `example` directory supplies workbook files and GridJs endpoints. The Vue demo displays a start page for selecting or uploading a workbook, then passes the loaded workbook JSON to `GridJsSpreadsheet` on a full-page editor.

## How to use

### Get the example from npm

Install `gridjs-spreadsheet`, then copy its complete example to a writable directory:

```shell
npm install gridjs-spreadsheet
cp -R node_modules/gridjs-spreadsheet/example ./gridjs-example
cd gridjs-example
```

On Windows, copy `node_modules/gridjs-spreadsheet/example` to a normal project directory and open a terminal there. The example requires Java 8 or newer, Node.js 18 or newer, and npm.

### Configure and start the Java backend

For local development, replace the `/app/...` Docker paths in `src/main/resources/application.properties` with absolute local paths:

```properties
testconfig.ListDir=/absolute/path/gridjs-example/wb
testconfig.CachePath=/absolute/path/gridjs-example/grid_cache
testconfig.UploadPath=/absolute/path/gridjs-example/upload
testconfig.AsposeLicensePath=/absolute/path/Aspose.Cells.lic
```

`ListDir` supplies the start-page file list. `CachePath` and `UploadPath` must be writable. When the configured license file does not exist, the current Java entry point continues without calling `setLicense`.

Start Java from `gridjs-example`:

```shell
./mvnw spring-boot:run -Dmaven.test.skip=true
```

On Windows:

```bat
mvnw.cmd spring-boot:run -Dmaven.test.skip=true
```

Verify `http://127.0.0.1:8080/gridjsdemo/api/health` before starting Vue.

### Start the Vue demo

Open a second terminal in `gridjs-example`:

```shell
cd vue-gridjs
npm install
npm run dev
```

Open `http://127.0.0.1:5174`.

`vue-gridjs/vite.config.js` proxies `/GridJs2` and `/gridjsdemo` to `http://127.0.0.1:8080`. The Vue application can therefore call the Java endpoints with relative URLs.

### Follow the demo flow

1. `App.vue` requests `/gridjsdemo/api/files` and stores the returned names in the `files` ref.
2. Select `permanent url load demo` or `highlight and custom context menu demo`, then click a workbook.
3. `openWorkbook` writes `file`, `demo`, and the applicable UID values to the URL.
4. `watch(current, loadWorkbook, { immediate: true })` reloads workbook JSON whenever the current route changes.
5. `permanent` mode calls `/GridJs2/DetailStreamJsonWithUid`; `highlight` mode calls `/GridJs2/DetailStreamJson`.
6. The returned payload is stored in `workbookData`. The template renders `GridJsSpreadsheet` with the `data` prop when that value is available.
7. Uploading an `.xlsx` file posts to `/gridjsdemo/api/upload`, then loads the generated `storedFile` through `/GridJs2/DetailStreamJsonWithUidFromUpload`.

The computed `workbookKey` changes with the loaded workbook and demo mode, causing Vue to remount the GridJs component for a different workbook. The current source implements the second demo mode through the non-UID load route; the UI label also mentions highlight and a custom context menu.

### Source files used by the demo

| File | Purpose |
| --- | --- |
| `vue-gridjs/src/main.js` | Imports the GridJs stylesheet and mounts the Vue application. |
| `vue-gridjs/src/App.vue` | Contains component state, file list, upload logic, workbook loading, markup, and events. |
| `vue-gridjs/src/routing.js` | Reads and writes URL state and creates Vue-specific UIDs. |
| `vue-gridjs/src/api.js` | Wraps `fetch` and reports non-success responses. |
| `vue-gridjs/vite.config.js` | Configures Vue and proxies Java API paths. |

## JavaScript API

### Import and render the Vue wrapper

The demo imports the named Vue export and stylesheet:

```javascript
import { GridJsSpreadsheet } from 'gridjs-spreadsheet/vue';
import 'gridjs-spreadsheet/xspreadsheet.css';
```

The template renders the wrapper after `loadWorkbook` sets `workbookData`:

```vue
<GridJsSpreadsheet
  v-if="workbookData"
  :data="workbookData"
  height="100vh"
  :show-toolbar="true"
  :show-contextmenu="true"
  @ready="onReady"
  @error="onError"
/>
```

The demo uses these Vue props and events:

| Prop or event | Use in the example |
| --- | --- |
| `data` | Receives the workbook payload returned by Java. |
| `height` | Sets the editor height to `100vh`. |
| `show-toolbar` | Displays the GridJs toolbar. |
| `show-contextmenu` | Enables the GridJs context menu. |
| `ready` | Restores the active sheet and cell and sets the open-file URL to `/`. |
| `change` | Logs that workbook data changed. |
| `error` | Logs a GridJs error payload. |
| `cell-selected`, `cell-edited`, `sheet-selected` | Log user interaction details. |

### URL parameters

| Parameter | Meaning in the Vue demo |
| --- | --- |
| `file` | Workbook name shown in the UI. Without it, Vue renders the start page. |
| `storedFile` | Server-side filename used after upload. It defaults to `file`. |
| `demo` | `permanent` or `highlight`; other values become `permanent`. |
| `uid` | Vue-prefixed cache identifier used for UID-based loading. |
| `fromUpload` | A non-empty value selects the upload-directory endpoint. |

### Backend endpoints used by the Vue demo

| Endpoint | Purpose |
| --- | --- |
| `/gridjsdemo/api/health` | Checks the Java backend. |
| `/gridjsdemo/api/files` | Returns the workbook directory and file list. |
| `/gridjsdemo/api/upload` | Saves an upload and returns its display and stored names. |
| `/GridJs2/DetailStreamJson` | Loads a workbook in `highlight` mode. |
| `/GridJs2/DetailStreamJsonWithUid` | Loads a workbook in `permanent` mode. |
| `/GridJs2/DetailStreamJsonWithUidFromUpload` | Loads a workbook from the upload directory. |

The npm wrapper supplies the standard GridJs update, image, download, OLE, and lazy-loading endpoint configuration under `/GridJs2`.

## Common Questions

Q: Where is the complete Vue project in the npm package?
A: Use `node_modules/gridjs-spreadsheet/example/vue-gridjs`, after copying the complete `example` directory outside `node_modules`.

Q: Why does the editor temporarily show a loading message?
A: `loadWorkbook` clears `workbookData` before requesting the next payload. The template shows `status` until the data is available.

Q: Why does a proxy error appear on port 5174?
A: The Vite proxy cannot reach the Java backend. Start Java on port 8080 and check `/gridjsdemo/api/health`.

Q: How do I build the Vue frontend?
A: Run `npm run build` in `vue-gridjs`. The generated files are written to `vue-gridjs/dist` and are not copied into the Spring Boot application by this example.
