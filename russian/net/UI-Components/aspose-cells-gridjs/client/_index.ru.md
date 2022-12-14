---
title: Работа с клиентской частью GridJs
type: docs
weight: 250
url: /ru/net/aspose-cells-gridjs/client/
---
# Работа с клиентской частью GridJs
Мы разработали клиент GridJs на основе[x-таблица](https://github.com/myliang/x-spreadsheet).

## основные шаги:

- создать экземпляр x_spreadsheet
```javascript
xs = x_spreadsheet(id, options)
```
- загрузить json-данные
```javascript
xs.loadData(jsondata.data)
```
- установить активный лист
```javascript
xs.setActiveSheetByName(jsondata.actname)
```
- установить активную ячейку
```javascript
xs.setActiveCell(jsondata.actrow,jsondata.actcol);
```

например, приведенный ниже код инициализирует объект x_spreadsheet.
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
 // параметры для опций:
 updateMode: в настоящее время мы поддерживаем только «сервер»
 updateUrl: установите URL-адрес на стороне сервера для действия обновления на основе json.
 режим: чтение означает электронную таблицу только для чтения/редактирование означает, что мы можем редактировать электронную таблицу
 showToolbar: означает, показывать ли панель инструментов
 showFileName: показывать ли имя файла
 local: поддержка нескольких языков для меню, локаль может быть: en, cn, es, pt, de, ru, nl для английского, китайского, испанского, португальского, немецкого, русского, голландского
 showContextmenu: означает, показывать ли контекстное меню при щелчке правой кнопкой мыши по ячейке.
## 

___
## другие полезные API
- Рендеринг вида
```javascript
xs.reRender()
```
- Получить выбранное изображение/форму, если ничего не выбрать, будет возвращено значение null
```javascript
xs.sheet.selector.getObj()
```

- Получить объект ячейки
```javascript
xs.sheet.data.getCell(ri,ci)
    // the parameters are:
    ri:row index 
	ci:column index
```
- Получить стиль ячейки
```javascript
xs.sheet.data.getCellStyle(ri,ci)
    // the parameters are:
    ri:row index 
	ci:column index
```
- Установите значение ячейки
```javascript
xs.sheet.data.setCellText(ri,ci,value,state)
    // the parameters are:
    ri:row index 
	ci:column index
	value:the cell value
	state: input | finished
```

- Получить/установить выбранный диапазон ячеек
```javascript
xs.sheet.data.selector.range
```
- Установите значение ячейки для выбранной ячейки или области ячейки
```javascript
xs.sheet.data.setSelectedCellText(value)
    // the parameters are:
	value:the  value for the cell
```
- Установите стиль для выбранной ячейки или области ячейки
```javascript
xs.sheet.data.setSelectedCellAttr(attributename,value)
    // the parameters are:
    attributename:font-name | font-bold | font-italic | font-size  | format|border|merge|formula |strike|textwrap |underline |align |valign |color|bgcolor|pattern
	value:the  value for the attribute
```

- Объединить выбранную область ячейки
```javascript
xs.sheet.data.merge()
```

- Разъединить выбранную область ячейки
```javascript
xs.sheet.data.unmerge()
```
-  Удалить выбранную ячейку
```javascript
xs.sheet.data.deleteCell(what)
    // the parameters are:
    what:all|format  all: means delete the cell and clear the style ;format means delete the cell value and keep the cell style
```
- Установите область заморозки
```javascript
xs.sheet.data.setFreeze(ri,ci)
    // the parameters are:
    ri:row index 
	ci:column index
```

-  Вставить строку или столбцы в выбранную ячейку
```javascript
xs.sheet.data.insert(type, n)
    // the parameters are:
    type: row | column
	n:the row or column number
```
-  Удалить строку или столбцы в выбранной ячейке
```javascript
xs.sheet.data.delete(type)
    // the parameters are:
    type: row | column
```

- Установить ширину столбца
```javascript
xs.sheet.data.setColWidth(ci,width)
    // the parameters are:
    ci:column index
	width:the width for the column
```
-  Получить ширину столбца
```javascript
xs.sheet.data.cols.sumWidth(min,max)
    // the parameters are:
    min:the start column index
	max:the end column index,not include
```

- Установить высоту строки
```javascript
xs.sheet.data.setRowHeight(ri,height)
    // the parameters are:
    ri:row index
	height:the height for the row
```
-  Получить высоту строки
```javascript
xs.sheet.data.rows.sumHeight(min,max)
    // the parameters are:
    min:the start row index
	max:the end row index,not include
```
- Получить/установить направление отображения
```javascript
xs.sheet.data.displayRight2Left
```



для получения подробной информации вы можете проверить пример здесь
<https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Examples_GridJs>



 
 
