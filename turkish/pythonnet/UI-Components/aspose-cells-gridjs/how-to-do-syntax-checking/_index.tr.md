---
title: GridJs için sözdizimi denetimi ve yazım düzeltmesi  
type: docs
weight: 250
url: /tr/python-net/aspose-cells-gridjs/how-to-do-syntax-checking/
description: Bu makale, GridJs için sözdizimi denetimi ve yazım düzeltmesi eklemenin nasıl yapılacağını anlatmaktadır.
keywords: GridJs,sözdizimi denetimi,yazım düzeltmesi,sözdizimi,yazım,grafik kontrolü,Gramer Kontrolü
aliases:
  - /python-net/aspose-cells-gridjs/syntax-checking/
  - /python-net/aspose-cells-gridjs/how-to-add-syntax-checking/
  - /python-net/aspose-cells-gridjs/how-to-add-spell-correction/
  - /python-net/aspose-cells-gridjs/spell-correction/
---


# Kullanıcı girişi üzerinde sözdizimi denetimi ve yazım düzeltmesi yapmak için adımlar
## Yükleme seçeneklerini ayarla.
örneğin:
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
## Sözdizimi denetimi ve yazım düzeltmesi için işlem URL'sini ayarla.
örneğin:
```javascript
 const checkurl = "/GridJs2/CheckSyntax";  
 xs.setSyntaxCheckUrl(checkurl);
```
Kullanıcı bir hücreye metin girdikten sonra, sözdizimi denetimi işlemi otomatik olarak elektronik tablo uygulaması tarafından tetiklenir. 

## Sunucu tarafında sözdizimi kontrolü ve yazım hatası düzeltmesi uygula.
örneğin:
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





