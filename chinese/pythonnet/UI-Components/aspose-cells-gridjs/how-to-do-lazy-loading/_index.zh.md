---
title: 如何在GridJs中实现懒加载  
type: docs
weight: 250
url: /zh/python-net/aspose-cells-gridjs/how-to-do-lazy-loading/
description: 本文描述了如何在GridJs中实现懒加载。
keywords: GridJs，懒加载，按需加载，
aliases:
  - /python-net/aspose-cells-gridjs/lazy-loading/
  - /python-net/aspose-cells-gridjs/loading-on-demand/

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
```python 
       Config.set_lazy_loading(True)
```
## 设置懒加载的动作URL。
例如：
```javascript
 const lazyLoadingUrl = "/GridJs2/LazyLoading";
 xs.setLazyLoadingUrl(lazyLoadingUrl);
```
用户点击非活动工作表时，查询数据的动作会由电子表格应用自动触发， 

## 在服务器端控制器中实现懒加载操作。
例如：
```python
@app.route('/GridJs2/LazyLoading', methods=['POST'])
def lazy_loading():
    sheet_name = request.form.get('name', '')
    uid = request.form.get('uid', '')
    if not sheet_name:
        return jsonify({'error': 'sheet_name is required'}), 400
    if not uid:
        return jsonify({'error': 'uid is required'}), 400

    wbj = GridJsWorkbook()
    try:

        output = io.BytesIO()
        with gzip.GzipFile(fileobj=output, mode='wb', compresslevel=9) as gzip_stream:
             wbj.lazy_loading_stream(gzip_stream,uid, sheet_name)


        response = Response(output.getvalue(), mimetype='application/json')
        response.headers['Content-Encoding'] = 'gzip'

        return response
    except Exception as e:
        return Response(str(e), status=500)
```





