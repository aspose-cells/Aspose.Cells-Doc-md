---
title: как реализовать ленивую загрузку в GridJs  
type: docs
weight: 250
url: /ru/python-net/aspose-cells-gridjs/how-to-do-lazy-loading/
description: В этой статье описывается, как реализовать ленивую загрузку в GridJs.
keywords: GridJs,ленивая загрузка,по требованию,
aliases:
  - /python-net/aspose-cells-gridjs/lazy-loading/
  - /python-net/aspose-cells-gridjs/loading-on-demand/

---

## о ленивой загрузке 
При работе с файлом электронной таблицы, содержащим множество листов, мы можем оптимизировать процесс загрузки, сначала загружая только активный лист.

Эта стратегия обеспечивает, что исходный JSON-ответ сервера содержит только данные активного листа.  

В результате первоначальный веб-трафик значительно снижается, что повышает опыт пользователя за счет минимизации времени загрузки.  

Более того, GridJs разработан для динамичного реагирования на действия пользователя. Особенно, когда пользователь кликает на другой лист,

GridJs умно инициирует запрос к серверу для получения данных именно этого листа.  

Этот механизм по требованию не только дополнительно сокращает ненужные передачи данных, но и обеспечивает пользователю доступ к самой актуальной информации листа, с которым он работает.  

Применяя такой подход, мы не только оптимизируем время начальной загрузки, но и поддерживаем отзывчивое и эффективное приложение, которое хорошо масштабируется с увеличением количества листов в файле.

# Чтобы реализовать ленивую загрузку в GridJs, необходимо выполнить следующие шаги
## Установка конфигурационных опций для ленивой загрузки.
например:
```python 
       Config.set_lazy_loading(True)
```
## Установка URL-адреса действия для ленивой загрузки.
например:
```javascript
 const lazyLoadingUrl = "/GridJs2/LazyLoading";
 xs.setLazyLoadingUrl(lazyLoadingUrl);
```
После того, как пользователь кликнет по другому листу, не являющемуся активным, запрос данных будет автоматически инициирован приложением таблицы. 

## Реализация действия ленивой загрузки в контроллере на сервере.
например:
```python
@app.route('/GridJs2/LazyLoading', methods=['POST'])
def lazy_loading():
    sheet_name = request.form.get('name', '')
    uid = request.form.get('uid', '')
    if not sheet_name:
        return jsonify({'error': 'sheet_name is required'}), 400
    if not uid:
        return jsonify({'error': 'uid is required'}), 400

    wbj = GridJsWorkbook()
    try:

        output = io.BytesIO()
        with gzip.GzipFile(fileobj=output, mode='wb', compresslevel=9) as gzip_stream:
             wbj.lazy_loading_stream(gzip_stream,uid, sheet_name)


        response = Response(output.getvalue(), mimetype='application/json')
        response.headers['Content-Encoding'] = 'gzip'

        return response
    except Exception as e:
        return Response(str(e), status=500)
```





