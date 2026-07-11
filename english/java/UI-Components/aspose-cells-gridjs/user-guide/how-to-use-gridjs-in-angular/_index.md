---
title: How to use GridJs in Angular
description: Run the Angular example included with the GridJs npm package and understand how its standalone component uses a shared Java backend for workbook listing, upload, loading, editing, and URL routing.
keywords: GridJsSpreadsheetComponent, Angular, angular-gridjs, gridjs-spreadsheet, Java, standalone component, proxy.conf.json, permanent, highlight, GridJs2
type: docs
weight: 1
url: /java/aspose-cells-gridjs/user-guide/how-to-use-gridjs-in-angular/
---

## Introduction

The complete Angular example is included in the npm package at `node_modules/gridjs-spreadsheet/example/angular-gridjs`. It uses the Spring Boot application at the root of the packaged `example` directory as its GridJs backend. The Angular demo is a standalone application that displays a workbook start page and renders `GridJsSpreadsheetComponent` after a workbook has been selected or uploaded.

## How to use

### Get the example from npm

Install `gridjs-spreadsheet`, then copy the packaged example to a writable project directory:

```shell
npm install gridjs-spreadsheet
cp -R node_modules/gridjs-spreadsheet/example ./gridjs-example
cd gridjs-example
```

On Windows, copy `node_modules/gridjs-spreadsheet/example` outside `node_modules` and open a terminal in the copied directory.

The Java backend requires Java 8 or newer. The included Angular 18 project declares Node.js `>=18 <23`, so use Node.js 18, 20, or 22 with npm.

### Configure and start the Java backend

The checked-in `src/main/resources/application.properties` contains `/app/...` paths for Docker. Replace them with absolute local paths before running Spring Boot directly:

```properties
testconfig.ListDir=/absolute/path/gridjs-example/wb
testconfig.CachePath=/absolute/path/gridjs-example/grid_cache
testconfig.UploadPath=/absolute/path/gridjs-example/upload
testconfig.AsposeLicensePath=/absolute/path/Aspose.Cells.lic
```

`ListDir` is returned by `/gridjsdemo/api/files`; `CachePath` and `UploadPath` must be writable. If the license path does not point to an existing file, the current Java startup code skips `setLicense`.

Start Spring Boot from `gridjs-example`:

```shell
./mvnw spring-boot:run -Dmaven.test.skip=true
```

On Windows:

```bat
mvnw.cmd spring-boot:run -Dmaven.test.skip=true
```

Confirm `http://127.0.0.1:8080/gridjsdemo/api/health` returns a successful response.

### Start the Angular demo

Open another terminal in `gridjs-example`:

```shell
cd angular-gridjs
npm install
npm run dev
```

Open `http://127.0.0.1:4200`.

The `dev` script starts Angular CLI with `proxy.conf.json`. That proxy forwards both `/GridJs2` and `/gridjsdemo` to `http://127.0.0.1:8080`.

### Follow the demo flow

1. `AppComponent.ngOnInit` calls `loadFiles`, which requests `/gridjsdemo/api/files` and fills the start-page list.
2. Choose `permanent url load demo` or `highlight and custom context menu demo`, then select a workbook.
3. `openWorkbook` updates the Angular state, writes the workbook information to the URL, and calls `loadWorkbook`.
4. `permanent` mode uses `/GridJs2/DetailStreamJsonWithUid`; `highlight` mode uses `/GridJs2/DetailStreamJson`.
5. `loadWorkbook` stores the returned JSON in `workbookData`. The template then renders `<gridjs-spreadsheet>` with its `data` input.
6. The wrapper emits ready, change, error, cell selection, cell edit, and sheet selection outputs. The demo writes these events to the browser console.
7. Uploading an `.xlsx` file posts to `/gridjsdemo/api/upload` and loads the generated server file through `/GridJs2/DetailStreamJsonWithUidFromUpload`.

`@HostListener('window:popstate')` reloads Angular state from the query string when the user navigates backward or forward. The current source differentiates the second demo mode through the non-UID load endpoint; the UI label also mentions highlight and a custom context menu.

### Source files used by the demo

| File | Purpose |
| --- | --- |
| `angular-gridjs/src/main.ts` | Bootstraps the standalone Angular component. |
| `angular-gridjs/src/app/app.component.ts` | Holds state, requests workbook data, handles uploads, and processes GridJs outputs. |
| `angular-gridjs/src/app/app.component.html` | Renders the start page, loading state, and `<gridjs-spreadsheet>`. |
| `angular-gridjs/src/app/routing.ts` | Reads and writes URL parameters and creates Angular-prefixed UIDs. |
| `angular-gridjs/src/app/api.ts` | Wraps `fetch` and reports response errors. |
| `angular-gridjs/proxy.conf.json` | Proxies Java API paths during `ng serve`. |
| `angular-gridjs/angular.json` | Adds `gridjs-spreadsheet/xspreadsheet.css` to the build styles. |

## JavaScript API

### Import and render the Angular wrapper

`AppComponent` imports the named Angular export and registers it in the standalone component:

```typescript
import { GridJsSpreadsheetComponent } from 'gridjs-spreadsheet/angular';

@Component({
  standalone: true,
  imports: [CommonModule, GridJsSpreadsheetComponent],
})
```

The stylesheet is configured in `angular.json`, and the template renders the component when `workbookData` is available:

```html
<gridjs-spreadsheet
  *ngIf="workbookData"
  [data]="workbookData"
  height="100vh"
  [showToolbar]="true"
  [showContextmenu]="true"
  (ready)="onReady($event)"
  (error)="onError($event)">
</gridjs-spreadsheet>
```

The demo uses these Angular inputs and outputs:

| Input or output | Use in the example |
| --- | --- |
| `data` | Receives workbook JSON returned by `loadWorkbook`. |
| `height` | Sets the editor height to `100vh`. |
| `showToolbar` | Displays the GridJs toolbar. |
| `showContextmenu` | Enables the GridJs context menu. |
| `ready` | Supplies `{ instance, adapter }`; the handler restores the active sheet and cell and sets the open-file URL. |
| `change` | Logs that workbook data changed. |
| `error` | Passes the GridJs error payload to `onError`. |
| `cellSelected`, `cellEdited`, `sheetSelected` | Emit argument arrays that the template formats for console logging. |

### URL parameters

| Parameter | Meaning in the Angular demo |
| --- | --- |
| `file` | Workbook display name. Without it, Angular renders the start page. |
| `storedFile` | Internal server filename, primarily used for uploaded workbooks. |
| `demo` | `permanent` or `highlight`; other values default to `permanent`. |
| `uid` | Angular-prefixed identifier for UID-based workbook loading. |
| `fromUpload` | A non-empty value selects the upload-directory load endpoint. |

### Backend endpoints used by the Angular demo

| Endpoint | Purpose |
| --- | --- |
| `/gridjsdemo/api/health` | Checks whether Java is running. |
| `/gridjsdemo/api/files` | Returns the workbook directory and file list. |
| `/gridjsdemo/api/upload` | Stores an upload and returns its generated server name and UID. |
| `/GridJs2/DetailStreamJson` | Loads a workbook in `highlight` mode. |
| `/GridJs2/DetailStreamJsonWithUid` | Loads a workbook in `permanent` mode. |
| `/GridJs2/DetailStreamJsonWithUidFromUpload` | Loads an uploaded workbook. |

The npm wrapper configures the remaining standard GridJs update, image, download, OLE, and lazy-loading endpoints under `/GridJs2`.

## Common Questions

Q: Where is the complete Angular project after npm installation?
A: It is in `node_modules/gridjs-spreadsheet/example/angular-gridjs`. Copy the full `example` directory to a writable location before running it.

Q: Why does Angular reject my Node.js version?
A: The included `package.json` declares Node.js `>=18 <23`. Use Node.js 18, 20, or 22.

Q: Why do API requests fail while the page still opens on port 4200?
A: Angular CLI can serve the frontend even when Java is unavailable. Start the backend on port 8080 and verify `/gridjsdemo/api/health`.

Q: How do I build the Angular frontend?
A: Run `npm run build` in `angular-gridjs`. Angular writes the output below `dist/gridjs-angular-demo`; the current example does not copy it into Spring Boot.
