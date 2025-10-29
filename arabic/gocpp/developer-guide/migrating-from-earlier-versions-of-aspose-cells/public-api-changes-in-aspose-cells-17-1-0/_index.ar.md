---
title: تغييرات الواجهة البرمجية العامة في Aspose.Cells 17.1.0
type: docs
weight: 20
url: /ar/go-cpp/public-api-changes-in-aspose-cells-17-1-0/
---

{{% alert color="primary" %}} 

تصف هذه الوثيقة التغييرات في واجهة برمجة تطبيقات Aspose.Cells من الإصدار 16.12.0 إلى 17.1.0 التي قد تكون مثيرة لاهتمام مطوري الوحدات/التطبيقات. تتضمن ليس فقط الطرق العامة الجديدة والمحدثة والطرق العامة التي تمت إضافتها وإزالتها وتغيير الفصول الخلفية في Aspose.Cells.

{{% /alert %}} 
## **واجهات برمجة التطبيقات الجديدة**
### **دعم نطاقات الأسماء**
يدعم الإصدار Aspose.Cells for C++ الآن إنشاء وتلاعب بنطاقات الأسماء. يبين الكود التالي كيفية استخدام واجهة برمجة التطبيقات Aspose.Cells for C++ بسهولة لـ [إنشاء نطاقات أسماء](/cells/ar/cpp/create-named-range-in-a-workbook/).

**C++**

{{< highlight csharp >}}

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

بالإضافة إلى إنشاء نطاقات أسماء جديدة، تدعم واجهات برمجة التطبيقات Aspose.Cells for C++ أيضًا تلاعب بنطاقات الأسماء الحالية. يستخدم الكود التالي واجهة برمجة التطبيقات Aspose.Cells for C++ لـ [تلاعب بنطاق الاسم الحالي](/cells/ar/cpp/manipulate-named-range-in-a-workbook/).

**C++**

{{< highlight csharp >}}

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
### **تمت إضافة طريقة ICells::LinkToXmlMap**
تمت إضافة الطريقة LinkToXmlMap إلى فئة ICells والتي تكون مفيدة في ربط خريطة XML.
### **تمت إضافة طريقة ICells::ImportCSV**
تمت إضافة الطريقة ImportCSV إلى فئة ICells والتي تكون مفيدة في استيراد ملف CSV إلى الخلايا لورقة العمل.
### **تمت إضافة الطريقة ICells::ImportTwoDimensionArray**
تمت إضافة الطريقة GetIProtectedRangeCollection إلى فئة ICells والتي تكون مفيدة في استيراد مصفوفة ثنائية الأبعاد من البيانات إلى ورقة العمل.
### **تمت إضافة الطريقة IWorksheet::GetIProtectedRangeCollection**
تمت إضافة الطريقة GetIProtectedRangeCollection إلى فئة IWorksheet والتي تكون مفيدة في استرجاع مجموعة من كائنات IProtectedRange.
### **تمت إضافة الطريقة IWorksheet::GetIProtectedRangeCollection**
تمت إضافة الطريقة GetIProtectedRangeCollection إلى فئة IWorksheet والتي تكون مفيدة في استرجاع مجموعة نطاقات التحرير من ورقة العمل.
### **تمت إضافة الطريقة IWorkbookSettings::ClearPivottables**
تمت إضافة طريقة ClearPivottables إلى فئة IWorkbookSettings، والتي تُعد مفيدة في مسح جميع الجداول المحورية من جدول بيانات معين.
### **تمت إضافة طريقة CreateIRange إلى واجهة IWorksheetCollection.**
تمت إضافة طريقة CreateIRange إلى فئة IWorksheetCollection والتي تعود بفائدة في إنشاء كائن من النوع IRange من خلال تمرير مراجع الخلية بتنسيق سلسلة.
### **تمت إضافة طريقة IsVisible إلى واجهة IExternalLink.**
تعود طريقة IsVisible بحالة الرؤية لرابط خارجي في تطبيق Excel.
### **تمت إضافة طرق GetScaleCrop و SetScaleCrop.**
قامت الإصدار 17.1.0 لرقم Aspose.Cells for C++ بتعريض طرق GetScaleCrop و SetScaleCrop لفئة IBuiltInDocumentPropertyCollection. تُعتبر هذه الطرق مفيدة للحصول على أو تعيين خاصية ScaleCrop والتي تشير إلى وضع عرض الصورة المصغرة للمستند.
### **تمت إضافة طرق GetLinksUpToDate و SetLinksUpToDate.**
قام الإصدار 17.1.0 لرقم Aspose.Cells for C++ بتعريض طرق GetLinksUpToDate و SetLinksUpToDate لفئة IBuiltInDocumentPropertyCollection. تُعتبر هذه الطرق مفيدة للحصول على أو تعيين خاصية LinkUpToDate والتي تشير إلى ما إذا كانت الروابط الفائقة للمستند محدثة.
### **تمت إضافة طرق GetAbsolutePath و SetAbsolutePath.**
قام الإصدار 17.1.0 لرقم Aspose.Cells for C++ بتعريض طرق GetAbsolutePath و SetAbsolutePath لفئة IWorkbook. تُعتبر هذه الطرق مفيدة للحصول على أو تعيين المسار المطلق للملف الذي يمكن استخدامه فقط للروابط الخارجية.
### **تمت إضافة طرق GetFormula و SetFormula.**
قام هذا الإصدار لرقم Aspose.Cells for C++ بتعريض طرق GetFormula و SetFormula لفئة IListColumn. تُعتبر هذه الطرق مفيدة للحصول على أو تعيين الصيغة لعمود القائمة.
### **تمت إضافة طرق GetCheckCompatibility و SetCheckCompatibility.**
قام هذا الإصدار لرقم Aspose.Cells for C++ بتعريض طرق GetCheckCompatibility و SetCheckCompatibility لفئة IWorkbookSettings. تُعتبر هذه الطرق مفيدة للحصول على أو تعيين خاصية التحقق من التوافق، مما يشير إلى ما إذا كان يجب على الواجهة البرمجية التحقق من التوافق عند حفظ دفتر العمل. القيمة الافتراضية هي صحيح، ويمكن تعيينها على خطأ إذا كانت متطلبات التطبيق لا تتطلب التحقق من التوافق.
### **تمت إضافة طرق GetILightCellsDataHandler و SetILightCellsDataHandler.**
قام الإصدار Aspose.Cells for C++ الآن بتعريض طرق GetILightCellsDataHandler و SetILightCellsDataHandler لفئة ILoadOptions. تُشير هذه الطرق إلى معالج البيانات لمعالجة بيانات الخلايا أثناء قراءة ملف القالب.
### **تمت إضافة طرق GetCultureInfo و SetCultureInfo.**
قام الإصدار Aspose.Cells for C++ بتعريض طرق GetCultureInfo و SetCultureInfo لفئة ILoadOptions. يمكن لهذه الطرق الحصول على معلومات ثقافية النظام أو تعيينها في وقت تحميل الملف.
## **تمت إزالة واجهات برمجة التطبيقات**
### **تمت إزالة أسلوب MaxDataRowInColumn من ICells**
يُنصح باستخدام طريقة GetLastDataRow في ICells بدلاً منها
### **تمت إزالة أسلوب GetConditionalIStyle من ICell**
يُنصح باستخدام طريقة GetIConditionalFormattingResult في ICell بدلاً منها
### **تمت إزالة أساليب GetDraft وSetDraft من IPageSetup**
يُنصح باستخدام طريقتي GetPrintDraft وSetPrintDraft في IPageSetup بدلاً منهما

{{% alert color="primary" %}} 

مع إطلاق الإصدار 17.1.0 من Aspose.Cells for C++، لقد تمت إزالة بعض الأساليب التي لم يتم استخدامها والتي اعتبرت غير ضرورية. إليك قائمة جميع تلك الأساليب

- طرق GetAcitvePaneType وSetAcitvePaneType في IPaneCollection
- طريقة ToString في IRange
- طريقة Equals في IRow
- طريقة SetISettings في IWorkbook
- طريقة ToString() في ICell
- طريقة Equals(ObjectPtr) في ICell
- طريقة GetHashCode في ICell
- طريقة ToString في IWorksheet

{{% /alert %}}
