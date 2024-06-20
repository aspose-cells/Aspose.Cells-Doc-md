---
title: Загрузка HTML в Excel с помощью поставщика потока
type: docs
weight: 80
url: /ru/java/convert-html-to-excel-with-streamprovider/
---

{{% alert color="primary" %}} 

При загрузке html, который содержит внешние ресурсы, мы часто сталкиваемся с двумя следующими проблемами:
1. При загрузке потока html изображения и внешние ресурсы, на которые ссылаются файлы html, не могут быть получены через относительные пути.
1. Внешние пути к ресурсам, на которые ссылаются в файлах html, должны быть отображены.

В этой статье объясняется, как реализовать интерфейс [**IStreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/IStreamProvider) для установки свойства [**HtmlLoadOptions.StreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#StreamProvider). Реализуя этот интерфейс, вы сможете загружать внешние ресурсы во время загрузки потоков Html или эти внешние ресурсы будут относительными.

{{% /alert %}} 

Это основной код, показывающий использование [**HtmlLoadOptions.StreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#StreamProvider)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Load-Html-With-StreamProvider.java" >}}
