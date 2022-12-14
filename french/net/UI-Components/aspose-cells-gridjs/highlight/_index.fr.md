---
title: Travailler avec la fonctionnalité GridJs Highlight
type: docs
weight: 250
url: /fr/net/aspose-cells-gridjs/highlight/
description: Cet article décrit comment utiliser GridJs pour mettre en surbrillance le texte des cellules, les plages de cellules, les formes et les images.
keywords: highlight, highlight spreadsheet
---
# Travailler avec la fonctionnalité GridJs Highlight
 Nous prenons en charge les API JS ci-dessous pour la fonctionnalité Highlight


- Activer la surbrillance et définir le style de surbrillance, toutes les API de surbrillance ne prendront effet qu'après la définition du style de surbrillance
```javascript
xs.showHighlights(style)
 // the parameter is:
 style: the style for highlight ,currently only support color
 for example: {'color':'rgba(85, 57, 47, 0.08)'}
```

- Désactiver la surbrillance
```javascript
xs.hideHighlights()
```
- Ajouter du texte de cellule à mettre en surbrillance
```javascript
xs.sheet.addHighlightText(row,col,startpostion,endposition)
    // the parameters are:
    row:row index 
	col:column index
	startpostion: highlight start postion in cell text 
	endpostion: highlight end postion in cell text 
```

- Supprimer la surbrillance du texte de la cellule dans le tableau
```javascript
xs.sheet.removeHighlightText(row,col)
    // the parameters are:
    row:row index 
	col:column index
```

-  Obtenir un tableau pour la surbrillance du texte de la cellule
```javascript
xs.sheet.getHighlightTexts()
```

- Ajouter une plage de cellules à mettre en surbrillance
```javascript
xs.sheet.addHighlightRange(sri,sci,eri,eci)
    // the parameters are:
    sri:start row index of cell range
	sci:start column index of cell range
	 eri:end row index of cell range
	eci:end column index of cell range
```

- Supprimer la surbrillance pour la plage de cellules dans le tableau
```javascript
xs.sheet.removeHighlightRange(sri,sci,eri,eci)
     // the parameters are:
    sri:start row index of cell range
	sci:start column index of cell range
	 eri:end row index of cell range
	eci:end column index of cell range
```

-  Obtenir un tableau pour la surbrillance de la plage de cellules
```javascript
xs.sheet.getHighlightRanges()
```

- Définir la plage de cellules sur la surbrillance inversée
```javascript
xs.sheet.setHighlightInverseRange(sri,sci,eri,eci)
    // the parameters are:
    sri:start row index of cell range
	sci:start column index of cell range
	 eri:end row index of cell range
	eci:end column index of cell range
```

- Supprimer la surbrillance pour la surbrillance inversée
```javascript
xs.sheet.removeHighlightInverseRange()
     
```

-  Obtenir la plage de cellules de surbrillance inverse
```javascript
xs.sheet.getHighlightInverseRange()
```


- Ajouter une forme pour mettre en surbrillance le tableau
```javascript
xs.sheet.addHighlightShape(shapeid)
    // the parameters are:
    shapeid: the id of shape, can be find in xs.sheet.data.shapes
```

- Supprimer la forme de surbrillance dans le tableau
```javascript
xs.sheet.removeHighlightShape(shapeid)
     // the parameters are:
    shapeid: the id of shape, can be find in xs.sheet.data.shapes
```

-  Obtenir un tableau pour la forme de surbrillance
```javascript
xs.sheet.getHighlightShaps()
```


- Ajouter une image pour mettre en surbrillance le tableau
```javascript
xs.sheet.addHighlightImage(imageid)
    // the parameters are:
    imageid: the id of image, can be find in xs.sheet.data.images
```

- Supprimer l'image en surbrillance dans le tableau
```javascript
xs.sheet.removeHighlightImage(imageid)
     // the parameters are:
    imageid: the id of image, can be find in xs.sheet.data.images
```

-  Obtenir un tableau pour l'image en surbrillance
```javascript
xs.sheet.getHighlightImages()
```

-  définir s'il faut mettre en surbrillance toutes les feuilles de calcul, inclure toutes les formes et images
```javascript
xs.sheet.setHighlightAll(ishighlightall,isrerender=true)
   // the parameters are:
   ishighlightall: true or false,whether to highlight all
   isrerender: true or false,whether to reRender
```


- définir la fonction de surbrillance d'image personnalisée
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

Vous pouvez en savoir plus sur notre page de démonstration github https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples_GridJs/wwwroot/xspread/index.html
