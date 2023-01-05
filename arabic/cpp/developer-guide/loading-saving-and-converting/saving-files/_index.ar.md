---
title: حفظ الملفات
type: docs
weight: 20
url: /ar/cpp/saving-files/
---
{{% alert color="primary" %}} 

Aspose.Cells يجعل من الممكن تكوين وحفظ الملفات ، ومعالجة الملفات الموجودة. تشرح هذه المقالة الطرق المختلفة التي يمكن بها حفظ الملفات.

{{% /alert %}} 
## **طرق مختلفة لحفظ الملفات**
 يوفر Aspose.Cells ملف[IWorkbook](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) والذي يمثل ملف Excel Microsoft ويوفر الطرق اللازمة للعمل مع ملفات Excel. ال[IWorkbook](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) فئة توفر[يحفظ](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook#a77072cfb929787df9ad1f38b02f58349) الطريقة المستخدمة لحفظ ملفات Excel. ال[يحفظ](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook#a77072cfb929787df9ad1f38b02f58349) الأسلوب يحتوي على العديد من التحميلات الزائدة التي تُستخدم لحفظ الملفات بطرق مختلفة. يتم تحديد تنسيق الملف الذي تم حفظ الملف به بواسطة ملف[SaveFormat](https://reference.aspose.com/cells/cpp/namespace/aspose.cells#a11cae527e4e68f1adcac8f47ea64481a)تعداد.
## **حفظ الملف في بعض المواقع**
لحفظ الملفات في موقع تخزين ، حدد اسم الملف (مكتمل بمسار التخزين) وتنسيق الملف المطلوب (من ملف[SaveFormat](https://reference.aspose.com/cells/cpp/namespace/aspose.cells#a11cae527e4e68f1adcac8f47ea64481a) تعداد) عند استدعاء[IWorkbook](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) أشياء[يحفظ](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook#a77072cfb929787df9ad1f38b02f58349)طريقة.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-SavingFiles-SavingFileToSomeLocation.cpp" >}}


## **حفظ الملف للدفق**
 لحفظ الملفات في تدفق ، أنشئ كائن MemoryStream أو FileStream واحفظ الملف في كائن الدفق هذا عن طريق استدعاء[IWorkbook](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) أشياء[يحفظ](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook#a77072cfb929787df9ad1f38b02f58349) طريقة. حدد تنسيق الملف المطلوب باستخدام امتداد[SaveFormat](https://reference.aspose.com/cells/cpp/namespace/aspose.cells#a11cae527e4e68f1adcac8f47ea64481a) التعداد عند استدعاء[يحفظ](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook#a77072cfb929787df9ad1f38b02f58349)طريقة.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-SavingFiles-SavingFileToStream.cpp" >}}
