---
title: Добавить цифровую подпись к уже подписанному файлу Excel
type: docs
weight: 20
url: /ru/java/add-digital-signature-to-an-already-signed-excel-file/
---

## **Возможные сценарии использования**

Aspose.Cells предоставляет метод [**Workbook.addDigitalSignature(DigitalSignatureCollection digitalSignatureCollection)**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#addDigitalSignature(com.aspose.cells.DigitalSignatureCollection)), который можно использовать для добавления цифровой подписи к уже подписанному файлу Excel.

{{% alert color="primary" %}}

Пожалуйста, обратите внимание, что при добавлении цифровой подписи к уже подписанному документу Excel, если исходный документ сгенерирован Aspose.Cells, все работает хорошо. Но если исходный документ сгенерирован другими движками (например, Microsoft Excel и т. д.), Aspose.Cells не сможет сохранить файл таким же после загрузки и повторного сохранения, что сделает исходную подпись недействительной.

{{% /alert %}}

## **Добавить цифровую подпись к уже подписанному файлу Excel**

Приведенный ниже образец кода объясняет, как использовать метод [**Workbook.addDigitalSignature(DigitalSignatureCollection digitalSignatureCollection)**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#addDigitalSignature(com.aspose.cells.DigitalSignatureCollection)) для добавления цифровой подписи к уже подписанному файлу Excel. Пожалуйста, проверьте [образец Excel-файла](50528287.xlsx), используемый в этом коде. Этот файл уже цифрово подписан. Пожалуйста, проверьте [выходной Excel-файл](50528288.xlsx), сгенерированный кодом. В этом коде мы использовали демонстрационный сертификат с именем [AsposeTest.pfx](50528289.pfx), который имеет пароль *aspose*. Снимок экрана показывает эффект образца кода на образец Excel-файла после выполнения.

![todo:image_alt_text](add-digital-signature-to-an-already-signed-excel-file_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-AddDigitalSignatureToAnAlreadySignedExcelFile.java" >}}
