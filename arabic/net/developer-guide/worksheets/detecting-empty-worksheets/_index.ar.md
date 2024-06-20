---
title: كشف الأوراق العمل الفارغة
type: docs
weight: 410
url: /ar/net/detecting-empty-worksheets/
description: توضح هذه المقالة كيفية كتابة الكود للكشف عن الأوراق العمل الفارغة في مصنفات Excel برمجياً باستخدام واجهة برمجة التطبيقات C# مع مكتبة .NET.
keywords: كشف ورقة عمل فارغة باستخدام C#، العثور على ورقة عمل Excel فارغة باستخدام C#
---

## **فحص الخلايا المعبأة**

يمكن أن تحتوي أوراق العمل على خلية واحدة أو أكثر ممتلئة بقيم حيث تكون القيمة يمكن أن تكون بسيطة (نص، رقم، تاريخ/وقت) أو صيغة أو قيمة تعتمد على صيغة. في مثل هذه الحالة، من السهل الكشف عما إذا كانت ورقة العمل معطاءة أم لا. كل ما علينا فعله هو التحقق من الخصائص [**Cells.MaxDataRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdatarow) أو [**Cells.MaxDataColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdatacolumn). إذا كانت الخصائص المذكورة تعيد قيمة صفر أو قيم موجبة فهذا يعني أن هناك خلية أو أكثر تمت ملؤها، ومع ذلك، إذا كانت أي من هذه الخصائص تعيد -1 فهذا يشير إلى أنه لم يتم ملء أيٌ من الخلايا في الورقة المعطاة.

{{% alert color="primary" %}}

مجموعات الصفوف والأعمدة لها فهرس مبني على الصفر لذلك خلية في الصف 0 والعمود 0 تعني الخلية الأولى في الورقة العمل وهي A1.

{{% /alert %}}

## **فحص الخلايا المهيأة الفارغة**

جميع الخلايا التي تحتوي على قيم تهيأ تلقائياً، ومع ذلك، هناك إمكانية أن يكون هناك ورقة عمل تحتوي على خلايا يتم تهيئتها فقط بالتنسيق. في مثل هذا السيناريو، ستعيد الخصائص [**Cells.MaxDataRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdatarow) أو [**Cells.MaxDataColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdatacolumn) قيمة -1 مشيرة إلى عدم وجود أي قيم معطاة ولكن تحتوي الخلايا التي تم تهيئتها على تنسيق ولا يمكن الكشف عنها باستخدام هذا النهج. من أجل التحقق مما إذا كانت ورقة العمل تحتوي على خلايا مهيأة فارغة، يُنصح باستخدام طريقة IEnumerator.MoveNext على المُعالج المُستدعى من مجموعة [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells). إذا قامت طريقة IEnumerator.MoveNext بإعادة **true** فهذا يعني وجود خلية مهيأة واحدة أو أكثر في الورقة العمل المعطاة.

## **فحص الأشكال**

قد لا تحتوي ورقة العمل المعطاة على خلايا معماء، ولكن قد تحتوي على أشكال وأجسام مثل عناصر التحكم، الرسوم البيانية، الصور وما إلى ذلك. إذا كنا بحاجة للتحقق مما إذا كانت ورقة العمل تحتوي على أي شكل، فيمكننا القيام بذلك عن طريق تفحص الخاصية [**ShapeCollection.Count**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection). أي قيمة موجبة تدل على وجود شكل/أشكال في ورقة العمل.

## **نموذج برمجة**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-DetectEmptyWorksheets-DetectEmptyWorksheets.cs" >}}
