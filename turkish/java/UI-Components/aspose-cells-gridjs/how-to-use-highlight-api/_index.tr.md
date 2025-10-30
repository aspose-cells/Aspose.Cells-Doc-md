---
title: GridJs vurgu özelliği ile çalışmak
type: docs
weight: 250
url: /tr/java/aspose-cells-gridjs/how-to-use-highlight-api/
description: Bu makale, GridJs de metin, hücre aralıkları, şekiller ve resimler üzerinde vurgu nasıl kullanılacağını açıklar.
keywords: GridJs, vurgulama, vurgulu hesap tablosu, sansürleme, açıklamalar
aliases:
  - /java/aspose-cells-gridjs/highlight/
  - /java/aspose-cells-gridjs/how-to-highlight/
  - /java/aspose-cells-gridjs/work-with-highlight-api/
  - /java/aspose-cells-gridjs/work-with-highlight-apis/
---

# GridJs Vurgulama Özelliği İle Çalışma 
Vurgulama özelliği için aşağıdaki JS API'lerini destekliyoruz 


- Vurgulamayı etkinleştir ve vurgulama stili ayarla, tüm vurgulama API'leri yalnızca etkin elektronik tabloda vurgulama stili ayarlandıktan sonra geçerli olacaktır 
```javascript
xs.sheet.showHighlights(style)
 // the parameter is:
 style: the style for highlight ,currently only support color
 for example: {'color':'rgba(85, 57, 47, 0.08)'}
```

- etkin elektronik tabloda ayarlanmış vurgulama stili güncelle 
```javascript
xs.sheet.updateHighlightStyle(style)
 // the parameter is:
 style: the style for highlight ,currently only support color
 for example: {'color':'rgba(85, 57, 47, 0.08)'}
```


- etkin elektronik tabloda vurgulamayı devre dışı bırak    
```javascript
xs.sheet.hideHighlights()
```
- etkin elektronik tabloda hücre metnini vurgulamak için diziye hücre metni ekle 
```javascript
xs.sheet.addHighlightText(row,col,startpostion,endposition)
    // the parameters are:
	row:row index 
	col:column index
	startpostion: highlight start postion in cell text 
	endpostion: highlight end postion in cell text 
    //it support multiple range postion inside one cell
```

- etkin elektronik tabloda hücre metni için vurgulamayı kaldır 
```javascript
xs.sheet.removeHighlightText(row,col,startpostion,endposition)
    // the parameters are:
	row:row index 
	col:column index
	startpostion: highlight start postion in cell text 
	endpostion: highlight end postion in cell text 
```

- etkin elektronik tabloda hücre metni için vurgulama dizisi al   
```javascript
xs.sheet.getHighlightTexts()
```

- Etkin çalışma sayfasına vurgulanacak hücre aralığını ekle 
```javascript
xs.sheet.addHighlightRange(sri,sci,eri,eci)
    // the parameters are:
	sri:start row index of cell range
	sci:start column index of cell range
	eri:end row index of cell range
	eci:end column index of cell range
```

- Etkin çalışma sayfasında dizi içindeki hücre aralığı için vurguyu kaldır 
```javascript
xs.sheet.removeHighlightRange(sri,sci,eri,eci)
     // the parameters are:
	sri:start row index of cell range
	sci:start column index of cell range
	eri:end row index of cell range
	eci:end column index of cell range
```

- Etkin çalışma sayfasında hücre aralığı için vurgu dizisini al   
```javascript
xs.sheet.getHighlightRanges()
```

- Etkin çalışma sayfasında ters vurgu için hücre aralığını ayarla 
```javascript
xs.sheet.setHighlightInverseRange(sri,sci,eri,eci)
    // the parameters are:
	sri:start row index of cell range
	sci:start column index of cell range
	eri:end row index of cell range
	eci:end column index of cell range
```

- Etkin çalışma sayfasında ters vurgu için vurguyu kaldır 
```javascript
xs.sheet.removeHighlightInverseRange()

```

- Etkin çalışma sayfasında ters vurgu hücre aralığını al 
```javascript
xs.sheet.getHighlightInverseRange()
```


- Etkin çalışma sayfasında vurgu dizisine şekil ekle 
```javascript
xs.sheet.addHighlightShape(shapeid)
    // the parameters are:
    shapeid: the id of shape, can be find in xs.sheet.data.shapes
```

- Etkin çalışma sayfasında vurgu şeklini dizi içinden kaldır 
```javascript
xs.sheet.removeHighlightShape(shapeid)
     // the parameters are:
    shapeid: the id of shape, can be find in xs.sheet.data.shapes
```

- Etkin çalışma sayfasında vurgu şekli için dizi al  
```javascript
xs.sheet.getHighlightShaps()
```

- Etkin çalışma sayfasında metin kutusu ekle, metin kutusu, "TextBox" türü özelliği olan özel bir şekildir 
```javascript
xs.sheet.addHighlightTextBox(shapeid, startpostion, endposition)
    // the parameters are:
    shapeid: the id of shape, can be find in xs.sheet.data.shapes whose type is 'TextBox'
    startpostion: highlight start postion in the text of textbox
    endpostion: highlight end postion in the text of textbox
    //it support multiple range postion inside one textbox
```


- Metin kutusunda vurgulu aralığı kaldır, metin kutusu, "TextBox" türü özelliği olan özel bir şekildir 
```javascript
xs.sheet.removeHighlightTextBox(shapeid, startpostion, endposition)
    // the parameters are:
    shapeid: the id of shape, can be find in xs.sheet.data.shapes whose type is 'TextBox'
    startpostion: highlight start postion in the text of textbox
    endpostion: highlight end postion in the text of textbox
    //it support multiple range postion inside one textbox
```

- Etkin çalışma sayfasında resme vurgu dizisi ekle 
```javascript
xs.sheet.addHighlightImage(imageid)
    // the parameters are:
    imageid: the id of image, can be find in xs.sheet.data.images
```

- Etkin çalışma sayfasında dizi içindeki resmi vurguyu kaldır 
```javascript
xs.sheet.removeHighlightImage(imageid)
     // the parameters are:
    imageid: the id of image, can be find in xs.sheet.data.images
```

- Vurgulu resim dizisi al  
```javascript
xs.sheet.getHighlightImages()
```

-  Etkin çalışma sayfasında tüm şekilleri ve resimleri ve tüm çalışma sayfası alanını vurgulayıp vurgulamamayı ayarla
```javascript
xs.sheet.setHighlightAll(ishighlightall,isrerender=true)
   // the parameters are:
   ishighlightall: true or false,whether to highlight all
   isrerender: true or false,whether to reRender
```


- Özel resim vurgu işlevini ayarla
```javascript
xs.sheet.setCustomHighlightImgFunc(func)
   // the parameters are:
   func: the custom highlight image function, it shall take two parameters ,first is ishighlight,the second one is the fabric image object 
   //we use fabric js to manage image object, please refer to http://fabricjs.com/image-filters to check more info
   below is an example for the decleare function: 
   const customHighlightImage = (ishighlight, imgobj) => {
            imgobj.filters[0] = ishighlight ? new fabric.Image.filters.Sepia() : false;
            imgobj.applyFilters();
        }

```

-  Etkin çalışma sayfasında vurgu ayarlarını temizle
```javascript
xs.sheet.clearHighlights()

```

### Metin Kutusu Nesnesi için Vurgu
Metin kutusu, "TextBox" türü özelliği olan özel bir şekildir
Örneğin: Aşağıdaki kod, hangi şeklin metin kutusu olduğunu gösterecektir

```javascript
for (let shape of xs.sheet.data.shapes) {
    if (shape.type === 'TextBox') {
        console.log(shape.id + ' is a textbox');
    }
}
```
- Metin kutusu nesnesi için vurgu ekle
```javascript
    addHighlight(startpostion,endposition)
    // the parameters are:
	startpostion: highlight start postion in textbox
	endpostion: highlight end postion in textbox

//for example,we assume shape 0 is a textbox object
const textbox=xs.sheet.data.shapes[0];
//first we shall add to highlight shape to enable the highlight for the textbox shape object,it support multiple range postion 
 xs.sheet.addHighlightShape(textbox.id);
 textbox.addHighlight(5,10);
 textbox.addHighlight(18,28);
```

- Metin kutusu nesnesi için vurguyu kaldır 
```javascript
    removeHighlight(startpostion,endposition)
    // the parameters are:
	startpostion: highlight start postion in textbox
	endpostion: highlight end postion in textbox
    //for example,we assume shape 0 is a textbox object
     const textbox=xs.sheet.data.shapes[0];
     textbox.removeHighlight(5,10);
```

- Metin kutusu nesnesi için vurguyu al 
```javascript
    getHighlight()
    //for example,we assume shape 0 is a textbox object
     const textbox=xs.sheet.data.shapes[0];
     textbox.getHighlight();
```




Daha fazlasını github demo sayfamızda bulabilirsiniz https://github.com/aspose-cells/Aspose.Cells.Grid-for-Java/blob/main/Examples.GridJs/src/main/resources/templates/index.html
