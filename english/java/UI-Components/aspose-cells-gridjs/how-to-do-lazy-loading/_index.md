---
title: How to Implement Lazy Loading in GridJs  
type: docs  
weight: 250  
url: /java/aspose-cells-gridjs/how-to-do-lazy-loading/  
description: This article describes how to implement lazy loading in GridJs.  
keywords: GridJs, lazy loading, On‑Demand loading, optimize loading  
aliases:
  - /java/aspose-cells-gridjs/lazy-loading/
  - /java/aspose-cells-gridjs/loading-on-demand/
  - /java/aspose-cells-gridjs/optimize-loading/
---

## About Lazy Loading  

When dealing with a spreadsheet file containing numerous worksheets, we can optimize the loading process by initially loading only the active worksheet.

This strategy ensures that the server‑side JSON response initially includes only the data pertaining to the actively selected worksheet. As a result, the initial web traffic is significantly reduced, enhancing the user experience by minimizing load times.

Furthermore, GridJs is designed to dynamically respond to user interactions. Specifically, when a user clicks on a different worksheet, GridJs intelligently triggers a request to the server to fetch the data **only** for that worksheet.

This on‑demand loading mechanism not only further reduces unnecessary data transfers but also ensures that the user always has access to the most up‑to‑date information for the worksheet they are currently working on.

By adopting this approach, we not only optimise the initial load time but also maintain a responsive and efficient application that scales well with the increasing number of worksheets in the spreadsheet file.

## Implementation Steps  

### Step 1: Configure Lazy Loading in Spring  

Set the lazy‑loading option either through **`Config`** or **`GridJsOptions`** – both have the same effect.

#### Example using `Config`

```java
// Enable lazy loading globally
Config.setLazyLoading(true);
```

#### Example using `GridJsOptions` (Spring‑style bean configuration)

```java
import com.aspose.gridjs.GridJsOptions;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class GridJsConfig {

    @Bean
    public GridJsOptions gridJsOptions() {
        GridJsOptions options = new GridJsOptions();
        // ... configure other options as required
        options.setLazyLoading(true);
        options.setBaseRouteName("GridJs2");
        return options;
    }
}
```

*In a Spring Boot application you would typically place the above `@Configuration` class in a package that is scanned automatically, or import it explicitly.*

### Step 2: Set Action URL in the Client File  

Configure the lazy‑loading URL in your client‑side JavaScript file.

```javascript
const lazyLoadingUrl = "/GridJs2/LazyLoadingStreamJson";
xs.setLazyLoadingUrl(lazyLoadingUrl);
```

After the user clicks on a worksheet that is not the active one, the data‑query action will be triggered automatically by the spreadsheet application.

### Step 3: Implement Lazy‑Loading Action in a Spring MVC Controller  

 

```java
package com.myapp.gridjs;

import com.aspose.gridjs.GridJsWorkbook;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.util.zip.GZIPOutputStream;

@RestController
@RequestMapping("/GridJs2")
public class GridJsLazyLoadingController {

    @PostMapping("/LazyLoadingStreamJson")
    public void lazyLoadingStreamJson(@RequestParam(name = "name", required = false) String sheetName,
                                      @RequestParam(name = "uid", required = false) String uid,
                                      HttpServletResponse response) throws IOException {

        GridJsWorkbook wbj = new GridJsWorkbook();

        response.setContentType("application/json");
        response.addHeader("Content-Encoding", "gzip");

        try (GZIPOutputStream gzip = new GZIPOutputStream(response.getOutputStream())) {
            // The Java API method name mirrors the .NET one
            wbj.lazyLoadingStream(gzip, uid, sheetName);
        }
    }
}
```

or If your Controller extends from **[`GridJsControllerBase`](https://reference.aspose.com/cells/java/com.aspose.gridjs/gridjscontrollerbase/)**.

```java

@PostMapping("/LazyLoadingStreamJson")
    public void lazyLoadingStreamJson(
            @RequestParam(value = "name", required = false) String sheetName,
            @RequestParam(value = "uid", required = false) String uid,
            HttpServletResponse response) throws IOException {


         super.lazyLoadingStreamJson(sheetName,uid,response);

    }
```


## Demo and Examples  

For a complete, runnable example, refer to the official Java demo repository:

[https://github.com/aspose-cells/Aspose.Cells.Grid-for-Java/tree/main/Examples.GridJs](https://github.com/aspose-cells/Aspose.Cells.Grid-for-Java/tree/main/Examples.GridJs)


## Additional Resources  

* **GridJs Server API Documentation** – <https://reference.aspose.com/cells/java/com.aspose.gridjs>  
* **GridJs Client API Documentation** – <https://docs.aspose.com/cells/java/aspose-cells-gridjs/how-to-use-gridjs-client-api>  