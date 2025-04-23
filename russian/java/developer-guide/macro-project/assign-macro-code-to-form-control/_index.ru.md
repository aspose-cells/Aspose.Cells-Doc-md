---
title: Назначить макросный код для элемента управления формой
type: docs
weight: 400
url: /ru/java/assign-macro-code-to-form-control/
---

{{% alert color="primary" %}} 

Aspose.Cells позволяет назначать макросы на элементы управления формы, такие как кнопки. Используйте [ShapeCollection.addShape()](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addShape-int-int-int-int-int-int-int-) для назначения нового макроса внутри рабочей книги.

{{% /alert %}} 
## **Назначение кода макроса элементу управления формой с использованием Aspose.Cells**
В следующем образце кода создается новая книга, назначается код макроса элементу управления формы и сохраняется результат в формате XLSM. После открытия выходного файла XLSM в Microsoft Excel вы увидите следующий код макроса.

{{< highlight java >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

Вот образец кода для создания выходного файла XLSM с кодом макроса.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AssignMacroToFormControl-AssignMacroToFormControl.java" >}}
{{< app/cells/assistant language="java" >}}
