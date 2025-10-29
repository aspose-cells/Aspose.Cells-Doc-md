---
title: Назначение макроса управлению формой с Golang через C++
linktitle: Назначить макрос на элемент управления формы
type: docs
weight: 60
url: /ru/go-cpp/assign-macro-to-form-control/
description: Узнайте, как назначить код макроса на элемент управления формы, такой как кнопка, используя Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Aspose.Cells позволяет назначить код макроса элементу управления формы, такому как кнопка. Используйте свойство [**Shape.GetMacroName()**](https://reference.aspose.com/cells/go-cpp/shape/getmacroname/), чтобы назначить новый код макроса элементу управления формы внутри книги.

{{% /alert %}}

Следующий пример создает новую рабочую книгу, назначает код макроса на кнопку формы и сохраняет результат в формате XLSM. После открытия файла XLSM в Microsoft Excel вы увидите следующий код макроса.

{{< highlight java >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

## **Назначение макроса элементу управления формы с помощью C++**

Вот пример кода для создания вывода в формате XLSM с кодом макроса.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AssignMacroToFormControl.go" >}}
