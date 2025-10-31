---  
title: How to Implement Lazy Loading in GridJs  
type: docs  
weight: 250  
url: /python/aspose-cells-gridjs/how-to-do-lazy-loading/  
description: This article describes how to implement lazy loading in GridJs.  
keywords: GridJs, lazy loading, On‑Demand loading, optimize loading  
aliases:  
  - /python/aspose-cells-gridjs/lazy-loading/  
  - /python/aspose-cells-gridjs/loading-on-demand/  
  - /python/aspose-cells-gridjs/optimize-loading/  
---  

## About Lazy Loading  

When dealing with a spreadsheet file containing numerous worksheets, we can optimize the loading process by initially loading only the active worksheet.  

This strategy ensures that the server‑side JSON response initially includes only the data pertaining to the actively selected worksheet. As a result, the initial web traffic is significantly reduced, enhancing the user experience by minimizing load times.  

Furthermore, GridJs is designed to dynamically respond to user interactions. Specifically, when a user clicks on a different worksheet, GridJs intelligently triggers a request to the server to fetch the data specifically for that worksheet.  

This on‑demand loading mechanism not only further reduces unnecessary data transfers but also ensures that the user always has access to the most up‑to‑date information for the worksheet they are currently working on.  

By adopting this approach, we not only optimize the initial load time but also maintain a responsive and efficient application that scales well with the increasing number of worksheets in the spreadsheet file.  

## Implementation Steps  

### Step 1: Configure Lazy Loading in Flask  

Set the lazy‑loading option either through **Config** or **GridJsOptions** – both have the same effect.  

#### Example using `Config`  

```python
# Import the Config class from the aspose.cellsgridjs namespace
from aspose.cellsgridjs import Config

# Enable lazy loading globally
Config.set_lazy_loading(True)
```  


### Step 2: Set Action URL in Client File  

Configure the lazy‑loading URL in your client‑side JavaScript file. The URL must match the route you registered in Flask (the `BaseRouteName` you set above).  

```javascript
// client.js
const lazyLoadingUrl = "/GridJs2/LazyLoadingStreamJson";
xs.setLazyLoadingUrl(lazyLoadingUrl);
```  

After the user clicks on a worksheet that is not the active one, the data‑query action will be triggered automatically by the spreadsheet application.  

### Step 3: Implement Lazy Loading Action in a Flask Controller  

Create a Flask route that implement the lazy loading.  

#### Example implementation without the base controller  

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
            wbj.lazy_loading_stream(gzip_stream, uid, sheet_name)

        response = Response(output.getvalue(), mimetype='application/json')
        response.headers['Content-Encoding'] = 'gzip'

        return response
    except Exception as e:
        return Response(str(e), status=500)

```  



## Demo and Examples  

For comprehensive implementation examples and detailed usage scenarios, refer to the official demo repository:  

<https://github.com/aspose-cells/Aspose.Cells.Grid-for-Python-via-.NET/tree/main/Examples.GridJs>  

## Additional Resources  

- [GridJs Server API Documentation](https://reference.aspose.com/cells/python-net/aspose.cellsgridjs)  
- [GridJs Client API Documentation](https://docs.aspose.com/cells/python-net/aspose-cells-gridjs/how-to-use-gridjs-client-api)  