---
title: Travailler avec GridJs côté client
type: docs
weight: 250
url: /fr/java/aspose-cells-gridjs/how-to-use-gridjs-client-api/
keywords: GridJs,personnalisé,logo,paramètre,api,js api,api client
description: Cet article présente les APIs ou fonctions client JavaScript dans GridJs.
aliases:
  - /java/aspose-cells-gridjs/client/
  - /java/aspose-cells-gridjs/work-with-client-api/
  - /java/aspose-cells-gridjs/use-js-api/
  - /java/aspose-cells-gridjs/gridjs-spreadsheet-api/
  - /java/aspose-cells-gridjs/client-api/
  - /java/aspose-cells-gridjs/js-api/
  - /java/aspose-cells-gridjs/javascript-api/
---

# Travailler avec GridJs côté client
Nous avons développé GridJs côté client sur [x-spreadsheet](https://github.com/myliang/x-spreadsheet).

## Les principales étapes sont:

- créer une instance x_spreadsheet
```javascript
xs = x_spreadsheet(id, options)
    // the parameters are:
    id:the html node id ,for example :'#gridjs-demo' for the html  <div id="gridjs-demo"></div>
    options: the load options


for example the below code init a gridjs_spreadsheet object.
	xs = x_spreadsheet('#gridjs-demo', {
			updateMode:'server',
			updateUrl:'/GridJs2/UpdateCell',
			mode: 'edit',
			showToolbar: true,
                        local: 'en',
			showContextmenu: true
			})
```
les paramètres pour les options de chargement :

| Paramètre | Description | Valeur par défaut | Optionnel |
| --- | --- | --- | --- |
| `allowSelectTextInTextBoxInReadMode` | Permet de sélectionner du texte dans les contrôles TextBox en mode lecture.<br>La valeur par défaut est false. | `false` | Oui |
| `checkSyntax` | Vérifie la syntaxe et corrige l'orthographe pour la saisie utilisateur dans le contenu texte.<br>Fonctionne avec setSyntaxCheckUrl.<br>La valeur par défaut est false. | `false` | Oui |
| `loadingGif` | URL du GIF de chargement lors du chargement des images/formes.<br>La valeur par défaut est content/img/updating.gif. | `content/img/updating.gif` | Oui |
| `local` | Définir les informations de localisation pour les menus et barres d'outils, prenant en charge plusieurs langues.<br>Les valeurs possibles incluent :<br>- `en, zh, es, pt, de, ru, nl` (pour anglais, chinois, espagnol, portugais, allemand, russe, néerlandais)<br>- `ar, fr, id, it, ja` (pour arabe, français, indonésien, italien, japonais)<br>- `ko, th, tr, vi, cht` (pour coréen, thaï, turc, vietnamien, chinois traditionnel) | `en` | Oui |
| `mode` | Peut être `read` ou `edit` ; `read` signifie une feuille en lecture seule ; `edit` signifie qu'elle peut être modifiée. | Aucun | Non |
| `isCollaborative` | Supporte le mode collaboratif ? | `false` | Oui |
| `searchHighlightColor` | Couleur de surbrillance pour le terme de recherche.<br>La couleur doit inclure un canal alpha pour la transparence. | `#dbe71338` | Oui |
| `showCheckSyntaxButton` | Affiche ou non les boutons de vérification syntaxique et correction orthographique dans la barre d'outils.<br>La valeur par défaut est false. | `false` | Oui |
| `showContextmenu` | Affiche ou non le menu contextuel lors du clic droit sur une cellule.<br>La valeur par défaut est true. | `true` | Oui |
| `showFileName` | Affiche ou non le nom du fichier. | `true` | Oui |
| `showFormulaExplain` | Afficher les explications de formule appliquées à cette cellule lorsque la souris passe dessus.<br>Fonctionne avec setFormulaExplainUrl.<br>La valeur par défaut est false. | `false` | Oui |
| `showFormulaTip` | Afficher la formule existante appliquée à cette cellule lorsque la souris passe dessus.<br>La valeur par défaut est false. | `false` | Oui |
| `showNonEditableSymbolInCell` | Afficher ou non un symbole non modifiable côté client dans la cellule.<br>Si réglé sur true, après avoir cliqué sur le menu contextuel droit "Désactiver la modification", la zone sélectionnée affichera le symbole.<br>La valeur par défaut est false. | `false` | Oui |
| `showToolbar` | Afficher ou non la barre d'outils. | `true` | Oui |
| `updateMode` | Actuellement, ne supporte que `server`. | `server` | Non |
| `updateUrl` | Définir l'URL côté serveur pour les actions de mise à jour basées sur JSON. | Aucun | Non |
| `view` | Définir la taille de la vue pour la feuille, par exemple, `{width: () => 1000, height: () => 500}`. | `{width: () => document.documentElement.clientWidth, height: () => document.documentElement.clientHeight }` | Oui |
| `token` | Définissez le jeton d'authentification. Lorsque le jeton n'est pas nul, l'en-tête `Authorization: Bearer {token}` sera automatiquement ajouté aux en-têtes de la requête. Vous pouvez utiliser `xs.refreshToken(token)` pour définir un nouveau jeton. | Aucun | Oui |    
| `showBottombarStats` | Afficher les statistiques de la barre inférieure.<br>La valeur par défaut est true. | `true` | Oui |   
| `showRowAppenderToolbar` | Afficher la barre d'outils pour ajouter des lignes en lot.<br>La valeur par défaut est true. | `true` | Oui |   

- charger avec des données json
```javascript
xs.loadData(data)
// the parameters is:
	data: the json data which describ the data structure for the worksheets
```
-  définir la feuille active par le nom de la feuille
```javascript
xs.setActiveSheetByName(sheetname)
// the parameters is:
	sheetname: the sheet name 
```
-  définir la feuille active par l'identifiant
```javascript
xs.setActiveSheet(id)
// the parameters is:
	sheetname: the sheet id 
```

-  définir la cellule active
```javascript
xs.setActiveCell(row,col);
// the parameters are:
	row: the cell row
	col: the cell column
```

-  définir actif pour plusieurs instances 
```javascript
xs.setActiveForMultipleInstance(isacitve);
// the parameters are:
	isacitve: whether need to do edit operation at this xs instanse 
// when there are more than one GridJs instances in one page, we need to call this method.
// we only support do edit operation for one instances at a page.
// for example,if we have two instances: xs1 and xs2 in one html page.
// if we need to keep edit operation in xs1,
// we shall call:
xs1.setActiveForMultipleInstance(true);
xs2.setActiveForMultipleInstance(false);

// if we need not do any edit operation for both,
// we shall call:
xs1.setActiveForMultipleInstance(false);
xs2.setActiveForMultipleInstance(false);

```
- définir un toast personnalisé
```javascript
xs.customToast(customToastFunction);
// the parameter is:
	customToastFunction: user defined function to toast message,it shall have three parameters :title, content,callback
	if set to null,it will use the default build-in toast.

    for example: 
            function myCustomToast(title, content, callback) {
	    //.....
	    }
            xs.customToast(myCustomToast);
```

- définir les infos pour l'opération des formes/images pour l'action côté serveur
```javascript
xs.setImageInfo(imageGetActionUrl, imageAddByUploadActionUrl, imageAddByUrlActionUrl, imageCopyActionUrl, zindex, loadingGif);
// the parameters are:
	imageGetActionUrl: the get image action URL in the server side controller
	imageAddByUploadActionUrl: the upload image action  URL in the server side controller
	imageAddByUrlActionUrl: the add image from URL action  URL in the server side controller
	imageCopyActionUrl: the copy image action  URL in the server side controller
	zindex: the minimum zindex of the image in the canvas
	loadingGif (optional): the loading gif url when loading the image/shape .it is optional,the default value is:content/img/updating.gif
    for example: 
            const imageurl = "/GridJs2/imageurl";
            const imageuploadurl1 = "/GridJs2/AddImage";
            const imageuploadurl2 = "/GridJs2/AddImageByURL";
            const imagecopyurl = "/GridJs2/CopyImage";  
            const basiczorder = 5678;
    xs.setImageInfo(imageurl, imageuploadurl1, imageuploadurl2, imagecopyurl, basiczorder);
```

- définir les infos pour l'opération de téléchargement pour l'action côté serveur
```javascript
xs.setFileDownloadInfo(downloadActionUrl);
// the parameters are:
	downloadActionUrl: the get download file action URL in the server side controller

    for example: 
            const fileDownloadUrl = "/GridJs2/Download";
            xs.setFileDownloadInfo(fileDownloadUrl);
```

- définir les infos pour l'opération d'objet OLE pour l'action côté serveur
```javascript
xs.setOleDownloadInfo(oleActionUrl);
// the parameters are:
	oleActionUrl: the ole object file action URL in the server side controller
    for example: 
            const oleDownloadUrl = "/GridJs2/Ole";
            xs.setOleDownloadInfo(oleDownloadUrl);
```
- définir des informations pour la vérification de syntaxe & la correction orthographique côté serveur
```javascript
xs.setSyntaxCheckUrl(checkUrl);
// the parameters are:
	checkUrl: the  syntax checking & spell correction operation action URL in the server side controller
    for example: 
            const checkurl = "/GridJs2/CheckSyntax";
            xs.setSyntaxCheckUrl(checkurl);
```

- définir des informations pour l'explication de formule côté serveur
```javascript
xs.setFormulaExplainUrl(formulaExplainUrl);
// the parameters are:
	formulaExplainUrl: the  formula explanation  action URL in the server side controller
    for example: 
            const formulaExplainUrl = "/GridJs2/FormulaExplain";
            xs.setFormulaExplainUrl(formulaExplainUrl);
```


___
## autres API utiles
-  Rendre la vue
```javascript
xs.reRender()
```

- Obtenir l'ID de la feuille active
```javascript
xs.getActiveSheet()
```

- Ajouter une nouvelle feuille de calcul
```javascript
xs.addSheet(name,isactive,tabcolor,fontcolor)
// the parameters are:
	name:the sheet name
	isactive:whether set this sheet as active sheet
	tabcolor:the background color for the sheet in the tab bottom menu
	fontcolor:the font color for the sheet name in the tab bottom menu
   for example:
    xs.addSheet('hello',true,'#12ee5b','#2c5d3b')
```
- Modifier le nom de la feuille
```javascript
xs.modifySheetName(oldName,newName)
// the parameters are:
	oldName:the sheet name
	newName:the new desired name
   for example:
     xs.modifySheetName('Sheet1','student');
```
- Supprimer la feuille
```javascript
xs.deleteSheet(name)
// the parameters is:
	name:the sheet name
   for example:
        xs.deleteSheet('Sheet1');

```

-  Définir le niveau de zoom
```javascript
xs.setZoomLevel(zoom)
// the parameters is:
	zoom:the zoom level ,can be number ,for example 0.5 for zoom out, or 2 for zoom in
```

-  Définir le nom de fichier 
```javascript
xs.setFileName(name)
// the parameters is:
	name:the file name with extension ,for example trip.xlsx
```
- Définir l'appel de fonction avant l'enregistrement 
```javascript
xs.setBeforeSaveFunction(func)
// the parameters is:
	func:This function is called before the save action. If it returns true, the save will proceed; otherwise, the save will not proceed.
   for example:
	xs.setBeforeSaveFunction(()=>{console.log('hello before save');return true;});
```

- Fonction de rappel pour la fonction d'envoi d'e-mail
```javascript
xs.setEmailSendCallFunction(callback)
// the parameters is:
	callback: the callback function to handle email sending, receives a mailObj parameter
		callback: function(mailObj) {
			// mailObj properties:
			// mailObj.receiver: the email address of the receiver, e.g., 'example@gmail.com'
			// mailObj.type: the format of the file to be sent, can be 'html', 'xlsx', or 'pdf'
		}
```

-  activer ou désactiver l'événement de touche de fenêtre pour GridJs
```javascript
xs.enableKeyEvent(isenable)
// the parameters is:
	isenable:whether the window key event is active for GridJs
//when has other controls in the same page, you may want to ignore the key event in GridJs 
```

-  délier tous les événements attachés à GridJs, y compris l'événement de touche de fenêtre et l'événement de redimensionnement de fenêtre.
```javascript
xs.destroy()
```

- Configurer les paramètres collaboratifs en mode collaboratif, assurez-vous de définir `setCollaborativeSetting` avant `setUniqueId`  
```javascript
xs.setCollaborativeSetting(url,wsendpoint,wsapp,wsuser,wstopic)
    //the parameters are:
         url: the basic action URL in the server side controller to get history messages ,the default is '/GridJs2/msg'
	 wsendpoint: the websocket endpoint in the server side , the default is '/ws'
	 wsapp: the websocket destinations prefixed with "/app", the default is '/app/opr'
	 wsuser: the websocket for user-specific queues prefixed with "/usr", the default is '/user/queue'
	 wstopic: the websocket destinations prefixed with "/topic", the default is '/topic/opr'


```

-  définir un filtre visible pour l'image/forme
```javascript
xs.setVisibleFilter((sheet,s) =>{})
    //  to set a function which return true(for visible) or false(for invisible) for the visible filter with the below parameters :
	sheet:the sheet instance
	s:the image or shape instance
    for example: 
	//this will make visible for image/shape in sheet with name 'Sheet3' and 'Sheet1' except for the 'Rectangle' type
		xs.setVisibleFilter((sheet,s) => { if (sheet.data.name==='Sheet3'||sheet.data.name==='Sheet1') return s.type!=='Rectangle';  return false; })
	//this will make visible for image/shape in sheet with name  'Sheet1' 
		xs.setVisibleFilter((sheet,s) => { if (sheet.data.name==='Sheet1') return true;  return false; })
	//this will make invisible for image/shape in all sheets 
		xs.setVisibleFilter((sheet,s) => {  return false; })
	//if all the image/shape is already loaded and you want to change the visible filter at runtime,you can call the below code to trigger a reload for image/shape
		xs.reRender()
```

-  Obtenir l'image/forme sélectionnée, si rien n'est sélectionné, retournera null
```javascript
xs.sheet.selector.getObj()
```
-  Afficher ou masquer un nœud HTML à une position de cellule spécifiée
```javascript
xs.sheet.showHtmlAtCell(isShow, html, ri, ci, deltaX, deltaY)

    //the parameters are:
      isShow: Boolean value indicating whether to show or hide the HTML content.
      html: The HTML string to be displayed.
      ri: Row index of the target cell.
      ci: Column index of the target cell.
      deltaX: (Optional) Relative X-position adjustment from the top-left corner of the cell.
      deltaY: (Optional) Relative Y-position adjustment from the top-left corner of the cell.

    for example: 
    // Show HTML at cell A1
    xs.sheet.showHtmlAtCell(true, "<span>html span</span><input length='30' id='myinput'>test</input>", 0, 0);

    // Hide the HTML node
    xs.sheet.showHtmlAtCell(false);

    // Note: When an HTML node is shown, the default GridJS event handling is disabled to allow interaction with the HTML content.
    // This means you cannot select any cells or perform edit operations until the HTML node is hidden.
```

-  Définir l'état sélectionnable pour image/forme 
```javascript
const shape=xs.sheet.selector.getObj();
shape.setControlable(isenable)
     // the parameter is:
      isenable: when set to true,the image or shape can be selectable and movable/resizeable
```


- Insérer des lignes
```javascript
xs.sheet.insertRows(start, n)
    // the parameters are:
	start: start row id 
	n:how many rows will be inserted
```
- Insérer des colonnes 
```javascript
xs.sheet.insertColumns(start, n)
    // the parameters are:
	start: start column id
	n:how many columns will be inserted
```
- Supprimer des lignes 
```javascript
xs.sheet.deleteRows(start, n)
    // the parameters are:
	start: start row id 
	n:how many rows will be deleted
```
-  Supprimer des colonnes 
```javascript
xs.sheet.deleteColumns(start, n)
    // the parameters are:
	start: start column id 
	n:how many columns will be deleted
```
-  Définir le volet gelé
```javascript
xs.sheet.freeze(ri,ci)
    // the parameters are:
	ri:row index 
	ci:column index
```
- Geler le volet
```javascript
xs.sheet.freeze(0,0)
```

- Définir la plage modifiable/en lecture seule
```javascript
xs.sheet.setEditableRange(range,isenable)
    // the parameters are:
	range:the cell range ,etc. {sri:0,sci:0,eri:2,eci:2} reprensents range start from cell A1 to C3
	isenable:when set to true,the range is editable.other wise,the range is readonly.
```

-  Cacher des lignes 
```javascript
xs.sheet.hideRows(sri,eri)
    // the parameters are:
	sri:the start row index 
	eri:the end row index
```

-  Débarrer les lignes
```javascript
xs.sheet.unhideRows(sri,eri)
    // the parameters are:
	sri:the start row index 
	eri:the end row index
```

-  Cacher des colonnes 
```javascript
xs.sheet.hideColumns(sci,eci)
    // the parameters are:
	sci:the start column index 
	eci:the end column index
```

-  Débarrer des colonnes
```javascript
xs.sheet.unhideColumns(sci,eci)
    // the parameters are:
	sci:the start column index 
	eci:the end column index
```


-  Définir la hauteur de la ligne
```javascript
xs.sheet.setRowHeight(ri,height)
    // the parameters are:
	ri:row index
	height:the height for the row
```
-  Définir la hauteur des lignes
```javascript
xs.sheet.setRowsHeight(sri,eri,height)
    // the parameters are:
	sri:start row index
	eri:end row index
	height:the height for the rows
```

-  Définir la hauteur de toutes les lignes
```javascript
xs.sheet.setAllRowsHeight(height)
    // the parameters are:
	height:the height for the rows
```

-  Définir la largeur pour la colonne
```javascript
xs.sheet.setColWidth(ci,width)
    // the parameters are:
	ci:column index
	width:the width for the column
```
-  Définir la largeur pour les colonnes
```javascript
xs.sheet.setColsWidth(sci,eci,width)
    // the parameters are:
	sci:the start column index
	eci:the end column index
	width:the width for the column
```

-  Définir la largeur pour toutes les colonnes
```javascript
xs.sheet.setAllColsWidth(width)
    // the parameters are:
	width:the width for the columns
```

-  Définir le commentaire dans la cellule
```javascript
xs.sheet.setComment(ri,ci,author,note)
    // the parameters are:
	ri:row index of the cell
	ci:column index of the cell
	author:the author for the comment
	note:the content for the comment
```

-  Supprimer le commentaire dans la cellule
```javascript
xs.sheet.removeComment(ri,ci)
    // the parameters are:
	ri:row index of the cell
	ci:column index of the cell
```


-  Obtenir l'objet de cellule
```javascript
xs.sheet.data.getCell(ri,ci)
    // the parameters are:
	ri:row index 
	ci:column index
```
-  Obtenir le style de cellule
```javascript
xs.sheet.data.getCellStyle(ri,ci)
    // the parameters are:
	ri:row index 
	ci:column index
```
-  Définir la valeur de cellule
```javascript
xs.sheet.data.setCellText(ri,ci,value,state)
    // the parameters are:
	ri:row index 
	ci:column index
	value:the cell value
	state: input | finished ,if finished ,it will do update action to servside
```

-  Obtenir/définir la plage de cellules sélectionnées
```javascript
xs.sheet.data.selector.range
```
-  Définir la valeur de cellule pour la cellule ou la zone de cellules sélectionnée
```javascript
xs.sheet.data.setSelectedCellText(value)
    // the parameters are:
	value:the  value for the cell
```
-  Définir le style pour la cellule ou la zone de cellules sélectionnée
```javascript
xs.sheet.data.setSelectedCellAttr(attributename,value)
    // the parameters are:
	attributename:font-name | font-bold | font-italic | font-size  | format|border|merge|formula |strike|textwrap |underline |align |valign |color|bgcolor|pattern
	value:the  value for the attribute
```

-  Définir le style pour la zone de cellules souhaitée
```javascript
xs.sheet.data.setRangeAttr(range,attributename,value)
    // the parameters are:
        range:the cell range ,etc. {sri:0,sci:0,eri:2,eci:2} reprensents range start from cell A1 to C3
	attributename:font-name | font-bold | font-italic | font-size  | format|border|merge|formula |strike|textwrap |underline |align |valign |color|bgcolor|pattern
	value:the  value for the attribute
   for example:
        xs.sheet.data.setRangeAttr({sri:0,sci:0,eri:2,eci:2},'bgcolor','#11ee2a');
```


-  Fusionner la zone de cellules sélectionnée
```javascript
xs.sheet.data.merge()
```

-  Dissocier la zone de cellules sélectionnée
```javascript
xs.sheet.data.unmerge()
```
-  Supprimer le contenu de la cellule ou effacer le style de la cellule sélectionnée  
```javascript
xs.sheet.data.deleteCell(type)
    // the parameters are:
	type:all|format  all: means delete the cell and clear the style ;format means delete the cell value and keep the cell style
```

-  Supprimer le contenu de la cellule ou effacer le style de la zone de cellules souhaitée
```javascript
xs.sheet.data.deleteRange(range,type)
    // the parameters are:
        range:the cell range ,etc. {sri:0,sci:0,eri:2,eci:2} reprensents range start from cell A1 to C3
	type:all|format  all: means delete the cell and clear the style ;format means delete the cell value and keep the cell style
```



-  Obtenir la largeur de la colonne 
```javascript
xs.sheet.data.cols.sumWidth(min,max)
    // the parameters are:
	min:the start column index
	max:the end column index,not include
```



-  Obtenir la hauteur de la ligne 
```javascript
xs.sheet.data.rows.sumHeight(min,max)
    // the parameters are:
	min:the start row index
	max:the end row index,not include
```

-  Obtenir/Définir la direction d'affichage
```javascript
xs.sheet.data.displayRight2Left
```

## Rappel d'événement
- Nous pouvons suivre les événements ci-dessous
```javascript
 xs.on('cell-selected', (cell, ri, ci) => {
                console.log('cell selected:', cell, ', ri:', ri, ', ci:', ci);
                if (ci === -1) {
                    console.log('ci === -1 means a row selected ',ri);
                }
                if (ri === -1) {
                    console.log('ri === -1 means a column selected',ci);
                }
            }).on('cells-selected', (cell, range) => {
                console.log('range   selected:', cell, ', rang:', range);
            }).on('object-selected', (shapeOrImageObj) => {
                console.log('shape or image selected id:', shapeOrImageObj.id, ', type: ', shapeOrImageObj.type);
            }).on('sheet-selected', (id,name) => {
                console.log('sheet selected id:', id, ', name: ',name);
            }).on('sheet-loaded', (id,name) => {
                console.log('sheet load finished:', id, ', name: ',name);
            }).on('cell-edited', (text, ri, ci) => {
	        //just edit the cell
                console.log('text:', text, ', ri: ', ri, ', ci:', ci);
            }).on('cells-updated', (name, cells) => {
	       //cell value got updated
                console.log('cells updated for sheet name:', name);
                cells.forEach((acell, index, array) => {
                console.log('acell got updated:', acell);
            })
            }).on('cells-deleted', (range) => {
                console.log('cells deleted :', range);
            }).on('rows-deleted', (ri, n) => {
                console.log('rows-deleted :', ri, ",size", n);

            }).on('columns-deleted', (ci, n) => {
                console.log('columns-deleted :', ci, ",size", n);

            }).on('rows-inserted', (ri, n) => {
                console.log('rows-inserted :', ri, ",size", n);

            }).on('columns-inserted', (ci, n) => {
                console.log('columns-inserted :', ci, ",size", n);

            });
```
- Événement de pré-vérification
  si la réponse est false, l'opération d'insertion/suppression ne continuera pas.
```javascript
  xs.checkRowInsert = (ri, size) => { if (ri % 2 == 1) return true; else return false; };
  xs.checkColumnInsert = (ci, size) => { if (ci % 2 == 1) return true; else return false; };
  xs.checkRowDelete = (ri, size) => { if (ri % 2 == 1) return true; else return false; };
  xs.checkColumnDelete = (ci, size) => { if (ci % 2 == 1) return true; else return false; };
```

## Personnalisation

- Définir l'icône et le lien d'accueil
```javascript
xs.sheet.menubar.icon.setHomeIcon(iconUrl,targetUrl)
    // the parameters are:
	iconUrl:the home icon URL
	targetUrl:the target link URL
	for example ,the below code will set the new logo and with link to google.com
	xs.sheet.menubar.icon.setHomeIcon('https://forum.aspose.com/letter_avatar_proxy/v4/letter/y/3e96dc/45.png','https://www.google.com')
```
- Afficher la barre de menu
```javascript
xs.sheet.menubar.show()
```

- Masquer la barre de menu
```javascript
xs.sheet.menubar.hide()
```
## API pour objet forme
-  Modifier la couleur de fond pour l'objet forme
```javascript
    setBackgroundColor(color)
    // the parameters are:
        color: the html color value in hex string value
    //for example,we assume shape 0 existed,this will set the background color to Yellow 
     const ashape=xs.sheet.data.shapes[0];
     ashape.setBackgroundColor('#FFFF00');
```

## APIs pour l'objet TextBox
TextBox est un type spécial de forme dont la propriété de type est : "TextBox",
par exemple: le code ci-dessous va montrer quelle forme est textbox

```javascript
for (let shape of xs.sheet.data.shapes) {
    if (shape.type === 'TextBox') {
        console.log(shape.id + ' is a textbox');
    }
}
```

-  Appliquer les paramètres de la police pour l'objet zone de texte
```javascript
    setFont(fontsettings)
    // the parameter is:
        fontsettings:   {'name':'Arial', 'size':12, 'bold':true, 'color':'#FFFF00', 'italic':true} ,the properties are 'name', 'size', 'bold', 'color', 'italic',they are all optional.
    //for example,we assume shape 0 is a textbox object,this will set the font color to Yellow ,and font size to 12pt,and bold the font. 
     const textbox=xs.sheet.data.shapes[0];
     const fontsettings= {'name':'Arial', 'size':12, 'bold':true, 'color':'#FFFF00'}; 
     textbox.setFont(fontsettings);
```
- Changer automatiquement la couleur de fond et la couleur du texte pour obtenir un effet actif visuel
```javascript
    setActiveEffect(boolvalue)
    // the parameters are:
        boolvalue: if true,will change background color and the text color of the textbox object;if false,restore to original appearence
```

Masquer/démasquer le contenu textuel dans l'objet zone de texte
```javascript
    hideText(boolvalue)
    // the parameters are:
        boolvalue: if true,will not display the text in the textbox object;if false,restore to original appearence
```

pour plus d'informations détaillées, vous pouvez consulter l'exemple ici
<https://github.com/aspose-cells/Aspose.Cells.Grid-for-Java/tree/main/Examples.GridJs>





