---
title: GridJs İstemci Tarafı ile Çalışma
type: docs
weight: 250
url: /tr/net/aspose-cells-gridjs/client/
---
# GridJs İstemci Tarafı ile Çalışma
GridJs istemcisini temel alarak geliştirdik[x-elektronik tablo](https://github.com/myliang/x-spreadsheet).

## ana adımlar şunlardır:

- x_spreadsheet örneği oluştur
```javascript
xs = x_spreadsheet(id, options)
```
- json verilerini yükle
```javascript
xs.loadData(jsondata.data)
```
- aktif sayfayı ayarla
```javascript
xs.setActiveSheetByName(jsondata.actname)
```
- aktif hücreyi ayarla
```javascript
xs.setActiveCell(jsondata.actrow,jsondata.actcol);
```

örneğin aşağıdaki kod bir x_spreadsheet nesnesi başlatır.
```javascript
 xs = x_spreadsheet('#gridjs-demo', {
			updateMode:'server',
			updateUrl:'/GridJs2/UpdateCell',
			mode: 'edit',
			showToolbar: true,
                        local: 'en',
            showContextmenu: true
        }).loadData(sheets)
```
 // seçenekler için parametreler:
 updateMode: şu anda yalnızca 'sunucu'yu destekliyoruz
 updateUrl: json tabanlı güncelleme eylemi için sunucu tarafı url'sini ayarlayın
 mod: okuma, salt okunur tablo anlamına gelir/düzenle, elektronik tabloyu düzenleyebileceğimiz anlamına gelir
 showToolbar: araç çubuğunun gösterilip gösterilmeyeceği anlamına gelir
 showFileName: dosya adının gösterilip gösterilmeyeceği
 yerel: menüler için çoklu dili destekler, yerel ayar şu şekilde olabilir: ingilizce, çince, İspanyolca, Portekizce, almanya, Rusça, Hollandaca için en, cn, es, pt, de, ru, nl
 showContextmenu: bir hücreye sağ tıklandığında bağlam menüsünün gösterilip gösterilmeyeceği anlamına gelir
## 

___
## diğer faydalı api'ler
- Görünümü oluştur
```javascript
xs.reRender()
```
- Seçilen Görüntüyü/şekli Al���hiçbir şey yoksa, seçim null değerini döndürmez
```javascript
xs.sheet.selector.getObj()
```

- Hücre nesnesini al
```javascript
xs.sheet.data.getCell(ri,ci)
    // the parameters are:
    ri:row index 
	ci:column index
```
- Hücre stilini al
```javascript
xs.sheet.data.getCellStyle(ri,ci)
    // the parameters are:
    ri:row index 
	ci:column index
```
- Hücre değerini ayarla
```javascript
xs.sheet.data.setCellText(ri,ci,value,state)
    // the parameters are:
    ri:row index 
	ci:column index
	value:the cell value
	state: input | finished
```

- Seçili hücre aralığını Al/Ayarla
```javascript
xs.sheet.data.selector.range
```
- Seçilen hücre veya hücre alanı için hücre değerini ayarlayın
```javascript
xs.sheet.data.setSelectedCellText(value)
    // the parameters are:
	value:the  value for the cell
```
- Seçilen hücre veya hücre alanı için stili ayarlayın
```javascript
xs.sheet.data.setSelectedCellAttr(attributename,value)
    // the parameters are:
    attributename:font-name | font-bold | font-italic | font-size  | format|border|merge|formula |strike|textwrap |underline |align |valign |color|bgcolor|pattern
	value:the  value for the attribute
```

- Seçilen hücre alanını birleştir
```javascript
xs.sheet.data.merge()
```

- Seçilen hücre alanını ayır
```javascript
xs.sheet.data.unmerge()
```
-  Seçili hücreyi sil
```javascript
xs.sheet.data.deleteCell(what)
    // the parameters are:
    what:all|format  all: means delete the cell and clear the style ;format means delete the cell value and keep the cell style
```
- Dondur bölmesini ayarla
```javascript
xs.sheet.data.setFreeze(ri,ci)
    // the parameters are:
    ri:row index 
	ci:column index
```

-  Seçili hücreye satır veya sütun ekle
```javascript
xs.sheet.data.insert(type, n)
    // the parameters are:
    type: row | column
	n:the row or column number
```
-  Seçili hücredeki satır veya sütunları sil
```javascript
xs.sheet.data.delete(type)
    // the parameters are:
    type: row | column
```

- Sütun için genişliği ayarlayın
```javascript
xs.sheet.data.setColWidth(ci,width)
    // the parameters are:
    ci:column index
	width:the width for the column
```
-  Sütun için genişliği alın
```javascript
xs.sheet.data.cols.sumWidth(min,max)
    // the parameters are:
    min:the start column index
	max:the end column index,not include
```

- Satır için yüksekliği ayarlayın
```javascript
xs.sheet.data.setRowHeight(ri,height)
    // the parameters are:
    ri:row index
	height:the height for the row
```
-  Satır için yüksekliği al
```javascript
xs.sheet.data.rows.sumHeight(min,max)
    // the parameters are:
    min:the start row index
	max:the end row index,not include
```
- Ekran yönünü Al/Ayarla
```javascript
xs.sheet.data.displayRight2Left
```



detaylı bilgi için buradan örneği inceleyebilirsiniz
<https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Examples_GridJs>



 
 
