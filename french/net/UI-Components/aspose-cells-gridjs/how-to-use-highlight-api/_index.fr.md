---
title: Travailler avec la fonction de surlignage de GridJs
type: docs
weight: 250
url: /fr/net/aspose-cells-gridjs/how-to-use-highlight-api/
description: Cet article décrit comment utiliser la surbrillance sur le texte de cellule, les plages de cellules, les formes et les images dans GridJs.
keywords: GridJs, surbrillance, feuille de calcul de surbrillance, retranchement, remarques
aliases:
  - /net/aspose-cells-gridjs/highlight/
  - /net/aspose-cells-gridjs/how-to-highlight/
  - /net/aspose-cells-gridjs/work-with-highlight-api/
  - /net/aspose-cells-gridjs/work-with-highlight-apis/
---

# Travailler avec la fonction de surlignage de GridJs 
Nous prenons en charge les API JS ci-dessous pour la fonction de surlignage 


-  Activer le surlignage et définir le style de surlignage, toutes les API de surlignage ne prendront effet qu'après que le style de surlignage ait été défini dans la feuille de calcul active 
```javascript
xs.sheet.showHighlights(style)
 // the parameter is:
 style: the style for highlight ,currently only support color
 for example: {'color':'rgba(85, 57, 47, 0.08)'}
```

-  mettre à jour le style de surlignage défini dans la feuille de calcul active 
```javascript
xs.sheet.updateHighlightStyle(style)
 // the parameter is:
 style: the style for highlight ,currently only support color
 for example: {'color':'rgba(85, 57, 47, 0.08)'}
```


-  Désactiver le surlignage dans la feuille de calcul active    
```javascript
xs.sheet.hideHighlights()
```
-  Ajouter du texte de cellule à surligner dans la feuille de calcul active 
```javascript
xs.sheet.addHighlightText(row,col,startpostion,endposition)
    // the parameters are:
	row:row index 
	col:column index
	startpostion: highlight start postion in cell text 
	endpostion: highlight end postion in cell text 
    //it support multiple range postion inside one cell
```

-  Supprimer le surlignage du texte de la cellule dans un tableau dans la feuille de calcul active 
```javascript
xs.sheet.removeHighlightText(row,col,startpostion,endposition)
    // the parameters are:
	row:row index 
	col:column index
	startpostion: highlight start postion in cell text 
	endpostion: highlight end postion in cell text 
```

-  Obtenir un tableau pour surligner le texte de la cellule dans la feuille de calcul active   
```javascript
xs.sheet.getHighlightTexts()
```

-  Ajouter une plage de cellules à surligner dans la feuille de calcul active 
```javascript
xs.sheet.addHighlightRange(sri,sci,eri,eci)
    // the parameters are:
	sri:start row index of cell range
	sci:start column index of cell range
	eri:end row index of cell range
	eci:end column index of cell range
```

-  Supprimer le surlignage de la plage de cellules dans un tableau dans la feuille de calcul active 
```javascript
xs.sheet.removeHighlightRange(sri,sci,eri,eci)
     // the parameters are:
	sri:start row index of cell range
	sci:start column index of cell range
	eri:end row index of cell range
	eci:end column index of cell range
```

-  Obtenir un tableau pour surligner la plage de cellules dans la feuille de calcul active   
```javascript
xs.sheet.getHighlightRanges()
```

-  Définir une plage de cellules pour inverser le surlignage dans la feuille de calcul active 
```javascript
xs.sheet.setHighlightInverseRange(sri,sci,eri,eci)
    // the parameters are:
	sri:start row index of cell range
	sci:start column index of cell range
	eri:end row index of cell range
	eci:end column index of cell range
```

-  Supprimer le surlignage pour inverser le surlignage dans la feuille de calcul active 
```javascript
xs.sheet.removeHighlightInverseRange()

```

-  Obtenir la plage de cellules de surlignage inverse dans la feuille de calcul active 
```javascript
xs.sheet.getHighlightInverseRange()
```


-  Ajouter une forme pour surligner un tableau dans la feuille de calcul active 
```javascript
xs.sheet.addHighlightShape(shapeid)
    // the parameters are:
    shapeid: the id of shape, can be find in xs.sheet.data.shapes
```

-  Supprimer la forme de surlignage dans un tableau dans la feuille de calcul active 
```javascript
xs.sheet.removeHighlightShape(shapeid)
     // the parameters are:
    shapeid: the id of shape, can be find in xs.sheet.data.shapes
```

-  Obtenir un tableau pour surligner la forme dans la feuille de calcul active  
```javascript
xs.sheet.getHighlightShaps()
```

-  Ajouter une zone de texte pour surligner, la zone de texte est un type de forme spécial dont la propriété de type est: "ZoneDeTexte", dans la feuille de calcul active 
```javascript
xs.sheet.addHighlightTextBox(shapeid, startpostion, endposition)
    // the parameters are:
    shapeid: the id of shape, can be find in xs.sheet.data.shapes whose type is 'TextBox'
    startpostion: highlight start postion in the text of textbox
    endpostion: highlight end postion in the text of textbox
    //it support multiple range postion inside one textbox
```


-  Supprimer la plage de surlignage dans la zone de texte, la zone de texte est un type de forme spécial dont la propriété de type est: "ZoneDeTexte", dans la feuille de calcul active 
```javascript
xs.sheet.removeHighlightTextBox(shapeid, startpostion, endposition)
    // the parameters are:
    shapeid: the id of shape, can be find in xs.sheet.data.shapes whose type is 'TextBox'
    startpostion: highlight start postion in the text of textbox
    endpostion: highlight end postion in the text of textbox
    //it support multiple range postion inside one textbox
```

-  Ajouter une image pour surligner un tableau dans la feuille de calcul active 
```javascript
xs.sheet.addHighlightImage(imageid)
    // the parameters are:
    imageid: the id of image, can be find in xs.sheet.data.images
```

-  Supprimer l'image de surlignage dans un tableau dans la feuille de calcul active 
```javascript
xs.sheet.removeHighlightImage(imageid)
     // the parameters are:
    imageid: the id of image, can be find in xs.sheet.data.images
```

-  Obtenir un tableau pour surligner l'image dans la feuille de calcul active  
```javascript
xs.sheet.getHighlightImages()
```

- Définir si mettre en évidence tous les objets dans la feuille active, y compris toutes les formes et images et toute la zone de la feuille de calcul
```javascript
xs.sheet.setHighlightAll(ishighlightall,isrerender=true)
   // the parameters are:
   ishighlightall: true or false,whether to highlight all
   isrerender: true or false,whether to reRender
```


-  Définir une fonction de surlignage d'image personnalisée
```javascript
xs.sheet.setCustomHighlightImgFunc(func)
   // the parameters are:
   func: the custom highlight image function, it shall take two parameters ,first is ishighlight,the second one is the fabric image object 
   //we use fabric js to manage image object, please refer to http://fabricjs.com/image-filters to check more info
   below is an example for the decleare function: 
   const customHighlightImage = (ishighlight, imgobj) => {
            imgobj.filters[0] = ishighlight ? new fabric.Image.filters.Sepia() : false;
            imgobj.applyFilters();
        }

```

- Effacer les paramètres de mise en évidence pour la feuille active
```javascript
xs.sheet.clearHighlights()

```

### Surlignage pour l'objet zone de texte
textbox est un type spécial de forme dont la propriété de type est :"TextBox",
par exemple: le code ci-dessous va montrer quelle forme est textbox

```javascript
for (let shape of xs.sheet.data.shapes) {
    if (shape.type === 'TextBox') {
        console.log(shape.id + ' is a textbox');
    }
}
```
- Ajouter un surlignage pour l'objet textbox
```javascript
    addHighlight(startpostion,endposition)
    // the parameters are:
	startpostion: highlight start postion in textbox
	endpostion: highlight end postion in textbox

//for example,we assume shape 0 is a textbox object
const textbox=xs.sheet.data.shapes[0];
//first we shall add to highlight shape to enable the highlight for the textbox shape object,it support multiple range postion 
 xs.sheet.addHighlightShape(textbox.id);
 textbox.addHighlight(5,10);
 textbox.addHighlight(18,28);
```

- Supprimer un surlignage pour l'objet textbox 
```javascript
    removeHighlight(startpostion,endposition)
    // the parameters are:
	startpostion: highlight start postion in textbox
	endpostion: highlight end postion in textbox
    //for example,we assume shape 0 is a textbox object
     const textbox=xs.sheet.data.shapes[0];
     textbox.removeHighlight(5,10);
```

- Obtenir un surlignage pour l'objet textbox 
```javascript
    getHighlight()
    //for example,we assume shape 0 is a textbox object
     const textbox=xs.sheet.data.shapes[0];
     textbox.getHighlight();
```




Vous pouvez trouver plus d'informations sur notre page de démonstration GitHub https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples_GridJs/wwwroot/xspread/index.html
