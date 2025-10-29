---
title: 如何在 GridJs 中自定义菜单和工具栏  
type: docs
weight: 250
url: /zh/net/aspose-cells-gridjs/how-to-customize-menus/
description: 本文介绍了如何在 GridJs 中自定义菜单和工具栏。
keywords: GridJs，自定义菜单，菜单，自定义
aliases:
  - /net/aspose-cells-gridjs/customize-menus/
  - /net/aspose-cells-gridjs/customize-ui/
  - /net/aspose-cells-gridjs/customize-toolbar/

---

## 关于自定义菜单和工具栏按钮
我们没有直接提供有用的 API。
但是我们可以根据 DOM 结构编写一些 JS 函数来实现它。



## 自定义菜单栏 
例如：只保留文件菜单，假设GridJs的div ID为"gridjs-divid"
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
调用此函数后 

![待办：自定义菜单栏界面](gridjs_customize_menubar.png)


## 自定义菜单栏中的项 
例如：只保留“另存为XLSX”菜单项，假设GridJs的div ID为"gridjs-divid"
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
调用此函数后 

![待办：自定义菜单栏项目界面](gridjs_customize_menu.png)

## 自定义工具栏项 
例如：只保留缩放按钮，假设GridJs的div ID为"gridjs-divid"
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
调用此函数后 

![待办：自定义工具栏界面](gridjs_customize_toolbar.png)


## 自定义工具栏悬停效果

打开浏览器检查窗口，选择工具栏按钮，

![待：选择检查工具栏按钮的屏幕](gridjs_hover_toolbar_button_inspect.png)

然后我们可以找到与该按钮相关的CSS键是：冻结

![待办：找到工具栏按钮的CSS键的屏幕](gridjs_hover_toolbar_button_csskey.png)

添加以下CSS规则：
```css
.x-spreadsheet-toolbar .x-spreadsheet-toolbar-btn:hover .x-spreadsheet-icon-img.freeze,
.x-spreadsheet-toolbar .x-spreadsheet-toolbar-btn.active .x-spreadsheet-icon-img.freeze {
  background: rgba(4, 71, 33, 0.08);
  filter: brightness(0) saturate(100%) invert(27%) sepia(51%) saturate(2878%) hue-rotate(346deg) brightness(104%) contrast(97%);
}
```
结果将是：

![待办：工具栏按钮悬停效果的屏幕](gridjs_hover_toolbar_button_hover.png)


## 底部栏中的自定义项目

### 概览
底部栏包含两个互动按钮：
1. &zwnj;**添加工作表按钮**&zwnj;（`add` 类） - 创建新工作表
2. &zwnj;**选择工作表按钮**&zwnj;（`ellipsis` 类） - 管理工作表选择

### DOM访问
你可以使用以下方法访问这些元素：
```javascript
// Add Worksheet Button
const addButton = document.querySelector('.x-spreadsheet-icon-img.add');

// Select Worksheet Button
const selectButton = document.querySelector('.x-spreadsheet-icon-img.ellipsis');

```

### 自定义示例
1. 隐藏按钮
要从DOM中移除按钮：
```javascript
// Hide Add Worksheet Button
const addButton = document.querySelector('.x-spreadsheet-icon-img.add');
addButton.parentElement.removeChild(addButton);

// Hide Select Worksheet Button
const selectButton = document.querySelector('.x-spreadsheet-icon-img.ellipsis');
selectButton.parentElement.removeChild(selectButton);

```

2. 更换图标
你可以使用外部SVG文件或内联SVG数据替换图标。
```javascript
const addButton = document.querySelector('.x-spreadsheet-icon-img.add');
addButton.style.backgroundImage = "url('https://example.com/fish-icon.svg')";
// Adjust size and position
addButton.style.width = '18px';
addButton.style.height = '18px';
addButton.style.left = '0';
addButton.style.top = '0';
```

3. 更改按钮行为
你可以修改点击事件以自定义功能：
```javascript
const addButton = document.querySelector('.x-spreadsheet-icon-img.add');
addButton.addEventListener('click', function() {
  // Custom action here
  console.log('Custom add worksheet action');
});
```

