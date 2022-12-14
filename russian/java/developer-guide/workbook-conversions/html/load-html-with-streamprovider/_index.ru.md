---
title: Загрузить Html в Excel с помощью StreamProvider
type: docs
weight: 80
url: /ru/java/convert-html-to-excel-with-streamprovider/
---
{{% alert color="primary" %}} 

При загрузке html, содержащего внешние ресурсы, мы часто сталкиваемся со следующими двумя проблемами:
1. При загрузке html-потока изображения и внешние ресурсы, на которые ссылается html-файл, не могут быть получены по относительным путям.
1. Пути к внешним ресурсам, на которые есть ссылки в html-файлах, должны быть сопоставлены.

 В этой статье объясняется, как реализовать[**IStreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/IStreamProvider) интерфейс для настройки[**Хтмллоадоптионс. StreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#StreamProvider) имущество. Реализуя этот интерфейс, вы сможете загружать внешние ресурсы во время загрузки потоков Html или эти внешние ресурсы являются относительными.

{{% /alert %}} 

 Это основной код, показывающий использование[**Хтмллоадоптионс. StreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#StreamProvider)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Load-Html-With-StreamProvider.java" >}}
