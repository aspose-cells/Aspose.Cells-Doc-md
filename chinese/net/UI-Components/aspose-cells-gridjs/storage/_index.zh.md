---
title: 使用 GridJs 存储
type: docs
weight: 250
url: /zh/net/aspose-cells-gridjs/storage/
description: 本文介绍Aspose.Cells.GridJs的一般处理。
keywords: file cache,storage,GridJs,GridJs storage,GridJs uid,download,uniqueid
---
# 使用 GridJs 存储
## 一般文件处理
在内存中导入电子表格文件并显示 ui 后，

GridJs 将创建一个具有指定 uid 的缓存文件，

格式为[Aspose.Cells.SaveFormat.Xlsx](https://reference.aspose.com/cells/net/aspose.cells/saveformat/ "Aspose.Cells.SaveFormat") ,

然后在 ui 中的每个更新操作之后，

例如设置单元格值，设置单元格样式等。 ,

GridJs 客户端 js 将触发控制器动作来执行 UpdateCell 操作。

在此操作中，将在 UpdateCell 方法期间从内存保存回缓存文件。
```C#   
        // post: /GridJs/UpdateCell
        [HttpPost] 
        public ActionResult UpdateCell( )
        {
            string p = HttpContext.Request.Form["p"];
            string uid = HttpContext.Request.Form["uid"];
            GridJsWorkbook gwb = new GridJsWorkbook();
            String ret = gwb.UpdateCell(p, uid);
            return Content(ret, "text/plain", System.Text.Encoding.UTF8);
        }
```
### 缓存目录在哪里
A. 如果我们实现 GridCacheForStream 并设置 GridJsWorkbook.CacheImp。
例如在下面的代码中，我们可以从中放置和获取缓存文件**“D:\临时”**
```C#
Config.FileCacheDirectory=@"D:\temp";
GridJsWorkbook.CacheImp=new LocalFileCache();
public class LocalFileCache  : GridCacheForStream
    {
         
        /// <summary>
        /// Implement this method to savecache,save the stream to the cache object with the key id.
        /// </summary>
        /// <param name="s">the source stream </param>
        /// <param name="uid">the key id.</param>
        public override void SaveStream(Stream s, String uid)
        {//make sure the directory exist
            String filepath = Path.Combine(Config.FileCacheDirectory, uid);
            using (FileStream fs = new FileStream(filepath, FileMode.Create)) 
            {
                s.Position = 0;
                s.CopyTo(fs);
            }

        }

        /// <summary>
        /// Implement this method to loadcache with the key uid,return the stream from the cache object.
        /// </summary>
        /// <param name="uid">the key id</param>
        /// <returns>the stream from  the cache</returns>
        public override Stream LoadStream(String uid)
        {//make sure the directory is exist
            String filepath = Path.Combine(Config.FileCacheDirectory, uid);;
            FileStream fs = new FileStream(filepath, FileMode.Open);
            return fs;
        }
		...
```
B.如果我们不设置GridJsWorkbook.CacheImp，

 GridJs 将在**配置文件缓存目录**，这是我们可以设置的默认缓存目录。

### 如何获取更新后的结果文件
#### 1. 文件的指定uid
确保一个指定的映射文件和uid之间的对应关系，

您始终可以获得指定文件名的相同 uid，而不是随机生成的。

例如只使用文件名就可以了。
```C#
//in controller  
...
        public ActionResult Uidtml(String filename)
        {
 
            return Redirect("~/xspread/uidload.html?file=" + filename + "&uid=" +  Path.GetFileNameWithoutExtension(filename));
        }
 ...
        public ActionResult DetailFileJsonWithUid(string filename,string uid)
        {
            String file = Path.Combine(TestConfig.ListDir, filename);
            GridJsWorkbook wbj = new GridJsWorkbook();
            //check if already in cache
           StringBuilder sb= wbj.GetJsonByUid(uid, filename);
            if(sb==null)
            {
                Workbook wb = new Workbook(file);
                wbj.ImportExcelFile(uid, wb);
                sb = wbj.ExportToJsonStringBuilder(filename);
            }

            return Content(sb.ToString(), "text/plain", System.Text.Encoding.UTF8);
        }
```

#### 2.与ui操作同步
其实对于一些ui操作，

例如：

将活动表切换到另一个，

更改图像位置，

旋转/调整图像大小等

不会触发 UpdateCell 操作。

因此，如果我们想获得与 ui 显示相同的更新文件，

我们需要在保存操作之前进行合并操作以同步这些 ui 操作。
```javascript
//in the js
  function save() {
            if (!xs.buffer.isFinish()) {
              alert('updating is inprogress,please try later');
                return;
            }
            let datas = xs.datas;
            delete datas.history;
            delete datas.search;
            delete datas.images;
            delete datas.shapes;

        var jsondata = {
          sheetname: xs.sheet.data.name,
          actrow: xs.sheet.data.selector.ri,
          actcol: xs.sheet.data.selector.ci,
          datas: xs.getUpdateDatas(),
        };

        const data = {
          p: JSON.stringify(jsondata),
          uid: uniqueid,
        };
		....
		//go on to do ajax post to trigger controller action
```
```C#
//in controller action 
  GridJsWorkbook wb = new GridJsWorkbook();
  wb.MergeExcelFileFromJson(uid, p);
  //after merge do save to chache or to a stream or whaterver you want to save to ,here we just save to cache
  wb.SaveToXlsx(Path.Combine(Config.FileCacheDirectory, uid));
```         
#### 3.从缓存中获取文件
例如：在下载动作中，你可以通过uid从缓存目录中获取它。
```C#
//in controller  

        public async Task<IActionResult> DownloadfromBytes(string uid,string ext)
        {
            byte[] byteArr = await System.IO.File.ReadAllBytesAsync(Path.Combine(Config.FileCacheDirectory, uid) );
            string mimeType = "application/octet-stream";
            return new FileContentResult(byteArr, mimeType)
            {
                FileDownloadName = uid+ ext
            };
        }
```

有关更多详细信息，您可以在此处查看示例：
<https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Examples_GridJs>
