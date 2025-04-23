---  
title: Подписывание и проверка цифровых подписей с помощью Node.js через C++  
linktitle: Подпись  
type: docs  
weight: 140  
url: /ru/nodejs-cpp/assign-and-validate-digital-signatures/  
description: Цифровая подпись файла Excel и её проверка с использованием Aspose.Cells for Node.js via C++. Защитите подлинность содержимого книги с помощью цифровых подписей.  
keywords: Цифровая подпись файла Excel, добавление цифровой подписи для Excel Node.js через C++, как проверить цифровую подпись Node.js через C++  
---  

{{% alert color="primary" %}}  
Цифровая подпись обеспечивает уверенность в том, что файл рабочей книги является действительным и никто его не изменял. Вы можете создать личную цифровую подпись, используя **Microsoft Selfcert.exe** или любой другой инструмент, или приобрести цифровую подпись. После создания цифровой подписи ее необходимо прикрепить к вашей рабочей книге. Прикрепление цифровой подписи аналогично запечатыванию конверта. Если приходит запечатанный конверт, у вас есть уверенность, что никто не затрагивал его содержимое.  
{{% /alert %}}  

## **Введение**  

Используйте диалоговое окно цифровой подписи для прикрепления цифровой подписи. Диалоговое окно цифровой подписи перечисляет действительные сертификаты. Вы можете использовать диалоговое окно цифровой подписи для просмотра сертификатов и выбора нужного. Если у рабочей книги есть цифровая подпись, имя подписи отображается в поле **Имя сертификата**. Если вы щелкнете кнопку **Удалить** в диалоговом окне цифровой подписи, Microsoft Excel также удалит цифровую подпись.  

## **Как добавить цифровую подпись в Excel**  

Aspose.Cells предоставляет модуль [**DigitalSignature**](https://reference.aspose.com/cells/nodejs-cpp/digitalsignature/) для выполнения задачи (подписывать и проверять цифровые подписи). Модуль обладает полезными функциями для добавления и проверки цифровых подписей.  

Пожалуйста, посмотрите следующий пример кода, который показывает, как выполнить задачу с помощью API Aspose.Cells for Node.js via C++.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const certPassword = "aa";

// dsc is signature collection that contains one or more signatures needed to sign
const dsc = new AsposeCells.DigitalSignatureCollection();

// Cert must contain a private key, it can be constructed from a cert file or Windows certificate collection.
const cert = new AsposeCells.DigitalSignature(dataDir + "mykey2.pfx", certPassword, "test for sign", new Date());
dsc.add(cert);

const wb = new AsposeCells.Workbook();

// wb.setDigitalSignature signs all signatures in dsc
wb.setDigitalSignature(dsc);
wb.save(path.join(dataDir, "newfile_out.xlsx"));

// open the file
const wb2 = new AsposeCells.Workbook(path.join(dataDir, "newfile_out.xlsx"));
console.log(wb2.isDigitallySigned);

// Get digitalSignature collection from workbook
const dsc2 = wb2.getDigitalSignature();
const digitalSignatures = dsc2.getEnumerator();
for (var dst of digitalSignatures)
{
    console.log(dst.getComments()); // test for sign - OK
    console.log(dst.getSignTime()); // 11/25/2010 1:22:01 PM - OK
    console.log(dst.isValid()); // True - OK
}

```  

## **Продвинутые темы**  
- [Добавить цифровую подпись к уже подписанному файлу Excel](/cells/ru/nodejs-cpp/add-digital-signature-to-an-already-signed-excel-file/)  
- [Добавить строку подписи на лист](/cells/ru/nodejs-cpp/add-signature-line/)  
- [Поддержка XAdES Signature](/cells/ru/nodejs-cpp/support-for-xades-signature/)  

