---
title: Vérification de syntaxe et correction orthographique pour GridJs  
type: docs
weight: 250
url: /fr/python-net/aspose-cells-gridjs/how-to-do-syntax-checking/
description: Cet article décrit comment ajouter la vérification de syntaxe & correction orthographique pour GridJs.
keywords: GridJs, vérification de syntaxe, correction orthographique, syntaxe, orthographe, Vérification de grammaire, Grammaire
aliases:
  - /python-net/aspose-cells-gridjs/syntax-checking/
  - /python-net/aspose-cells-gridjs/how-to-add-syntax-checking/
  - /python-net/aspose-cells-gridjs/how-to-add-spell-correction/
  - /python-net/aspose-cells-gridjs/spell-correction/
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

## Implémenter la vérification de syntaxe et la correction orthographique côté serveur.
par exemple :
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





