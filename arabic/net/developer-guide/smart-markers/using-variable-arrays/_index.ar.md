---
title: استيراد المصفوفات المتغيرة بذكاء إلى إكسل باستخدام العلامات الذكية
type: docs
weight: 30
url: /ar/net/how-to-import-variable-arrays-with-smart-markers/
---

## **لماذا نستخدم المصفوفات المتغيرة للعلامات الذكية**
Variable arrays (e.g., <<products[0].name>> or <<foreach item in cart>>) enable dynamic handling of repeated data structures in templates. They solve limitations of flat/nested objects when dealing with lists, tables, or collections.

1. التكرار الديناميكي بدون ترميز صلب: تفشل العلامات الثابتة للبيانات ذات الطول المتغير (على سبيل المثال، عناصر الطلب، أذونات المستخدم). تقوم المصفوفات بالتكرار بشكل ديناميكي. 
2. التجميع المبسط: حساب المجاميع، المتوسطات، أو المرشحات مباشرة. تجنب منطق جافا سكريبت / C# اليدوي في القوالب.
3. تمثيل البيانات بشكل جدولي / قائمة: مناسب بشكل طبيعي: الجداول، الشبكات، والقوائم تتطابق بشكل جوهري مع المصفوفات.
4. كفاءة الذاكرة: تقلل المصفوفات من تعقيد القالب وحمل ربط البيانات.
5. التكامل مع API / مصادر البيانات: يتوافق مع بيانات JSON / مركزة على المصفوفة (على سبيل المثال، واجهات برمجة التطبيقات REST).

## **كيفية استيراد المصفوفات المتغيرة باستخدام العلامات الذكية**
يوضح الكود المثالي التالي كيفية استخدام متغيرات الصفوف في العلامات الذكية. نضع علامة صفوف متغيرة في الخلية A1 للورقة العمل الأولى للدفتر بشكل ديناميكي والتي تحتوي على سلسلة من القيم التي نحددها للعلامة، نقوم بمعالجة العلامات لملء البيانات في الخلايا ضد العلامة. أخيرًا نقوم بحفظ ملف Excel.


{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingVariableArray-1.cs" >}}

## **كيفية استيراد خاصية HTML باستخدام العلامات الذكية**
The following sample code explains the use of HTML property of the Smart Markers. When it will be processed, it will show "World" in "Hello World" as bold because of HTML <b> tag.


{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingHTMLProperty-1.cs" >}}

{{< app/cells/assistant language="csharp" >}}
