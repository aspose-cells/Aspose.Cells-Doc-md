---
title: حفظ الملفات
type: docs
weight: 20
url: /ar/go-cpp/saving-files/
---

{{% alert color="primary" %}}

تمكّن Aspose.Cells من إنشاء وحفظ الملفات والتلاعب بالملفات الموجودة. يوضح هذا المقال الطرق المختلفة التي يمكن من خلالها حفظ الملفات.

{{% /alert %}}

## **طرق مختلفة لحفظ الملفات**

يقدم Aspose.Cells فئة [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/)， والتي تمثل ملف Excel وتوفر الطرق اللازمة للعمل مع ملفات Excel. توفر فئة [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) طريقة [Save](https://reference.aspose.com/cells/go-cpp/workbook/save/) لحفظ ملفات Excel. تحتوي طريقة [Save](https://reference.aspose.com/cells/go-cpp/workbook/save/) على العديد من التحميلات الزائدة التي تُستخدم لحفظ الملفات بطرق مختلفة. يحدد تنسيق الملف الذي يُحفظ فيه الملف بواسطة تعداد [SaveFormat](https://reference.aspose.com/cells/go-cpp/saveformat/).

## **حفظ ملف في موقع معين**

لحفظ الملفات إلى موقع تخزين، حدد اسم الملف (مع مسار التخزين كاملًا) والتنسيق المطلوب للملف (من تعداد [SaveFormat](https://reference.aspose.com/cells/go-cpp/saveformat/)) عند استدعاء طريقة [Save](https://reference.aspose.com/cells/go-cpp/workbook/save_string/)، لفئة [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SavingFileToSomeLocation.go" >}}

## **حفظ الملف في تدفق**

لحفظ الملفات إلى تيار، أنشئ كائن MemoryStream أو FileStream واحفظ الملف إلى ذلك الكائن من خلال استدعاء طريقة [Save](https://reference.aspose.com/cells/go-cpp/workbook/save_saveFormat/) لكائن [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/). حدد تنسيق الملف المطلوب باستخدام تعداد [SaveFormat](https://reference.aspose.com/cells/go-cpp/saveformat/) عند استدعاء طريقة [Save](https://reference.aspose.com/cells/go-cpp/workbook/save_saveFormat/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SavingFileToStream.go" >}}

## **حفظ الملف إلى صيغة PDF**

لحفظ المحتوى المطلوب كملف PDF باستخدام مكتبة Aspose.Cells for Go via C++، أنشئ كائن [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) جديد أو أنشئه من خلال قراءة ملف Excel موجود، ثم استخدم طريقة [save](https://reference.aspose.com/cells/go-cpp/workbook/save_string_saveOptions/) لحفظ الملف كملف PDF. عند استدعاء طريقة save، استخدم تعداد [SaveFormat](https://reference.aspose.com/cells/go-cpp/saveformat/) لتحديد تنسيق الملف المطلوب.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SavingFileToPdf.go" >}}
