---
title: Travailler avec GridJs côté client
type: docs
weight: 250
url: /fr/net/aspose-cells-gridjs/client/
---
# Travailler avec GridJs côté client
Nous avons développé le client GridJs basé sur[feuille de calcul x](https://github.com/myliang/x-spreadsheet).

## les principales étapes sont :

- créer une instance x_spreadsheet
```javascript
xs = x_spreadsheet(id, options)
```
- charger les données json
```javascript
xs.loadData(jsondata.data)
```
- définir la feuille active
```javascript
xs.setActiveSheetByName(jsondata.actname)
```
- définir la cellule active
```javascript
xs.setActiveCell(jsondata.actrow,jsondata.actcol);
```

par exemple, le code ci-dessous init un objet x_spreadsheet.
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
 // les paramètres des options :
 updateMode : actuellement, nous ne prenons en charge que le "serveur"
 updateUrl : définit l'URL côté serveur pour l'action de mise à jour basée sur json
 mode : lire signifie feuille de calcul en lecture seule/modifier signifie que nous pouvons modifier la feuille de calcul
 showToolbar : signifie s'il faut afficher la barre d'outils
 showFileName : s'il faut afficher le nom du fichier
 local : prend en charge plusieurs langues pour les menus, les paramètres régionaux peuvent être : en, cn, es, pt, de, ru, nl pour l'anglais, le chinois, l'espagnol, le portugais, l'allemagne, le russe, le néerlandais
 showContextmenu : signifie s'il faut afficher le menu contextuel lors d'un clic droit sur une cellule
## 

___
## autres API utiles
- Rendre la vue
```javascript
xs.reRender()
```
- Obtenir l'image / la forme sélectionnée �� si rien, sélectionnez renverra null
```javascript
xs.sheet.selector.getObj()
```

- Obtenir l'objet cellule
```javascript
xs.sheet.data.getCell(ri,ci)
    // the parameters are:
    ri:row index 
	ci:column index
```
- Obtenir le style de cellule
```javascript
xs.sheet.data.getCellStyle(ri,ci)
    // the parameters are:
    ri:row index 
	ci:column index
```
- Définir la valeur de la cellule
```javascript
xs.sheet.data.setCellText(ri,ci,value,state)
    // the parameters are:
    ri:row index 
	ci:column index
	value:the cell value
	state: input | finished
```

- Obtenir/Définir la plage de cellules sélectionnée
```javascript
xs.sheet.data.selector.range
```
- Définir la valeur de la cellule pour la cellule ou la zone de cellule sélectionnée
```javascript
xs.sheet.data.setSelectedCellText(value)
    // the parameters are:
	value:the  value for the cell
```
- Définir le style de la cellule ou de la zone de cellule sélectionnée
```javascript
xs.sheet.data.setSelectedCellAttr(attributename,value)
    // the parameters are:
    attributename:font-name | font-bold | font-italic | font-size  | format|border|merge|formula |strike|textwrap |underline |align |valign |color|bgcolor|pattern
	value:the  value for the attribute
```

- Fusionner la zone de cellule sélectionnée
```javascript
xs.sheet.data.merge()
```

- Annuler la fusion de la zone de cellule sélectionnée
```javascript
xs.sheet.data.unmerge()
```
-  Supprimer la cellule sélectionnée
```javascript
xs.sheet.data.deleteCell(what)
    // the parameters are:
    what:all|format  all: means delete the cell and clear the style ;format means delete the cell value and keep the cell style
```
- Définir le volet de gel
```javascript
xs.sheet.data.setFreeze(ri,ci)
    // the parameters are:
    ri:row index 
	ci:column index
```

-  Insérer une ligne ou des colonnes dans la cellule sélectionnée
```javascript
xs.sheet.data.insert(type, n)
    // the parameters are:
    type: row | column
	n:the row or column number
```
-  Supprimer la ligne ou les colonnes de la cellule sélectionnée
```javascript
xs.sheet.data.delete(type)
    // the parameters are:
    type: row | column
```

- Définir la largeur de la colonne
```javascript
xs.sheet.data.setColWidth(ci,width)
    // the parameters are:
    ci:column index
	width:the width for the column
```
-  Obtenir la largeur de la colonne
```javascript
xs.sheet.data.cols.sumWidth(min,max)
    // the parameters are:
    min:the start column index
	max:the end column index,not include
```

- Définir la hauteur de la ligne
```javascript
xs.sheet.data.setRowHeight(ri,height)
    // the parameters are:
    ri:row index
	height:the height for the row
```
-  Obtenir la hauteur de la ligne
```javascript
xs.sheet.data.rows.sumHeight(min,max)
    // the parameters are:
    min:the start row index
	max:the end row index,not include
```
- Obtenir/Définir la direction d'affichage
```javascript
xs.sheet.data.displayRight2Left
```



pour plus d'informations, vous pouvez consulter l'exemple ici
<https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Examples_GridJs>



 
 
