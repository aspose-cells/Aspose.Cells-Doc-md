---
title: قم بإنشاء نطاق مسمى في مصنف
type: docs
weight: 60
url: /ar/cpp/create-named-range-in-a-workbook/
---
## **سيناريوهات الاستخدام الممكنة**
 يدعم Aspose.Cells تكوين نطاق مسمى. هناك طرق مختلفة لإنشاء نطاق مسمى. إحدى أبسط الطرق هي الخلق أولاً[IRange](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_range) الكائن ثم قم بتعيين اسمه باستخدام[IRange.SetName ()](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_range#a78480b6b6db0f24cffc8acc2b06552eb) طريقة. يمكنك رؤية جميع النطاقات المسماة داخل ملف Excel الخاص بك عبر Microsoft Excel*مدير الاسم*واجهه المستخدم.
## **قم بإنشاء نطاق مسمى في مصنف**
 يشرح نموذج التعليمات البرمجية التالي كيفية إنشاء ملف*نطاق مسمى* عبر Aspose.Cells. مرة واحدة ،*نطاق مسمى* تم إنشاؤه ، وهو مرئي داخل[IWorkbook.GetIWorksheets (). GetINames ()](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection#aa9e7bc07917a152a2c0de161cca133fa) مجموعة. الرجاء مراجعة[ملف اكسل الناتج](23167006.xlsx) تم إنشاؤها بواسطة رمز كمرجع.
## **عينة من الرموز**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-CreateNamedRangeInWorkbook.cpp" >}}
## **إخراج وحدة التحكم**
 إخراج وحدة التحكم التالية يطبع قيم[GetFullText](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_name#a5b450ef193365dec035c58280fbe9563) و `GetRefersTo` تم إنشاؤه*نطاق مسمى*في الكود أعلاه.

{{< highlight "java" >}}

 Full Text: MyNamedRange

Refers To: =Sheet1!$A$5:$C$10

{{< /highlight >}}
