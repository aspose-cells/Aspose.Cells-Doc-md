---
title: comprobación de sintaxis y corrección ortográfica para GridJs  
type: docs
weight: 250
url: /es/net/aspose-cells-gridjs/how-to-do-syntax-checking/
description: Este artículo describe cómo agregar comprobación de sintaxis y corrección ortográfica para GridJs.
keywords: GridJs,verificación de sintaxis,corrección ortográfica,sintaxis,ortografía,Verificación gramatical,Gramática
aliases:
  - /net/aspose-cells-gridjs/syntax-checking/
  - /net/aspose-cells-gridjs/how-to-add-syntax-checking/
  - /net/aspose-cells-gridjs/how-to-add-spell-correction/
  - /net/aspose-cells-gridjs/spell-correction/
---


# Para realizar la verificación de sintaxis y corrección ortográfica en la entrada del usuario, los pasos son
## Configurar opciones de carga.
por ejemplo:
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
## Establecer URL de acción para verificación de sintaxis y corrección ortográfica.
por ejemplo:
```javascript
 const checkurl = "/GridJs2/CheckSyntax";  
 xs.setSyntaxCheckUrl(checkurl);
```
Después de que un usuario ingresa contenido de texto en una celda, la acción de verificación de sintaxis se activará automáticamente por la aplicación de hoja de cálculo. 

## Implementar API de acción de verificación de sintaxis y corrección ortográfica en el Controlador del lado del servidor.
por ejemplo:
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

Puedes encontrar más en nuestra página de demostración en GitHub https://github.com/aspose-cells/Aspose.Cells.Grid-for-.NET/blob/master/Examples_GridJs/wwwroot/xspread/index.html



