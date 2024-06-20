---
title: Сохранить HTML с помощью StreamProvider
type: docs
weight: 120
url: /ru/java/convert-excel-to-html-with-streamprovider/
---

{{% alert color="primary" %}}

При конвертации файлов Excel, содержащих изображения и фигуры, в HTML-файлы мы часто сталкиваемся с двумя проблемами:
1. Где следует сохранять изображения и фигуры при сохранении файла Excel в HTML-поток.
1. Заменять путь по умолчанию на ожидаемый путь.

В данной статье объясняется, как реализовать интерфейс [**IStreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/IStreamProvider) для установки свойства [**HtmlSaveOptions.StreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#StreamProvider). Реализуя этот интерфейс, вы сможете сохранять созданные ресурсы во время генерации HTML в определенных местах или потоках памяти.

{{% /alert %}}

## Образец кода

Это основной код, показывающий использование свойства [**HtmlSaveOptions.StreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#StreamProvider)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-HtmlSaveOptions-HtmlSaveOptions.java" >}}

Вот код для класса *ExportStreamProvider*, который реализует интерфейс [**IStreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/IStreamProvider), используемый в вышеприведенном коде.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ExportStreamProvider-ExportStreamProvider.java" >}}

