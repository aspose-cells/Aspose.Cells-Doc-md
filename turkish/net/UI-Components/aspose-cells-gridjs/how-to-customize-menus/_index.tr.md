---
title: GridJs de menüleri ve araç çubuklarını nasıl özelleştirirsiniz  
type: docs
weight: 250
url: /tr/net/aspose-cells-gridjs/how-to-customize-menus/
description: Bu makale, GridJs de menüleri ve araç çubuklarını nasıl özelleştireceğinizi anlatır.
keywords: GridJs, özelleştirilebilir menüler, menüler, özelleştir
aliases:
  - /net/aspose-cells-gridjs/customize-menus/
  - /net/aspose-cells-gridjs/customize-ui/
  - /net/aspose-cells-gridjs/customize-toolbar/

---

## Menüleri ve araç çubuğu düğmelerini özelleştirme hakkında
doğrudan kullanışlı API'ler sağlamıyoruz.
ancak dom yapısına dayalı bazı js fonksiyonları yazarak bunu başarabiliriz.



## Menü çubuğunu özelleştir 
örneğin: yalnızca Dosya menüsünü tutmak için, GridJs div kimliğinin "gridjs-divid" olduğunu varsayın
```javascript
   //get menubar parent dom
   const menubar=document.querySelector("#gridjs-divid > div > div:nth-child(1) > div > div.x-spreadsheet-banner-info-s > div.x-spreadsheet-toolbar.x-spreadsheet-menubar");
   var childs = menubar.childNodes;


   for (var i = childs.length - 1; i >= 0; i--)
   {  
     // keep File menu  only
     if(childs[i].childNodes[0].childNodes[0].textContent!=="File")
       {
         menubar.removeChild(childs[i]);
       }
   }


```
Bu fonksiyon çağrıldıktan sonra 

![yapılacak:menü çubuğunu özelleştirme ekranı](gridjs_customize_menubar.png)


## Menü çubuğundaki öğeleri özelleştir 
örneğin: sadece Dosya menüsünde "Farklı Kaydet XLSX Olarak" menü öğesini tutmak için, GridJs div kimliğinin "gridjs-divid" olduğunu varsayın
```javascript
   //get menubar parent dom
   const menubar=document.querySelector("#gridjs-divid > div > div:nth-child(1) > div > div.x-spreadsheet-banner-info-s > div.x-spreadsheet-toolbar.x-spreadsheet-menubar");
   var childs = menubar.childNodes;

   // keep the first one ->File menu  only
   for (var i = childs.length - 1; i >= 0; i--)
   {  //find the File menu
     if(childs[i].childNodes[0].childNodes[0].textContent==="File")
       {
            var dropdownparent = childs[i].childNodes[0].childNodes[1];
            var menuitems = dropdownparent.childNodes;
            for (var ii = menuitems.length - 1; ii >=0; ii--)
            {   
	        //remove other menu item that is not "Download As XLSX"
                if (menuitems[ii].textContent !== 'Download As XLSX')
                {
                    dropdownparent.removeChild(menuitems[ii]);
                }
            }
       }
   }


```
Bu fonksiyon çağrıldıktan sonra 

![yapılacak: menü çubuğu öğesini özelleştirme ekranı](gridjs_customize_menu.png)

## Araç çubuğu öğelerini özelleştir 
örneğin: yalnızca yakınlaştırma düğmesini tutmak için, GridJs div kimliğinin "gridjs-divid" olduğunu varsayın
```javascript
   //get toolbar parent dom
   const toolbar=document.querySelector("#gridjs-divid > div > div.x-spreadsheet-toolbar > div.x-spreadsheet-toolbar-btns");
   var childs = toolbar.childNodes;


   for (var i = childs.length - 1; i >= 0; i--)
   {  
     // keep File menu  only
     if(childs[i].getAttribute("data-tooltip")!=="Zoom")
       {
         toolbar.removeChild(childs[i]);
       }
   }


```
Bu fonksiyon çağrıldıktan sonra 

![yapılacak: araç çubuğu özelleştirme ekranı](gridjs_customize_toolbar.png)


## Araç çubuğu üzerine gelme efektini özelleştir

tarayıcı inceleme penceresini açın, araç çubuğu düğmesini seçin,

![todo:inceleme araç çubuğu düğmesini seçmek için ekran](gridjs_hover_toolbar_button_inspect.png)

sonra bu düğme için ilgili css anahtarını bulabiliriz:dondur

![todo: araç çubuğu düğmesi için css anahtarını bulmak üzere ekran](gridjs_hover_toolbar_button_csskey.png)

aşağıdaki css kuralını ekleyin:
```css
.x-spreadsheet-toolbar .x-spreadsheet-toolbar-btn:hover .x-spreadsheet-icon-img.freeze,
.x-spreadsheet-toolbar .x-spreadsheet-toolbar-btn.active .x-spreadsheet-icon-img.freeze {
  background: rgba(4, 71, 33, 0.08);
  filter: brightness(0) saturate(100%) invert(27%) sepia(51%) saturate(2878%) hue-rotate(346deg) brightness(104%) contrast(97%);
}
```
sonuç şu olacak :

![todo: araç çubuğu düğmesi üzerine hover efektini gösteren ekran](gridjs_hover_toolbar_button_hover.png)


## Alt Çubuğu Özelleştirme Öğeleri

### Genel Bakış
Alt çubuk iki etkileşimli düğme içerir:
1. &zwnj;**Sayfa Çalışma Sayfası Ekle Tuşu**&zwnj; (`add` sınıfı) - yeni çalışma sayfaları oluşturur
2. &zwnj;**Çalışma Sayfası Seç Tuşu**&zwnj; (`ellipsis` sınıfı) - çalışma sayfası seçimlerini yönetir

### DOM Erişimi
Bu öğelere erişebilirsiniz:
```javascript
// Add Worksheet Button
const addButton = document.querySelector('.x-spreadsheet-icon-img.add');

// Select Worksheet Button
const selectButton = document.querySelector('.x-spreadsheet-icon-img.ellipsis');

```

### Özelleştirme Örnekleri
1. Düğmeleri Gizle
Bir düğmeyi DOM’dan kaldırmak için:
```javascript
// Hide Add Worksheet Button
const addButton = document.querySelector('.x-spreadsheet-icon-img.add');
addButton.parentElement.removeChild(addButton);

// Hide Select Worksheet Button
const selectButton = document.querySelector('.x-spreadsheet-icon-img.ellipsis');
selectButton.parentElement.removeChild(selectButton);

```

2. İkonları Değiştir
İkonları dış SVG dosyaları veya satır içi SVG verileri kullanarak değiştirebilirsiniz.
```javascript
const addButton = document.querySelector('.x-spreadsheet-icon-img.add');
addButton.style.backgroundImage = "url('https://example.com/fish-icon.svg')";
// Adjust size and position
addButton.style.width = '18px';
addButton.style.height = '18px';
addButton.style.left = '0';
addButton.style.top = '0';
```

3. Düğme Davranışını Değiştir
Tıklama olayını özelleştirmek için değiştirebilirsiniz:
```javascript
const addButton = document.querySelector('.x-spreadsheet-icon-img.add');
addButton.addEventListener('click', function() {
  // Custom action here
  console.log('Custom add worksheet action');
});
```

