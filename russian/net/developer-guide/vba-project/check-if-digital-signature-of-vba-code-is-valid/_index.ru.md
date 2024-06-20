---
title: Проверить, действителен ли цифровой подпись кода VBA
type: docs
weight: 120
url: /ru/net/check-if-digital-signature-of-vba-code-is-valid/
---

{{% alert color="primary" %}}

Aspose.Cells позволяет проверить, действительна ли цифровая подпись кода VBA с помощью свойства [**Workbook.VbaProject.IsValidSigned**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbaproject/properties/isvalidsigned). Он вернет **true**, если подпись действительна, в противном случае он вернет **false**. Цифровая подпись кода VBA становится недействительной, когда вы изменяете код VBA.

{{% /alert %}}

## **Проверить, действителен ли цифровая подпись кода VBA на C#**

Следующий код демонстрирует использование этого свойства с [образцовым файлом Excel](5115030.xlsm), который вы можете загрузить по предоставленной ссылке. В этом же файле Excel имеется действительная подпись, но после изменения его кода VBA, сохранения книги и повторной проверки мы обнаружим, что его подпись стала недействительной.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingVBAModules-CheckVbaSignatureIsValid-CheckVbaSignatureIsValid.cs" >}}
