---
title: Предоставьте путь к экспортированному файлу HTML листа через интерфейс IFilePathProvider
type: docs
weight: 70
url: /ru/net/provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface/
---

## **Возможные сценарии использования**
Предположим, у вас есть файл Excel с несколькими листами, и вы хотите экспортировать каждый лист в отдельный файл HTML. Если у ваших листов есть ссылки на другие листы, то эти ссылки будут нарушены в экспортированном HTML. Для решения этой проблемы Aspose.Cells предоставляет интерфейс [IFilePathProvider](https://reference.aspose.com/cells/net/aspose.cells/ifilepathprovider), который вы можете реализовать, чтобы исправить нарушенные ссылки.
## **Предоставьте путь к экспортированному файлу HTML рабочего листа через интерфейс IFilePathProvider**
Пожалуйста, скачайте [образец файла Excel](5115213.zip), использованный в следующем коде, и его экспортированные HTML-файлы. Все эти файлы находятся в каталоге Temp. Вам следует извлечь их на диск C:. Тогда это станет каталогом C:\Temp. Затем вы откроете файл Sheet1.html в браузере и кликнете по двум ссылкам внутри него. Эти ссылки относятся к этим двум экспортированным HTML-листам, которые находятся в каталоге C:\Temp\OtherSheets.

{{< highlight java >}}

 file:///C:/Temp/OtherSheets/Sheet2.html#RANGE!A1

file:///C:/Temp/OtherSheets/Sheet3.html#RANGE!A1

{{< /highlight >}}

Ниже показано, как выглядят C:\Temp\Sheet1.html и его ссылки

![todo:image_alt_text](provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface_1.png)

Ниже показан исходный код HTML. Как видите, теперь ссылки указывают на каталог C:\Temp\OtherSheets. Это было достигнуто с помощью интерфейса [IFilePathProvider](https://reference.aspose.com/cells/net/aspose.cells/ifilepathprovider)

![todo:image_alt_text](provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface_2.png)
## **Образец кода**
Обратите внимание, что каталог C:\Temp приведён только в иллюстративных целях. Вы можете использовать любой каталог на ваше усмотрение, поместив внутрь его [образец файла Excel](5115211.xlsx) и выполнить предоставленный образец кода. Затем он создаст подкаталог OtherSheets в вашем каталоге и экспортирует HTML второго и третьего листов внутрь него. Перед выполнением измените переменную dirPath в предоставленном коде и укажите на ваш выбранный каталог.

{{% alert color="primary" %}} 

Пример кода будет работать только в том случае, если вы установите лицензию Aspose.Cells. Если вы попытаетесь запустить код без установки лицензии, он зайдет в бесконечный цикл. Поэтому мы добавили проверку для вывода сообщения и остановки выполнения, если лицензия не установлена. Вы можете либо приобрести лицензию, либо запросить временную лицензию на 30 дней у команды Aspose.Purchase.

{{% /alert %}} 

Пожалуйста, обратите внимание, что комментирование этих строк внутри кода нарушит ссылки в Sheet1.html, и Sheet2.html или Sheet3.html не откроются, когда их ссылки будут кликнуты внутри Sheet1.html



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithHTMLFormat-ExportedWorkSheetViaIFilePathProvider-hyperlinks.cs" >}}



Вот полный образец кода, который можно выполнить с предоставленным [образцом файла Excel](5115211.xlsx).



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithHTMLFormat-ExportedWorkSheetViaIFilePathProvider-ExportedWorkSheetViaIFilePathProvider.cs" >}}
{{< app/cells/assistant language="csharp" >}}
