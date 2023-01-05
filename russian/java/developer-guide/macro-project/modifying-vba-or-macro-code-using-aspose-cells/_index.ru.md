---
title: Изменение кода VBA или макроса с помощью Aspose.Cells
type: docs
weight: 90
url: /ru/java/modifying-vba-or-macro-code-using-aspose-cells/
---
{{% alert color="primary" %}} 

Вы можете изменить код VBA или макроса, используя Aspose.Cells. Aspose.Cells добавил следующие классы для чтения и изменения проекта VBA в файле Excel.

- VbaProject
- ВбаМодулеКоллекция
- VbaModule

Эта статья покажет вам, как изменить код VBA или макроса внутри исходного файла Excel, используя Aspose.Cells.

{{% /alert %}} 
## **Пример**
Следующий пример кода загружает исходный файл Excel, внутри которого находится следующий код VBA или макроса.

{{< highlight "java" >}}

 Sub Button1_Click()

MsgBox "This is test message."

End Sub

{{< /highlight >}}

После выполнения образца кода Aspose.Cells код VBA или макроса будет изменен следующим образом.

{{< highlight "java" >}}

 Sub Button1_Click()

MsgBox "This is Aspose.Cells message."

End Sub

{{< /highlight >}}

 Вы можете скачать[исходный файл Excel](5472596.xlsm) и[выходной файл Excel](5472597.xlsm) по указанным ссылкам.







{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ModifyVBAorMacroCode-ModifyVBAorMacroCode.java" >}}






