---
title: Подтвердите пароль, используемый для защиты рабочего листа
type: docs
weight: 370
url: /ru/net/verify-password-used-to-protect-the-worksheet/
---
{{% alert color="primary" %}}

 Aspose.Cells API расширили возможности[**Защита**](https://reference.aspose.com/cells/net/aspose.cells/protection) класс, введя некоторые полезные свойства и методы. Одним из таких методов является[**Подтвердите пароль**](https://reference.aspose.com/cells/net/aspose.cells/protection/methods/verifypassword) который позволяет указать пароль как экземпляр*нить* и проверяет, использовался ли тот же пароль для защиты[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet).

{{% /alert %}}

[**Защита.VerifyPassword**](https://reference.aspose.com/cells/net/aspose.cells/protection/methods/verifypassword) метод возвращает**истинный**если указанный пароль совпадает с паролем, используемым для защиты данного рабочего листа и**ЛОЖЬ** если указанный пароль не совпадает. Следующий фрагмент кода использует[**Защита.VerifyPassword**](https://reference.aspose.com/cells/net/aspose.cells/protection/methods/verifypassword) метод в сочетании с[**Protection.IsProtectedWithPassword**](https://reference.aspose.com/cells/net/aspose.cells/protection/properties/isprotectedwithpassword)свойство для обнаружения защиты паролем и проверяет пароль.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-VerifyPasswordUsedToProtectWorksheets-VerifyPasswordUsedToProtectWorksheets.cs" >}}
