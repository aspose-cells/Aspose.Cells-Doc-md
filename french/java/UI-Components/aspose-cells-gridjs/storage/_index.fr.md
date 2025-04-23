---
title: Travailler avec le stockage GridJs
type: docs
weight: 250
url: /fr/java/aspose-cells-gridjs/storage/
description: Cet article décrit le traitement général des fichiers pour GridJs.
keywords: cache de fichier, stockage, GridJs, stockage GridJs, uid GridJs, téléchargement, uniqueid
aliases:
  - /java/aspose-cells-gridjs/storage-introduction/
  - /java/aspose-cells-gridjs/work-with-storage/
---


# Travailler avec le stockage GridJs
## le processus général du fichier 
Après avoir importé un fichier de feuille de calcul,

GridJs créera un fichier cache avec l'uid spécifié dans le dossier **`Config.getFileCacheDirectory()`**,

avec le format de [Aspose.Cells.SaveFormat.Xlsx](https://reference.aspose.com/cells/java/aspose.cells/saveformat/ "Aspose.Cells.SaveFormat"),

GridJs sauvegardera également toutes les formes/images dans un fichier archive zip dans le dossier **`Config.getPictureCacheDirectory()`** pour une affichage ultérieur des formes/images dans l'interface utilisateur du client.

et après chaque opération de mise à jour dans l'interface utilisateur du client,

par exemple, définir la valeur de la cellule, définir le style de la cellule, etc. ,

Le code côté client de GridJs déclenchera une action de contrôleur pour effectuer une opération UpdateCell.

Dans cette action, une sauvegarde dans le fichier de cache se produira pendant la méthode UpdateCell.
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
### où se trouve le fichier cache en réalité 

A. Si nous implementons GridCacheForStream et configurons GridJsWorkbook.CacheImp.
par exemple, dans le code ci-dessous, nous pouvons simplement mettre et obtenir le fichier cache depuis **"D:\temp"**
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
B. Si nous ne configurons pas GridJsWorkbook.CacheImp,

GridJs créera et enregistrera le fichier dans le dossier **`Config.getFileCacheDirectory()`** par défaut, qui est le répertoire cache que nous pouvons définir.

### comment obtenir le fichier de résultat mis à jour
#### 1. un uid spécifié pour le fichier 
Assurez-vous qu'il existe une correspondance de mappage spécifiée entre le fichier et l'uid. 

vous pouvez toujours obtenir le même uid pour un nom de fichier spécifié, pas généré aléatoirement.

Par exemple, utilisez simplement le nom du fichier.
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

#### 2. synchroniser avec l'opération de l'interface utilisateur du client
En fait, pour certaines opérations de l'interface utilisateur du client,

par exemple :

passer à une autre feuille active,

changer la position de l'image,

faire pivoter/redimensionner l'image, etc.

l'action UpdateCell ne sera pas déclenchée.

Ainsi, si nous voulons obtenir le fichier mis à jour exactement comme l'interface utilisateur du client le montre,

nous devons effectuer une opération de fusion avant l'action de sauvegarde pour synchroniser ces opérations de l'interface utilisateur du client.
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
#### 3. obtenir l'URL du fichier depuis le cache
par exemple : dans l'action de téléchargement, vous pouvez simplement le récupérer dans le répertoire de cache par uid.
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

Pour plus d'informations détaillées, vous pouvez consulter l'exemple ici :
<https://github.com/aspose-cells/Aspose.Cells-for-java/tree/master/Examples_GridJs>
