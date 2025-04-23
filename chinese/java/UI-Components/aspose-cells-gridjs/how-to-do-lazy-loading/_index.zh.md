---
title: 如何在GridJs中实现懒加载  
type: docs
weight: 250
url: /zh/java/aspose-cells-gridjs/how-to-do-lazy-loading/
description: 本文描述了如何在GridJs中实现懒加载。
keywords: GridJs，懒加载，按需加载，
aliases:
  - /java/aspose-cells-gridjs/lazy-loading/
  - /java/aspose-cells-gridjs/loading-on-demand/

---

## 关于懒加载 
当处理包含大量工作表的电子表格文件时，我们可以通过最初仅加载活动工作表来优化加载过程。

此策略确保服务器端的JSON响应最初仅包含与当前选择的工作表相关的数据。  

因此，最初的网页流量大大减少，提升用户体验，缩短加载时间。  

此外，GridJs被设计为能动态响应用户交互，尤其是当用户点击不同工作表时，

GridJs会智能触发请求，获取特定该工作表的数据。  

这种按需加载机制不仅进一步减少不必要的数据传输，还确保用户始终可以访问当前工作表的最新信息。  

采用这种方式，我们不仅优化了初次加载时间，还能保持应用的响应性和高效性，随着电子表格文件中工作表数量的增加而良好扩展。

# 实现GridJs中的懒加载步骤如下
## 设置懒加载的配置选项。
例如：
```java 
  Config.setLazyLoading(true);
```
## 设置懒加载的动作URL。
例如：
```javascript
 const lazyLoadingUrl = "/GridJs2/LazyLoading";
 xs.setLazyLoadingUrl(lazyLoadingUrl);
```
当用户点击不是当前激活的工作表时，查询数据的操作会由电子表应用程序自动触发。 

## 在服务器端控制器中实现懒加载操作。
例如：
```java
    @PostMapping("/LazyLoading")
    public void lazyLoadingStreamJson(
            @RequestParam(value = "name", required = false) String sheetName,
            @RequestParam(value = "uid", required = false) String uid,
            HttpServletResponse response) throws IOException {

        GridJsWorkbook wbj = new GridJsWorkbook();
        response.setContentType(MediaType.APPLICATION_JSON_VALUE);
        response.setHeader(HttpHeaders.CONTENT_ENCODING, "gzip");

        try (GZIPOutputStream gzipOutputStream = new GZIPOutputStream(response.getOutputStream())) {
            try {
				wbj.lazyLoadingStream(gzipOutputStream, uid, sheetName);
			} catch (Exception e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
        }
    }
```





