---
title: التجميع وفك تجميع الصفوف والأعمدة
type: docs
weight: 30
url: /ar/cpp/grouping-ungrouping-rows-and-columns/
---
##  **مقدمة**
في ملف Excel Microsoft، يمكنك إنشاء مخطط تفصيلي للبيانات للسماح لك بإظهار وإخفاء مستويات التفاصيل بنقرة واحدة بالماوس.

انقر فوق *رموز المخطط التفصيلي** و1،2،3، + و- لعرض الصفوف أو الأعمدة التي توفر ملخصات أو عناوين للأقسام في ورقة العمل بسرعة، أو يمكنك استخدام الرموز لرؤية التفاصيل ضمن ملخص فردي أو عنوان.
##  **إدارة المجموعة للصفوف والأعمدة**
 Aspose.Cells يوفر فئة،[دفتر العمل](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) الذي يمثل ملف Excel Microsoft. ال[دفتر العمل](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) يحتوي الفصل على أ[أوراق عمل](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) المجموعة التي تسمح بالوصول إلى كل ورقة عمل في ملف Excel. يتم تمثيل ورقة العمل بواسطة[ورقة عمل](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) فصل. ال[ورقة عمل](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) يوفر الفصل[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)المجموعة التي تمثل كافة الخلايا في ورقة العمل.

 ال[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)توفر المجموعة عدة طرق لإدارة الصفوف أو الأعمدة في ورقة العمل، ويتم مناقشة القليل منها أدناه بمزيد من التفاصيل.
###  **تجميع الصفوف والأعمدة**
 من الممكن تجميع الصفوف أو الأعمدة عن طريق استدعاء[صفوف المجموعة](https://reference.aspose.com/cells/cpp/aspose.cells/cells/grouprows/) و[أعمدة المجموعة](https://reference.aspose.com/cells/cpp/aspose.cells/cells/groupcolumns/) أساليب[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)مجموعة. تأخذ كلتا الطريقتين المعلمات التالية:

- فهرس الصف/العمود الأول، الصف أو العمود الأول في المجموعة.
- فهرس الصف/العمود الأخير، آخر صف أو عمود في المجموعة.
- مخفي، وهو معلمة منطقية تحدد ما إذا كان سيتم إخفاء الصفوف/الأعمدة بعد التجميع أم لا.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-GroupingUngroupingRowsAndColumns-GroupingRowsColumns-new.cpp" >}}
####  **إعدادات المجموعة**
Microsoft يتيح لك Excel تكوين إعدادات المجموعة لعرض:

- صفوف التلخيص أدناه التفاصيل.
- أعمدة التلخيص على يمين التفاصيل.
##  **فك تجميع الصفوف والأعمدة**
 لفك تجميع أي صفوف أو أعمدة مجمعة، اتصل بـ[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) المجموعة[فك تجميع الصفوف](https://reference.aspose.com/cells/cpp/aspose.cells/cells/ungrouprows/) و[فك تجميع الأعمدة](https://reference.aspose.com/cells/cpp/aspose.cells/cells/ungroupcolumns/)طُرق. تأخذ كلتا الطريقتين معلمتين:

- فهرس الصف أو العمود الأول، أول صف/عمود سيتم فك تجميعه.
- فهرس الصف أو العمود الأخير، آخر صف/عمود سيتم فك تجميعه.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-GroupingUngroupingRowsAndColumns-UnGroupingRowsColumns-new.cpp" >}}
