---
title: GridJs Highlight özelliği ile çalışma
type: docs
weight: 250
url: /tr/net/aspose-cells-gridjs/highlight/
description: Bu makale, hücre metnini, hücre aralıklarını, şekilleri ve resimleri vurgulamak için GridJ'lerin nasıl kullanılacağını açıklamaktadır.
keywords: highlight, highlight spreadsheet
---
#  GridJs Highlight özelliği ile çalışma
 Vurgulama özelliği için aşağıdaki JS API'lerini destekliyoruz


-  Vurgulamayı etkinleştir ve Vurgu stilini ayarla , tüm vurgu API'leri yalnızca vurgu stili ayarlandıktan sonra etkili olacaktır
```javascript
xs.showHighlights(style)
 // the parameter is:
 style: the style for highlight ,currently only support color
 for example: {'color':'rgba(85, 57, 47, 0.08)'}
```

-  Vurgulamayı devre dışı bırak
```javascript
xs.hideHighlights()
```
-  Vurgulamak için hücre metni ekleyin
```javascript
xs.sheet.addHighlightText(row,col,startpostion,endposition)
    // the parameters are:
    row:row index 
	col:column index
	startpostion: highlight start postion in cell text 
	endpostion: highlight end postion in cell text 
    //it support multiple range postion inside one cell
```

-  Dizideki hücre metni için vurgulamayı kaldır
```javascript
xs.sheet.removeHighlightText(row,col)
    // the parameters are:
    row:row index 
	col:column index
```

-  Hücre metni için vurgulama için dizi alın
```javascript
xs.sheet.getHighlightTexts()
```

-  Vurgulamak için hücre aralığı ekleyin
```javascript
xs.sheet.addHighlightRange(sri,sci,eri,eci)
    // the parameters are:
    sri:start row index of cell range
	sci:start column index of cell range
	 eri:end row index of cell range
	eci:end column index of cell range
```

-  Dizideki hücre aralığı için vurgulamayı kaldır
```javascript
xs.sheet.removeHighlightRange(sri,sci,eri,eci)
     // the parameters are:
    sri:start row index of cell range
	sci:start column index of cell range
	 eri:end row index of cell range
	eci:end column index of cell range
```

-  Hücre aralığı için vurgulamak için dizi alın
```javascript
xs.sheet.getHighlightRanges()
```

-  Hücre aralığını ters vurgu olarak ayarla
```javascript
xs.sheet.setHighlightInverseRange(sri,sci,eri,eci)
    // the parameters are:
    sri:start row index of cell range
	sci:start column index of cell range
	 eri:end row index of cell range
	eci:end column index of cell range
```

-  Ters vurgu için vurguyu kaldır
```javascript
xs.sheet.removeHighlightInverseRange()
     
```

-  Ters vurgu hücre aralığını alın
```javascript
xs.sheet.getHighlightInverseRange()
```


-  Diziyi vurgulamak için şekil ekleyin
```javascript
xs.sheet.addHighlightShape(shapeid)
    // the parameters are:
    shapeid: the id of shape, can be find in xs.sheet.data.shapes
```

-  Dizideki vurgulama şeklini kaldır
```javascript
xs.sheet.removeHighlightShape(shapeid)
     // the parameters are:
    shapeid: the id of shape, can be find in xs.sheet.data.shapes
```

-  Vurgu şekli için dizi alın
```javascript
xs.sheet.getHighlightShaps()
```

-  Vurgulamak için metin kutusu ekleyin, metin kutusu, tip özelliğinin : "TextBox" olduğu özel bir şekil türüdür.
```javascript
xs.sheet.addHighlightTextBox(shapeid, startpostion, endposition)
    // the parameters are:
    shapeid: the id of shape, can be find in xs.sheet.data.shapes whose type is 'TextBox'
    startpostion: highlight start postion in the text of textbox
    endpostion: highlight end postion in the text of textbox
    //it support multiple range postion inside one textbox
```


- Metin kutusundaki vurgu aralığını kaldır, metin kutusu, tip özelliğinin : "TextBox" olduğu özel bir şekil türüdür.
```javascript
xs.sheet.removeHighlightTextBox(shapeid, startpostion, endposition)
    // the parameters are:
    shapeid: the id of shape, can be find in xs.sheet.data.shapes whose type is 'TextBox'
    startpostion: highlight start postion in the text of textbox
    endpostion: highlight end postion in the text of textbox
    //it support multiple range postion inside one textbox
```

-  Diziyi vurgulamak için resim ekleyin
```javascript
xs.sheet.addHighlightImage(imageid)
    // the parameters are:
    imageid: the id of image, can be find in xs.sheet.data.images
```

-  Dizideki vurgulanan görüntüyü kaldır
```javascript
xs.sheet.removeHighlightImage(imageid)
     // the parameters are:
    imageid: the id of image, can be find in xs.sheet.data.images
```

-  Vurgu resmi için dizi alın
```javascript
xs.sheet.getHighlightImages()
```

-  tüm çalışma sayfasının vurgulanıp vurgulanmayacağını, tüm şekillerin ve resimlerin dahil edilip edilmeyeceğini ayarlayın
```javascript
xs.sheet.setHighlightAll(ishighlightall,isrerender=true)
   // the parameters are:
   ishighlightall: true or false,whether to highlight all
   isrerender: true or false,whether to reRender
```


-  Özel görüntü vurgulama işlevini ayarla
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

###  Metin kutusu nesnesi için vurgula
textbox, tip özelliğinin :"TextBox" olduğu özel bir şekil türüdür.
örneğin: aşağıdaki kod hangi şeklin metin kutusu olduğunu gösterecek

```javascript
for (let shape of xs.sheet.data.shapes) {
    if (shape.type === 'TextBox') {
        console.log(shape.id + ' is a textbox');
    }
}
```
-  Metin kutusu nesnesi için vurgu ekle
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

-  Metin kutusu nesnesi için vurguyu kaldır
```javascript
    removeHighlight(startpostion,endposition)
    // the parameters are:
	startpostion: highlight start postion in textbox
	endpostion: highlight end postion in textbox
    //for example,we assume shape 0 is a textbox object
     const textbox=xs.sheet.data.shapes[0];
     textbox.removeHighlight(5,10);
```

-  Metin kutusu nesnesi için vurguyu alın
```javascript
    getHighlight()
    //for example,we assume shape 0 is a textbox object
     const textbox=xs.sheet.data.shapes[0];
     textbox.getHighlight();
```

-  Metin kutusu nesnesi için arka plan rengini değiştir
```javascript
    setBackgroundColor(color)
    // the parameters are:
        color: the html color value in hex string value
    //for example,we assume shape 0 is a textbox object,this will set the background color to Yellow 
     const textbox=xs.sheet.data.shapes[0];
     textbox.setBackgroundColor('#FFFF00');
```
-  Görsel bir aktif efekt elde etmek için arka plan rengini ve metin rengini otomatik olarak değiştirin
```javascript
    setActiveEffect(boolvalue)
    // the parameters are:
        boolvalue: if true,will change background color and the text color of the textbox object;if false,restore to original appearence
```

-  metin kutusu nesnesindeki metin içeriğini gizle/göster
```javascript
    hideText(boolvalue)
    // the parameters are:
        boolvalue: if true,will not display the text in the textbox object;if false,restore to original appearence
```



Github demo sayfamızda daha fazlasını bulabilirsiniz https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples_GridJs/wwwroot/xspread/index.html
