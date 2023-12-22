---
title: Определение успешности загрузки лицензии
type: docs
weight: 260
url: /ru/net/determining-if-the-license-is-loaded-successfully/
description: Узнайте, как определить, успешно ли загружена лицензия, с помощью API Aspose.Cells для NET.
keywords: How to Detect if the License is loaded successfully in C#, Determine if the License is loaded successfully using C#, Check if the License is loaded successfully via C#, check the status of license.
---
{{% alert color="primary" %}}

 Aspose.Cells обеспечивает[**Рабочая книга.IsLicensed**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/islicensed) свойство, которое вы можете использовать, чтобы определить, успешно ли загружена лицензия. Если вы получите доступ к этому свойству до установки лицензии, оно вернется**ЛОЖЬ** и если вы вызовете это свойство после установки лицензии, оно вернется**истинный** указывая, что лицензия успешно загружена.

{{% /alert %}}

##  Код C#, чтобы определить, успешно ли загружена лицензия.

 Следующий код обращается к[**Рабочая книга.IsLicensed**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/islicensed)перед установкой лицензии и возвращает *false**. Затем он загружает лицензию и снова обращается к свойству, которое теперь возвращает *true**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-DeterminingLicenseLoading-DeterminingLicenseLoading.cs" >}}

##  **Консольный вывод**

Вот консольный (отладочный) вывод приведенного выше примера кода.

{{< highlight "java" >}}

False

True

{{< /highlight >}}
