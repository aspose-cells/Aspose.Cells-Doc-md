---
title: احصل على قائمة الخطوط المستخدمة في جدول بيانات أو مصنف
type: docs
weight: 20
url: /ar/java/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/
---
## **سيناريوهات الاستخدام الممكنة**

 غالبًا ما يكون من الضروري معرفة الخطوط المستخدمة في المصنف الخاص بك لغرض العرض. عندما تقوم بتحويل المصنف الخاص بك إلى PDF أو صورة ، فإن Aspose.Cells يتطلب تثبيت جميع الخطوط المطلوبة على نظامك أو وجودها في**دليل الخطوط**إذا لم يتمكن Aspose.Cells من العثور على الخط المطلوب ، فإنه يحاول استبداله بخط آخر مناسب موجود في نظامك أو في دليل الخطوط الخاص بك ويمكنه استبدال الخط الفعلي. لا ينتج عن هذا العرض غير المرغوب فيه لملفات PDF أو الصور فحسب ، بل يستغرق أيضًا وقتًا في المعالجة للعثور على الخطوط المناسبة.

للتعامل مع مثل هذه الحالات ، يجب أن تعرف الخطوط التي يستخدمها المصنف الخاص بك ، ثم قم بتثبيت تلك الخطوط على نظامك في حالة بيئة Windows أو وضعها في دليل الخطوط في حالة بيئة windows أو Linux.

 يوفر Aspose.Cells ملف[Workbook.getFonts ()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#getFonts()) الطريقة التي تُرجع قائمة بجميع الخطوط المستخدمة في المصنف أو جدول البيانات.

## **احصل على قائمة الخطوط المستخدمة في جدول بيانات أو مصنف**

 يقوم نموذج التعليمات البرمجية التالي بتحميل ملف Excel المصدر واسترداد قائمة الخطوط المستخدمة بداخله. يحتوي على ورقة عمل وهمية تحتوي على بعض الخطوط الوهمية المضافة لغرض التوضيح. عندما يطبع الكود جميع الخطوط داخل المصنف ، فإنه يطبع أيضًا تلك الخطوط الوهمية. تُظهر لقطة الشاشة التالية ملف[نموذج ملف اكسل](sampleGetFonts.xlsx)وكيف يتم سرد الخطوط الوهمية.

![ما يجب القيام به: image_بديل_نص](get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook_1.png)

## **عينة من الرموز**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetFontsUsedinWorkbook-GetFontsUsedinWorkbook.java" >}}

## **إخراج وحدة التحكم**

 هنا هو إخراج وحدة التحكم من نموذج التعليمات البرمجية أعلاه عند تنفيذه مع المعطى[نموذج ملف اكسل](sampleGetFonts.xlsx).

{{< highlight "java" >}}

Aspose.Cells.Font [ Calibri; 11.0; Regular; com.aspose.cells.Color@ff000000 ]Aspose.Cells.Font [ Arial; 10.0; Regular; com.aspose.cells.Color@ff000000 ]Aspose.Cells.Font [ Calibri; 10.0; Bold; com.aspose.cells.Color@ff000000 ]Aspose.Cells.Font [ Calibri; 10.0; Regular; com.aspose.cells.Color@ff808080 ]Aspose.Cells.Font [ Calibri; 10.0; Regular; com.aspose.cells.Color@ff376268 ]Aspose.Cells.Font [ Calibri; 16.0; Bold; com.aspose.cells.Color@ffffffff ]Aspose.Cells.Font [ Calibri; 36.0; Regular; com.aspose.cells.Color@ff376268 ]Aspose.Cells.Font [ Calibri; 20.0; Bold; com.aspose.cells.Color@ff376268 ]Aspose.Cells.Font [ Calibri; 16.0; Regular; com.aspose.cells.Color@ff376268 ]Aspose.Cells.Font [ Calibri; 11.0; Regular; com.aspose.cells.Color@ff376268 ]Aspose.Cells.Font [ Calibri; 11.0; Bold; com.aspose.cells.Color@ff376268 ]Aspose.Cells.Font [ Calibri; 11.0; Bold; com.aspose.cells.Color@ffffffff ]Aspose.Cells.Font [ Calibri; 11.0; Italic; com.aspose.cells.Color@ff376268 ]Aspose.Cells.Font [ Calibri; 16.0; Regular; com.aspose.cells.Color@ff376268 ]Aspose.Cells.Font [ Calibri; 16.0; Bold; com.aspose.cells.Color@ff376268 ]Aspose.Cells.Font [ Calibri; 16.0; Regular; com.aspose.cells.Color@ff000000 ]Aspose.Cells.Font [ Calibri; 16.0; Regular; com.aspose.cells.Color@ff294a4e ]Aspose.Cells.Font [ Calibri; 16.0; Regular; com.aspose.cells.Color@ff294a4e ]Aspose.Cells.Font [ Calibri; 12.0; Regular; com.aspose.cells.Color@ff294a4e ]Aspose.Cells.Font [ Calibri; 11.0; Regular; com.aspose.cells.Color@ff294a4e ]Aspose.Cells.Font [ Calibri; 11.0; Bold; com.aspose.cells.Color@ffffffff ]Aspose.Cells.Font [ Dummy-Arial-X; 11.0; Regular; com.aspose.cells.Color@ff000000 ]Aspose.Cells.Font [ Dummy-Arial-Y; 11.0; Regular; com.aspose.cells.Color@ff000000 ]Aspose.Cells.Font [ Dummy-Arial-Z; 11.0; Regular; com.aspose.cells.Color@ff000000 ]Aspose.Cells.Font [ Dummy-Times-I; 11.0; Regular; com.aspose.cells.Color@ff000000 ]Aspose.Cells.Font [ Dummy-Times-II; 11.0; Regular; com.aspose.cells.Color@ff000000 ]Aspose.Cells.Font [ Dummy-Times-III; 11.0; Regular; com.aspose.cells.Color@ff000000 ]Aspose.Cells.Font [ Calibri; 10.5; Regular; com.aspose.cells.Color@ff376268 ]Aspose.Cells.Font [ Calibri; 20.0; Regular; com.aspose.cells.Color@ff376268 ]Aspose.Cells.Font [ Calibri; 11.0; Regular; com.aspose.cells.Color@ff376268 ]{{< /highlight >}}
