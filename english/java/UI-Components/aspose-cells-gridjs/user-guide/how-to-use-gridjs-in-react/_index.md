---
title: How to use GridJs in React
description: Run the React example included with the GridJs npm package and understand how it uses a shared Java backend for workbook listing, upload, loading, editing, and URL routing.
keywords: GridJsSpreadsheet, React, react-gridjs, gridjs-spreadsheet, Java, Vite, loader, permanent, highlight, GridJs2
type: docs
weight: 1
url: /java/aspose-cells-gridjs/user-guide/how-to-use-gridjs-in-react/
---

## Introduction

The complete React example is included in the npm package at `node_modules/gridjs-spreadsheet/example/react-gridjs`. The same `example` directory contains the Spring Boot backend used by the React, Vue, Angular, and Vanilla HTML demos. The React demo displays a start page with a demo selector, workbook list, and upload input, then mounts `GridJsSpreadsheet` as a full-page editor after a workbook is selected.

## How to use

### Get the example from npm

Install `gridjs-spreadsheet`, then copy the packaged example to a writable directory. Do not edit the copy under `node_modules`, because another npm install can replace it.

```shell
npm install gridjs-spreadsheet
cp -R node_modules/gridjs-spreadsheet/example ./gridjs-example
cd gridjs-example
```

On Windows, copy `node_modules/gridjs-spreadsheet/example` to a normal project directory and open a terminal in that copied directory.

The example requires Java 8 or newer, Node.js 18 or newer, and npm.

### Configure and start the Java backend

For a local run, edit `src/main/resources/application.properties`. The checked-in values use `/app/...` Docker paths, so replace them with absolute paths on your machine.

```properties
testconfig.ListDir=/absolute/path/gridjs-example/wb
testconfig.CachePath=/absolute/path/gridjs-example/grid_cache
testconfig.UploadPath=/absolute/path/gridjs-example/upload
testconfig.AsposeLicensePath=/absolute/path/Aspose.Cells.lic
```

`ListDir` contains the workbooks shown on the start page. `CachePath` and `UploadPath` must point to writable locations. If the configured license file does not exist, the current Java entry point does not call `setLicense` and the example runs in evaluation mode.

Start Spring Boot from the `gridjs-example` directory:

```shell
./mvnw spring-boot:run -Dmaven.test.skip=true
```

On Windows, run:

```bat
mvnw.cmd spring-boot:run -Dmaven.test.skip=true
```

Confirm that the backend is available at `http://127.0.0.1:8080/gridjsdemo/api/health`.

### Start the React demo

Open another terminal in `gridjs-example`:

```shell
cd react-gridjs
npm install
npm run dev
```

Open `http://127.0.0.1:5173`.

The Vite configuration forwards requests beginning with `/GridJs2` and `/gridjsdemo` to `http://127.0.0.1:8080`. The browser therefore calls relative URLs on port 5173 while Vite sends the API requests to Java.

### Follow the demo flow

1. The start page requests `/gridjsdemo/api/files` and renders the workbook names returned by Java.
2. Select `permanent url load demo` or `highlight and custom context menu demo`.
3. Click a workbook. The demo stores the selection in the URL and changes from the start page to the editor page.
4. In `permanent` mode, the React `loader` requests `/GridJs2/DetailStreamJsonWithUid` with `filename` and `uid`.
5. In `highlight` mode, the loader requests `/GridJs2/DetailStreamJson` without a persistent UID route. This endpoint choice is the load-path difference implemented by the current React source.
6. Edit cells and inspect the browser console. The demo logs change, cell selection, cell edit, and sheet selection events.
7. Return to the start page and upload an `.xlsx` file. The demo posts it to `/gridjsdemo/api/upload`, stores both the display name and generated server filename in the URL, and loads it through `/GridJs2/DetailStreamJsonWithUidFromUpload`.

Browser back and forward navigation is supported because `src/routing.js` reads the query string again on the `popstate` event.

### Source files used by the demo

| File | Purpose |
| --- | --- |
| `react-gridjs/src/main.jsx` | Imports the GridJs stylesheet and mounts the React application. |
| `react-gridjs/src/App.jsx` | Implements the start page, upload flow, workbook loader, editor, and GridJs event handlers. |
| `react-gridjs/src/routing.js` | Reads and writes workbook state in the URL and creates React-specific UIDs. |
| `react-gridjs/src/api.js` | Wraps `fetch` and throws an error for non-success responses. |
| `react-gridjs/vite.config.js` | Proxies `/GridJs2` and `/gridjsdemo` to the Java backend. |

## JavaScript API

### Import and mount the React wrapper

The demo imports the named React export and the GridJs stylesheet:

```jsx
import { GridJsSpreadsheet } from 'gridjs-spreadsheet/react';
import 'gridjs-spreadsheet/xspreadsheet.css';
```

`App.jsx` passes the asynchronous `loader` directly to the wrapper:

```jsx
<GridJsSpreadsheet
  loader={loader}
  height="100vh"
  showToolbar
  showContextmenu
  onReady={handleReady}
  onError={handleError}
/>
```

The demo uses these React props:

| Prop | Use in the example |
| --- | --- |
| `loader` | Returns the workbook JSON selected by the current URL. |
| `height` | Sets the editor height to `100vh`. |
| `showToolbar` | Displays the GridJs toolbar. |
| `showContextmenu` | Enables the GridJs context menu. |
| `onReady` | Restores the active sheet and cell, sets the open-file URL to `/`, and stores the adapter reference. |
| `onChange` | Logs that workbook data changed. |
| `onError` | Logs GridJs mounting or update errors. |
| `onCellSelected`, `onCellEdited`, `onSheetSelected` | Log user interaction details. |

### URL parameters

| Parameter | Meaning in the React demo |
| --- | --- |
| `file` | Workbook name displayed to the user. Without it, the start page is shown. |
| `storedFile` | Internal server filename. It differs from `file` after an upload. |
| `demo` | `permanent` or `highlight`. Any other value is normalized to `permanent`. |
| `uid` | React-prefixed cache identifier used by UID-based loading. |
| `fromUpload` | A non-empty value tells the demo to load from the upload directory. |

### Backend endpoints used by the React demo

| Endpoint | Purpose |
| --- | --- |
| `/gridjsdemo/api/health` | Confirms that the Java backend is running. |
| `/gridjsdemo/api/files` | Returns the configured workbook directory and file list. |
| `/gridjsdemo/api/upload` | Stores an uploaded workbook and returns `file`, `displayName`, `uid`, and `fromUpload`. |
| `/GridJs2/DetailStreamJson` | Loads the selected workbook in `highlight` mode. |
| `/GridJs2/DetailStreamJsonWithUid` | Loads the selected workbook in `permanent` mode. |
| `/GridJs2/DetailStreamJsonWithUidFromUpload` | Loads a workbook from the upload directory. |

The npm wrapper also configures the standard GridJs update, image, download, OLE, and lazy-loading endpoints under `/GridJs2`.

## Common Questions

Q: Where is the complete React project after installing the npm package?
A: It is under `node_modules/gridjs-spreadsheet/example/react-gridjs`. Copy the complete `example` directory before running it.

Q: Why does the browser report a proxy or connection error?
A: The React development server expects Java to be running on `127.0.0.1:8080`. Check `/gridjsdemo/api/health` before opening port 5173.

Q: Why are both `file` and `storedFile` kept after an upload?
A: `file` preserves the original display name, while `storedFile` is the generated name saved in the Java upload directory.

Q: How do I create a production build of the frontend?
A: Run `npm run build` in `react-gridjs`. Vite writes the result to that project's `dist` directory; the current example does not copy it into Spring Boot.
