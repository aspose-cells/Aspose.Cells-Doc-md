---
title: التلاعب في النطاق المسمى في سجل عمل
type: docs
weight: 90
url: /ar/cpp/manipulate-named-range-in-a-workbook/
---

## **سيناريوهات الاستخدام المحتملة**
Aspose.Cells يدعم التلاعب بالنطاقات المسماة الموجودة. يمكن الوصول إلى جميع النطاقات المسماة الموجودة من مجموعة [Workbook.GetWorksheets().GetNames()](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/getnames/). بمجرد أن يتم الوصول إلى النطاق المسمى، يمكنك تغيير طرقه المختلفة مثل [GetFullText](https://reference.aspose.com/cells/cpp/aspose.cells/name/getfulltext/) و [GetRefersTo](https://reference.aspose.com/cells/cpp/aspose.cells/name/getrefersto/) على سبيل المثال.
## **التلاعب في النطاق المسمى في سجل عمل**
الكود العينة التالي يقرأ اول نطاق مسمى داخل [ملف إكسل المصدر](23167008.xlsx) ويطبع [نص كامل](https://reference.aspose.com/cells/cpp/aspose.cells/name/getfulltext/) و [يشير الى](https://reference.aspose.com/cells/cpp/aspose.cells/name/getrefersto/) الخصائص على الكونسول. بعد ذلك، يعدل خاصية `يشير الى` ويحفظ [ملف إكسل الناتج](23167009.xlsx).
## **الكود المثالي**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-ManipulateNamedRangeInWorkbook-new.cpp" >}}
## **مخرجات الوحدة**
الناتج الخاص بالكونسول يطبع قيم [نص كامل](https://reference.aspose.com/cells/cpp/aspose.cells/name/getfulltext/) و [يشير الى](https://reference.aspose.com/cells/cpp/aspose.cells/name/getrefersto/) لأعضاء النطاق المسمى الحالي في الكود أعلاه.

{{< highlight java >}}

 Full Text: TestRange

Refers To: =Sheet1!$D$3:$G$6

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
