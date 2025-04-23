---
title: Снять защиту листа
type: docs
weight: 20
url: /ru/python-net/unprotect-a-worksheet/
---

{{% alert color="primary" %}}

Если разработчик хочет снять защиту с защищенного листа во время выполнения, чтобы внести изменения в файл? Это легко реализуемо с API Aspose.Cells для Python via .NET.

{{% /alert %}}

## **Снятие защиты с листа**

### **Использование Microsoft Excel**

Для снятия защиты с листа:

Из меню **Инструменты** выберите **Защиту**, а затем **Снять защиту листа**. Защита будет снята, если только лист защищен паролем. В этом случае появится диалоговое окно для ввода пароля. Введите пароль, и лист будет разблокирован.

### **Снятие защиты с простого защищенного листа с помощью Aspose.Cells для Python via .NET**

Лист можно разблокировать, вызвав метод [**unprotect**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/unprotect) класса [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet).
Просто защищенный лист - это лист, который не защищен паролем. Такие листы можно разблокировать, вызвав метод [**unprotect**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/unprotect) без передачи параметра.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-UnprotectingSimplyProtectedWorksheet-1.py" >}}

### **Снятие защиты с пароленного листа с помощью Aspose.Cells для Python via .NET**

Защищенный паролем лист - это лист, защищенный паролем. Такие листы можно разблокировать, вызвав перегруженную версию метода [**unprotect**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/unprotect/), принимающую пароль в качестве параметра.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-UnprotectingPasswordProtectedWorksheet-1.py" >}}

