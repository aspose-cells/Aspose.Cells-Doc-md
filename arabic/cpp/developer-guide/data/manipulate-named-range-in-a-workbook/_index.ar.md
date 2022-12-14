---
title: معالجة النطاق المحدد في مصنف
type: docs
weight: 90
url: /ar/cpp/manipulate-named-range-in-a-workbook/
---
## **سيناريوهات الاستخدام الممكنة**
 يدعم Aspose.Cells معالجة النطاقات المسماة الموجودة. يمكن الوصول إلى كافة النطاقات المسماة الموجودة من[IWorkbook.GetIWorksheets (). GetINames ()](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection#aa9e7bc07917a152a2c0de161cca133fa) مجموعة. بمجرد الوصول إلى النطاق المحدد ، يمكنك تغيير طرقه المختلفة على سبيل المثال[GetFullText](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_name#a5b450ef193365dec035c58280fbe9563)و[GetRefersTo](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_name#afdb10a12d8d395ae81de231f017eba36).
## **معالجة النطاق المحدد في مصنف**
يقرأ نموذج التعليمات البرمجية التالي النطاق المسمى الأول داخل ملف[ملف اكسل المصدر](23167008.xlsx) ويطبع لها[نص كامل](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_name#a5b450ef193365dec035c58280fbe9563)و[يعود الى](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_name#afdb10a12d8d395ae81de231f017eba36) خصائص على وحدة التحكم. بعد ذلك ، يقوم بتعديل `RefersTo` الخاصية ويحفظ ملف[ملف اكسل الناتج](23167009.xlsx).
## **عينة من الرموز**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-ManipulateNamedRangeInWorkbook.cpp" >}}
## **إخراج وحدة التحكم**
 إخراج وحدة التحكم التالية يطبع قيم[نص كامل](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_name#a5b450ef193365dec035c58280fbe9563)و[يعود الى](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_name#afdb10a12d8d395ae81de231f017eba36) أعضاء القائمة*نطاق مسمى*في الكود أعلاه.

{{< highlight "java" >}}

 Full Text: TestRange

Refers To: =Sheet1!$D$3:$G$6

{{< /highlight >}}
