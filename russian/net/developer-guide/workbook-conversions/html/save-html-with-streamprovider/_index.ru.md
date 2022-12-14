---
title: Сохранить HTML с помощью StreamProvider
type: docs
weight: 80
url: /ru/net/convert-excel-to-html-with-streamprovider/
---
{{% alert color="primary" %}} 

При преобразовании полей Excel, содержащих изображения и фигуры, в файлы html мы часто сталкиваемся со следующими двумя проблемами:
1. Где мы должны сохранять изображения и фигуры при сохранении файла excel в поток html.
1. Замените путь по умолчанию на исключенный путь.

 В этой статье объясняется, как реализовать[IStreamProvider](https://reference.aspose.com/cells/net/aspose.cells/istreamprovider) интерфейс для настройки[Хтмлсавеоптионс. StreamProvider](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/streamprovider) имущество. Внедрив этот интерфейс, вы сможете сохранять созданные ресурсы во время генерации HTML в определенных местах или потоках памяти.

{{% /alert %}} 

 Это основной код, показывающий использование[Хтмлсавеоптионс. StreamProvider](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/streamprovider)имущество



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithHTMLFormat-ImplementIStreamProvider-ImplementIStreamProvider.cs" >}}



 Вот код для*ExportStreamProvider* класс, который реализует[IStreamProvider](https://reference.aspose.com/cells/net/aspose.cells/istreamprovider)интерфейс, используемый внутри приведенного выше кода.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithHTMLFormat-ImplementIStreamProvider-ExportStreamProviderClass.cs" >}}

