---
title: تنسيق الخلايا
type: docs
weight: 50
url: /ar/cpp/cells-formatting/
---

## **تنسيق خلية أو مجموعة الخلايا**
إذا كنت ترغب في تنسيق خلية أو مجموعة من الخلايا، فإن Aspose.Cells توفر فئة Style (https://reference.aspose.com/cells/cpp/aspose.cells/style/). يمكنك القيام بكل عمليات التنسيق للخلية أو مجموعة الخلايا باستخدام هذه الفئة. بعض الأشياء المتعلقة بالتنسيق التي يمكن تحقيقها باستخدام فئة IStyle هي

- تعيين لون التعبئة للخلية
- تعيين تضمين النص للخلية
- تعيين حدود الخلايا مثل الحدود العلوية، اليسرى، السفلية واليمنى، إلخ.
- تعيين لون الخط، حجم الخط، اسم الخط، خط النص، جريء، مائل، تحت الخط، إلخ.
- تعيين محاذاة النص أفقيًا أو عموديًا لليمين، اليسار، الأعلى، الأسفل، الوسط، إلخ.

إذا كنت ترغب في تحديد نمط خلية واحدة، يرجى استخدام طريقة [Cell->SetStyle()] (https://reference.aspose.com/cells/cpp/aspose.cells/cell/setstyle/)، وإذا كنت تريد تعيين نمط لمجموعة من الخلايا، فيرجى استخدام الطريقة [Range->ApplyStyle()] (https://reference.aspose.com/cells/cpp/aspose.cells/range/applystyle/).
## **الكود المثالي**
يقوم الكود العينة التالي بتنسيق الخلية C4 في ورقة العمل بطرق مختلفة والصورة توضح الملف الإكسل الناتج للإشارة الخاصة بك.

![todo:image_alt_text](cells-formatting_1.png)



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-CellsFormatting-FormatCellOrRangeOfCells-new.cpp" >}}
