---
title: Изменение VBA или кода макроса с помощью Aspose.Cells
type: docs
weight: 90
url: /ru/java/modifying-vba-or-macro-code-using-aspose-cells/
---

{{% alert color="primary" %}} 

Вы можете изменять VBA или код макроса с помощью Aspose.Cells. Aspose.Cells добавил следующие классы для чтения и изменения проекта VBA в файле Excel

- VbaProject
- VbaModuleCollection
- VbaModule

Эта статья покажет вам, как изменить код VBA или макроса в исходном файле Excel с помощью Aspose.Cells.

{{% /alert %}} 
## **Пример**
Приведенный ниже образец кода загружает исходный файл Excel с встроенным VBA-кодом или макросом.

{{< highlight java >}}

 Sub Button1_Click()

MsgBox "This is test message."

End Sub

{{< /highlight >}}

После выполнения приведенного выше образца кода Aspose.Cells код VBA или макрос будет изменен таким образом.

{{< highlight java >}}

 Sub Button1_Click()

MsgBox "This is Aspose.Cells message."

End Sub

{{< /highlight >}}

Вы можете загрузить [исходный файл Excel](5472596.xlsm) и [выводной файл Excel](5472597.xlsm) по указанным ссылкам







{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ModifyVBAorMacroCode-ModifyVBAorMacroCode.java" >}}






{{< app/cells/assistant language="java" >}}
