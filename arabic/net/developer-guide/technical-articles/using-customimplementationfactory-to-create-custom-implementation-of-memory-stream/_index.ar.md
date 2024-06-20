---
title: استخدام CustomImplementationFactory لإنشاء تنفيذ مخصص لـ Memory Stream
type: docs
weight: 40
url: /ar/net/using-customimplementationfactory-to-create-custom-implementation-of-memory-stream/
---

## **سيناريوهات الاستخدام المحتملة**

لقد قدمت Aspose.Cells واجهة برمجة تطبيقات تسمى [**CellsHelper.CustomImplementationFactory**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/properties/customimplementationfactory) التي تتيح للمستخدم تقديم تنفيذ مخصص مثل استخدام تنفيذ الذاكرة القابلة لإعادة الاستخدام بدلاً من MemoryStream الافتراضي.

## **استخدام CustomImplementationFactory لإنشاء تنفيذ مخصص لـ Memory Stream**

الكود النموذجي التالي يوضح كيفية استخدام [**CellsHelper.CustomImplementationFactory**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/properties/customimplementationfactory) في برنامجك. في بعض الأحيان، هناك ما يكفي من الذاكرة في النظام الخاص بك ولكن الذاكرة غير متصلة. تستخدم كائنات Memory Stream ذاكرة متصلة ولكن يمكنك تقديم تنفيذ لـ Memory Stream بحيث يستخدم الذاكرة غير المتصلة بدلاً من ذلك

## **الكود المثالي**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-CellsHelper-UsingCustomImplementationFactoryToCreateCustomImplementationOfMemoryStream.cs" >}}
