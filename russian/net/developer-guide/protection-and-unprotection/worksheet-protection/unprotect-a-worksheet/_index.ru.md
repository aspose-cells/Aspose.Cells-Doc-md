---
title: Снять защиту листа
type: docs
weight: 20
url: /ru/net/unprotect-a-worksheet/
---

{{% alert color="primary" %}}

Если разработчику необходимо удалить защиту с защищенного листа во время выполнения, чтобы внести изменения в файл? Это легко можно сделать с помощью Aspose.Cells.

{{% /alert %}}

## **Снятие защиты с листа**

### **Использование Microsoft Excel**

Для снятия защиты с листа:

Из меню **Инструменты** выберите **Защиту**, а затем **Снять защиту листа**. Защита будет снята, если только лист защищен паролем. В этом случае появится диалоговое окно для ввода пароля. Введите пароль, и лист будет разблокирован.

### **Снятие защиты с просто защищенного листа с помощью Aspose.Cells**

Лист можно разблокировать, вызвав метод [**Unprotect**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/unprotect/index) класса [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet).
Просто защищенный лист - это лист, который не защищен паролем. Такие листы можно разблокировать, вызвав метод [**Unprotect**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/unprotect/index) без передачи параметра.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Unprotect-UnprotectingSimplyProtectedWorksheet-1.cs" >}}

### **Снятие защиты с защищенного паролем листа с помощью Aspose.Cells**

Защищенный паролем лист - это лист, защищенный паролем. Такие листы можно разблокировать, вызвав перегруженную версию метода [**Unprotect**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/unprotect/methods/1), принимающую пароль в качестве параметра.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Unprotect-UnprotectingPasswordProtectedWorksheet-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
