---
title: GridJs için özel bağlam menüleri  
type: docs
weight: 250
url: /tr/net/aspose-cells-gridjs/custommenu/
description: Bu makale, GridJs için bağlam menülerini nasıl yapılandıracağınızı açıklar.
keywords: GridJs, özel menü öğeleri, bağlam menüsü, özel, bağlam, menü
---

# Özel bağlam menüleri
Örneğin, satır/sütun ekleme/silme ve benzeri bazı yerleşik bağlam menü öğelerimiz var
Ancak kullanıcı özel bağlam menü öğeleri istiyorsa.
Yükleme seçeneklerinde bağlam menü öğelerini ayarlamayı destekliyoruz.
örneğin:
```javascript
        const onMyActionClick1 = (sheet) => {
            console.log('my action clicked1' +  sheet.data.name)
        };
        const onMyActionClick2 = (sheet) => {
            console.log('my action clicked2' + sheet.data.name)
        };
  xs = x_spreadsheet('#gridjs-demo', {
                updateMode: 'server',
                updateUrl: '/GridJs2/UpdateCell',
                showToolbar: true,
                mode: 'edit',
                local: 'en',
                showContextmenu: true,
		//this option is for context menus,we need to set usedefault to false to load custom context menus
                contextMenuItems: {
                    usedefault: false,
                    customItems: [{ 'key': 'key1', 'text': 'c title 11111', 'callback': onMyActionClick1 },
                                  { 'key': 'key2', 'text': 'c title 22222', 'callback': onMyActionClick2 }]
                }
            })
```

Özel bağlam menü öğeleri için aşağıdaki JS API'lerini destekliyoruz


- özel bağlam menü öğelerini al
```javascript
xs.sheet.getCustomContextMenuItems()
```

- özel bağlam menü öğelerini ekle
```javascript
xs.sheet.addCustomContextMenuItems(itemsarray)
 // the parameter is:
 itemsarray: the array of custom menu items,the callback function x parameter will be the js variable of xs.sheet
 for example: [{'key':'key4','text':'menu4','callback':(x)=>{console.log('hello4444');}},{'key':'key3','text':'menu3','callback':(x)=>{console.log('hello3333');}}]
```

- özel bağlam menü öğelerini sil
```javascript
 xs.sheet.delCustomContextMenuItems(keysarray)()
 // the parameter is:
 keysarray: the array of the keys of the menu items
 for example: ['key4','key3']
```

- belirtilen konuma özel bağlam menü öğesi ekle
```javascript
xs.sheet.insertCustomContextMenuItem(item,postion)
 // the parameter is:
 item: the custom menu item,the callback function x parameter will be the js variable of xs.sheet
 for example: {'key':'key4','text':'menu4','callback':(x)=>{console.log('hello4444');}} 
 postion:the postion for the inserted item in the items array
```

- anahtarla özel bağlam menü öğesini güncelle
```javascript
xs.sheet.updateCustomContextMenuItem(key,item)
 // the parameter is:
 item: the updated properties that with text or callback
 for example: {'text':'menu updated'}
 key:the key of the menu item
```


- resim/şekil için özel bağlam menü öğelerini al
```javascript
xs.sheet.getImageContextMenuItems()
```

- resim/şekil için özel bağlam menü öğelerini ekle
```javascript
xs.sheet.addImageContextMenuItems(itemsarray)
 // the parameter is:
 itemsarray: the array of custom menu items,the callback function x parameter will be the js variable of xs.sheet
 for example: [{'key':'key4','text':'img operation1','callback':(x)=>{console.log('operation1 on image');}},{'key':'key3','text':'img operation2','callback':(x)=>{console.log('operation2 on image');}}]
```

- resim/şekil için özel bağlam menü öğelerini sil
```javascript
 xs.sheet.delImageContextMenuItems(keysarray)()
 // the parameter is:
 keysarray: the array of the keys of the menu items
 for example: ['key4','key3']
```

Daha fazlasını github demo sayfamızda bulabilirsiniz https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples_GridJs/wwwroot/xspread/index.html



