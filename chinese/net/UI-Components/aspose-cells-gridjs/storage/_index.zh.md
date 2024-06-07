---
title: 使用 GridJs 存储实现
type: docs
weight: 250
url: /zh/net/aspose-cells-gridjs/storage/
description: 本文描述了GridJs的通用文件处理。
keywords: 文件缓存，存储，GridJs，GridJs存储，GridJs uid，下载，唯一标识
---


# 使用 GridJs 存储
##  通用文件处理 
导入电子表格文件后，

GridJs将在**`Config.FileCacheDirectory`**文件夹中创建具有指定uid的缓存文件，

采用[Aspose.Cells.SaveFormat.Xlsx](https://reference.aspose.com/cells/net/aspose.cells/saveformat/ "Aspose.Cells.SaveFormat")的格式保存所有形状/图像。

GridJs还将所有形状/图像保存到**`Config.PictureCacheDirectory`**文件夹中的zip归档文件中，以便稍后在客户端UI中显示形状/图像。

在客户端 UI 中的每次更新操作之后，

例如设置单元格值、设置单元格样式等，

GridJs客户端JS将触发控制器动作进行更新单元操作。

在此操作过程中，UpdateCell 方法将发生对缓存文件的保存。
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
### 实际的缓存文件在哪里 

A. 如果我们实现 GridCacheForStream 并设置 GridJsWorkbook.CacheImp。
例如，在下面的代码中，我们可以将缓存文件放在 **"D:\temp"** 中进行获取和放置
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
B. 如果我们没有设置 GridJsWorkbook.CacheImp,

GridJs 将在**`Config.FileCacheDirectory`**中创建并保存文件，这是默认的缓存目录，可以进行设置。

### 如何获取更新后的结果文件
#### 1. 为文件指定uid 
请确保文件和uid之间有指定的映射对应关系， 

您可以始终为指定的文件名获取相同的uid，而不是随机生成的。

例如，只需使用文件名即可。
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

#### 2. 与客户端UI操作同步
实际上，对于一些客户端UI操作，

例如：

切换活动工作表到另一个，

更改图像位置，

旋转/调整图像等。

UpdateCell操作将不被触发。

因此，如果我们想要获得更新后的文件与客户端UI显示的完全相同，

我们需要在保存操作之前执行合并操作，以同步这些客户端UI操作。
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
#### 3. get the file from cache
例如：在下载操作中，您可以通过 uid 从缓存目录中获取它。
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

更多详细信息，请查看这里的示例:
<https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Examples_GridJs>
