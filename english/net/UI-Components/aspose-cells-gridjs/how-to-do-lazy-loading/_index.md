---
title: How to Implement Lazy Loading in GridJs  
type: docs
weight: 250
url: /net/aspose-cells-gridjs/how-to-do-lazy-loading/
description: This article describes how to implement lazy loading in GridJs.
keywords: GridJs, lazy loading, On-Demand loading, optimize loading
aliases:
  - /net/aspose-cells-gridjs/lazy-loading/
  - /net/aspose-cells-gridjs/loading-on-demand/
  - /net/aspose-cells-gridjs/optimize-loading/
---

## About Lazy Loading

When dealing with a spreadsheet file containing numerous worksheets, we can optimize the loading process by initially loading only the active worksheet.

This strategy ensures that the server-side JSON response initially includes only the data pertaining to the actively selected worksheet. As a result, the initial web traffic is significantly reduced, enhancing the user experience by minimizing load times.

Furthermore, GridJs is designed to dynamically respond to user interactions. Specifically, when a user clicks on a different worksheet, GridJs intelligently triggers a request to the server to fetch the data specifically for that worksheet.

This on-demand loading mechanism not only further reduces unnecessary data transfers but also ensures that the user always has access to the most up-to-date information for the worksheet they are currently working on.

By adopting this approach, we not only optimize the initial load time but also maintain a responsive and efficient application that scales well with the increasing number of worksheets in the spreadsheet file.

## Implementation Steps

### Step 1: Configure Lazy Loading in Startup.cs

Set the lazy loading option either through [Config](https://reference.aspose.com/cells/net/aspose.cells.gridjs/config/) or [GridJsOptions](https://reference.aspose.com/cells/net/aspose.cells.gridjs/gridjsoptions/) - both have the same effect.

**Example using Config:**

```csharp
Config.LazyLoading = true;
```

**Example using GridJsOptions:**

```csharp
services.Configure<GridJsOptions>(options =>
{
    // ... other options
    options.LazyLoading = true;
    options.BaseRouteName = "GridJs2";
});
```

### Step 2: Set Action URL in Client File

Configure the lazy loading URL in your client-side JavaScript file.

**Example:**

```javascript
const lazyLoadingUrl = "/GridJs2/LazyLoadingStreamJson";
xs.setLazyLoadingUrl(lazyLoadingUrl);
```

After the user clicks on a worksheet that is not the active one, the data query action will be triggered automatically by the spreadsheet application.

### Step 3: Implement Lazy Loading Action in Controller

Implement the lazy loading action on the server side.
(If your controller extends from [GridJsControllerBase](https://reference.aspose.com/cells/net/aspose.cells.gridjs/gridjscontrollerbase/), you don't need to add this implementation as it is already provided in [GridJsControllerBase](https://reference.aspose.com/cells/net/aspose.cells.gridjs/gridjscontrollerbase/).)

**Example:**

```csharp
[HttpPost]
// POST: /GridJs2/LazyLoadingStreamJson?name=&uid=
public ActionResult LazyLoadingStreamJson()
{
    string sheetName = HttpContext.Request.Form["name"];
    string uid = HttpContext.Request.Form["uid"];
    GridJsWorkbook wbj = new GridJsWorkbook();

    Response.ContentType = "application/json";
    Response.Headers.Add("Content-Encoding", "gzip");

    using (GZipStream gzip = new GZipStream(Response.Body, CompressionLevel.Optimal))
    {
        wbj.LazyLoadingStream(gzip, uid, sheetName);
    }

    return new EmptyResult();
}
```

## Demo and Examples

For comprehensive implementation examples and detailed usage scenarios, refer to the official demo repository:

<https://github.com/aspose-cells/Aspose.Cells.Grid-for-.NET/tree/main/Examples_GridJs>

## Additional Resources

- [GridJs Server API Documentation](https://reference.aspose.com/cells/net/aspose.cells.gridjs)
- [GridJs Client API Documentation](https://docs.aspose.com/cells/net/aspose-cells-gridjs/how-to-use-gridjs-client-api)