---
title: Сохранить HTML с помощью StreamProvider
type: docs
weight: 120
url: /ru/java/convert-excel-to-html-with-streamprovider/
---
{{% alert color="primary" %}}

При преобразовании полей Excel, содержащих изображения и фигуры, в файлы html мы часто сталкиваемся со следующими двумя проблемами:
1. Где мы должны сохранять изображения и фигуры при сохранении файла excel в поток html.
1. Замените путь по умолчанию на исключенный путь.

 В этой статье объясняется, как реализовать[**IStreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/IStreamProvider) интерфейс для настройки[**Хтмлсавеоптионс. StreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#StreamProvider) имущество. Внедрив этот интерфейс, вы сможете сохранять созданные ресурсы во время генерации HTML в определенных местах или потоках памяти.

{{% /alert %}}

## Образец кода

 Это основной код, показывающий использование[**Хтмлсавеоптионс. StreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#StreamProvider)имущество

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-HtmlSaveOptions-HtmlSaveOptions.java" >}}

 Вот код для*ExportStreamProvider* класс, который реализует[**IStreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/IStreamProvider)интерфейс, используемый внутри приведенного выше кода.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ExportStreamProvider-ExportStreamProvider.java" >}}

