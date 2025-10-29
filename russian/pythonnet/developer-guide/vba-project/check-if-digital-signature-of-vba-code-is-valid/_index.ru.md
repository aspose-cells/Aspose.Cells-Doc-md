---
title: Проверить, действителен ли цифровой подпись кода VBA
type: docs
weight: 120
url: /ru/python-net/check-if-digital-signature-of-vba-code-is-valid/
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET позволяет проверить, действительна ли цифровая подпись VBA-кода, используя свойство [**Workbook.vba_project.is_valid_signed**](https://reference.aspose.com/cells/python-net/aspose.cells.vba/vbaproject/is_valid_signed). Он вернет **true**, если подпись действительна, иначе — **false**. Цифровая подпись VBA становится недействительной, если изменить VBA-код.

{{% /alert %}}

## **Проверка действительности цифровой подписи VBA-кода в Python**

Следующий код демонстрирует использование этого свойства с [образцовым файлом Excel](5115030.xlsm), который вы можете загрузить по предоставленной ссылке. В этом же файле Excel имеется действительная подпись, но после изменения его кода VBA, сохранения книги и повторной проверки мы обнаружим, что его подпись стала недействительной.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "VBAProject-CheckVbaSignatureIsValid.py" >}}

{{< app/cells/assistant language="python-net" >}}
