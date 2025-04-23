---
title: как реализовать ленивую загрузку в GridJs  
type: docs
weight: 250
url: /ru/net/aspose-cells-gridjs/how-to-do-lazy-loading/
description: В этой статье описывается, как реализовать ленивую загрузку в GridJs.
keywords: GridJs,ленивая загрузка,по требованию,
aliases:
  - /net/aspose-cells-gridjs/lazy-loading/
  - /net/aspose-cells-gridjs/loading-on-demand/

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
```C# 
   Config.LazyLoading = true;
```
## Установка URL-адреса действия для ленивой загрузки.
например:
```javascript
 const lazyLoadingUrl = "/GridJs2/LazyLoadingStreamJson";
 xs.setLazyLoadingUrl(lazyLoadingUrl);
```
После того, как пользователь кликнет по другому листу, не являющемуся активным, запрос данных будет автоматически инициирован приложением таблицы. 

## Реализация действия ленивой загрузки в контроллере на сервере.
например:
```C#
    [HttpPost]
 // post: /GridJs2/LazyLoadingStreamJson?name=&uid=
 public ActionResult LazyLoadingStreamJson()
 {
     string sheetName = HttpContext.Request.Form["name"];
     string uid = HttpContext.Request.Form["uid"];
     GridJsWorkbook wbj = new GridJsWorkbook();


     Response.ContentType = "application/json";
     Response.Headers.Add("Content-Encoding", "gzip");

     using (GZipStream gzip = new GZipStream(Response.Body, CompressionLevel.Optimal))
     {
        wbj.LazyLoadingStream(gzip, uid, sheetName);

     }

     return new EmptyResult();
 }
```





