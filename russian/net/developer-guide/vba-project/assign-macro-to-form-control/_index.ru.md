---
title: Назначить макрос на элемент управления формы
type: docs
weight: 60
url: /ru/net/assign-macro-to-form-control/
---

{{% alert color="primary" %}}

Aspose.Cells позволяет назначить код макроса элементу управления формы, такому как кнопка. Используйте свойство [**Shape.MarcoName**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/macroname), чтобы назначить новый код макроса элементу управления формы внутри книги.

{{% /alert %}}

В следующем примере кода создается новая книга, назначается код макроса элементу управления формы и сохраняется вывод в формате XLSM. После открытия файла XLSM в Microsoft Excel вы увидите следующий код макроса.

{{< highlight java >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

## **Назначить макрос на элемент управления формы на C#**

Вот пример кода для создания вывода в формате XLSM с кодом макроса.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingVBAModules-AssignMacroToFormControl-1.cs" >}}
