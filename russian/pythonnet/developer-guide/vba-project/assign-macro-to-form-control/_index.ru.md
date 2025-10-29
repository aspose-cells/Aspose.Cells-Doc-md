---
title: Назначить макрос на элемент управления формы
type: docs
weight: 60
url: /ru/python-net/assign-macro-to-form-control/
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET позволяет присвоить макрос-код элементу управления формы, например кнопке. Используйте свойство [**Shape.macro_name**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/macro_name) для назначения нового макроса внутри рабочей книги.

{{% /alert %}}

В следующем примере кода создается новая книга, назначается код макроса элементу управления формы и сохраняется вывод в формате XLSM. После открытия файла XLSM в Microsoft Excel вы увидите следующий код макроса.

{{< highlight java >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

## **Назначение макроса элементу формы на Python**

Вот пример кода для создания вывода в формате XLSM с кодом макроса.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "VBAProject-AssignMacroToFormControl-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
