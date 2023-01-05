---
title: Назначить макрос элементу управления формой
type: docs
weight: 60
url: /ru/net/assign-macro-to-form-control/
---
{{% alert color="primary" %}}

 Aspose.Cells позволяет назначить код макроса элементу управления формы, например кнопке. Пожалуйста, используйте[**Форма.MarcoName**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/macroname) свойство, чтобы назначить новый код макроса элементу управления формы внутри рабочей книги.

{{% /alert %}}

Следующий пример кода создает новую книгу, назначает код макроса кнопке формы и сохраняет выходные данные в формате XLSM. После того, как вы откроете выходной файл XLSM в Microsoft Excel, вы увидите следующий код макроса.

{{< highlight "java" >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

## **Назначьте макрос для управления формой в C#**

Вот пример кода для создания выходного файла XLSM с кодом макроса.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingVBAModules-AssignMacroToFormControl-1.cs" >}}
