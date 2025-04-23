---
title: mostrar explicación de fórmula para GridJs  
type: docs
weight: 250
url: /es/net/aspose-cells-gridjs/how-to-show-formula-explanation/
description: Este artículo describe cómo mostrar la explicación de fórmula para GridJs.
keywords: GridJs,fórmula,explicación de la fórmula,mostrar explicación de fórmula,intérprete de fórmulas
aliases:
  - /net/aspose-cells-gridjs/show-formula-explanation/
  - /net/aspose-cells-gridjs/display-formula-explanation/
  - /net/aspose-cells-gridjs/how-to-display-formula-explanation/
  - /net/aspose-cells-gridjs/formula-explanation/
  - /net/aspose-cells-gridjs/formula-interpreter/
---


# Para mostrar la explicación de la fórmula al pasar el mouse sobre una celda específica que contiene una fórmula, los pasos son
## Configurar opciones de carga.
por ejemplo:
```javascript
 const option = {
     ...
     //set showFormulaExplain to true
    showFormulaExplain:true,
 };
  xs = x_spreadsheet('#gridjs-demo', option)
```
## Establecer la URL de acción para showFormulaExplain.
por ejemplo:
```javascript
    const formulaExplainUrl = "/GridJs2/FormulaExplain";
    xs.setFormulaExplainUrl(formulaExplainUrl);
```
Cuando el usuario pasa el mouse sobre una celda que contiene una fórmula, la acción de mostrar la explicación de la fórmula se activará automáticamente por la aplicación de hoja de cálculo. 

## Implementar la API de acción de mostrar explicación de fórmula en Controller en el lado del servidor.
por ejemplo:
```C#
  [HttpPost]
 public async Task<IActionResult> FormulaExplainAsync()
 {
     String formulaText = HttpContext.Request.Form["v"];
     String locale = HttpContext.Request.Form["locale"];
     if (string.IsNullOrEmpty(formulaText))
     {
         return Ok(new
         {
             Success = false,
             v = ""
         });
     }
     //here the formulaText is the formula ,etc "=SUM(B1:B10)"
     string correctedContent = await GetFormulaExplainAsync(formulaText, locale);

     return Ok(new
     {
         Success = true,
         v = correctedContent
     });
 }
 //you need to implement it youself
 private async Task<string> GetFormulaExplainAsync(string formulaText,string locale)
 {   String result=null;
     //your logic to get the detail explanation for the formulaText
     return result;
 }
```
![por hacer: la pantalla de mostrar explicación de fórmula](gridjs_show_formula_explanation.png)




