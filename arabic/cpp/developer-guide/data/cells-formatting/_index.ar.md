---
title: Cells التنسيق
type: docs
weight: 50
url: /ar/cpp/cells-formatting/
---
##  **التنسيق Cell أو النطاق Cells**
 إذا كنت تريد تنسيق خلية أو نطاق من الخلايا، فإن Aspose.Cells يوفر لك[أسلوب](https://reference.aspose.com/cells/cpp/aspose.cells/style/)فصل. يمكنك إنجاز جميع تنسيقات الخلية أو نطاق الخلايا باستخدام هذه الفئة. فيما يلي بعض الأشياء المتعلقة بالتنسيق التي يمكن تحقيقها باستخدام فئة IStyle

- تعيين لون تعبئة الخلية
- قم بتعيين التفاف النص للخلية
- قم بتعيين حدود الخلايا مثل الحدود العلوية واليسرى والسفلية واليمنى وما إلى ذلك.
- قم بتعيين لون الخط وحجم الخط واسم الخط والخط الغامق والمائل والتسطير وما إلى ذلك.
- اضبط محاذاة النص أفقيًا أو رأسيًا إلى اليمين أو اليسار أو الأعلى أو الأسفل أو الوسط، وما إلى ذلك.

 إذا كنت تريد تعيين نمط خلية واحدة، فيرجى استخدامها[Cell->SetStyle()](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setstyle/) الطريقة وإذا كنت تريد تعيين نمط نطاق من الخلايا، فيرجى استخدامها[النطاق->ApplyStyle()](https://reference.aspose.com/cells/cpp/aspose.cells/range/applystyle/)طريقة.
##  **عينة من الرموز**
 يقوم نموذج التعليمات البرمجية التالي بتنسيق الخلية C4 من ورقة العمل بطرق مختلفة وتظهر لقطة الشاشة[إخراج ملف إكسل](21266438.xlsx) تم إنشاؤها بواسطة ذلك للرجوع إليها.

![ما يجب القيام به:image_alt_text](cells-formatting_1.png)



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-CellsFormatting-FormatCellOrRangeOfCells-new.cpp" >}}
