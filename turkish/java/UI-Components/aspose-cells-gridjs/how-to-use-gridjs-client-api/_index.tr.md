---
title: GridJs İstemci Tarafı İle Çalışmak
type: docs
weight: 250
url: /tr/java/aspose-cells-gridjs/how-to-use-gridjs-client-api/
keywords: GridJs, özel, logo, ayarlama, api
description: Bu makale, GridJs te istemci tarafı için JavaScript API lerini veya işlevleri tanıtır.
aliases:
  - /java/aspose-cells-gridjs/client/
  - /java/aspose-cells-gridjs/work-with-client-api/
  - /java/aspose-cells-gridjs/use-js-api/
  - /java/aspose-cells-gridjs/gridjs-spreadsheet-api/
---

# GridJs İstemci Tarafı İle Çalışmak
[x-spreadsheet](https://github.com/myliang/x-spreadsheet) tabanlı GridJs istemcisini geliştirdik.

## Ana adımlar:

- x_spreadsheet örneği oluştur
```javascript
xs = x_spreadsheet(id, options)
    // the parameters are:
    id:the html node id ,for example :'#gridjs-demo' for the html  <div id="gridjs-demo"></div>
    options:the load options,
     // the parameters for options:
	    updateMode:  currently we only support 'server'
	    updateUrl:  set the server side  url for update action based on json
		view: set the view size for the sheet,for example `{width: () => 1000, height: ()=> 500}`
	    mode: read means readonly spread sheet/edit means we can edit the spread sheet
            allowSelectTextInTextBoxInReadMode: whether allow select text in TextBox control when in read mode,the default value is false
	    showToolbar:   means whether to show toolbar
	    showFileName:  whether to show the filename 
	    local:         support multiple language for menus ,the locale can be:
	                        en, cn, es, pt, de, ru, nl, 
	                   for  English,Chinese,Spanish,Portuguese,German,Russian,Dutch
			        ar, fr,id,it,ja
                           for  Arabic,French,Indonesian,Italian,Japanese
			        ko,th,tr,vi,cht
                           for  Korean,Thai,Turkey,Vietnamese,Traditional Chinese                  
	    showContextmenu:   means whether to show contextmenu on right click on a cell
            loadingGif:  the loading gif url when loading the image/shape .it is optional,the default value is:content/img/updating.gif
	for example the below code init a x_spreadsheet object.
	xs = x_spreadsheet('#gridjs-demo', {
			updateMode:'server',
			updateUrl:'/GridJs2/UpdateCell',
			mode: 'edit',
			showToolbar: true,
                        local: 'en',
			showContextmenu: true
			})
```

- json verileri ile yükle
```javascript
xs.loadData(data)
// the parameters is:
	data: the json data which describ the data structure for the worksheets
```
- sayfa adıyla etkin tabloyu ayarla
```javascript
xs.setActiveSheetByName(sheetname)
// the parameters is:
	sheetname: the sheet name 
```
- id ile etkin tabloyu ayarla
```javascript
xs.setActiveSheet(id)
// the parameters is:
	sheetname: the sheet id 
```

- etkin hücreyi ayarla
```javascript
xs.setActiveCell(row,col);
// the parameters are:
	row: the cell row
	col: the cell column
```

- sunucu taraflı eylem için şekil/resim işlemi için bilgi ayarla
```javascript
xs.setImageInfo(imageGetActionUrl, imageAddByUploadActionUrl, imageAddByUrlActionUrl, imageCopyActionUrl, zindex, loadingGif);
// the parameters are:
	imageGetActionUrl: the get image action URL in the server side controller
	imageAddByUploadActionUrl: the upload image action  URL in the server side controller
	imageAddByUrlActionUrl: the add image from URL action  URL in the server side controller
	imageCopyActionUrl: the copy image action  URL in the server side controller
	zindex: the minimum zindex of the image in the canvas
	loadingGif (optional): the loading gif url when loading the image/shape .it is optional,the default value is:content/img/updating.gif
    for example: 
            const imageurl = "/GridJs2/imageurl";
            const imageuploadurl1 = "/GridJs2/AddImage";
            const imageuploadurl2 = "/GridJs2/AddImageByURL";
            const imagecopyurl = "/GridJs2/CopyImage";  
	    const basiczorder = 5678;
    xs.setImageInfo(imageurl, imageuploadurl1, imageuploadurl2, imagecopyurl, basiczorder);
```

- sunucu taraflı eylem için indirme işlemi için bilgi ayarla
```javascript
xs.setFileDownloadInfo(downloadActionUrl);
// the parameters are:
	downloadActionUrl: the get download file action URL in the server side controller

    for example: 
            const fileDownloadUrl = "/GridJs2/Download";
            xs.setFileDownloadInfo(fileDownloadUrl);
```

- sunucu taraflı eylem için ole nesnesi işlemi için bilgi ayarla
```javascript
xs.setOleDownloadInfo(oleActionUrl);
// the parameters are:
	oleActionUrl: the ole object file action URL in the server side controller
    for example: 
            const oleDownloadUrl = "/GridJs2/Ole";
            xs.setOleDownloadInfo(oleDownloadUrl);
```


___
## diğer faydalı api'ler
- Görünümü oluştur
```javascript
xs.reRender()
```

- etkin tablo id'sini al
```javascript
xs.getActiveSheet()
```

- Yakınlaştırma seviyesi ayarla
```javascript
xs.setZoomLevel(zoom)
// the parameters is:
	zoom:the zoom level ,can be number ,for example 0.5 for zoom out, or 2 for zoom in
```

- Dosya adını ayarla 
```javascript
xs.setFileName(name)
// the parameters is:
	name:the file name with extension ,for example trip.xlsx
```

- E-posta gönderme özelliği için geri çağrı işlevi.
```javascript
xs.setEmailSendCallFunction(callback)
// the parameters is:
	callback: the callback function to handle email sending, receives a mailObj parameter
		callback: function(mailObj) {
			// mailObj properties:
			// mailObj.receiver: the email address of the receiver, e.g., 'example@gmail.com'
			// mailObj.type: the format of the file to be sent, can be 'html', 'xlsx', or 'pdf'
		}
```

- GridJs için pencere olayı etkinleştirilsin mi
```javascript
xs.enableKeyEvent(isenable)
// the parameters is:
	isenable:whether the window key event is active for GridJs
//when has other controls in the same page, you may want to ignore the key event in GridJs 
```

- pencereye bağlı tüm olayları, pencere olayı ve pencere yeniden boyutlandırma olayını içeren GridJs'ten çözülmemiş tüm olayları ayır
```javascript
xs.destroy()
```


-  Görüntü/şekil için görünür filtre ayarla
```javascript
    // need to set a function which return true(for visible) or false(for invisible) for the visible filter with the below parameters :
	sheet:the sheet instance
	s:the image or shape instance
    for example: 
	//this will make visible for image/shape in sheet with name 'Sheet3' and 'Sheet1' except for the 'Rectangle' type
		xs.setVisibleFilter((sheet,s) => { if (sheet.data.name==='Sheet3'||sheet.data.name==='Sheet1') return s.type!=='Rectangle';  return false; })
	//this will make visible for image/shape in sheet with name  'Sheet1' 
		xs.setVisibleFilter((sheet,s) => { if (sheet.data.name==='Sheet1') return true;  return false; })
	//this will make invisible for image/shape in all sheets 
		xs.setVisibleFilter((sheet,s) => {  return false; })
	//if all the image/shape is already loaded and you want to change the visible filter at runtime,you can call the below code to trigger a reload for image/shape
		xs.setActiveSheet(xs.getActiveSheet())
```

-  Seçili görüntü/şekli al, eğer bir şey seçilmediyse null dönecektir
```javascript
xs.sheet.selector.getObj()
```

-  Görüntü/şekil için seçilebilir durumu ayarla 
```javascript
const shape=xs.sheet.selector.getObj();
shape.setControlable(isenable)
     // the parameter is:
      isenable: when set to true,the image or shape can be selectable and movable/resizeable
```

-  Hücre nesnesini al
```javascript
xs.sheet.data.getCell(ri,ci)
    // the parameters are:
	ri:row index 
	ci:column index
```
-  Hücre stilini al
```javascript
xs.sheet.data.getCellStyle(ri,ci)
    // the parameters are:
	ri:row index 
	ci:column index
```
-  Hücre değerini ayarla
```javascript
xs.sheet.data.setCellText(ri,ci,value,state)
    // the parameters are:
	ri:row index 
	ci:column index
	value:the cell value
	state: input | finished ,if finished ,it will do update action to servside
```

-  Seçili hücre aralığını al/ayarla
```javascript
xs.sheet.data.selector.range
```
-  Seçili hücre veya hücre alanı için hücre değerini ayarla
```javascript
xs.sheet.data.setSelectedCellText(value)
    // the parameters are:
	value:the  value for the cell
```
-  Seçili hücre veya hücre alanı için stil ayarla
```javascript
xs.sheet.data.setSelectedCellAttr(attributename,value)
    // the parameters are:
	attributename:font-name | font-bold | font-italic | font-size  | format|border|merge|formula |strike|textwrap |underline |align |valign |color|bgcolor|pattern
	value:the  value for the attribute
```

-  Seçili hücre alanını birleştir
```javascript
xs.sheet.data.merge()
```

-  Seçili hücre alanının birleşimini kaldır
```javascript
xs.sheet.data.unmerge()
```
-  Seçili hücreyi sil  
```javascript
xs.sheet.data.deleteCell(type)
    // the parameters are:
	type:all|format  all: means delete the cell and clear the style ;format means delete the cell value and keep the cell style
```
-  Sabit pencereyi ayarla
```javascript
xs.sheet.data.setFreeze(ri,ci)
    // the parameters are:
	ri:row index 
	ci:column index
```

-  Seçili hücrede satır veya sütun ekle  
```javascript
xs.sheet.data.insert(type, n)
    // the parameters are:
	type: row | column
	n:the row or column number
```
-  Seçili hücrede satır veya sütun sil  
```javascript
xs.sheet.data.delete(type)
    // the parameters are:
	type: row | column
```

-  Sütun için genişliği ayarla
```javascript
xs.sheet.data.setColWidth(ci,width)
    // the parameters are:
	ci:column index
	width:the width for the column
```
-  Sütunlar için genişliği ayarla
```javascript
xs.sheet.data.setColsWidth(sci,eci,width)
    // the parameters are:
	sci:the start column index
	eci:the end column index
	width:the width for the column
```

-  Tüm sütunlar için genişliği ayarla
```javascript
xs.sheet.data.setAllColsWidth(width)
    // the parameters are:
	width:the width for the columns
```

-  Sütun için genişliği al 
```javascript
xs.sheet.data.cols.sumWidth(min,max)
    // the parameters are:
	min:the start column index
	max:the end column index,not include
```

-  Satır için yüksekliği ayarla
```javascript
xs.sheet.data.setRowHeight(ri,height)
    // the parameters are:
	ri:row index
	height:the height for the row
```
-  Satırlar için yüksekliği ayarla
```javascript
xs.sheet.data.setRowsHeight(sri,eri,height)
    // the parameters are:
	sri:start row index
	eri:end row index
	height:the height for the rows
```

-  Tüm satırlar için yüksekliği ayarla
```javascript
xs.sheet.data.setAllRowsHeight(height)
    // the parameters are:
	height:the height for the rows
```


-  Satır için yükseklik al 
```javascript
xs.sheet.data.rows.sumHeight(min,max)
    // the parameters are:
	min:the start row index
	max:the end row index,not include
```

-  Görüntüleme yönünü al/ayarla
```javascript
xs.sheet.data.displayRight2Left
```

## Olay geri çağrısı
- Aşağıdaki olayları takip edebiliriz
```javascript
 xs.on('cell-selected', (cell, ri, ci) => {
                console.log('cell selected:', cell, ', ri:', ri, ', ci:', ci);
                if (ci === -1) {
                    console.log('ci === -1 means a row selected ',ri);
                }
                if (ri === -1) {
                    console.log('ri === -1 means a column selected',ci);
                }
            }).on('cells-selected', (cell, range) => {
                console.log('range   selected:', cell, ', rang:', range);
            }).on('object-selected', (shapeOrImageObj) => {
                console.log('shape or image selected id:', shapeOrImageObj.id, ', type: ', shapeOrImageObj.type);
            }).on('sheet-selected', (id,name) => {
                console.log('sheet selected id:', id, ', name: ',name);
            }).on('sheet-loaded', (id,name) => {
                console.log('sheet load finished:', id, ', name: ',name);
            }).on('cell-edited', (text, ri, ci) => {
                console.log('text:', text, ', ri: ', ri, ', ci:', ci);
            });
```

## Özelleştirme

- Ana simgeyi ve bağlantıyı ayarlayın
```javascript
xs.sheet.menubar.icon.setHomeIcon(iconUrl,targetUrl)
    // the parameters are:
	iconUrl:the home icon URL
	targetUrl:the target link URL
	for example ,the below code will set the new logo and with link to google.com
	xs.sheet.menubar.icon.setHomeIcon('https://forum.aspose.com/letter_avatar_proxy/v4/letter/y/3e96dc/45.png','https://www.google.com')
```
- Menü çubuğunu göster
```javascript
xs.sheet.menubar.show()
```

- Menü çubuğunu gizle
```javascript
xs.sheet.menubar.hide()
```


## TextBox nesnesi için API'lar
TextBox özel bir şekil türüdür ve tip özelliği: "TextBox",
Örneğin: Aşağıdaki kod, hangi şeklin metin kutusu olduğunu gösterecektir

```javascript
for (let shape of xs.sheet.data.shapes) {
    if (shape.type === 'TextBox') {
        console.log(shape.id + ' is a textbox');
    }
}
```

- Metin kutusu nesnesi için arka plan rengini değiştir
```javascript
    setBackgroundColor(color)
    // the parameters are:
        color: the html color value in hex string value
    //for example,we assume shape 0 is a textbox object,this will set the background color to Yellow 
     const textbox=xs.sheet.data.shapes[0];
     textbox.setBackgroundColor('#FFFF00');
```
- Görsel etki elde etmek için arka plan rengini ve metin rengini otomatik olarak değiştir
```javascript
    setActiveEffect(boolvalue)
    // the parameters are:
        boolvalue: if true,will change background color and the text color of the textbox object;if false,restore to original appearence
```

- TextBox nesnesinde metin içeriğini gizle/göster
```javascript
    hideText(boolvalue)
    // the parameters are:
        boolvalue: if true,will not display the text in the textbox object;if false,restore to original appearence
```

detaylı bilgi için buradaki örneği kontrol edebilirsiniz
<https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Examples_GridJs>





