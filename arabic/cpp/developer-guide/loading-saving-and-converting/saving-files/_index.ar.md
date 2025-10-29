---
title: حفظ الملفات
type: docs
weight: 20
url: /ar/cpp/saving-files/
---

{{% alert color="primary" %}} 

يجعل Aspose.Cells من الممكن إنشاء وحفظ الملفات، وتعديل الملفات الحالية. يشرح هذا المقال الطرق المختلفة التي يمكن بها حفظ الملفات.

{{% /alert %}} 
## **طرق مختلفة لحفظ الملفات**
يوفر Aspose.Cells [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) الذي يمثل ملف Microsoft Excel ويوفر الأساليب اللازمة للعمل مع ملفات Excel. يوفر فئة [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) الأسلوب [Save](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) المستخدم لحفظ ملفات Excel. يحتوي أسلوب [Save](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) على العديد من التحميلات التي تُستخدم لحفظ الملفات بطرق مختلفة. يُقرر تنسيق الملف الذي يتم حفظه إليه بواسطة تعداد [SaveFormat](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/).
## **حفظ ملف في موقع معين**
لحفظ الملفات في مكان تخزين ما، حدد اسم الملف (مع المسار التخزيني الكامل) وتنسيق الملف المطلوب (من تعداد [SaveFormat](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/)) عند استدعاء أسلوب [Save](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) الكائن [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/).



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-SavingFiles-SavingFileToSomeLocation-new.cpp" >}}


## **حفظ الملف في تدفق**
لحفظ الملفات في تدفق، أنشئ كائن MemoryStream أو FileStream واحفظ الملف في ذلك الكائن تدفقًا عن طريق استدعاء أسلوب [Save](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) الكائن [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/). حدد تنسيق الملف المطلوب باستخدام تعداد [SaveFormat](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) عند استدعاء أسلوب [Save](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/).



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-SavingFiles-SavingFileToStream-new.cpp" >}}

## **حفظ الملف إلى صيغة PDF**
لحفظ المحتوى المرغوب فيه إلى ملف PDF باستخدام مكتبة Aspose.Cells for C++ ، أنشئ [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) جديد أو قم بإنشاء [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) عن طريق قراءة ملف Excel موجود، ثم [احفظ](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) الملف إلى صيغة PDF عن طريق استدعاء الطريقة Save من [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/). عند استدعاء طريقة Save ، استخدم تعداد [SaveFormat](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) لتحديد الصيغة المرغوبة للملف.


{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-SavingFiles-SavingFileToPdf-new.cpp" >}}
{{< app/cells/assistant language="cpp" >}}
