---
title: Укажите путь к файлу html экспортированного листа через интерфейс IFilePathProvider.
type: docs
weight: 70
url: /ru/net/provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface/
---
## **Возможные сценарии использования**
 Предположим, у вас есть файл Excel с несколькими листами, и вы хотите экспортировать каждый лист в отдельный файл HTML. Если какой-либо из ваших листов имеет ссылки на другие листы, то эти ссылки будут нарушены в экспортированном HTML. Чтобы решить эту проблему, Aspose.Cells предоставляет[Ифилепаспровидер](https://reference.aspose.com/cells/net/aspose.cells/ifilepathprovider)интерфейс, который вы можете реализовать для исправления неработающих ссылок.
## **Укажите путь к файлу экспортированного рабочего листа HTML через интерфейс IFilePathProvider.**
 Пожалуйста, загрузите[образец эксель файла](5115213.zip)используется в следующем коде и его экспортированных файлах HTML. Все эти файлы находятся внутри каталога Temp. Вы должны извлечь его на диск C:. Тогда он станет каталогом C:\Temp. Затем вы откроете файл Sheet1.html в браузере и щелкните две ссылки внутри него. Эти ссылки относятся к этим двум экспортированным рабочим листам HTML, которые находятся в каталоге C:\Temp\OtherSheets.

{{< highlight "java" >}}

 file:///C:/Temp/OtherSheets/Sheet2.html#RANGE!A1

file:///C:/Temp/OtherSheets/Sheet3.html#RANGE!A1

{{< /highlight >}}

На следующем снимке экрана показано, как выглядит файл C:\Temp\Sheet1.html и его ссылки.

![дело:изображение_альтернативный_текст](provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface_1.png)

 На следующем снимке экрана показан источник HTML. Как видите, ссылки теперь указывают на каталог C:\Temp\OtherSheets. Это было достигнуто с помощью[Ифилепаспровидер](https://reference.aspose.com/cells/net/aspose.cells/ifilepathprovider)интерфейс.

![дело:изображение_альтернативный_текст](provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface_2.png)
## **Образец кода**
 Обратите внимание, что каталог C:\Temp предназначен только для иллюстрации. Вы можете использовать любой каталог по вашему выбору и разместить[образец эксель файла](5115211.xlsx)внутри и выполните предоставленный образец кода. Затем он создаст подкаталог OtherSheets внутри вашего каталога и экспортирует в него второй и третий листы HTML. Пожалуйста, измените переменную dirPath в предоставленном коде и укажите ее в каталоге по вашему выбору перед выполнением.

{{% alert color="primary" %}} 

Пример кода будет работать, только если вы установите лицензию Aspose.Cells. Если вы попытаетесь запустить код без установки лицензии, он войдет в бесконечный цикл. Поэтому мы добавили проверку, чтобы распечатать сообщение и остановить выполнение, когда лицензия не установлена. Вы можете либо приобрести лицензию, либо запросить временную лицензию на 30 дней у команды Aspose.Purchase.

{{% /alert %}} 

Обратите внимание, что комментирование этих строк внутри кода приведет к разрыву ссылок в Sheet1.html, а Sheet2.html или Sheet3.html не будут открываться, когда их ссылки будут нажаты внутри Sheet1.html.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithHTMLFormat-ExportedWorkSheetViaIFilePathProvider-hyperlinks.cs" >}}



 Вот полный пример кода, который вы можете выполнить с предоставленным[образец эксель файла](5115211.xlsx).



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithHTMLFormat-ExportedWorkSheetViaIFilePathProvider-ExportedWorkSheetViaIFilePathProvider.cs" >}}
