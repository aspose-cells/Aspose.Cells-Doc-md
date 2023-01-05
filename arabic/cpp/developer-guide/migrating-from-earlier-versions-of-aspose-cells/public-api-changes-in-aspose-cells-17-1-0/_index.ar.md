---
title: API عام تغييرات في Aspose.Cells 17.1.0
type: docs
weight: 20
url: /ar/cpp/public-api-changes-in-aspose-cells-17-1-0/
---
{{% alert color="primary" %}} 

يصف هذا المستند التغييرات التي تم إجراؤها على Aspose.Cells API من الإصدار 16.12.0 إلى 17.1.0 والتي قد تهم مطوري الوحدة / التطبيق. لا يشمل فقط الأساليب العامة الجديدة والمحدثة ، والفئات المضافة والمحذوفة وما إلى ذلك ، بل يشمل أيضًا وصفًا لأي تغييرات في السلوك خلف الكواليس في Aspose.Cells.

{{% /alert %}} 
## **تمت إضافة واجهات برمجة التطبيقات**
### **دعم النطاقات المسماة**
 Aspose.Cells for C++ يدعم الآن الإنشاء بالإضافة إلى معالجة النطاقات المسماة. يوضح مقتطف الكود التالي مدى سهولة استخدام Aspose.Cells for C++ API[إنشاء نطاقات مسماة](/cells/ar/cpp/create-named-range-in-a-workbook/).

**C ++**

{{< highlight "csharp" >}}

 //Path of your directory where you want to read or write files from

StringPtr dirPath = new String("D:\\Downloads\\");

//Path of output excel file

StringPtr outCreateNamedRange = (new String(dirPath))->Append(new String("outCreateNamedRange.xlsx"));

//Create a workbook

intrusive_ptr<IWorkbook> wb = Factory::CreateIWorkbook();

//Access first worksheet

intrusive_ptr<IWorksheet> ws = wb->GetIWorksheets()->GetObjectByIndex(0);

//Create a range

intrusive_ptr<IRange> rng = ws->GetICells()->CreateIRange((intrusive_ptr<String>)new String("A5:C10"));

//Set its name to make it named range

rng->SetName((intrusive_ptr<String>)new String("MyNamedRange"));

//Read the named range created above from names collection

intrusive_ptr<IName> nm = wb->GetIWorksheets()->GetINames()->GetObjectByIndex(0);

//Print its FullText and RefersTo properties

printf("Full Text: %s\n", nm->GetFullText()->charValue());

printf("Refers To: %s\n", nm->GetRefersTo()->charValue());

//Save the workbook in xlsx format

wb->Save(outCreateNamedRange, SaveFormat_Xlsx);

{{< /highlight >}}

 إلى جانب إنشاء نطاقات مسماة جديدة ، تدعم واجهات برمجة التطبيقات Aspose.Cells for C++ أيضًا معالجة النطاقات المسماة الحالية. يستخدم مقتطف التعليمات البرمجية التالي Aspose.Cells for C++ API إلى[معالجة نطاق مسمى موجود](/cells/ar/cpp/manipulate-named-range-in-a-workbook/).

**C ++**

{{< highlight "csharp" >}}

 //Path of your directory where you want to read or write files from

StringPtr dirPath = new String("D:\\Downloads\\");

//Path of source excel file

StringPtr srcManipulateRange = (new String(dirPath))->Append(new String("srcManipulateRange.xlsx"));

//Path of output excel file

StringPtr outManipulateRange = (new String(dirPath))->Append(new String("outManipulateRange.xlsx"));

//Create a workbook

intrusive_ptr<IWorkbook> wb = Factory::CreateIWorkbook(srcManipulateRange);

//Read the named range created above from names collection

intrusive_ptr<IName> nm = wb->GetIWorksheets()->GetINames()->GetObjectByIndex(0);

//Print its FullText and RefersTo properties

printf("Full Text: %s\n", nm->GetFullText()->charValue());

printf("Refers To: %s\n", nm->GetRefersTo()->charValue());

//Manipulate the RefersTo property of NamedRange

nm->SetRefersTo((intrusive_ptr<String>)new String("=Sheet1!$D$5:$J$10"));

//Save the workbook in xlsx format

wb->Save(outManipulateRange, SaveFormat_Xlsx);

{{< /highlight >}}
### **تمت إضافة طريقة ICells :: LinkToXmlMap**
تمت إضافة طريقة LinkToXmlMap إلى فئة ICells والتي تفيد في ربط مخطط XML.
### **تمت إضافة طريقة ICells :: ImportCSV**
تمت إضافة أسلوب ImportCSV إلى فئة ICells وهو أمر مفيد في استيراد ملف CSV إلى خلايا ورقة العمل.
### **تمت إضافة طريقة ICells :: ImportTwoDimensionArray**
تمت إضافة أسلوب GetIProtectedRangeCollection إلى فئة ICells وهو أمر مفيد في استيراد مصفوفة ثنائية الأبعاد من البيانات إلى ورقة عمل.
### **تمت إضافة طريقة IWorksheet :: GetIProtectedRangeCollection**
تمت إضافة أسلوب GetIProtectedRangeCollection إلى فئة IWorksheet وهو أمر مفيد في استرداد مجموعة كائنات IProtectedRange.
### **تمت إضافة طريقة IWorksheet :: GetIProtectedRangeCollection**
تمت إضافة أسلوب GetIProtectedRangeCollection إلى فئة IWorksheet وهو أمر مفيد في استرداد مجموعة نطاق التحرير من ورقة العمل.
### **تمت إضافة IWorkbookSettings :: طريقة ClearPivottables**
تمت إضافة طريقة ClearPivottables إلى فئة IWorkbookSettings والتي تفيد في مسح جميع الجداول المحورية من جدول بيانات معين.
### **تمت إضافة طريقة IWorksheetCollection :: CreateIRange**
تمت إضافة طريقة CreateIRange إلى فئة IWorksheetCollection والتي تكون مفيدة في إنشاء كائن من IRange عن طريق تمرير مراجع الخلية في تنسيق سلسلة.
### **تمت إضافة طريقة IExternalLink :: IsVisible**
تحصل طريقة IsVisible على حالة رؤية الارتباط الخارجي في تطبيق Excel.
### **تمت إضافة أساليب GetScaleCrop و SetScaleCrop**
كشف Aspose.Cells for C++ 17.1.0 طرق GetScaleCrop & SetScaleCrop لفئة IBuiltInDocumentPropertyCollection. هذه الطرق مفيدة للحصول على أو تعيين خاصية ScaleCrop التي تشير إلى وضع عرض الصورة المصغرة للوثيقة.
### **تمت إضافة أساليب GetLinksUpToDate & SetLinksUpToDate**
كشف Aspose.Cells for C++ 17.1.0 طرق GetLinksUpToDate & SetLinksUpToDate لفئة IBuiltInDocumentPropertyCollection. هذه الطرق مفيدة للحصول على أو تعيين خاصية LinkUpToDate التي تشير إلى ما إذا كانت الارتباطات التشعبية في مستند محدثة.
### **تمت إضافة أساليب GetAbsolutePath & SetAbsolutePath**
كشف Aspose.Cells for C++ 17.1.0 طرق GetAbsolutePath & SetAbsolutePath لفئة IWorkbook. هذه الطرق مفيدة للحصول على المسار المطلق للملف أو تعيينه والذي لا يمكن استخدامه إلا للارتباطات الخارجية.
### **تمت إضافة طرق GetFormula و SetFormula**
كشف هذا الإصدار من Aspose.Cells for C++ عن أساليب GetFormula & SetFormula لفئة IListColumn. هذه الطرق مفيدة للحصول على صيغة عمود القائمة أو تعيينها.
### **تمت إضافة GetCheckCompatibility وطرق SetCheckCompatibility**
كشف هذا الإصدار من Aspose.Cells for C++ عن أساليب GetCheckCompatibility & GetCheckCompatibility لفئة IWorkbookSettings. هذه الطرق مفيدة للحصول على أو تعيين خاصية التحقق من التوافق التي تشير إلى ما إذا كان يجب أن يتحقق API من التوافق عند حفظ المصنف. القيمة الافتراضية هي true ، ويمكن تعيينها على false إذا لم تكن متطلبات التطبيق هي التحقق من التوافق.
### **تمت إضافة أساليب GetILightCellsDataHandler & SetILightCellsDataHandler**
كشف Aspose.Cells for C++ الآن أساليب GetILightCellsDataHandler & SetILightCellsDataHandler لفئة ILoadOptions. تشير هذه الطرق إلى معالج البيانات لمعالجة بيانات الخلايا أثناء قراءة ملف القالب.
### **تمت إضافة أساليب GetCultureInfo & SetCultureInfo**
كشف Aspose.Cells for C++ طرق GetCultureInfo & SetCultureInfo لفئة ILoadOptions. يمكن لهذه الطرق الحصول على معلومات ثقافة النظام أو تعيينها في وقت تحميل الملف.
## **إزالة واجهات برمجة التطبيقات**
### **تمت إزالة طريقة ICells :: MaxDataRowInColumn**
يُنصح باستخدام طريقة ICells :: GetLastDataRow بدلاً من ذلك.
### **تمت إزالة طريقة ICell :: GetConditionalIStyle**
يُنصح باستخدام طريقة ICell :: GetIConditionalFormattingResult بدلاً من ذلك.
### **تمت إزالة IPageSetup :: GetDraft وأساليب SetDraft**
يُنصح باستخدام أساليب IPageSetup :: GetPrintDraft & IPageSetup :: SetPrintDraft بدلاً من ذلك.

{{% alert color="primary" %}} 

مع إصدار Aspose.Cells for C++ 17.1.0 ، قمنا بإزالة بعض الطرق التي لم تكن قيد الاستخدام وبالتالي اعتبرناها غير ضرورية. فيما يلي قائمة بجميع هذه الأساليب.

- IPaneCollection :: GetAcitvePaneType وأساليب SetAcitvePaneType
- طريقة IRange :: ToString
- IRow :: طريقة يساوي
- IWorkbook :: طريقة SetISettings
- طريقة ICell :: ToString ()
- طريقة ICell :: Equals (ObjectPtr)
- طريقة ICell :: GetHashCode
- IWorksheet :: طريقة ToString

{{% /alert %}}
