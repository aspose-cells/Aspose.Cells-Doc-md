---
title: تجميع وإلغاء تجميع الأسطر والأعمدة
type: docs
weight: 30
url: /ar/go-cpp/grouping-ungrouping-rows-and-columns/
---

## **مقدمة**

في ملف Microsoft Excel، يمكنك إنشاء مخطط للبيانات للسماح لك بإظهار وإخفاء مستويات التفاصيل بنقرة واحدة على الفأرة.

انقر فوق **رموز الإطار العام** ، 1،2،3 ، + و - لعرض الصفوف أو الأعمدة التي تقدم ملخصات أو عناوين للأقسام في ورقة العمل بسرعة ، أو يمكنك استخدام الرموز لرؤية التفاصيل تحت ملخص فردي أو عنوان.

## **إدارة تجميع الصفوف والأعمدة**

يوفر Aspose.Cells فئة [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) التي تمثل ملف Excel من Microsoft. تحتوي فئة [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) على مجموعة [Worksheets](https://reference.aspose.com/cells/go-cpp/worksheetcollection/) التي تمكنك من الوصول إلى كل ورقة عمل في ملف Excel. تمثل ورقة العمل بواسطة فئة [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/). توفر فئة [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) مجموعة [Cells](https://reference.aspose.com/cells/go-cpp/cells/) التي تمثل جميع الخلايا في ورقة العمل.

توفر مجموعة [Cells](https://reference.aspose.com/cells/go-cpp/cells/) عدة طرق لإدارة الصفوف أو الأعمدة في ورقة العمل، وسيتم مناقشة بعض منها بمزيد من التفصيل أدناه.

### **تجميع الصفوف والأعمدة**

من الممكن تجميع الصفوف أو الأعمدة عن طريق استدعاء طريقتي [GroupRows](https://reference.aspose.com/cells/go-cpp/cells/grouprows/) و [GroupColumns](https://reference.aspose.com/cells/go-cpp/cells/groupcolumns/) لمجموعة [Cells](https://reference.aspose.com/cells/go-cpp/cells/). كلتا الطريقتين تتطلب المعاملات التالية:

- مؤشر الصف/العمود الأول ، الصف أو العمود الأول في المجموعة.
- مؤشر الصف/العمود الأخير ، الصف أو العمود الأخير في المجموعة.
- يتم إخفاءها، معلمة منطقية تحدد ما إذا كان سيتم إخفاء الصفوف/الأعمدة بعد التجميع أم لا.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GroupingRowsColumns.go" >}}

#### **إعدادات التجميع**

يسمح Microsoft Excel لك بتكوين إعدادات التجميع لعرض:

- صفوف ملخصية أسفل التفاصيل.
- أعمدة ملخصية على يمين التفاصيل.

## **إلغاء تجميع الصفوف والأعمدة**

لإلغاء تجميع أي صفوف أو أعمدة مجمعة، قم باستدعاء الطريقتين [UngroupRows](https://reference.aspose.com/cells/go-cpp/cells/ungrouprows/) و [UngroupColumns](https://reference.aspose.com/cells/go-cpp/cells/ungroupcolumns/) لمجموعة [Cells](https://reference.aspose.com/cells/go-cpp/cells/). تتطلب كلتا الطريقتين معاملين:

- مؤشر الصف أو العمود الأول ، الصف/العمود الأول الذي سيتم إلغاء تجميعه.
- مؤشر الصف أو العمود الأخير ، الصف/العمود الأخير الذي سيتم إلغاء تجميعه.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-UnGroupingRowsColumns.go" >}}
