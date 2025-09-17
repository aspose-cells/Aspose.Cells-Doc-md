##Custom context menus for GridJs
This article describes how to configure context menus for GridJs.
# Custom build-in context menus
We have some build in context menu items ,for example insert/delete row/column and so on.
for example:to delete "Delete row","Link","Hide" menu items in context menus,assume the div id of GridJs is "gridjs-divid"
```javascript
//get context menus parent dom
const menus=document.querySelector("#gridjs-divid > div > div.x-spreadsheet-sheet > div.x-spreadsheet-contextmenu");
var childs = menus.childNodes;
for (var i = childs.length - 1; i >= 0; i--)
{
// check the item text
if(childs[i].childNodes[0]?.textContent==="Delete row"||childs[i].childNodes[0]?.textContent==="Link"||childs[i].childNodes[0]?.textContent==="Hide")
{
menus.removeChild(childs[i]);
}
}
```
After call this function
![todo:the screen for customize build-in menu items](gridjs_customize_build_in_context_menu.png)
# Custom self-defined context menus
We have some build in context menu items ,for example insert/delete row/column and so on.
However if user want to custom context menu items.
We support set context menu items in load options.
for example:
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
We support the below JS APIs for custom context menu items at runtime
-  get custom context menu items
```javascript
xs.sheet.getCustomContextMenuItems()
```
-  add custom context menu items
```javascript
xs.sheet.addCustomContextMenuItems(itemsarray)
// the parameter is:
itemsarray: the array of custom menu items,the callback function x parameter will be the js variable of xs.sheet
for example: [{'key':'key4','text':'menu4','callback':(x)=>{console.log('hello4444');}},{'key':'key3','text':'menu3','callback':(x)=>{console.log('hello3333');}}]
```
-  delete custom context menu items
```javascript
xs.sheet.delCustomContextMenuItems(keysarray)()
// the parameter is:
keysarray: the array of the keys of the menu items
for example: ['key4','key3']
```
-  insert custom context menu item at specified postion
```javascript
xs.sheet.insertCustomContextMenuItem(item,postion)
// the parameter is:
item: the custom menu item,the callback function x parameter will be the js variable of xs.sheet
for example: {'key':'key4','text':'menu4','callback':(x)=>{console.log('hello4444');}}
postion:the postion for the inserted item in the items array
```
-  update custom context menu item by the key
```javascript
xs.sheet.updateCustomContextMenuItem(key,item)
// the parameter is:
item: the updated properties that with text or callback
for example: {'text':'menu updated'}
key:the key of the menu item
```
-  get custom context menu items for image/shape
```javascript
xs.sheet.getImageContextMenuItems()
```
-  add custom context menu items for image/shape
```javascript
xs.sheet.addImageContextMenuItems(itemsarray)
// the parameter is:
itemsarray: the array of custom menu items,the callback function x parameter will be the js variable of xs.sheet
for example: [{'key':'key4','text':'img operation1','callback':(x)=>{console.log('operation1 on image');}},{'key':'key3','text':'img operation2','callback':(x)=>{console.log('operation2 on image');}}]
```
-  delete custom context menu items for image/shape
```javascript
xs.sheet.delImageContextMenuItems(keysarray)()
// the parameter is:
keysarray: the array of the keys of the menu items
for example: ['key4','key3']
```
You can find more in our github demo page https://github.com/aspose-cells/Aspose.Cells-for-Python-via-.NET/tree/main/Examples_GridJs_Python_Net/wwwroot/xspread/index.html
