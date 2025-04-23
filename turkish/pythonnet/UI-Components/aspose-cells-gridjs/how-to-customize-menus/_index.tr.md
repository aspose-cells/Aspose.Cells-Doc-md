---
title: GridJs de menüleri ve araç çubuklarını nasıl özelleştirirsiniz  
type: docs
weight: 250
url: /tr/python-net/aspose-cells-gridjs/how-to-customize-menus/
description: Bu makale, GridJs de menüleri ve araç çubuklarını nasıl özelleştireceğinizi anlatır.
keywords: GridJs, özelleştirilebilir menüler, menüler, özelleştir
aliases:
  - /python-net/aspose-cells-gridjs/customize-menus/
  - /python-net/aspose-cells-gridjs/customize-ui/
  - /python-net/aspose-cells-gridjs/customize-toolbar/

---

## Menüleri ve araç çubuğu düğmelerini özelleştirme hakkında
doğrudan kullanışlı API'ler sağlamıyoruz.
ancak dom yapısına dayalı bazı js fonksiyonları yazarak bunu başarabiliriz.



## menü çubuğunu özelleştir 
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





