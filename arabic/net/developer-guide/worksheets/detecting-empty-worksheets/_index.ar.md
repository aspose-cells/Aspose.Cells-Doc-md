---
title: كشف أوراق العمل الفارغة
type: docs
weight: 410
url: /ar/net/detecting-empty-worksheets/
---
## **تحقق من وجود Cells بالسكان**

يمكن أن تحتوي أوراق العمل على خلية واحدة أو أكثر مليئة بالقيم حيث يمكن أن تكون القيمة بسيطة (نصية أو رقمية أو تاريخ / وقت) أو صيغة أو قيمة قائمة على صيغة. في مثل هذه الحالة ، من السهل اكتشاف ما إذا كانت ورقة عمل معينة فارغة أم لا. كل ما علينا التحقق منه هو[**Cells.MaxDataRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdatarow) أو[**Cells.MaxDataColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdatacolumn)الخصائص. إذا كانت الخصائص المذكورة أعلاه ترجع صفرًا أو قيمًا موجبة ، فهذا يعني أنه تم ملء خلية واحدة أو أكثر ، ومع ذلك ، إذا أرجع أي من هذه الخصائص -1 ، فهذا يشير إلى أنه لم يتم ملء أي خلية في ورقة العمل المحددة.

{{% alert color="primary" %}}

تحتوي مجموعات الصفوف والأعمدة على فهرس قائم على الصفر ، وبالتالي فإن الخلية الموجودة في الصف 0 والعمود 0 تعني الخلية الأولى في ورقة العمل ، وهي A1.

{{% /alert %}}

## **تحقق من وجود فارغ مهيأ Cells**

 تتم تهيئة جميع الخلايا التي تحتوي على قيم تلقائيًا ، ومع ذلك ، هناك احتمال أن تحتوي ورقة العمل على خلايا مع تطبيق التنسيق فقط. في مثل هذا السيناريو ، فإن[**Cells.MaxDataRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdatarow)أو[**Cells.MaxDataColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdatacolumn) ستعيد الخصائص -1 مما يشير إلى عدم وجود أي قيم مملوءة ولكن لا يمكن اكتشاف الخلايا المهيأة بسبب تنسيق الخلية باستخدام هذا الأسلوب. للتحقق مما إذا كانت ورقة العمل تحتوي على خلايا مهيأة فارغة ، يُنصح باستخدام طريقة IEnumerator.MoveNext على العداد الذي تم الحصول عليه من[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) مجموعة. إذا تم إرجاع أسلوب IEnumerator.MoveNext**حقيقي** هذا يعني أن هناك خلية واحدة أو أكثر تمت تهيئتها في ورقة العمل المحددة.

## **تحقق من وجود الأشكال**

 من المحتمل ألا تحتوي ورقة العمل المحددة على أي خلايا مأهولة ، ومع ذلك ، يمكن أن تحتوي على أشكال وكائنات مثل عناصر التحكم والمخططات والصور وما إلى ذلك. إذا احتجنا إلى التحقق مما إذا كانت ورقة العمل تحتوي على أي شكل ، فيمكننا القيام بذلك عن طريق فحص ملف[**ShapeCollection.Count**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection)منشأه. تشير أي قيمة موجبة إلى وجود شكل (أشكال) في ورقة العمل.

## **عينة البرمجة**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-DetectEmptyWorksheets-DetectEmptyWorksheets.cs" >}}
