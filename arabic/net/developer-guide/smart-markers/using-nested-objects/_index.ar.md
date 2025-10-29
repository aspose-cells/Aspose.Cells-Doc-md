---
title: استيراد الكائنات المتداخلة بذكاء إلى إكسل باستخدام العلامات الذكية
type: docs
weight: 30
url: /ar/net/how-to-import-nested-objects-with-smart-markers/
---

## **لماذا نستخدم الكائنات المتداخلة للعلامات الذكية**
Smart Markers (in tools like FoxPro, reporting engines, or modern template systems) are placeholders that dynamically inject data into templates. Using nested objects (e.g., <<customer.address.city>>) enhances flexibility, organization, and expressiveness.

1. تمثيل البيانات الهرمية: البيانات في العالم الحقيقي بطبيعتها متداخلة (مثلاً، طلب يحتوي على عميل، والذي لديه عنوان). الكائنات المتداخلة تعكس هذا الهيكل، مما يتجنب الحقول المسطحة/الاصطناعية مثل customer_city.
2. تجنب تصادم الأسماء: الهياكل المسطحة تخاطر بالتعارض (مثل product_name مقابل supplier_name). التداخل يضع الأسماء بشكل طبيعي:
<<product.name>> vs. <<supplier.name>>.
3. القابلية للتجزئة وإعادة الاستخدام: إعادة استخدام الكائنات الفرعية في سياقات مختلفة، يمكن تضمين كائن العنوان في علامات العميل، البائع، أو الموظف. التغييرات على العنوان تنتشر بشكل عالمي.
4. Simplified Data Binding: Bind entire nested objects to templates, <<order.customer>> auto-expands to all customer fields. Reduces manual mapping for sub-fields.
5. Dynamic Data Traversal: Traverse relationships on-demand, <<invoice.line_items[0].price>> accesses array elements or child objects. Enables complex queries without pre-processing.
6. Clearer Template Logic: Markers self-document relationships, <<user.profile.email>> is more intuitive than <<user_email>>. Reduces ambiguity in large templates.
7. دعم الأطر والأدوات: المحركات الحديثة (مثل Handlebars، React، FoxPro) تحل بشكل أصلي مسارات التداخل. يتوافق مع JSON/واجهات برمجة التطبيقات حيث البيانات المتداخلة معيارية.

## **كيفية استيراد الأنواع المجهولة أو الكائنات المخصصة باستخدام العلامات الذكية**
تدعم Aspose.Cells أيضًا أنواع الكائنات المجهولة أو الكائنات المخصصة في العلامات الذكية. يظهر المثال التالي كيف يعمل هذا. لاستيراد البيانات من الكائنات الديناميكية باستخدام العلامات الذكية، قم بزيارة المقالة التالية:

[استيراد من كائن ديناميكي كمصدر بيانات](/cells/ar/net/import-data-into-worksheet/#importdataintoworksheet-importingfromdynamicobjectasdatasource)


{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingAnonymousTypes-1.cs" >}}

## **كيفية استيراد الكائنات المتداخلة باستخدام العلامات الذكية**
تدعم Aspose.Cells الكائنات المتدرجة في العلامات الذكية، ويجب أن تكون الكائنات المتدرجة بسيطة. نحن نستخدم ملف قالب بسيط. راجع جدول التصميم الذي يحتوي على بعض العلامات الذكية المتدرجة.

|**الصفحة العملية الأولى لملف SM_NestedObjects.xlsx التي تظهر علامات ذكية متدرجة.**|
| :- |
|![todo:image_alt_text](using-smart-markers_7.png)|
المثال التالي يوضح كيف يعمل هذا.


{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingNestedObjects-1.cs" >}}


## **كيفية استيراد قائمة عامة ككائن متداخل باستخدام العلامات الذكية**
تدعم Aspose.Cells الآن أيضًا استخدام القائمة العامة ككائن متداخل. يرجى التحقق من لقطة الشاشة لملف الإكسل الناتج الذي تم إنشاؤه بالشيفرة التالية. كما يمكنك رؤية في لقطة الشاشة أنَّ كائن المعلم يحتوي على عدة كائنات متداخلة للطلاب.

|![todo:image_alt_text](using-smart-markers_8.png)|
| :- |

{{< gist  "aspose-com-gists" "24a8eac23c3325e20dababecf735a43b" "Examples-CSharp-SmartMarkers-UsingGenericList-1.cs" >}}

## **كيفية استيراد كائنات متداخلة غير خطية باستخدام العلامات الذكية**
الطريقة الحالية الافتراضية للمعالجة هي معالجة العناصر الذكية بشكل سطري. ولكن في بعض الأحيان، يحتاج علامات الذكاء الذكية في نفس جدول البيانات إلى أن تتم معالجتها معًا، بغض النظر عما إذا كانت في نفس الصف أم لا، فيجب عليك تحديد نطاق مسمى "_CellsSmartMarkers" وتحديد WorkbookDesigner.LineByLine بأنها خطأ قبل استدعاء المعالجة. 
الحصول على الإشعارات أثناء دمج البيانات مع علامات ذكاء

|![todo:image_alt_text](using-smart-markers_11.png)|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-LayerByLayer.cs" >}}

{{< app/cells/assistant language="csharp" >}}
