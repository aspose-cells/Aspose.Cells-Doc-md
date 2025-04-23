---
title: как реализовать ленивую загрузку в GridJs  
type: docs
weight: 250
url: /ru/java/aspose-cells-gridjs/how-to-do-lazy-loading/
description: В этой статье описывается, как реализовать ленивую загрузку в GridJs.
keywords: GridJs,ленивая загрузка,по требованию,
aliases:
  - /java/aspose-cells-gridjs/lazy-loading/
  - /java/aspose-cells-gridjs/loading-on-demand/

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
```java 
  Config.setLazyLoading(true);
```
## Установка URL-адреса действия для ленивой загрузки.
например:
```javascript
 const lazyLoadingUrl = "/GridJs2/LazyLoading";
 xs.setLazyLoadingUrl(lazyLoadingUrl);
```
После того как пользователь нажмёт на другой лист, который не является активным, действие запроса данных будет автоматически запущено приложением таблицы. 

## Реализация действия ленивой загрузки в контроллере на сервере.
например:
```java
    @PostMapping("/LazyLoading")
    public void lazyLoadingStreamJson(
            @RequestParam(value = "name", required = false) String sheetName,
            @RequestParam(value = "uid", required = false) String uid,
            HttpServletResponse response) throws IOException {

        GridJsWorkbook wbj = new GridJsWorkbook();
        response.setContentType(MediaType.APPLICATION_JSON_VALUE);
        response.setHeader(HttpHeaders.CONTENT_ENCODING, "gzip");

        try (GZIPOutputStream gzipOutputStream = new GZIPOutputStream(response.getOutputStream())) {
            try {
				wbj.lazyLoadingStream(gzipOutputStream, uid, sheetName);
			} catch (Exception e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
        }
    }
```





