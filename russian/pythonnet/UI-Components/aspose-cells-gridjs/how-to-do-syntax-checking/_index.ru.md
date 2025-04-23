---
title: проверка синтаксиса и автозамена ошибок для GridJs  
type: docs
weight: 250
url: /ru/python-net/aspose-cells-gridjs/how-to-do-syntax-checking/
description: В этой статье описывается, как добавить проверку синтаксиса и автозамену ошибок для GridJs.
keywords: GridJs,проверка синтаксиса,автозамена ошибок,синтаксис,ошибка,Грамматическая проверка,Грамматика
aliases:
  - /python-net/aspose-cells-gridjs/syntax-checking/
  - /python-net/aspose-cells-gridjs/how-to-add-syntax-checking/
  - /python-net/aspose-cells-gridjs/how-to-add-spell-correction/
  - /python-net/aspose-cells-gridjs/spell-correction/
---


# Для проверки синтаксиса и исправления орфографии пользовательского ввода, шаги следующие
## Установить параметры загрузки.
например:
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
## Установить адрес URL для действия проверки синтаксиса и исправления орфографии.
например:
```javascript
 const checkurl = "/GridJs2/CheckSyntax";  
 xs.setSyntaxCheckUrl(checkurl);
```
После ввода текста пользователем в ячейке, действие проверки синтаксиса будет автоматически запущено приложением электронной таблицы. 

## Реализовать проверку синтаксиса и исправление орфографии на серверной стороне.
например:
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





