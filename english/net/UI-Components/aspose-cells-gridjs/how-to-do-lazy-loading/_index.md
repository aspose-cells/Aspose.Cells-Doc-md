---
title: how to do lazy loading in GridJs  
type: docs
weight: 250
url: /net/aspose-cells-gridjs/how-to-do-lazy-loading/
description: This article describes how to implement lazy loading in GridJs.
keywords: GridJs,lazy loading,On-Demand loading,
aliases:
  - /net/aspose-cells-gridjs/lazy-loading/
  - /net/aspose-cells-gridjs/loading-on-demand/

---

## about lazy loading 
When dealing with a spreadsheet file containing numerous worksheets, we can optimize the loading process by initially loading only the active worksheet.

This strategy ensures that the server-side JSON response initially includes only the data pertaining to the actively selected worksheet.  
  
As a result, the initial web traffic is significantly reduced, enhancing the user experience by minimizing load times.  
  
Furthermore, GridJs is designed to dynamically respond to user interactions. Specifically, when a user clicks on a different worksheet,

GridJs intelligently triggers a request to the server to fetch the data specifically for that worksheet.  
  
This on-demand loading mechanism not only further reduces unnecessary data transfers but also ensures that the user always has access to the most up-to-date information for the worksheet they are currently working on.  
  
By adopting this approach, we not only optimize the initial load time but also maintain a responsive and efficient application that scales well with the increasing number of worksheets in the spreadsheet file.

# To implement lazy loading in GridJs ,the steps are
## Set Config Option for lazy loading.
for example:
```C# 
   Config.LazyLoading = true;
```
## Set action URL for lazy loading.
for example:
```javascript
 const lazyLoadingUrl = "/GridJs2/LazyLoadingStreamJson";
 xs.setLazyLoadingUrl(lazyLoadingUrl);
```
After user click the other worksheet that is not the active one£¬the action of query data wil be triggered automatically by the spreadsheet application 

## Implement lazy loading action in Controller  in serverside .
for example:
```C#
    [HttpPost]
 // post: /GridJs2/LazyLoadingStreamJson?name=&uid=
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




 
