---
title: كشف الأوراق العمل الفارغة
type: docs
weight: 410
url: /ar/python-net/detecting-empty-worksheets/
description: يوضح هذا المقال الشفرة التي تشرح كيفية اكتشاف الأوراق الفارغة من مصنفات Excel برمجياً باستخدام مكتبة Aspose.Cells for Python via .NET.
keywords: مكتبة Excel في بايثون، اكتشاف ورقة عمل فارغة باستخدام بايثون، العثور على ورقة عمل فارغة في بايثون.
---

## **فحص الخلايا المعبأة**

يمكن أن تحتوي أوراق العمل على خلية واحدة أو أكثر ممتلئة بقيم حيث تكون القيمة يمكن أن تكون بسيطة (نص، رقم، تاريخ/وقت) أو صيغة أو قيمة تعتمد على صيغة. في مثل هذه الحالة، من السهل الكشف عما إذا كانت ورقة العمل معطاءة أم لا. كل ما علينا فعله هو التحقق من الخصائص [**Cells.max_data_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/max_data_row/) أو [**Cells.max_data_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/max_data_column/). إذا كانت الخصائص المذكورة تعيد قيمة صفر أو قيم موجبة فهذا يعني أن هناك خلية أو أكثر تمت ملؤها، ومع ذلك، إذا كانت أي من هذه الخصائص تعيد -1 فهذا يشير إلى أنه لم يتم ملء أيٌ من الخلايا في الورقة المعطاة.

{{% alert color="primary" %}}

مجموعات الصفوف والأعمدة لها فهرس مبني على الصفر لذلك خلية في الصف 0 والعمود 0 تعني الخلية الأولى في الورقة العمل وهي A1.

{{% /alert %}}

## **فحص الخلايا المهيأة الفارغة**

جميع الخلايا التي تحتوي على قيم يتم تهيئتها تلقائياً، ومع ذلك، هناك احتمال أن تحتوي ورقة العمل على خلايا مقتصرة على التنسيق فقط. في مثل هذا السيناريو، ستُرجع الخاصيتان [**Cells.max_data_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/max_data_row/) أو [**Cells.max_data_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/max_data_column/) القيمة -1، مما يدل على عدم وجود قيم ممتلئة، لكن لا يمكن اكتشاف الخلايا المهيأة بالتنسيق باستخدام هذه الطريقة. للتحقق مما إذا كانت ورقة العمل تحتوي على خلايا مهيأة فارغة، يُنصح باستخدام طريقة IEnumerator.MoveNext على المُعدّ الدُولي، التي يتم الحصول عليها من مجموعة [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells). إذا أعادت طريقة IEnumerator.MoveNext القيمة **true**، فهذا يعني وجود خلية أو أكثر مهيأة في ورقة العمل المحددة.

## **فحص الأشكال**

من الممكن ألا تحتوي ورقة العمل المعطاة على أي خلايا ممتلئة، إلا أنها قد تحتوي على أشكال وأشياء مثل عناصر تحكم، رسوم بيانية، صور، وهكذا. إذا أردنا التحقق مما إذا كانت الورقة تحتوي على أي شكل، يمكننا القيام بذلك بفحص عناصر [**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection). تشير أي قيمة إيجابية إلى وجود شكل أو أشكال في الورقة.

## **نموذج برمجة**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-DetectEmptyWorksheets.py" >}}
{{< app/cells/assistant language="python-net" >}}
