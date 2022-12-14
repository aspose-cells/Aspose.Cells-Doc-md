---
title: Добавить цифровую подпись к уже подписанному файлу Excel
type: docs
weight: 20
url: /ru/net/add-digital-signature-to-an-already-signed-excel-file/
---
## **Возможные сценарии использования**

 Aspose.Cells обеспечивает[**Workbook.AddDigitalSignature(DigitalSignatureCollection digitalSignatureCollection)**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/adddigitalsignature)метод, который можно использовать для добавления цифровой подписи к уже подписанному файлу Excel.

{{% alert color="primary" %}}

Обратите внимание, что при добавлении цифровой подписи к уже подписанному документу Excel, если исходный документ является сгенерированным документом Aspose.Cells, он работает хорошо. Но если исходный документ создан другими механизмами (например, Microsoft Excel и т. д.), Aspose.Cells не сможет сохранить файл таким же после его загрузки и повторного сохранения, это сделает исходную подпись недействительной.

{{% /alert %}}

## **Добавить цифровую подпись к уже подписанному файлу Excel**

В следующем примере кода показано, как использовать[**Workbook.AddDigitalSignature(DigitalSignatureCollection digitalSignatureCollection)**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/adddigitalsignature) метод добавления цифровой подписи к уже подписанному файлу Excel. Пожалуйста, проверьте[образец файла Excel](50528280.xlsx) используется в этом коде. Этот файл уже имеет цифровую подпись. Пожалуйста, проверьте[выходной файл Excel](50528281.xlsx) генерируется кодом. Мы использовали демонстрационный сертификат с именем[AsposeДемо.pfx](50528279.pfx) в этом коде, у которого есть пароль**предполагать**На снимке экрана показано влияние примера кода на образец файла Excel после выполнения.

![дело:изображение_альтернативный_текст](add-digital-signature-to-an-already-signed-excel-file_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-AddDigitalSignatureToAnAlreadySignedExcelFile.cs" >}}
