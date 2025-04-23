---
title: Vérification de syntaxe et correction orthographique pour GridJs  
type: docs
weight: 250
url: /fr/net/aspose-cells-gridjs/how-to-do-syntax-checking/
description: Cet article décrit comment ajouter la vérification de syntaxe & correction orthographique pour GridJs.
keywords: GridJs, vérification de syntaxe, correction orthographique, syntaxe, orthographe, Vérification de grammaire, Grammaire
aliases:
  - /net/aspose-cells-gridjs/syntax-checking/
  - /net/aspose-cells-gridjs/how-to-add-syntax-checking/
  - /net/aspose-cells-gridjs/how-to-add-spell-correction/
  - /net/aspose-cells-gridjs/spell-correction/
---


# Pour effectuer une vérification de syntaxe et une correction orthographique sur l'entrée utilisateur, les étapes sont
## Définir les options de chargement.
par exemple :
```javascript
 const option = {
     ...
     //set showCheckSyntaxButton to true
    showCheckSyntaxButton:true,
    //set checkSyntax to true
    checkSyntax:true,
 };
  xs = x_spreadsheet('#gridjs-demo', option)
```
## Définir l'URL d'action pour la vérification de syntaxe et la correction orthographique.
par exemple :
```javascript
 const checkurl = "/GridJs2/CheckSyntax";  
 xs.setSyntaxCheckUrl(checkurl);
```
Après qu'un utilisateur entre du contenu textuel dans une cellule, l'action de vérification de syntaxe sera déclenchée automatiquement par l'application de feuille de calcul 

## Implémenter l'API d'action de vérification de syntaxe et de correction orthographique dans le Contrôleur côté serveur.
par exemple :
```C#
 [HttpPost]
 public async Task<IActionResult> CheckSyntaxAsync()
 {   //the input text content 
     String text = HttpContext.Request.Form["v"];
     /* the locale info : support multiple language for menus ,the locale can be:
	                        en, zh, es, pt, de, ru, nl, 
	                   for  English,Chinese,Spanish,Portuguese,German,Russian,Dutch
			        ar, fr,id,it,ja
                           for  Arabic,French,Indonesian,Italian,Japanese
			        ko,th,tr,vi,cht
                           for  Korean,Thai,Turkey,Vietnamese,Traditional Chinese    
			   */
     String locale = HttpContext.Request.Form["locale"];
     if (string.IsNullOrEmpty(text))
     {
         return Ok(new
         {
             Success = false,
             v = ""
         });
     }

     // The logic for invoking syntax checking here can be implemented through a third-party library or custom logic.
     string correctedContent = await CorrectSyntaxAsync(text, locale);

     return Ok(new
     {
         Success = true,
         v = correctedContent
     });
 }
 //you need to implement it youself
 private async Task<string> CorrectSyntaxAsync(string text,string locale)
 {   String result=null;
     //your logic to do syntax checking
     return result;
 }
```

Vous pouvez trouver plus d'informations sur notre page de démonstration GitHub https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples_GridJs/wwwroot/xspread/index.html



