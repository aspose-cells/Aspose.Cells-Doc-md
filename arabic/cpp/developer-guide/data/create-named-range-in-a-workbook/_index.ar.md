---
title: إنشاء نطاق مسمى في مصنف
type: docs
weight: 60
url: /ar/cpp/create-named-range-in-a-workbook/
---
##  **سيناريوهات الاستخدام المحتملة**
 Aspose.Cells يدعم إنشاء نطاق مسمى. هناك طرق مختلفة لإنشاء نطاق مسمى. واحدة من أبسط الطرق هي الإنشاء أولاً[يتراوح](https://reference.aspose.com/cells/cpp/aspose.cells/range) كائن ثم قم بتعيين اسمه باستخدام[اسم النطاق ()](https://reference.aspose.com/cells/cpp/aspose.cells/range/setname) طريقة. يمكنك رؤية جميع النطاقات المسماة داخل ملف Excel الخاص بك عبر Microsoft Excel*مدير الاسم*واجهه المستخدم.
##  **إنشاء نطاق مسمى في مصنف**
 يشرح نموذج التعليمات البرمجية التالي كيفية إنشاء ملف*النطاق المسمى* عبر Aspose.Cells. ذات مرة*النطاق المسمى* يتم إنشاؤه، وهو مرئي داخل[Workbook.GetWorksheets().GetNames()](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/getnames) مجموعة. الرجاء مراجعة[إخراج ملف إكسل](23167006.xlsx) تم إنشاؤها بواسطة رمز كمرجع.
##  **عينة من الرموز**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-CreateNamedRangeInWorkbook-new.cpp" >}}
##  **إخراج وحدة التحكم**
 يطبع إخراج وحدة التحكم التالية قيم[GetFullText](https://reference.aspose.com/cells/cpp/aspose.cells/name/getfulltext/) و[GetRefersTo](https://reference.aspose.com/cells/cpp/aspose.cells/name/getrefersto/) طرق الخلق*النطاق المسمى*في الكود أعلاه.

{{< highlight "java" >}}

 Full Text: MyNamedRange

Refers To: =Sheet1!$A$5:$C$10

{{< /highlight >}}
