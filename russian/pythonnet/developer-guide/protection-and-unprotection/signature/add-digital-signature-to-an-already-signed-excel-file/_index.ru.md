---
title: Добавить цифровую подпись к уже подписанному файлу Excel
type: docs
weight: 20
url: /ru/python-net/add-digital-signature-to-an-already-signed-excel-file/
description: В этой статье описано, как добавить цифровую подпись к уже подписанному файлу Excel с помощью кода на C# и Aspose.Cells для Python via .NET.
keywords: Добавить цифровую подпись к уже подписанному файлу Excel, Как добавить цифровую подпись к уже подписанному документу Excel
---

## **Возможные сценарии использования**

Aspose.Cells для Python via .NET предоставляет метод [**Workbook.add_digital_signature**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/add_digital_signature), который можно использовать для добавления цифровой подписи к уже подписанному файлу Excel.

{{% alert color="primary" %}}

Обратите внимание, что при добавлении цифровой подписи к уже подписанному файлу Excel, если исходный документ был создан с помощью Aspose.Cells для Python via .NET, все работает хорошо. Но если исходный документ создан другими движками (например, Microsoft Excel и др.), Aspose.Cells для Python via .NET не сможет сохранить файл без изменений после загрузки и повторного сохранения, что сделает оригинальную подпись недействительной.

{{% /alert %}}

## **Как добавить цифровую подпись к уже подписанному файлу Excel**

Приведенный ниже образец кода демонстрирует способ использования метода [**Workbook.add_digital_signature**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/add_digital_signature) для добавления цифровой подписи к уже подписанному файлу Excel. Пожалуйста, проверьте [образец файла Excel](50528280.xlsx), используемый в этом коде. Этот файл уже имеет цифровую подпись. Пожалуйста, проверьте [выходной файл Excel](50528281.xlsx), сгенерированный кодом. В этом коде мы использовали демонстрационный сертификат с именем [AsposeDemo.pfx](50528279.pfx), у которого пароль **aspose**. Снимок экрана показывает эффект образца кода на образец файла Excel после выполнения.

![todo:image_alt_text](add-digital-signature-to-an-already-signed-excel-file_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-AddDigitalSignatureToAnAlreadySignedExcelFile.py" >}}

