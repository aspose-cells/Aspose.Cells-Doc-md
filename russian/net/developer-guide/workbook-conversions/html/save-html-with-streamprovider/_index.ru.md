---
title: Сохранить HTML с помощью StreamProvider
type: docs
weight: 80
url: /ru/net/convert-excel-to-html-with-streamprovider/
---

{{% alert color="primary" %}} 

При преобразовании файлов Excel, содержащих изображения и формы, мы часто сталкиваемся с следующими двумя проблемами:
1. Где следует сохранять изображения и фигуры при сохранении файла Excel в HTML-поток.
1. Заменять путь по умолчанию на ожидаемый путь.

В этой статье объясняется, как реализовать интерфейс [IStreamProvider](https://reference.aspose.com/cells/net/aspose.cells/istreamprovider) для установки свойства [HtmlSaveOptions.StreamProvider](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/streamprovider). Реализуя этот интерфейс, вы сможете сохранять созданные ресурсы во время генерации HTML в вашем определенном местоположении или потоки памяти.

{{% /alert %}} 

Это основной код, демонстрирующий использование свойства [HtmlSaveOptions.StreamProvider](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/streamprovider).



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithHTMLFormat-ImplementIStreamProvider-ImplementIStreamProvider.cs" >}}



Вот код для *ExportStreamProvider* класса, который реализует интерфейс [IStreamProvider](https://reference.aspose.com/cells/net/aspose.cells/istreamprovider), используемый в вышеприведенном коде.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithHTMLFormat-ImplementIStreamProvider-ExportStreamProviderClass.cs" >}}

{{< app/cells/assistant language="csharp" >}}
