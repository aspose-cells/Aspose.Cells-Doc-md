---
title: Добавить цифровую подпись к уже подписанному файлу Excel
type: docs
weight: 20
url: /ru/net/add-digital-signature-to-an-already-signed-excel-file/
description: В этой статье описано, как добавить цифровую подпись к уже подписанному файлу Excel с использованием кодов C# с помощью Aspose.Cells для .Net.
keywords: Добавить цифровую подпись к уже подписанному файлу Excel, Как добавить цифровую подпись к уже подписанному документу Excel
---

## **Возможные сценарии использования**

Aspose.Cells предоставляет метод [**Workbook.AddDigitalSignature(DigitalSignatureCollection digitalSignatureCollection)**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/adddigitalsignature), который вы можете использовать для добавления цифровой подписи к уже подписанному файлу Excel.

{{% alert color="primary" %}}

Пожалуйста, обратите внимание, что при добавлении цифровой подписи к уже подписанному документу Excel, если исходный документ сгенерирован Aspose.Cells, все работает хорошо. Но если исходный документ сгенерирован другими движками (например, Microsoft Excel и т. д.), Aspose.Cells не сможет сохранить файл таким же после загрузки и повторного сохранения, что сделает исходную подпись недействительной.

{{% /alert %}}

## **Как добавить цифровую подпись к уже подписанному файлу Excel**

Приведенный ниже образец кода демонстрирует способ использования метода [**Workbook.AddDigitalSignature(DigitalSignatureCollection digitalSignatureCollection)**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/adddigitalsignature) для добавления цифровой подписи к уже подписанному файлу Excel. Пожалуйста, проверьте [образец файла Excel](50528280.xlsx), используемый в этом коде. Этот файл уже имеет цифровую подпись. Пожалуйста, проверьте [выходной файл Excel](50528281.xlsx), сгенерированный кодом. В этом коде мы использовали демонстрационный сертификат с именем [AsposeDemo.pfx](50528279.pfx), у которого пароль **aspose**. Снимок экрана показывает эффект образца кода на образец файла Excel после выполнения.

![todo:image_alt_text](add-digital-signature-to-an-already-signed-excel-file_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-AddDigitalSignatureToAnAlreadySignedExcelFile.cs" >}}
