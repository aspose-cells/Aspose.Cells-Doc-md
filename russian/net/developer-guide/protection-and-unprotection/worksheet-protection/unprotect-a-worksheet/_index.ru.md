---
title: Снять защиту листа
type: docs
weight: 20
url: /ru/net/unprotect-a-worksheet/
---
{{% alert color="primary" %}}

Если разработчику необходимо снять защиту с защищенного рабочего листа во время выполнения, чтобы можно было внести некоторые изменения в файл? Это легко сделать по номеру Aspose.Cells.

{{% /alert %}}

## **Снять защиту листа**

### **Использование Microsoft Excel**

Чтобы снять защиту с листа:

 От**Инструменты** меню, выберите**Защита** с последующим**Снять защиту с листа**. Защита будет снята, если рабочий лист не защищен паролем. В этом случае диалоговое окно запрашивает пароль. Введите пароль, и рабочий лист будет незащищен.

### **Снятие защиты с простого защищенного листа с помощью Aspose.Cells**

 Рабочий лист можно снять с защиты, вызвав метод[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) учебный класс'[**Снять защиту**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/unprotect/index)метод.
 Просто защищенный лист — это лист, не защищенный паролем. Такие рабочие листы можно снять с защиты, вызвав метод[**Снять защиту**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/unprotect/index)метод без передачи параметра.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Unprotect-UnprotectingSimplyProtectedWorksheet-1.cs" >}}

### **Снятие защиты с рабочего листа, защищенного паролем, с помощью Aspose.Cells**

Рабочий лист, защищенный паролем, — это лист, защищенный паролем. Такие рабочие листы можно снять с защиты, вызвав перегруженную версию[**Снять защиту**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/unprotect/methods/1)метод, который принимает пароль в качестве параметра.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Unprotect-UnprotectingPasswordProtectedWorksheet-1.cs" >}}
