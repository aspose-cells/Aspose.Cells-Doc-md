---
title: Step‑by‑Step Guide to Load a Spreadsheet with GridJs
type: docs
weight: 250
url: /net/aspose-cells-gridjs/load-spreadsheet/
description: Learn how to use Aspose.Cells.GridJs to load an Excel workbook in a .NET 6 MVC web application and display it with the GridJs client library.
keywords: GridJs,load spreadsheet,ASP.NET MVC,client‑side,server‑side,gridjs‑spreadsheet
aliases:
  - /net/aspose-cells-gridjs/how-to-load-spreadsheet/
  - /net/aspose-cells-gridjs/gridjs-load-demo/
  - /net/aspose-cells-gridjs/step-by-step-demo/
  - /net/aspose-cells-gridjs/step-by-step-example/
  - /net/aspose-cells-gridjs/gridjs-demo/
---

# Load a Spreadsheet with GridJs

## Introduction

This article demonstrates a **complete end‑to‑end solution** for loading an Excel workbook into a web page using **Aspose.Cells.GridJs**.  
The guide covers:

* Creating a .NET 6 MVC project.  
* Adding the required Aspose.Cells and GridJs NuGet packages.  
* Configuring the `GridJsService` in `Startup.cs`.  
* Implementing the `GridJsController` that supplies JSON data to the client.  
* Building the client‑side HTML page that uses the `gridjs-spreadsheet` JavaScript library to render the workbook, handle updates, and support image, OLE and file download operations.

All code snippets are **runnable** and follow Aspose.Cells documentation standards.

{{% alert color="primary" %}}
Make sure you have a valid Aspose.Cells license before running the demo; otherwise, the library will work in evaluation mode with a watermark.
{{% /alert %}}

---

## Prerequisites

| Item | Version / Requirement |
|------|-----------------------|
| .NET SDK | 6.0 or later |
| ASP.NET Core MVC | .NET 6 |
| NuGet Packages | `Aspose.Cells (>= 25.*)`, `Aspose.Cells.GridJs (>= 25.*)`, `Newtonsoft.Json (13.0.1)` |
| Client Libraries | jQuery 2.1.1, jQuery‑UI 1.12.1, JSZip 3.6.0, GridJs Spreadsheet assets (from CDN) |
| Browser | Modern browsers supporting ES6 |

---

## 1. Create the MVC Project

```bash
# Create a new ASP.NET Core MVC project called GridJsDemo
dotnet new mvc -n GridJsDemo --framework net6.0
cd GridJsDemo
```

Add the required NuGet packages:

```bash
dotnet add package Aspose.Cells --version 25.*
dotnet add package Aspose.Cells.GridJs --version 25.*
dotnet add package Newtonsoft.Json --version 13.0.1
```

The project structure after adding the packages will resemble:

```
./GridJsDemo/
├─ Controllers/
│  └─ GridJsController.cs
├─ Views/
│  └─ GridJs/
│     └─ Index.cshtml
├─ wwwroot/
│  └─ js/
│     └─ gridjs-demo.js
├─ Startup.cs
└─ GridJsDemo.csproj
```

---

## 2. Server‑Side Configuration

### 2.1 `Startup.cs`

```csharp
// ./Startup.cs
using Aspose.Cells.GridJs;
using Microsoft.AspNetCore.Builder;
using Microsoft.AspNetCore.Hosting;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;

namespace GridJsDemo
{
    public class Startup
    {
        public Startup(IConfiguration configuration) => Configuration = configuration;
        public IConfiguration Configuration { get; }

        // This method gets called by the runtime. Use this to add services to the container.
        public void ConfigureServices(IServiceCollection services)
        {
            services.AddControllersWithViews();

            // Register GridJs service
            services.AddScoped<IGridJsService, GridJsService>();

            // Configure GridJs options
            services.Configure<GridJsOptions>(options =>
            {
                // Folder used for temporary file cache
                options.FileCacheDirectory = @"D:\storage\Aspose.Cells.GridJs\";

                // Base route used by the controller (e.g. /GridJs/LoadSpreadsheet)
                options.BaseRouteName = "/GridJs";
            });
        }

        // This method gets called by the runtime. Use this to configure the HTTP request pipeline.
        public void Configure(IApplicationBuilder app, IWebHostEnvironment env)
        {
            if (env.IsDevelopment())
                app.UseDeveloperExceptionPage();
            else
                app.UseExceptionHandler("/Home/Error");

            app.UseStaticFiles();
            app.UseRouting();

            app.UseAuthorization();

            app.UseEndpoints(endpoints =>
            {
                // Default route
                endpoints.MapControllerRoute(
                    name: "default",
                    pattern: "{controller=Home}/{action=Index}/{id?}");
            });
        }
    }
}
```

### 2.2 `GridJsController.cs`

```csharp
// ./Controllers/GridJsController.cs
using System;
using System.IO;
using System.Text;
using Aspose.Cells.GridJs;
using Microsoft.AspNetCore.Mvc;

namespace GridJsDemo.Controllers
{
    // The controller inherits from GridJsControllerBase which already implements
    // most of the required actions (UpdateCell, Download, etc.).
    public class GridJsController : GridJsControllerBase
    {
        private readonly IGridJsService _gridJsService;

        public GridJsController(IGridJsService gridJsService) : base(gridJsService)
        {
            _gridJsService = gridJsService;
        }

        // Default view that hosts the client HTML page
        public IActionResult Index()
        {
            return View("Index");
        }

        // GET: /GridJs/LoadSpreadsheet?filename=sample.xlsx&uid=12345
        [HttpGet]
        public ActionResult LoadSpreadsheet(string filename, string uid)
        {
            // Resolve the absolute file path (adjust to your environment)
            string fullFilePath = GetFullFilePath(filename);

            // Generate JSON that contains worksheets data, active sheet info, etc.
            var jsonBuilder = _gridJsService.DetailFileJsonWithUid(fullFilePath, uid);
            return Content(jsonBuilder.ToString(), "text/plain", Encoding.UTF8);
        }

        // Helper: convert a relative file name to an absolute path.
        private string GetFullFilePath(string filename)
        {
            // Example: store workbook files under wwwroot/files/
            var rootPath = Path.Combine(Directory.GetCurrentDirectory(), "wwwroot", "files");
            return Path.Combine(rootPath, filename);
        }
    }
}
```

> **Note:** All other actions such as `UpdateCell`, `Download`, `Ole`, and image handling are already provided by `GridJsControllerBase`; no extra code is required.

---

## 3. Client‑Side Implementation

### 3.1 HTML View (`Index.cshtml`)

```html
@* ./Views/GridJs/Index.cshtml *@
@{
    ViewData["Title"] = "GridJs Spreadsheet Viewer";
}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8" />
    <title>@ViewData["Title"]</title>

    <!-- jQuery -->
    <script src="https://code.jquery.com/jquery-2.1.1.min.js"></script>

    <!-- jQuery UI -->
    <link rel="stylesheet" href="https://code.jquery.com/ui/1.12.1/themes/base/jquery-ui.css" />
    <script src="https://code.jquery.com/ui/1.12.1/jquery-ui.min.js"></script>

    <!-- JSZip (required for export) -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jszip/3.6.0/jszip.min.js"></script>

    <!-- GridJs Spreadsheet assets -->
    <link rel="stylesheet" href="https://unpkg.com/gridjs-spreadsheet/xspreadsheet.css">
    <script src="https://unpkg.com/gridjs-spreadsheet/xspreadsheet.js"></script>

    <!-- Custom script for this demo -->
    <script src="~/js/gridjs-demo.js"></script>

    <style>
        /* Simple page layout */
        body { margin: 20px; font-family: Arial, Helvetica, sans-serif; }
        #gridjs-demo-uid { width: 100%; height: 800px; }
    </style>
</head>
<body>
    <h2>GridJs Spreadsheet Viewer</h2>

    <!-- Container for the GridJs UI -->
    <div id="gridjs-demo-uid"></div>

    <!-- Hidden inputs to pass server‑side parameters (optional) -->
    <input type="hidden" id="fileName" value="sample.xlsx" />
</body>
</html>
```

### 3.2 JavaScript (`gridjs-demo.js`)

```javascript
/* ./wwwroot/js/gridjs-demo.js */

/**
 * Utility: generate a UUID (RFC4122 version 4)
 */
function generateUUID() {
    // Credit: https://stackoverflow.com/a/2117523
    return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function (c) {
        const r = (crypto.getRandomValues(new Uint8Array(1))[0] & 0xf) >> (c === 'x' ? 0 : 1);
        const v = c === 'x' ? r : (r & 0x3) | 0x8;
        return v.toString(16);
    });
}

/* ------------------------------------------------------------------ */
/* Configuration – action URLs used by the GridJs client side           */
const queryJsonUrl   = "/GridJs/LoadSpreadsheet";
const updateUrl      = "/GridJs/UpdateCell";
const fileDownloadUrl= "/GridJs/Download";
const oleDownloadUrl = "/GridJs/Ole";
const imageurl       = "/GridJs/ImageUrl";
const imageuploadurl1= "/GridJs/AddImage";
const imageuploadurl2= "/GridJs/AddImageByURL";
const imagecopyurl   = "/GridJs/CopyImage";

/* ------------------------------------------------------------------ */
/* Global GridJs instance */
let xs; // will hold the x_spreadsheet instance

/**
 * Loads workbook JSON from the server and renders it.
 * @param {Object} jsonData - Parsed JSON returned by LoadSpreadsheet.
 * @param {Object} option   - GridJs options (update mode, locale, etc.).
 */
function loadWithOption(jsonData, option) {
    $('#gridjs-demo-uid').empty();

    const sheets = jsonData.data;          // array of worksheet objects
    const filename = jsonData.filename;   // original file name

    // Initialise GridJs client UI and bind it to the container element
    xs = x_spreadsheet('#gridjs-demo-uid', option)
        .loadData(sheets)
        .updateCellError(msg => console.error(msg));

    // Optional UI adjustments
    if (!jsonData.showtabs) xs.bottombar.hide();

    xs.setUniqueId(jsonData.uid);
    xs.setFileName(filename);

    // Set the active sheet and cell
    let activeSheetName = jsonData.actname;
    if (xs.bottombar.dataNames.includes(activeSheetName)) {
        xs.setActiveSheetByName(activeSheetName)
          .setActiveCell(jsonData.actrow, jsonData.actcol);
    } else {
        // Fallback to the first visible sheet
        activeSheetName = xs.bottombar.dataNames[0];
        xs.setActiveSheetByName(activeSheetName).setActiveCell(0, 0);
    }

    // Register URLs for images, OLE objects, and file download
    xs.setImageInfo(imageurl, imageuploadurl1, imageuploadurl2, imagecopyurl, true);
    xs.setFileDownloadInfo(fileDownloadUrl);
    xs.setOleDownloadInfo(oleDownloadUrl);
    xs.setOpenFileUrl("/GridJs/Index");
}

/**
 * Entry point – called when the page is ready.
 */
$(function () {
    const uid = generateUUID();                 // unique session id
    const fileName = $('#fileName').val();      // workbook file to load

    // Options passed to the GridJs constructor
    const option = {
        updateMode: 'server',   // all edits are sent to server via updateUrl
        updateUrl: updateUrl,
        locale: 'en'            // language (en, zh, etc.)
    };

    // Prepare request parameters
    const queryParams = $.param({ filename: fileName, uid: uid });

    // AJAX request to get workbook JSON data
    $.ajax({
        url: `${queryJsonUrl}?${queryParams}`,
        method: 'GET',
        dataType: 'text',
        success: function (responseJsonString) {
            const jsonData = JSON.parse(responseJsonString);
            // Attach the generated uid to the JSON for later use
            jsonData.uid = uid;
            loadWithOption(jsonData, option);
        },
        error: function (xhr, status, err) {
            console.error(`Failed to load spreadsheet: ${err}`);
        }
    });
});
```

---

## 4. Running the Demo

1. **Place a sample workbook** (e.g., `sample.xlsx`) inside `wwwroot/files/`.  
2. **Build and run** the application:

   ```bash
   dotnet run
   ```

3. Open a browser and navigate to `https://localhost:5001/GridJs/Index`.  
   You should see the spreadsheet rendered inside the `<div id="gridjs-demo-uid"></div>` container.  

   ![GridJs Spreadsheet Viewer](./images/load-spreadsheet.png)

{{% alert color="primary" %}}
If you encounter a **“FileCacheDirectory does not exist”** error, create the directory specified in `GridJsOptions.FileCacheDirectory` (`D:\storage\Aspose.Cells.GridJs\`) or change the path to a location that exists on your machine.
{{% /alert %}}

---

## 5. Additional Resources

* **GridJs Server API** – <https://reference.aspose.com/cells/net/aspose.cells.gridjs>  
* **GridJs Client API** – <https://docs.aspose.com/cells/net/aspose-cells-gridjs/how-to-use-gridjs-client-api/>
* **GridJs‑spreadsheet NPM package** – <https://www.npmjs.com/package/gridjs-spreadsheet>
* **Source code for this demo** – <https://github.com/aspose-cells/Aspose.Cells.Grid-for-.NET/tree/main/Examples_GridJs.Simple>  


---