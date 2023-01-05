---
title: Проверьте, действительна ли цифровая подпись кода VBA
type: docs
weight: 120
url: /ru/net/check-if-digital-signature-of-vba-code-is-valid/
---
{{% alert color="primary" %}}

 Aspose.Cells позволяет проверить, действительна ли цифровая подпись кода VBA с помощью[**Workbook.VbaProject.IsValidSigned**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbaproject/properties/isvalidsigned) имущество. Он вернется**истинный** если подпись действительна, в противном случае она вернется**ЛОЖЬ**. Цифровая подпись кода VBA становится недействительной при изменении кода VBA.

{{% /alert %}}

## **Проверьте, действительна ли цифровая подпись кода VBA в C#.**

 Следующий код демонстрирует использование этого свойства с помощью[образец эксель файла](5115030.xlsm)который вы можете скачать по предоставленной ссылке. Тот же файл Excel имеет действительную подпись, но когда мы изменим его код VBA и сохраним книгу, а затем перепроверим, мы обнаружим, что ее подпись стала недействительной.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingVBAModules-CheckVbaSignatureIsValid-CheckVbaSignatureIsValid.cs" >}}
