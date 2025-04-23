---
title: Предоставьте путь к экспортированному файлу HTML рабочего листа через интерфейс IFilePathProvider
type: docs
weight: 870
url: /ru/java/provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface/
---

## **Возможные сценарии использования**
Предположим, у вас есть файл Excel с несколькими листами, и вы хотите экспортировать каждый лист в отдельный файл HTML. Если у одного из ваших листов есть ссылки на другие листы, то эти ссылки будут сломаны в экспортированном HTML. Чтобы решить эту проблему, Aspose.Cells предоставляет интерфейс [IFilePathProvider](https://reference.aspose.com/cells/java/com.aspose.cells/IFilePathProvider), который вы можете реализовать, чтобы исправить сломанные ссылки.
## **Предоставьте путь к экспортированному файлу HTML рабочего листа через интерфейс IFilePathProvider**
Пожалуйста, загрузите [образец файла Excel](5473417.zip), используемый в следующем коде, и его экспортированные файлы HTML. Все эти файлы находятся в каталоге *Temp*. Распакуйте их на диск *C:*. Тогда это станет каталогом *C:\Temp*. Затем откройте файл *Sheet1.html* в браузере и щелкните по двум ссылкам внутри него. Эти ссылки относятся к двум экспортированным HTML-листам, которые находятся в каталоге *C:\Temp\OtherSheets*.

{{< highlight java >}}

 file:///C:/Temp/OtherSheets/Sheet2.html#RANGE!A1

file:///C:/Temp/OtherSheets/Sheet3.html#RANGE!A1

{{< /highlight >}}

На следующем снимке экрана показано, как выглядят *C:\Temp\Sheet1.html* и его ссылки

![todo:image_alt_text](provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface_1.png)

На следующем снимке экрана показан исходный код HTML. Как видите, ссылки теперь указывают на каталог *C:\Temp\OtherSheets*. Это было достигнуто с использованием интерфейса [IFilePathProvider](https://reference.aspose.com/cells/java/com.aspose.cells/IFilePathProvider).

![todo:image_alt_text](provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface_2.png)
## **Образец кода**
Обратите внимание, что каталог *C:\Temp* предназначен только для иллюстраций. Вы можете использовать любой каталог на ваше усмотрение и поместить [образец файла Excel](5473414.xlsx) внутри него и выполнить предоставленный образец кода. Затем создайте подкаталог *OtherSheets* внутри вашего каталога и экспортируйте HTML второго и третьего листов внутри него. Пожалуйста, измените переменную *dirPath* в предоставленном коде и укажите его в каталог вашего выбора перед выполнением.

{{% alert color="primary" %}} 

Пример кода будет работать только в том случае, если вы установите лицензию Aspose.Cells. Если вы попытаетесь запустить код без установки лицензии, он зайдет в бесконечный цикл. Поэтому мы добавили проверку для вывода сообщения и остановки выполнения, если лицензия не установлена. Вы можете либо приобрести лицензию, либо запросить временную лицензию на 30 дней у команды Aspose.Purchase.

{{% /alert %}} 

Пожалуйста, убедитесь, что закомментирование этих строк в коде приведет к разрыву ссылок в *Sheet1.html* и *Sheet2.html* или *Sheet3.html* не будет открываться при щелчке на их ссылки внутри *Sheet1.html*



{{< highlight java >}}

 //If you will comment this line, then hyperlinks will be broken

options.setFilePathProvider(new FilePathProvider());

{{< /highlight >}}



Вот полный пример кода, который вы можете выполнить с предоставленным [образцом файла Excel](5473414.xlsx).



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-files-handling-OpeningFilesThroughPath-1.java" >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-FilePathProvider-FilePathProvider.java" >}}
{{< app/cells/assistant language="java" >}}
