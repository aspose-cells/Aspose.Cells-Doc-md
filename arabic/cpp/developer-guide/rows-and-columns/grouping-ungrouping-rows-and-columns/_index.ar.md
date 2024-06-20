---
title: تجميع وإلغاء تجميع الأسطر والأعمدة
type: docs
weight: 30
url: /ar/cpp/grouping-ungrouping-rows-and-columns/
---

## **مقدمة**
في ملف Microsoft Excel، يمكنك إنشاء مخطط للبيانات للسماح لك بإظهار وإخفاء مستويات التفاصيل بنقرة واحدة على الفأرة.

انقر فوق **رموز الإطار العام** ، 1،2،3 ، + و - لعرض الصفوف أو الأعمدة التي تقدم ملخصات أو عناوين للأقسام في ورقة العمل بسرعة ، أو يمكنك استخدام الرموز لرؤية التفاصيل تحت ملخص فردي أو عنوان.
## **إدارة تجميع الصفوف والأعمدة**
يوفر Aspose.Cells فئة ، [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) التي تمثل ملف Microsoft Excel. تحتوي الفئة [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) على مجموعة [Worksheets](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) التي تسمح بالوصول إلى كل ورقة عمل في ملف Excel. تمثل ورقة العمل بواسطة فئة [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) . توفر فئة [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) مجموعة [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) التي تمثل جميع الخلايا في ورقة العمل.

تقدم مجموعة [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) العديد من الطرق لإدارة الصفوف أو الأعمدة في ورقة العمل ، ويتم مناقشة بعض هذه الطرق أدناه بمزيد من التفصيل.
### **تجميع الصفوف والأعمدة**
من الممكن تجميع الصفوف أو الأعمدة عن طريق استدعاء [GroupRows](https://reference.aspose.com/cells/cpp/aspose.cells/cells/grouprows/) و [GroupColumns](https://reference.aspose.com/cells/cpp/aspose.cells/cells/groupcolumns/) من مجموعة [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) . تأخذ كلا الطريقتين المعلمات التالية:

- مؤشر الصف/العمود الأول ، الصف أو العمود الأول في المجموعة.
- مؤشر الصف/العمود الأخير ، الصف أو العمود الأخير في المجموعة.
- يتم إخفاءها، معلمة منطقية تحدد ما إذا كان سيتم إخفاء الصفوف/الأعمدة بعد التجميع أم لا.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-GroupingUngroupingRowsAndColumns-GroupingRowsColumns-new.cpp" >}}
#### **إعدادات التجميع**
يسمح Microsoft Excel لك بتكوين إعدادات التجميع لعرض:

- صفوف ملخصية أسفل التفاصيل.
- أعمدة ملخصية على يمين التفاصيل.
## **إلغاء تجميع الصفوف والأعمدة**
لإلغاء أي صفوف أو أعمدة مجمعة ، يمكنك استدعاء [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) مجموعة [UngroupRows](https://reference.aspose.com/cells/cpp/aspose.cells/cells/ungrouprows/) و [UngroupColumns](https://reference.aspose.com/cells/cpp/aspose.cells/cells/ungroupcolumns/) . تأخذ كلتا الطريقتين معلمتين:

- مؤشر الصف أو العمود الأول ، الصف/العمود الأول الذي سيتم إلغاء تجميعه.
- مؤشر الصف أو العمود الأخير ، الصف/العمود الأخير الذي سيتم إلغاء تجميعه.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-GroupingUngroupingRowsAndColumns-UnGroupingRowsColumns-new.cpp" >}}
