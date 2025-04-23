---
title: Расширение текста справа налево при экспорте файла Excel в HTML
type: docs
weight: 60
url: /ru/net/expanding-text-from-right-to-left-while-exporting-excel-file-to/
---

{{% alert color="primary" %}} 

Теперь Aspose.Cells поддерживает расширение текста справа налево при экспорте файла Excel в HTML. Эта функция была реализована с версии v8.9.0.0. Теперь, если ваш исходный файл Excel содержит текст, который расширяется справа налево, то Aspose.Cells экспортирует его в HTML правильно.

{{% /alert %}} 
## **Развертывание текста справа налево при экспорте файла Excel в HTML**
Следующий пример кода конвертирует [образец файла Excel](5115502.xlsx) в HTML. На этом скриншоте показано, как выглядит образец Excel в Microsoft Excel 2013.

![todo:image_alt_text](expanding-text-from-right-to-left-while-exporting-excel-file-to-html_1.png)

Этот скриншот показывает [выходной HTML, сгенерированный с помощью более старой версии](5115509).

![todo:image_alt_text](expanding-text-from-right-to-left-while-exporting-excel-file-to-html_2.png)

Этот скриншот показывает [выходной HTML, сгенерированный с помощью новой версии](5115508).

![todo:image_alt_text](expanding-text-from-right-to-left-while-exporting-excel-file-to-html_3.png)

Как видно на снимках экрана, новая версия корректно разворачивает правосторонний текст влево, как и Microsoft Excel.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithHTMLFormat-ExpandTextFromRightToLeft-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
