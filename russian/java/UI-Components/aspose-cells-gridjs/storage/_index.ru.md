---
title: Работа с хранилищем GridJs
type: docs
weight: 250
url: /ru/java/aspose-cells-gridjs/storage/
description: Эта статья описывает обработку общего файла для GridJs.
keywords: кэш файлов, хранение, GridJs, хранение GridJs, идентификатор, загрузка, уникальный идентификатор
aliases:
  - /java/aspose-cells-gridjs/storage-introduction/
  - /java/aspose-cells-gridjs/work-with-storage/
---


# Работа с хранилищем GridJs
##  процесс работы с общим файлом 
После импорта файла таблицы ,

GridJs создаст файл кеша с указанным uid в папке **`Config.getFileCacheDirectory()`** ,

в формате [Aspose.Cells.SaveFormat.Xlsx](https://reference.aspose.com/cells/java/aspose.cells/saveformat/ "Aspose.Cells.SaveFormat") ,

GridJs также сохраняет все фигуры/изображения в zip-архивный файл в папке **`Config.getPictureCacheDirectory()`** для дальнейшего отображения фигур/изображений в клиентском интерфейсе.

и после каждой операции обновления в клиентском интерфейсе (UI),

например, установка значения ячейки, установка стиля ячейки и т. д.,

клиентский js GridJs вызовет действие контроллера для выполнения операции UpdateCell.

В этом действии происходит сохранение обратно в файл кэша во время выполнения метода UpdateCell.
```JAVA  
    @PostMapping("/UpdateCell")
    public ResponseEntity<String> updateCell(HttpServletRequest request) {
        String p = request.getParameter("p");
        String uid = request.getParameter("uid");
        GridJsWorkbook gwb = new GridJsWorkbook();
        String ret;
		try {
			ret = gwb.updateCell(p, uid);
			return new ResponseEntity<>(ret, HttpStatus.OK);
		} catch (Exception e) {
			// TODO Auto-generated catch block
			return new ResponseEntity<>(gwb.errorJson(e.getMessage()), HttpStatus.OK);
		}

    }
```
###  где на самом деле находится файл кэша 

A. Если мы реализуем GridCacheForStream и установим GridJsWorkbook.CacheImp.
например, в приведенном ниже коде мы можем просто поместить и получить файл кэша из **"D:\temp"**
```JAVA
Config.setFileCacheDirectory("D:\temp");
GridJsWorkbook.CacheImp=new LocalFileCache();
public class LocalFileCache extends GridCacheForStream {

	@Override
	public void saveStream(InputStream s, String uid) {
		// make sure the directory is exist
		String filepath = Paths.get(Config.getFileCacheDirectory(), "streamcache", uid.replace('/', '.')).toString();
		try (FileOutputStream fos = new FileOutputStream(filepath.toString())) {
			s.reset(); // Equivalent to s.Position = 0 in C#
			byte[] buffer = new byte[1024];
			int length;
			while ((length = s.read(buffer)) > 0) {
				fos.write(buffer, 0, length);
			}
			fos.flush();
		} catch (IOException e) {
			e.printStackTrace();
		}

	}

	@Override
	public InputStream loadStream(String uid) {
		String filepath = Paths.get(Config.getFileCacheDirectory(), "streamcache", uid.replace('/', '.')).toString();
		try {
			return new FileInputStream(filepath);
		} catch (FileNotFoundException e) {
			e.printStackTrace();
			return null;
		}
	}

	@Override
	public boolean isExisted(String uid) {
		String filepath = Paths.get(Config.getFileCacheDirectory(), "streamcache", uid.replace('/', '.')).toString();
		return Files.exists(Paths.get(filepath));
	}

	@Override
	public String getFileUrl(String uid) {
		return "/GridJs2/GetFileUseCacheStream?id=" + uid;
	}

}
		...
```
B. Если мы не установим GridJsWorkbook.CacheImp,

GridJs создаст и сохранит файл внутри папки **`Config.getFileCacheDirectory()`**, которая является папкой кеша по умолчанию, которую мы можем установить.

###  как получить обновленный результат файла
#### 1. указанный идентификатор (UID) для файла 
Убедитесь, что существует соответствие между файлом и идентификатором (UID), 

вы всегда можете получить один и тот же идентификатор (UID) для заданного имени файла, а не случайно сгенерированный.

Например, достаточно использовать имя файла.
```JAVA
//in controller  

     @GetMapping("/DetailStreamJsonWithUid")
    public void detailStreamJsonWithUid(@RequestParam String filename, @RequestParam String uid,HttpServletResponse response) {


        	Path filePath = Paths.get(listDir, filename);
            GridJsWorkbook wbj = new GridJsWorkbook();

            response.setContentType("application/json");
            response.setHeader("Content-Encoding", "gzip");
            try (GZIPOutputStream gzipOutputStream = new GZIPOutputStream(response.getOutputStream())) {
                wbj.importExcelFile(filePath.toString());
                wbj.jsonToStream(gzipOutputStream, filename);
            } catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			} catch (Exception e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
    }
```

#### 2. синхронизация с клиентским интерфейсом (UI)
Фактически, для некоторых операций интерфейса (UI) клиента,

например:

смена активного листа на другой,

изменение позиции изображения,

вращать/изменить размер изображения и т. д.

действие UpdateCell не будет вызвано.

Таким образом, если мы хотим получить обновленный файл такой же, как показывает клиентский интерфейс,

нам нужно выполнить операцию слияния перед сохранением, чтобы синхронизировать операции клиентского интерфейса.
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
```JAVA
//in controller action 
  GridJsWorkbook wb = new GridJsWorkbook();
  wb.mergeExcelFileFromJson(uid, p);
  //after merge do save to chache or to a stream or whaterver you want to save to ,here we just save to cache
  wb.saveToCacheWithFileName(uid,filename,password);
```         
#### 3. получить URL файла из кеша
например: в операции загрузки, вы можете просто получить его из каталога кэша по UID.
```JAVA
//in controller  

      String fileUrl = null;
			if (GridJsWorkbook.CacheImp != null) {
				fileUrl = GridJsWorkbook.CacheImp.getFileUrl(uid + "/" + filename);
			} else {
				fileUrl = "/GridJs2/GetFile?id=" + uid + "&filename=" + filename;
			}
			return ResponseEntity.ok("\""+fileUrl+"\"");
```

Для получения более подробной информации вы можете проверить пример здесь:
<https://github.com/aspose-cells/Aspose.Cells.Grid-for-Java/tree/master/Examples_GridJs>
