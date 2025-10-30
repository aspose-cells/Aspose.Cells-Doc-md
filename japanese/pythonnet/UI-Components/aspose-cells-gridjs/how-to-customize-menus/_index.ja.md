---
title: GridJsでのメニューとツールバーのカスタマイズ方法  
type: docs
weight: 250
url: /ja/python-net/aspose-cells-gridjs/how-to-customize-menus/
description: この記事では、GridJsにおけるメニューとツールバーのカスタマイズ方法について説明します。
keywords: GridJs、メニューのカスタマイズ、メニュー、カスタマイズ
aliases:
  - /python-net/aspose-cells-gridjs/customize-menus/
  - /python-net/aspose-cells-gridjs/customize-ui/
  - /python-net/aspose-cells-gridjs/customize-toolbar/

---

## メニューとツールバーボタンのカスタマイズに関して
直接便利なAPIは提供していません。
ただし、DOM構造に基づくJavaScript関数を書いて実現可能です。



## メニューバーのカスタマイズ 
例：Fileメニューだけを残すために、GridJsのdiv idを "gridjs-divid" と仮定します。
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
この関数を呼び出した後 

![カスタマイズされたメニューバーの画面](gridjs_customize_menubar.png)


## メニューバーの項目をカスタマイズ 
例：Fileメニューの「Download As XLSX」メニュー項目だけを残すために、GridJsのdiv idを "gridjs-divid" と仮定します。
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
この関数を呼び出した後 

![カスタマイズされたメニューバー項目の画面](gridjs_customize_menu.png)

## ツールバー項目のカスタマイズ 
例：ズームボタンだけを残すために、GridJsのdiv idを "gridjs-divid" と仮定します。
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
この関数を呼び出した後 

![カスタマイズされたツールバーの画面](gridjs_customize_toolbar.png)


## ツールバーホバー効果のカスタマイズ

ブラウザ検査ウィンドウを開き、ツールバーのボタンを選択します。

![todo:inspectツールバーのボタンの選択画面](gridjs_hover_toolbar_button_inspect.png)

次に、このボタンに関連付けられているCSSキーは:freezeです。

![todo:ツールバーのCSSキーの検索画面](gridjs_hover_toolbar_button_csskey.png)

次のCSSルールを追加します：
```css
.x-spreadsheet-toolbar .x-spreadsheet-toolbar-btn:hover .x-spreadsheet-icon-img.freeze,
.x-spreadsheet-toolbar .x-spreadsheet-toolbar-btn.active .x-spreadsheet-icon-img.freeze {
  background: rgba(4, 71, 33, 0.08);
  filter: brightness(0) saturate(100%) invert(27%) sepia(51%) saturate(2878%) hue-rotate(346deg) brightness(104%) contrast(97%);
}
```
結果は次のようになります：

![todo:ツールバーのホバー効果のスクリーンショット](gridjs_hover_toolbar_button_hover.png)


## ボトムバーのアイテムのカスタマイズ

### 概要
ボトムバーには二つのインタラクティブボタンが含まれています：
1. &zwnj;**ワークシート追加ボタン**&zwnj; (`add`クラス) - 新しいワークシートを作成します
2. &zwnj;**ワークシート選択ボタン**&zwnj; (`ellipsis`クラス) - ワークシートの管理と選択

### DOMアクセス
これらの要素には次の方法でアクセスできます：
```javascript
// Add Worksheet Button
const addButton = document.querySelector('.x-spreadsheet-icon-img.add');

// Select Worksheet Button
const selectButton = document.querySelector('.x-spreadsheet-icon-img.ellipsis');

```

### カスタマイズ例
1. ボタンを非表示にする
DOMからボタンを削除するには：
```javascript
// Hide Add Worksheet Button
const addButton = document.querySelector('.x-spreadsheet-icon-img.add');
addButton.parentElement.removeChild(addButton);

// Hide Select Worksheet Button
const selectButton = document.querySelector('.x-spreadsheet-icon-img.ellipsis');
selectButton.parentElement.removeChild(selectButton);

```

2. アイコンを変更する
外部SVGファイルまたはインラインSVGデータを使用してアイコンを置き換えることができます。
```javascript
const addButton = document.querySelector('.x-spreadsheet-icon-img.add');
addButton.style.backgroundImage = "url('https://example.com/fish-icon.svg')";
// Adjust size and position
addButton.style.width = '18px';
addButton.style.height = '18px';
addButton.style.left = '0';
addButton.style.top = '0';
```

3. ボタンの動作変更
クリックイベントを変更して機能をカスタマイズできます：
```javascript
const addButton = document.querySelector('.x-spreadsheet-icon-img.add');
addButton.addEventListener('click', function() {
  // Custom action here
  console.log('Custom add worksheet action');
});
```





