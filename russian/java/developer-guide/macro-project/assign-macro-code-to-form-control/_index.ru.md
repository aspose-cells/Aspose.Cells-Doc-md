---
title: Назначение кода макроса элементу управления формой
type: docs
weight: 400
url: /ru/java/assign-macro-code-to-form-control/
---
{{% alert color="primary" %}} 

 Aspose.Cells позволяет назначить код макроса элементу управления формы, например кнопке. Пожалуйста, используйте[ShapeCollection.addShape()](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addShape\(int,%20int,%20int,%20int,%20int,%20int,%20int\)) для назначения нового кода макроса элементу управления формы внутри рабочей книги.

{{% /alert %}} 
## **Назначение кода макроса для управления формой с использованием Aspose.Cells**
Следующий пример кода создает новую книгу, назначает код макроса кнопке формы и сохраняет выходные данные в формате XLSM. После того, как вы откроете выходной файл XLSM в Microsoft Excel, вы увидите следующий код макроса.

{{< highlight "java" >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

Вот пример кода для создания выходного файла XLSM с кодом макроса.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AssignMacroToFormControl-AssignMacroToFormControl.java" >}}
