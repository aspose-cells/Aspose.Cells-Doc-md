---
title: comprobación de sintaxis y corrección ortográfica para GridJs  
type: docs
weight: 250
url: /es/python-net/aspose-cells-gridjs/how-to-do-syntax-checking/
description: Este artículo describe cómo agregar comprobación de sintaxis y corrección ortográfica para GridJs.
keywords: GridJs,verificación de sintaxis,corrección ortográfica,sintaxis,ortografía,Verificación gramatical,Gramática
aliases:
  - /python-net/aspose-cells-gridjs/syntax-checking/
  - /python-net/aspose-cells-gridjs/how-to-add-syntax-checking/
  - /python-net/aspose-cells-gridjs/how-to-add-spell-correction/
  - /python-net/aspose-cells-gridjs/spell-correction/
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

## Implementar revisión de sintaxis y corrección ortográfica en el servidor.
por ejemplo:
```python
# The logic for invoking syntax checking here can be implemented through a third-party library or custom logic.
def correct_syntax(text, locale):  
# replace your logic  here     
    return text  

@app.route('/GridJs2/CheckSyntax', methods=['POST'])  
def check_syntax():  
    text = request.form.get('v')  
    locale = request.form.get('locale')  

    if not text:  
        return jsonify({  
            'Success': False,  
            'v': ''  
        }), 200  

    corrected_content = correct_syntax(text, locale)  

    return jsonify({  
        'Success': True,  
        'v': corrected_content  
    }), 200  
```





