---
title: إنشاء نطاق مسمى في مصنف
type: docs
weight: 60
url: /ar/cpp/create-named-range-in-a-workbook/
---

## **سيناريوهات الاستخدام المحتملة**
تدعم Aspose.Cells إنشاء نطاق مسمى. هناك طرق مختلفة لإنشاء نطاق مسمى. أحد أسهل الطرق هو إنشاء كائن [Range](https://reference.aspose.com/cells/cpp/aspose.cells/range) أولاً ثم تعيين اسمه باستخدام طريقة [Range.SetName()](https://reference.aspose.com/cells/cpp/aspose.cells/range/setname). يمكنك رؤية جميع النطاقات المسماة داخل ملف Excel الخاص بك عبر واجهة *مدير الأسماء* في Microsoft Excel.
## **إنشاء نطاق مسمى في مصنف**
الكود النموذجي التالي يوضح كيفية إنشاء *نطاق مسمى* عبر Aspose.Cells. بمجرد إنشاء *نطاق مسمى*، يكون مرئيا داخل [Workbook.GetWorksheets().GetNames()](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/getnames) المجموعة. يُرجى الاطلاع على [ملف الإكسل الناتج](23167006.xlsx) الذي تم إنشاؤه بواسطة الكود للرجوع إليه.
## **الكود المثالي**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-CreateNamedRangeInWorkbook-new.cpp" >}}
## **مخرجات الوحدة**
يُطبع الإخراج لوحدة التحكم التالية قيم طرق [GetFullText](https://reference.aspose.com/cells/cpp/aspose.cells/name/getfulltext/) و [GetRefersTo](https://reference.aspose.com/cells/cpp/aspose.cells/name/getrefersto/) لـ *نطاق مسمى* المُنشأ في الكود أعلاه.

{{< highlight java >}}

 Full Text: MyNamedRange

Refers To: =Sheet1!$A$5:$C$10

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
