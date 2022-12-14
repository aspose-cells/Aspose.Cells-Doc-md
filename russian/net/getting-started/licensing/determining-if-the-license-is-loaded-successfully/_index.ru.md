---
title: Определение того, успешно ли загружена лицензия
type: docs
weight: 260
url: /ru/net/determining-if-the-license-is-loaded-successfully/
---
{{% alert color="primary" %}}

 Aspose.Cells предоставляет[**Workbook.IsLicensed**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/islicensed) свойство, которое вы можете использовать, чтобы определить, успешно ли загружена лицензия или нет. Если вы получите доступ к этому свойству до установки лицензии, оно вернет**ЛОЖЬ**и если вы вызовете это свойство после установки лицензии, оно вернет**истинный** указывает на то, что лицензия была успешно загружена.

{{% /alert %}}

## Код C#, чтобы определить, успешно ли загружена лицензия

 Следующий код обращается к[**Workbook.IsLicensed**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/islicensed) свойство перед установкой лицензии, и оно возвращает**ЛОЖЬ** . Затем он загружает лицензию и снова обращается к свойству, которое теперь возвращает**истинный**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-DeterminingLicenseLoading-DeterminingLicenseLoading.cs" >}}

## **Консольный вывод**

Вот консольный (отладочный) вывод приведенного выше примера кода.

{{< highlight "java" >}}

False

True

{{< /highlight >}}
