---
title: التعامل مع النطاق المسمى في مصنف
type: docs
weight: 90
url: /ar/cpp/manipulate-named-range-in-a-workbook/
---
##  **سيناريوهات الاستخدام المحتملة**
 Aspose.Cells يدعم معالجة النطاقات المسماة الموجودة. يمكن الوصول إلى كافة النطاقات المسماة الموجودة من[Workbook.GetWorksheets().GetNames()](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/getnames/) مجموعة. بمجرد وصولك إلى النطاق المسمى، يمكنك تغيير أساليبه المختلفة، على سبيل المثال[GetFullText](https://reference.aspose.com/cells/cpp/aspose.cells/name/getfulltext/)و[GetRefersTo](https://reference.aspose.com/cells/cpp/aspose.cells/name/getrefersto/).
##  **التعامل مع النطاق المسمى في مصنف**
 يقرأ نموذج التعليمات البرمجية التالي النطاق المسمى الأول داخل ملف[ملف اكسيل المصدر](23167008.xlsx) ويطبع لها[نص كامل](https://reference.aspose.com/cells/cpp/aspose.cells/name/getfulltext/)و[يعود الى](https://reference.aspose.com/cells/cpp/aspose.cells/name/getrefersto/) الخصائص على وحدة التحكم. بعد ذلك يقوم بتعديل الخاصية `RefersTo` ويحفظها[إخراج ملف إكسل](23167009.xlsx).
##  **عينة من الرموز**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-ManipulateNamedRangeInWorkbook-new.cpp" >}}
##  **إخراج وحدة التحكم**
 يطبع إخراج وحدة التحكم التالية قيم[نص كامل](https://reference.aspose.com/cells/cpp/aspose.cells/name/getfulltext/)و[يعود الى](https://reference.aspose.com/cells/cpp/aspose.cells/name/getrefersto/) أعضاء الموجودين*النطاق المسمى*في الكود أعلاه.

{{< highlight "java" >}}

 Full Text: TestRange

Refers To: =Sheet1!$D$3:$G$6

{{< /highlight >}}
