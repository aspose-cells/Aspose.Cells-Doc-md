---
title: دمج أو إلغاء دمج مجموعة من الخلايا
type: docs
weight: 190
url: /ar/python-net/merge-or-unmerge-range-of-cells/
description: توضح هذه المقالة كيفية دمج وفك دمج الخلايا في نطاق في إكسل بمكتبة أسبوز.سيلز لبايثون via .NET.
keywords: مكتبة بايثون لإكسل، دمج وفك دمج الخلايا في البايثون، دمج وفك دمج الخلايا في نطاق مع بايثون.
---

## **سيناريوهات الاستخدام المحتملة**

يمكنك استخدام أسبوز.سيلز لبايثون via .NET لدمج أو تقسيم نطاق الخلايا. توفر أسبوز.سيلز لبايثون via .NET الطريقة [**Range.merge()**](https://reference.aspose.com/cells/python-net/aspose.cells/range/merge/#) والطريقة [**Range.un_merge()**](https://reference.aspose.com/cells/python-net/aspose.cells/range/un_merge/#) لهذا الغرض. تشرح هذه المقالة كيفية دمج نطاق الخلايا في خلية واحدة.


## **كيفية دمج أو فك دمج نطاق الخلايا**

يقوم الشفرة العينية التالية أولاً بإنشاء مجموعة - A1:D4 - ثم يدمج الخلايا في المجموعة في خلية واحدة باستخدام الأسلوب [**Range.merge()**](https://reference.aspose.com/cells/python-net/aspose.cells/range/merge/#). بالمثل، يمكنك تقسيم الخلايا عن طريق إنشاء مجموعة واستدعاء الأسلوب [**Range.un_merge()**](https://reference.aspose.com/cells/python-net/aspose.cells/range/un_merge/#).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-MergeUnmergeRangeOfCells-1.py" >}}
