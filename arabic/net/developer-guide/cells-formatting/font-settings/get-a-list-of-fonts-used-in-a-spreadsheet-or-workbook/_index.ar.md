---
title: احصل على قائمة الخطوط المستخدمة في جدول بيانات أو مصنف
type: docs
weight: 20
url: /ar/net/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/
---
## **سيناريوهات الاستخدام الممكنة**

غالبًا ما يكون من الضروري معرفة الخطوط المستخدمة في المصنف الخاص بك لأغراض العرض. عندما تقوم بتحويل المصنف الخاص بك إلى PDF أو صورة ، فإن Aspose.Cells يتطلب تثبيت جميع الخطوط المطلوبة على نظامك أو وجودها في**دليل الخطوط**إذا لم يتمكن Aspose.Cells من العثور على الخط المطلوب ، فإنه يحاول استبداله بخط آخر مناسب موجود في نظامك أو في دليل الخطوط الخاص بك ويمكنه استبدال الخط الفعلي. لا ينتج عن هذا العرض غير المرغوب فيه لـ PDF أو الصور فحسب ، بل يستغرق أيضًا وقت المعالجة للعثور على الخطوط المناسبة.

للتعامل مع مثل هذه الحالات ، يجب أن تعرف الخطوط التي يستخدمها المصنف الخاص بك ، ثم قم بتثبيت هذه الخطوط على نظامك في حالة بيئة Windows أو وضعها في دليل الخطوط في حالة بيئة windows أو Linux.

 يوفر Aspose.Cells ملف**[Workbook.GetFonts] (https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/getfonts)**الطريقة التي تُرجع قائمة بجميع الخطوط المستخدمة في المصنف أو جدول البيانات.

## **احصل على قائمة الخطوط المستخدمة في جدول بيانات أو مصنف**

 يقوم نموذج التعليمات البرمجية التالي بتحميل ملف Excel المصدر واسترداد قائمة الخطوط المستخدمة بداخله. يحتوي على ورقة عمل وهمية تحتوي على بعض الخطوط الوهمية المضافة لأغراض التوضيح. عندما يطبع الكود جميع الخطوط داخل المصنف ، فإنه يطبع أيضًا تلك الخطوط الوهمية. تُظهر لقطة الشاشة التالية ملف[نموذج ملف اكسل](25395211.xlsx) وكيف يتم سرد الخطوط الوهمية.

![ما يجب القيام به: image_بديل_نص](get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook_1.png)

## **عينة من الرموز**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Fonts-GetListOfFontsUsedInSpreadsheetOrWorkbook.cs" >}}

## **إخراج وحدة التحكم**

 هنا هو إخراج وحدة التحكم من نموذج التعليمات البرمجية أعلاه عند تنفيذه مع المعطى[نموذج ملف اكسل](25395211.xlsx).

{{< highlight "java" >}}

Aspose.Cells.Font [ Calibri; 11; Regular; Color [Black]]

Aspose.Cells.Font [ Arial; 10; Regular; Color [A=255, R=0, G=0, B=0]]

Aspose.Cells.Font [ Calibri; 10; Bold; Color [Black]]

Aspose.Cells.Font [ Calibri; 10; Regular; Color [A=255, R=128, G=128, B=128]]

Aspose.Cells.Font [ Calibri; 10; Regular; Color [A=255, R=55, G=98, B=104]]

Aspose.Cells.Font [ Calibri; 16; Bold; Color [A=255, R=255, G=255, B=255]]

Aspose.Cells.Font [ Calibri; 36; Regular; Color [A=255, R=55, G=98, B=104]]

Aspose.Cells.Font [ Calibri; 20; Bold; Color [A=255, R=55, G=98, B=104]]

Aspose.Cells.Font [ Calibri; 16; Regular; Color [A=255, R=55, G=98, B=104]]

Aspose.Cells.Font [ Calibri; 11; Regular; Color [A=255, R=55, G=98, B=104]]

Aspose.Cells.Font [ Calibri; 11; Bold; Color [A=255, R=55, G=98, B=104]]

Aspose.Cells.Font [ Calibri; 11; Bold; Color [A=255, R=255, G=255, B=255]]

Aspose.Cells.Font [ Calibri; 11; Italic; Color [A=255, R=55, G=98, B=104]]

Aspose.Cells.Font [ Calibri; 16; Regular; Color [A=255, R=55, G=98, B=104]]

Aspose.Cells.Font [ Calibri; 16; Bold; Color [A=255, R=55, G=98, B=104]]

Aspose.Cells.Font [ Calibri; 16; Regular; Color [Black]]

Aspose.Cells.Font [ Calibri; 16; Regular; Color [A=255, R=41, G=74, B=78]]

Aspose.Cells.Font [ Calibri; 16; Regular; Color [A=255, R=41, G=74, B=78]]

Aspose.Cells.Font [ Calibri; 12; Regular; Color [A=255, R=41, G=74, B=78]]

Aspose.Cells.Font [ Calibri; 11; Regular; Color [A=255, R=41, G=74, B=78]]

Aspose.Cells.Font [ Calibri; 11; Bold; Color [A=255, R=255, G=255, B=255]]

Aspose.Cells.Font [ Dummy-Arial-X; 11; Regular; Color [Black]]

Aspose.Cells.Font [ Dummy-Arial-Y; 11; Regular; Color [Black]]

Aspose.Cells.Font [ Dummy-Arial-Z; 11; Regular; Color [Black]]

Aspose.Cells.Font [ Dummy-Times-I; 11; Regular; Color [Black]]

Aspose.Cells.Font [ Dummy-Times-II; 11; Regular; Color [Black]]

Aspose.Cells.Font [ Dummy-Times-III; 11; Regular; Color [Black]]

Aspose.Cells.Font [ Calibri; 10.5; Regular; Color [A=255, R=55, G=98, B=104]]

Aspose.Cells.Font [ Calibri; 20; Regular; Color [A=255, R=55, G=98, B=104]]

Aspose.Cells.Font [ Calibri; 11; Regular; Color [A=255, R=55, G=98, B=104]]

{{< /highlight >}}
