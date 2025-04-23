---
title: Определение успешной загрузки лицензии
type: docs
weight: 260
url: /ru/net/determining-if-the-license-is-loaded-successfully/
description: Узнайте, как определить успешную загрузку лицензии через API Aspose.Cells for NET.
keywords: Как определить успешную загрузку лицензии в C#, Определение успешной загрузки лицензии с помощью C#, Проверка успешной загрузки лицензии через C#, проверка статуса лицензии.
---

{{% alert color="primary" %}}

Aspose.Cells предоставляет свойство [**Workbook.IsLicensed**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/islicensed), которое можно использовать для определения успешной загрузки лицензии. Если вы обратитесь к этому свойству до установки лицензии, оно вернет **false**, а если вы вызовете это свойство после установки лицензии, оно вернет **true**, что указывает на успешную загрузку лицензии.

{{% /alert %}}

## Код на C#, чтобы определить успешную загрузку лицензии

Следующий код обращается к свойству [**Workbook.IsLicensed**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/islicensed) до установки лицензии и возвращает **false**. Затем он загружает лицензию, снова обращается к свойству, которое теперь возвращает **true**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-DeterminingLicenseLoading-DeterminingLicenseLoading.cs" >}}

## **Вывод в консоль**

Вот отладочный вывод примерного кода

{{< highlight java >}}

False

True

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
