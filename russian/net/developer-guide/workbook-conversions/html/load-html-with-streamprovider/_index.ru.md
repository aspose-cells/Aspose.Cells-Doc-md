---
title: Загрузка HTML в Excel с помощью поставщика потока
type: docs
weight: 80
url: /ru/net/convert-html-to-excel-with-streamprovider/
---

{{% alert color="primary" %}} 

При загрузке html-файлов, содержащих внешние ресурсы, мы часто сталкиваемся с следующими двумя проблемами:
1. При загрузке потока html изображения и внешние ресурсы, на которые ссылаются файлы html, не могут быть получены через относительные пути.
1. Внешние пути к ресурсам, указанные в html-файлах, нужно сопоставить

В этой статье объясняется, как реализовать интерфейс [IStreamProvider](https://reference.aspose.com/cells/net/aspose.cells/istreamprovider) для установки свойства [HtmlLoadOptions.StreamProvider](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/streamprovider/). Реализуя этот интерфейс, вы сможете загружать внешние ресурсы во время загрузки потоков Html, или эти внешние ресурсы являются относительными.

{{% /alert %}} 

Это основной код, показывающий использование свойства [HtmlLoadOptions.StreamProvider](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/streamprovider/)



{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Load-Html-With-StreamProvider.cs" >}}
