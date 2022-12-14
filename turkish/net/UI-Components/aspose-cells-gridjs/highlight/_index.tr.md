---
title: GridJs Highlight özelliği ile çalışma
type: docs
weight: 250
url: /tr/net/aspose-cells-gridjs/highlight/
description: Bu makale, hücre metnini, hücre aralıklarını, şekilleri ve resimleri vurgulamak için GridJ'lerin nasıl kullanılacağını açıklamaktadır.
keywords: highlight, highlight spreadsheet
---
# GridJs Highlight özelliği ile çalışma
 Vurgulama özelliği için aşağıdaki JS API'lerini destekliyoruz


- Vurgulamayı etkinleştir ve Vurgu stilini ayarla , tüm vurgu API'leri yalnızca vurgu stili ayarlandıktan sonra etkili olacaktır
```javascript
xs.showHighlights(style)
 // the parameter is:
 style: the style for highlight ,currently only support color
 for example: {'color':'rgba(85, 57, 47, 0.08)'}
```

- Vurgulamayı devre dışı bırak
```javascript
xs.hideHighlights()
```
- Vurgulamak için hücre metni ekleyin
```javascript
xs.sheet.addHighlightText(row,col,startpostion,endposition)
    // the parameters are:
    row:row index 
	col:column index
	startpostion: highlight start postion in cell text 
	endpostion: highlight end postion in cell text 
```

- Dizideki hücre metni için vurgulamayı kaldır
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

- Vurgulamak için hücre aralığı ekleyin
```javascript
xs.sheet.addHighlightRange(sri,sci,eri,eci)
    // the parameters are:
    sri:start row index of cell range
	sci:start column index of cell range
	 eri:end row index of cell range
	eci:end column index of cell range
```

- Dizideki hücre aralığı için vurgulamayı kaldır
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

- Hücre aralığını ters vurgu olarak ayarla
```javascript
xs.sheet.setHighlightInverseRange(sri,sci,eri,eci)
    // the parameters are:
    sri:start row index of cell range
	sci:start column index of cell range
	 eri:end row index of cell range
	eci:end column index of cell range
```

- Ters vurgu için vurguyu kaldır
```javascript
xs.sheet.removeHighlightInverseRange()
     
```

-  Ters vurgu hücre aralığını alın
```javascript
xs.sheet.getHighlightInverseRange()
```


- Diziyi vurgulamak için şekil ekleyin
```javascript
xs.sheet.addHighlightShape(shapeid)
    // the parameters are:
    shapeid: the id of shape, can be find in xs.sheet.data.shapes
```

- Dizideki vurgulama şeklini kaldır
```javascript
xs.sheet.removeHighlightShape(shapeid)
     // the parameters are:
    shapeid: the id of shape, can be find in xs.sheet.data.shapes
```

-  Vurgu şekli için dizi alın
```javascript
xs.sheet.getHighlightShaps()
```


- Diziyi vurgulamak için resim ekleyin
```javascript
xs.sheet.addHighlightImage(imageid)
    // the parameters are:
    imageid: the id of image, can be find in xs.sheet.data.images
```

- Dizideki vurgulanan görüntüyü kaldır
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


- özel görüntü vurgulama işlevini ayarla
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

Github demo sayfamızda daha fazlasını bulabilirsiniz https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples_GridJs/wwwroot/xspread/index.html
