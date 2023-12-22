---
title: حفظ الملفات
type: docs
weight: 20
url: /ar/cpp/saving-files/
---
{{% alert color="primary" %}} 

Aspose.Cells يجعل من الممكن إنشاء وحفظ الملفات، ومعالجة الملفات الموجودة. تشرح هذه المقالة الطرق المختلفة التي يمكن من خلالها حفظ الملفات.

{{% /alert %}} 
##  **طرق مختلفة لحفظ الملفات**
 Aspose.Cells يوفر[دفتر العمل](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) والذي يمثل ملف Excel Microsoft ويوفر الطرق اللازمة للعمل مع ملفات Excel. ال[دفتر العمل](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) يوفر الفصل[يحفظ](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) الطريقة المستخدمة لحفظ ملفات Excel. ال[يحفظ](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) تحتوي الطريقة على العديد من الأحمال الزائدة التي تستخدم لحفظ الملفات بطرق مختلفة. يتم تحديد تنسيق الملف الذي يتم حفظ الملف فيه بواسطة[حفظ التنسيق](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/)تعداد.
##  **حفظ الملف إلى بعض المواقع**
لحفظ الملفات في موقع تخزين، حدد اسم الملف (مكتملًا بمسار التخزين) وتنسيق الملف المطلوب (من ملف[حفظ التنسيق](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) التعداد) عند استدعاء[دفتر العمل](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) أشياء[يحفظ](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/)طريقة.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-SavingFiles-SavingFileToSomeLocation-new.cpp" >}}


##  **حفظ الملف للدفق**
 لحفظ الملفات في دفق، قم بإنشاء كائن MemoryStream أو FileStream واحفظ الملف في كائن الدفق هذا عن طريق استدعاء الأمر[دفتر العمل](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) أشياء[يحفظ](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) طريقة. حدد تنسيق الملف المطلوب باستخدام[حفظ التنسيق](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) التعداد عند استدعاء[يحفظ](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/)طريقة.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-SavingFiles-SavingFileToStream-new.cpp" >}}
