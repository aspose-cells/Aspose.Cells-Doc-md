---
title: Cells التنسيق
type: docs
weight: 50
url: /ar/cpp/cells-formatting/
---
## **تنسيق Cell أو نطاق Cells**
 إذا كنت تريد تنسيق خلية أو نطاق من الخلايا ، فإن Aspose.Cells يوفر تنسيق[IStyle](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_style)صف دراسي. يمكنك إنجاز جميع تنسيقات الخلية أو نطاق الخلايا باستخدام هذه الفئة. فيما يلي بعض الأشياء المتعلقة بالتنسيق التي يمكن إنجازها باستخدام فئة IStyle

- عيّن لون تعبئة الخلية
- اضبط التفاف النص في الخلية
- عيّن حدود الخلايا مثل الحدود العلوية واليسرى والسفلية واليمنى ، إلخ.
- اضبط لون الخط وحجم الخط واسم الخط والخط الغامق والمائل والتسطير وما إلى ذلك.
- اضبط النص الأفقي أو الرأسي المحاذاة إلى اليمين ، اليسار ، أعلى ، أسفل ، وسط ، إلخ.

 إذا كنت ترغب في تعيين نمط خلية واحدة ، فيرجى استخدام[ICell-> SetIStyle ()](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#afa3d5b2aa5e90b286effc9e92de59dd5) إذا كنت تريد تعيين نمط مجموعة من الخلايا ، فيرجى استخدام[IRange-> تطبيق](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_range#aaad6703b803565b674999bbaf5eed3a0)طريقة.
## **عينة من الرموز**
 يقوم نموذج التعليمات البرمجية التالي بتنسيق الخلية C4 من ورقة العمل بطرق مختلفة وتعرض لقطة الشاشة ملف[ملف اكسل الناتج](21266438.xlsx) ولدت به للرجوع اليها.

![ما يجب القيام به: image_بديل_نص](cells-formatting_1.png)



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-CellsFormatting-FormatCellOrRangeOfCells.cpp" >}}
